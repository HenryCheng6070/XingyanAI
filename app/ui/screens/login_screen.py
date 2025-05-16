from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        # 创建主布局
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 添加标题
        title = Label(text='星妍AI - 登录', font_name='Chinese', font_size='24sp', size_hint_y=None, height='50dp')
        layout.add_widget(title)
        
        # 添加用户名输入框
        self.username_input = TextInput(hint_text='用户名', font_name='Chinese', multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.username_input)
        
        # 添加密码输入框
        self.password_input = TextInput(hint_text='密码', font_name='Chinese', password=True, multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.password_input)
        
        # 添加登录按钮
        login_button = Button(text='登录', font_name='Chinese', size_hint_y=None, height='50dp')
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)
        
        # 添加注册按钮
        register_button = Button(text='注册新账号', font_name='Chinese', size_hint_y=None, height='50dp')
        register_button.bind(on_press=self.go_to_register)
        layout.add_widget(register_button)
        
        # 添加错误信息标签
        self.error_label = Label(text='', font_name='Chinese', color=(1, 0, 0, 1), size_hint_y=None, height='30dp')
        layout.add_widget(self.error_label)
        
        self.add_widget(layout)
    
    def login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        
        if not username or not password:
            self.error_label.text = '请输入用户名和密码'
            return
        
        # 获取数据库实例
        db = App.get_running_app().db
        user = db.login_user(username, password)
        
        if user:
            # 登录成功，保存用户ID到应用实例
            App.get_running_app().user_id = user[0]
            App.get_running_app().username = user[1]
            
            # 跳转到主界面
            self.manager.current = 'main'
            
            # 清空输入框和错误信息
            self.username_input.text = ''
            self.password_input.text = ''
            self.error_label.text = ''
        else:
            self.error_label.text = '用户名或密码错误'
    
    def go_to_register(self, instance):
        # 跳转到注册界面
        self.manager.current = 'register'
        
        # 清空输入框和错误信息
        self.username_input.text = ''
        self.password_input.text = ''
        self.error_label.text = ''