from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock

from app.ui.components.rounded_button import RoundedButton
from app.ui.components.card import Card
from app.ui.components.status_bar import StatusBar
from app.ui.styles import COLORS, FONT_SIZES, SPACING

class ReportScreen(Screen):
    def __init__(self, **kwargs):
        super(ReportScreen, self).__init__(**kwargs)
        
        # 创建主布局
        main_layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        
        # 添加状态栏
        status_bar = StatusBar()
        main_layout.add_widget(status_bar)
        
        # 创建可滚动内容区域
        scroll_view = ScrollView()
        content_layout = BoxLayout(
            orientation='vertical', 
            padding=[dp(15), dp(10), dp(15), dp(15)], 
            spacing=dp(15),
            size_hint_y=None
        )
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        # 添加标题
        title_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(50)
        )
        
        back_btn = Label(
            text='←',
            font_size=FONT_SIZES['h1'],
            size_hint_x=None,
            width=dp(40),
            color=COLORS['text_primary']
        )
        back_btn.bind(on_touch_down=self.go_back)
        
        title_label = Label(
            text='皮肤检测报告',
            font_name='Chinese',
            font_size=FONT_SIZES['h2'],
            color=COLORS['text_primary']
        )
        
        title_layout.add_widget(back_btn)
        title_layout.add_widget(title_label)
        
        content_layout.add_widget(title_layout)
        
        # 添加报告日期
        date_label = Label(
            text='检测日期: 2025-05-21',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            halign='left',
            size_hint_y=None,
            height=dp(30),
            text_size=(dp(300), None),
            color=COLORS['text_secondary']
        )
        content_layout.add_widget(date_label)
        
        # 添加皮肤状态总览卡片
        overview_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(200),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        overview_title = Label(
            text='皮肤状态总览',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            halign='left',
            size_hint_y=None,
            height=dp(30),
            text_size=(dp(300), None),
            color=COLORS['text_primary']
        )
        
        # 这里可以添加皮肤状态的详细信息
        # 例如：水分、油分、弹性等指标
        
        overview_card.add_widget(overview_title)
        content_layout.add_widget(overview_card)
        
        # 添加皮肤问题分析卡片
        analysis_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(250),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        analysis_title = Label(
            text='皮肤问题分析',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            halign='left',
            size_hint_y=None,
            height=dp(30),
            text_size=(dp(300), None),
            color=COLORS['text_primary']
        )
        
        # 这里可以添加皮肤问题的分析内容
        
        analysis_card.add_widget(analysis_title)
        content_layout.add_widget(analysis_card)
        
        # 添加护肤建议卡片
        suggestion_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(200),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        suggestion_title = Label(
            text='护肤建议',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            halign='left',
            size_hint_y=None,
            height=dp(30),
            text_size=(dp(300), None),
            color=COLORS['text_primary']
        )
        
        # 这里可以添加护肤建议的内容
        
        suggestion_card.add_widget(suggestion_title)
        content_layout.add_widget(suggestion_card)
        
        # 设置内容布局的高度
        content_layout.height = sum(child.height + dp(15) for child in content_layout.children)
        
        scroll_view.add_widget(content_layout)
        main_layout.add_widget(scroll_view)
        
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
            color=COLORS['text_secondary']
        )
        device_btn.add_widget(device_icon)
        device_btn.add_widget(device_label)
        device_btn.bind(on_touch_down=self.go_to_device)
        
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
        
        self.add_widget(main_layout)
    
    def go_back(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.manager.current = 'main'
            return True
    
    def go_to_home(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.manager.current = 'main'
            return True
    
    def go_to_device(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.manager.current = 'device'
            return True
    
    def go_to_profile(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # 假设有个人资料页面
            # self.manager.current = 'profile'
            print("前往个人资料页面")
            return True