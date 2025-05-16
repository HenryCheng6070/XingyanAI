from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        
        # 创建主布局
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 添加标题
        title = Label(text='星妍AI - 注册', font_size='24sp', size_hint_y=None, height='50dp')
        layout.add_widget(title)
        
        # 添加用户名输入框
        self.username_input = TextInput(hint_text='用户名', multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.username_input)
        
        # 添加密码输入框
        self.password_input = TextInput(hint_text='密码', password=True, multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.password_input)
        
        # 添加确认密码输入框
        self.confirm_password_input = TextInput(hint_text='确认密码', password=True, multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.confirm_password_input)
        
        # 添加年龄输入框
        self.age_input = TextInput(hint_text='年龄（可选）', multiline=False, size_hint_y=None, height='40dp', input_filter='int')
        layout.add_widget(self.age_input)
        
        # 添加皮肤类型输入框
        self.skin_type_input = TextInput(hint_text='皮肤类型（可选，如：干性/油性/混合性）', multiline=False, size_hint_y=None, height='40dp')
        layout.add_widget(self.skin_type_input)
        
        # 添加注册按钮
        register_button = Button(text='注册', size_hint_y=None, height='50dp')
        register_button.bind(on_press=self.register)
        layout.add_widget(register_button)
        
        # 添加返回登录按钮
        back_button = Button(text='返回登录', size_hint_y=None, height='50dp')
        back_button.bind(on_press=self.go_to_login)
        layout.add_widget(back_button)
        
        # 添加错误信息标签
        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint_y=None, height='30dp')
        layout.add_widget(self.error_label)
        
        self.add_widget(layout)
    
    def register(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()
        
        if not username or not password:
            self.error_label.text = '请输入用户名和密码'
            return
        
        if password != confirm_password:
            self.error_label.text = '两次输入的密码不一致'
            return
        
        # 获取可选信息
        age = self.age_input.text.strip()
        skin_type = self.skin_type_input.text.strip()
        
        # 转换年龄为整数
        age = int(age) if age else None
        
        # 获取数据库实例
        db = App.get_running_app().db
        user_id = db.register_user(username, password, age, skin_type)
        
        if user_id:
            # 注册成功，跳转到登录界面
            self.manager.current = 'login'
            
            # 清空输入框和错误信息
            self.username_input.text = ''
            self.password_input.text = ''
            self.confirm_password_input.text = ''
            self.age_input.text = ''
            self.skin_type_input.text = ''
            self.error_label.text = ''
        else:
            self.error_label.text = '用户名已存在，请选择其他用户名'
    
    def go_to_login(self, instance):
        # 跳转到登录界面
        self.manager.current = 'login'
        
        # 清空输入框和错误信息
        self.username_input.text = ''
        self.password_input.text = ''
        self.confirm_password_input.text = ''
        self.age_input.text = ''
        self.skin_type_input.text = ''
        self.error_label.text = ''