from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.app import App

from app.ui.components.card import Card
from app.ui.components.status_bar import StatusBar
from app.ui.components.rounded_button import RoundedButton
from app.ui.styles import COLORS, FONT_SIZES

class DeviceScreen(Screen):
    def __init__(self, **kwargs):
        super(DeviceScreen, self).__init__(**kwargs)
        
        # 创建主布局
        main_layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        
        # 添加状态栏
        status_bar = StatusBar()
        main_layout.add_widget(status_bar)
        
        # 创建内容布局
        content_layout = BoxLayout(
            orientation='vertical', 
            padding=[dp(15), dp(10), dp(15), dp(15)], 
            spacing=dp(15)
        )
        
        # 添加标题和返回按钮
        header_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(50)
        )
        
        back_button = Button(
            text='←',
            font_size=FONT_SIZES['h2'],
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            background_color=(0, 0, 0, 0),
            color=COLORS['text_primary'],
            on_release=self.go_back
        )
        
        title_label = Label(
            text='您好，',
            font_name='Chinese',
            font_size=FONT_SIZES['h3'],
            halign='left',
            color=COLORS['text_primary']
        )
        
        username_label = Label(
            text='Caomeidaxigua',
            font_size=FONT_SIZES['h3'],
            halign='left',
            color=COLORS['text_primary']
        )
        
        header_layout.add_widget(back_button)
        header_layout.add_widget(title_label)
        header_layout.add_widget(username_label)
        header_layout.add_widget(BoxLayout())  # 空白填充
        
        content_layout.add_widget(header_layout)
        
        # 添加设备卡片
        device_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(300),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        # 设备图片
        device_image = Image(
            source='resources/images/skin_device.png',
            size_hint_y=0.7
        )
        
        # 设备名称
        device_name = Label(
            text='皮肤检测仪',
            font_name='Chinese',
            font_size=FONT_SIZES['h3'],
            size_hint_y=0.15,
            halign='center',
            color=COLORS['text_primary']
        )
        
        # 添加设备按钮
        add_device_button = RoundedButton(
            text='添加设备',
            font_name='Chinese',
            font_size=FONT_SIZES['button'],
            size_hint=(None, None),
            size=(dp(150), dp(40)),
            pos_hint={'center_x': 0.5},
            background_color=COLORS['primary'],
            on_release=self.add_device
        )
        
        device_card.add_widget(device_image)
        device_card.add_widget(device_name)
        device_card.add_widget(add_device_button)
        
        content_layout.add_widget(device_card)
        
        # 添加设备说明
        instruction_label = Label(
            text='其他方式连接',
            font_name='Chinese',
            font_size=FONT_SIZES['small'],
            size_hint_y=None,
            height=dp(30),
            halign='center',
            color=COLORS['text_secondary']
        )
        
        content_layout.add_widget(instruction_label)
        
        # 将内容布局添加到主布局
        main_layout.add_widget(content_layout)
        
        # 添加底部导航栏
        nav_bar = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(60),
            padding=[dp(20), dp(5), dp(20), dp(5)],
            spacing=dp(30)
        )
        
        # 首页按钮
        home_btn = BoxLayout(orientation='vertical')
        home_icon = Label(text='🏠', font_size=FONT_SIZES['h2'])
        home_label = Label(
            text='首页',
            font_name='Chinese',
            font_size=FONT_SIZES['tiny'],
            color=COLORS['text_secondary']
        )
        home_btn.add_widget(home_icon)
        home_btn.add_widget(home_label)
        home_btn.bind(on_touch_down=self.go_to_home)
        
        # 设备按钮
        device_btn = BoxLayout(orientation='vertical')
        device_icon = Label(text='📱', font_size=FONT_SIZES['h2'])
        device_label = Label(
            text='设备',
            font_name='Chinese',
            font_size=FONT_SIZES['tiny'],
            color=COLORS['primary']  # 高亮颜色，表示当前页面
        )
        device_btn.add_widget(device_icon)
        device_btn.add_widget(device_label)
        
        # 我的按钮
        profile_btn = BoxLayout(orientation='vertical')
        profile_icon = Label(text='👤', font_size=FONT_SIZES['h2'])
        profile_label = Label(
            text='我的',
            font_name='Chinese',
            font_size=FONT_SIZES['tiny'],
            color=COLORS['text_secondary']
        )
        profile_btn.add_widget(profile_icon)
        profile_btn.add_widget(profile_label)
        profile_btn.bind(on_touch_down=self.go_to_profile)
        
        nav_bar.add_widget(home_btn)
        nav_bar.add_widget(device_btn)
        nav_bar.add_widget(profile_btn)
        
        main_layout.add_widget(nav_bar)
        
        # 将主布局添加到屏幕
        self.add_widget(main_layout)
    
    def go_back(self, instance):
        self.manager.current = 'main'
    
    def add_device(self, instance):
        # 这里可以添加设备连接逻辑
        # 例如打开蓝牙连接界面或显示连接指南
        print("添加设备")
        # 连接成功后可以跳转到设备详情页面
        # self.manager.current = 'device_detail'
    
    def go_to_home(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.manager.current = 'main'
            return True
    
    def go_to_profile(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # 假设有个人资料页面
            # self.manager.current = 'profile'
            print("前往个人资料页面")
            return True