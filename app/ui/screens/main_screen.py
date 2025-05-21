from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.app import App
from kivy.properties import StringProperty

from app.ui.components.rounded_button import RoundedButton
from app.ui.components.card import Card
from app.ui.components.status_bar import StatusBar
from app.ui.components.circular_progress import CircularProgress
from app.ui.styles import COLORS, FONT_SIZES, SPACING

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # 创建主布局
        self.main_layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        
        # 添加状态栏
        status_bar = StatusBar()
        self.main_layout.add_widget(status_bar)
        
        # 创建可滚动内容区域
        scroll_view = ScrollView()
        content_layout = BoxLayout(
            orientation='vertical', 
            padding=[dp(15), dp(10), dp(15), dp(15)], 
            spacing=dp(15),
            size_hint_y=None
        )
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        # 添加欢迎区域
        greeting_card = Card(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(80),
            padding=[dp(15), dp(10), dp(15), dp(10)]
        )
        
        # 添加欢迎文本
        greeting_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        
        self.greeting_label = Label(
            text='早上好，',
            font_name='Chinese',
            font_size=FONT_SIZES['h3'],
            halign='left',
            valign='bottom',
            size_hint_y=None,
            height=dp(30),
            text_size=(dp(200), None),
            color=COLORS['text_primary']
        )
        
        self.username_label = Label(
            text='',  # 将在on_enter中设置
            font_size=FONT_SIZES['h3'],
            halign='left',
            valign='top',
            size_hint_y=None,
            height=dp(30),
            text_size=(dp(200), None),
            color=COLORS['text_primary']
        )
        
        greeting_layout.add_widget(self.greeting_label)
        greeting_layout.add_widget(self.username_label)
        
        # 添加用户头像
        self.user_avatar = Image(
            source='',  # 将在on_enter中设置
            size_hint=(None, None),
            size=(dp(50), dp(50))
        )
        
        greeting_card.add_widget(greeting_layout)
        greeting_card.add_widget(BoxLayout())  # 空白填充
        greeting_card.add_widget(self.user_avatar)
        
        content_layout.add_widget(greeting_card)
        
        # 添加今日提示
        tip_label = Label(
            text='今天想做点什么？',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            halign='left',
            size_hint_y=None,
            height=dp(40),
            text_size=(dp(300), None),
            color=COLORS['text_secondary']
        )
        content_layout.add_widget(tip_label)
        
        # 添加皮肤状态仪表盘
        dashboard_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(250),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        # 仪表盘标题
        dashboard_title = Label(
            text='皮肤检测',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            size_hint_y=None,
            height=dp(30),
            halign='center',
            color=COLORS['text_primary']
        )
        
        # 仪表盘内容
        gauge_layout = BoxLayout(orientation='vertical')
        
        # 添加圆形进度条
        progress = CircularProgress(
            thickness=dp(10),
            progress=0.75,
            size_hint=(None, None),
            size=(dp(150), dp(150)),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # 添加检测按钮
        scan_button = RoundedButton(
            text='开始检测',
            font_name='Chinese',
            font_size=FONT_SIZES['button'],
            size_hint=(None, None),
            size=(dp(150), dp(40)),
            pos_hint={'center_x': 0.5},
            background_color=COLORS['primary'],
            on_release=self.go_to_camera
        )
        
        gauge_layout.add_widget(progress)
        gauge_layout.add_widget(scan_button)
        
        dashboard_card.add_widget(dashboard_title)
        dashboard_card.add_widget(gauge_layout)
        
        content_layout.add_widget(dashboard_card)
        
        # 添加历史记录卡片
        history_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(200),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        history_title = Label(
            text='历史检测',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            size_hint_y=None,
            height=dp(30),
            halign='left',
            color=COLORS['text_primary']
        )
        
        # 历史记录列表
        history_list = GridLayout(
            cols=1,
            spacing=dp(10),
            size_hint_y=None,
            height=dp(140)
        )
        
        # 添加历史记录项
        for i in range(2):
            history_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=dp(60),
                spacing=dp(10)
            )
            
            date_label = Label(
                text=f'2024-05-{10+i}',
                font_size=FONT_SIZES['small'],
                size_hint_x=0.3,
                color=COLORS['text_secondary']
            )
            
            result_label = Label(
                text='皮肤状态良好',
                font_name='Chinese',
                font_size=FONT_SIZES['small'],
                size_hint_x=0.5,
                color=COLORS['text_primary']
            )
            
            view_button = Button(
                text='查看',
                font_name='Chinese',
                font_size=FONT_SIZES['small'],
                size_hint_x=0.2,
                background_color=COLORS['secondary'],
                on_release=self.go_to_history
            )
            
            history_item.add_widget(date_label)
            history_item.add_widget(result_label)
            history_item.add_widget(view_button)
            
            history_list.add_widget(history_item)
        
        history_card.add_widget(history_title)
        history_card.add_widget(history_list)
        
        content_layout.add_widget(history_card)
        
        # 添加产品推荐卡片
        product_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(200),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        product_title = Label(
            text='推荐产品',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            size_hint_y=None,
            height=dp(30),
            halign='left',
            color=COLORS['text_primary']
        )
        
        # 产品列表
        product_list = BoxLayout(
            orientation='horizontal',
            spacing=dp(10)
        )
        
        # 添加产品项
        for i in range(2):
            product_item = BoxLayout(
                orientation='vertical',
                size_hint_x=0.5
            )
            
            product_image = Image(
                source=f'resources/images/product_{i+1}.png',
                size_hint_y=0.7
            )
            
            product_name = Label(
                text=f'护肤产品 {i+1}',
                font_name='Chinese',
                font_size=FONT_SIZES['small'],
                size_hint_y=0.15,
                color=COLORS['text_primary']
            )
            
            product_price = Label(
                text=f'¥{99+i*50}.00',
                font_size=FONT_SIZES['small'],
                size_hint_y=0.15,
                color=COLORS['primary']
            )
            
            product_item.add_widget(product_image)
            product_item.add_widget(product_name)
            product_item.add_widget(product_price)
            
            product_list.add_widget(product_item)
        
        product_card.add_widget(product_title)
        product_card.add_widget(product_list)
        
        content_layout.add_widget(product_card)
        
        # 添加资讯卡片
        news_card = Card(
            orientation='vertical',
            size_hint_y=None,
            height=dp(200),
            padding=[dp(15), dp(15), dp(15), dp(15)]
        )
        
        news_title = Label(
            text='护肤资讯',
            font_name='Chinese',
            font_size=FONT_SIZES['body'],
            size_hint_y=None,
            height=dp(30),
            halign='left',
            color=COLORS['text_primary']
        )
        
        # 资讯列表
        news_list = GridLayout(
            cols=1,
            spacing=dp(10),
            size_hint_y=None,
            height=dp(140)
        )
        
        # 添加资讯项
        news_items = [
            '《中国身体皮肤护理白皮书(2023)》在北京发布',
            '皮肤护理一键解决护肤5个小贴士'
        ]
        
        for news in news_items:
            news_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height=dp(60),
                spacing=dp(10)
            )
            
            news_image = Image(
                source='resources/images/news_icon.png',
                size_hint_x=0.2
            )
            
            news_label = Label(
                text=news,
                font_name='Chinese',
                font_size=FONT_SIZES['small'],
                size_hint_x=0.6,
                text_size=(dp(150), None),
                halign='left',
                color=COLORS['text_primary']
            )
            
            read_button = Button(
                text='阅读',
                font_name='Chinese',
                font_size=FONT_SIZES['small'],
                size_hint_x=0.2,
                background_color=COLORS['secondary'],
                on_release=self.go_to_news
            )
            
            news_item.add_widget(news_image)
            news_item.add_widget(news_label)
            news_item.add_widget(read_button)
            
            news_list.add_widget(news_item)
        
        news_card.add_widget(news_title)
        news_card.add_widget(news_list)
        
        content_layout.add_widget(news_card)
        
        # 设置内容布局的高度
        content_layout.height = sum(child.height + dp(15) for child in content_layout.children)
        
        scroll_view.add_widget(content_layout)
        self.main_layout.add_widget(scroll_view)
        
        # 添加底部导航栏
        nav_bar = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(60),
            padding=[dp(20), dp(5), dp(20), dp(5)],
            spacing=dp(30),
            background_color=COLORS['white']
        )
        
        # 首页按钮
        home_btn = BoxLayout(orientation='vertical')
        home_icon = Label(text='🏠', font_size=FONT_SIZES['h2'])
        home_label = Label(
            text='首页',
            font_name='Chinese',
            font_size=FONT_SIZES['tiny'],
            color=COLORS['primary']  # 高亮颜色
        )
        home_btn.add_widget(home_icon)
        home_btn.add_widget(home_label)
        
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
        
        self.main_layout.add_widget(nav_bar)
        
        # 将主布局添加到屏幕
        self.add_widget(self.main_layout)
    
    def on_enter(self):
        # 屏幕进入时更新用户信息
        app = App.get_running_app()
        self.username_label.text = app.username
        self.user_avatar.source = app.user_avatar
        
        # 根据时间更新问候语
        from datetime import datetime
        hour = datetime.now().hour
        
        if 5 <= hour < 12:
            greeting = '早上好，'
        elif 12 <= hour < 18:
            greeting = '下午好，'
        else:
            greeting = '晚上好，'
        
        self.greeting_label.text = greeting
    
    def go_to_camera(self, instance):
        self.manager.current = 'camera'
    
    def go_to_history(self, instance):
        self.manager.current = 'history'
    
    def go_to_product(self, instance):
        self.manager.current = 'product'
    
    def go_to_device(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.manager.current = 'device'
            return True
    
    def go_to_profile(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # 这里可以添加个人资料页面
            return True
    
    def go_to_news(self, instance):
        self.manager.current = 'news'