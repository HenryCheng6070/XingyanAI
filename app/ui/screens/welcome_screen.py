from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.clock import Clock

from app.ui.components.rounded_button import RoundedButton
from app.ui.styles import COLORS, FONT_SIZES

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        
        # 创建主布局
        main_layout = BoxLayout(
            orientation='vertical',
            padding=[dp(20), dp(40), dp(20), dp(20)],
            spacing=dp(20)
        )
        
        # 添加应用Logo
        logo_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=0.4
        )
        
        logo = Image(
            source='resources/images/logo.png',
            size_hint=(None, None),
            size=(dp(150), dp(150)),
            pos_hint={'center_x': 0.5}
        )
        
        app_name = Label(
            text='星妍AI',
            font_name='Chinese',
            font_size=FONT_SIZES['h1'],
            halign='center',
            color=COLORS['primary']
        )
        
        app_slogan = Label(
            text='此刻开始，认识自己，照顾自己',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            halign='center',
            color=COLORS['text_secondary']
        )
        
        logo_layout.add_widget(logo)
        logo_layout.add_widget(app_name)
        logo_layout.add_widget(app_slogan)
        
        # 添加背景图片
        bg_image = Image(
            source='resources/images/skin_care_bg.jpg',
            opacity=0.2,
            size_hint_y=0.3
        )
        
        # 添加按钮区域
        button_layout = BoxLayout(
            orientation='vertical',
            spacing=dp(15),
            size_hint_y=0.3,
            pos_hint={'center_x': 0.5}
        )
        
        start_button = RoundedButton(
            text='Start Now',
            font_size=FONT_SIZES['button'],
            size_hint=(None, None),
            size=(dp(200), dp(50)),
            pos_hint={'center_x': 0.5},
            background_color=COLORS['primary'],
            on_release=self.go_to_login
        )
        
        button_layout.add_widget(start_button)
        
        # 添加到主布局
        main_layout.add_widget(logo_layout)
        main_layout.add_widget(bg_image)
        main_layout.add_widget(button_layout)
        
        self.add_widget(main_layout)
        
        # 添加动画效果
        Clock.schedule_once(self.start_animations, 0.5)
    
    def start_animations(self, dt):
        # 为子部件添加动画效果
        for child in self.children[0].children:
            anim = Animation(opacity=0, duration=0) + Animation(opacity=1, duration=0.8)
            anim.start(child)
    
    def go_to_login(self, instance):
        self.manager.current = 'login'