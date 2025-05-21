from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.metrics import dp

from app.ui.components.rounded_button import RoundedButton
from app.ui.components.rounded_text_input import RoundedTextInput
from app.ui.components.status_bar import StatusBar
from app.ui.styles import COLORS, FONT_SIZES, SPACING

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        # 创建主布局
        main_layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        
        # 添加状态栏
        status_bar = StatusBar()
        main_layout.add_widget(status_bar)
        
        # 创建内容布局
        content_layout = BoxLayout(
            orientation='vertical', 
            padding=[dp(20), dp(10), dp(20), dp(20)], 
            spacing=dp(15)
        )
        
        # 添加背景图片（半透明）
        background = Image(
            source='resources/images/skin_background.jpg',  # 需要添加适当的背景图片
            opacity=0.2,
            allow_stretch=True,
            keep_ratio=False
        )
        
        # 添加标语
        slogan_label = Label(
            text='此刻开始，\n认识自己，照顾自己',
            font_name='Chinese',
            font_size=FONT_SIZES['h2'],
            halign='left',
            valign='middle',
            size_hint_y=None,
            height=dp(100),
            text_size=(dp(300), None),
            color=[0.3, 0.4, 0.5, 1]
        )
        content_layout.add_widget(slogan_label)
        
        # 添加空白区域
        content_layout.add_widget(BoxLayout(size_hint_y=None, height=dp(50)))
        
        # 添加国家代码和手机号输入框
        phone_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(50),
            spacing=dp(10)
        )
        
        country_code = RoundedTextInput(
            text='+86',
            multiline=False,
            size_hint_x=None,
            width=dp(70),
            font_size=FONT_SIZES['body'],
            halign='center'
        )
        
        phone_input = RoundedTextInput(
            hint_text='请输入手机号',
            multiline=False,
            font_name='Chinese',
            font_size=FONT_SIZES['body']
        )
        
        phone_layout.add_widget(country_code)
        phone_layout.add_widget(phone_input)
        content_layout.add_widget(phone_layout)
        
        # 添加登录按钮
        login_button = RoundedButton(
            text='点击获取验证码',
            font_name='Chinese',
            size_hint_y=None,
            height=dp(50),
            btn_color=[0.43, 0.55, 0.63, 1],  # 蓝灰色
            border_radius=dp(10)
        )
        login_button.bind(on_press=self.request_verification)
        content_layout.add_widget(login_button)
        
        # 添加用户协议提示
        agreement_text = Label(
            text='点击按钮即表示您同意《用户协议》和《隐私条款》',
            font_name='Chinese',
            font_size=FONT_SIZES['tiny'],
            size_hint_y=None,
            height=dp(30),
            color=[0.5, 0.5, 0.5, 1]
        )
        content_layout.add_widget(agreement_text)
        
        # 添加底部空白
        content_layout.add_widget(BoxLayout())
        
        # 将内容布局添加到主布局
        main_layout.add_widget(content_layout)
        
        # 添加背景和主布局到屏幕
        self.add_widget(background)
        self.add_widget(main_layout)
    
    def request_verification(self, instance):
        # 这里添加请求验证码的逻辑
        # 验证成功后跳转到主界面
        self.manager.current = 'main'
    
    def go_to_register(self, instance):
        self.manager.current = 'register'