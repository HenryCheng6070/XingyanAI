from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # 创建主布局
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 添加标题
        title = Label(text='星妍AI - 皮肤分析与护肤推荐', font_size='24sp', size_hint_y=None, height='50dp')
        layout.add_widget(title)
        
        # 添加欢迎信息
        self.welcome_label = Label(text='欢迎使用星妍AI', font_size='18sp', size_hint_y=None, height='40dp')
        layout.add_widget(self.welcome_label)
        
        # 添加功能按钮
        camera_button = Button(text='开始拍照分析', size_hint_y=None, height='60dp')
        camera_button.bind(on_press=self.go_to_camera)
        layout.add_widget(camera_button)
        
        history_button = Button(text='查看历史记录', size_hint_y=None, height='60dp')
        history_button.bind(on_press=self.go_to_history)
        layout.add_widget(history_button)
        
        product_button = Button(text='浏览产品推荐', size_hint_y=None, height='60dp')
        product_button.bind(on_press=self.go_to_product)
        layout.add_widget(product_button)
        
        # 添加退出登录按钮
        logout_button = Button(text='退出登录', size_hint_y=None, height='50dp')
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
        
        self.add_widget(layout)
    
    def on_enter(self):
        # 屏幕进入时更新欢迎信息
        app = App.get_running_app()
        if hasattr(app, 'username'):
            self.welcome_label.text = f'欢迎您，{app.username}'
    
    def go_to_camera(self, instance):
        # 跳转到相机界面
        self.manager.current = 'camera'
    
    def go_to_history(self, instance):
        # 跳转到历史记录界面
        self.manager.current = 'history'
    
    def go_to_product(self, instance):
        # 跳转到产品推荐界面
        self.manager.current = 'product'
    
    def logout(self, instance):
        # 退出登录，清除用户信息
        app = App.get_running_app()
        if hasattr(app, 'user_id'):
            delattr(app, 'user_id')
        if hasattr(app, 'username'):
            delattr(app, 'username')
        
        # 跳转到登录界面
        self.manager.current = 'login'