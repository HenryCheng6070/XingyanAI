from kivy.config import Config

# 在导入其他模块之前设置
Config.set('kivy', 'default_font', ['Chinese', 'resources/fonts/msyh.ttf'])

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock

# 导入自定义模块
from app.models.database import Database
from app.ui.screens.login_screen import LoginScreen
from app.ui.screens.main_screen import MainScreen
from app.ui.screens.camera_screen import CameraScreen
from app.ui.screens.analysis_screen import AnalysisScreen
from app.ui.screens.history_screen import HistoryScreen
from app.ui.screens.product_screen import ProductScreen
from app.ui.screens.register_screen import RegisterScreen
from app.ui.screens.welcome_screen import WelcomeScreen
from app.ui.screens.device_screen import DeviceScreen
from app.ui.screens.report_screen import ReportScreen
from app.ui.screens.news_screen import NewsScreen

# 注册中文字体
LabelBase.register(name='Chinese', 
                  fn_regular='resources/fonts/msyh.ttf')  # 使用微软雅黑或其他中文字体

# 设置窗口大小模拟手机屏幕
Window.size = (400, 700)

class XingYanAIApp(App):
    # 用户信息
    username = StringProperty("")
    user_avatar = StringProperty("resources/images/default_avatar.png")
    
    def build(self):
        # 初始化数据库
        self.db = Database()
        
        # 加载KV文件
        Builder.load_file('app/ui/styles/main.kv')
        
        # 创建屏幕管理器，使用滑动过渡效果
        self.sm = ScreenManager(transition=SlideTransition())
        
        # 添加各个屏幕
        self.sm.add_widget(WelcomeScreen(name='welcome'))
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(CameraScreen(name='camera'))
        self.sm.add_widget(AnalysisScreen(name='analysis'))
        self.sm.add_widget(HistoryScreen(name='history'))
        self.sm.add_widget(ProductScreen(name='product'))
        self.sm.add_widget(DeviceScreen(name='device'))
        self.sm.add_widget(ReportScreen(name='report'))
        self.sm.add_widget(NewsScreen(name='news'))
        
        # 设置初始屏幕
        return self.sm
    
    def on_start(self):
        # 检查是否有保存的登录状态
        user_data = self.db.get_logged_in_user()
        if user_data:
            self.username = user_data.get('username', 'User')
            self.user_avatar = user_data.get('avatar', 'resources/images/default_avatar.png')
            Clock.schedule_once(lambda dt: self.set_screen('main'), 2)
        else:
            Clock.schedule_once(lambda dt: self.set_screen('welcome'), 2)
    
    def set_screen(self, screen_name):
        self.sm.current = screen_name
    
    def login_user(self, username, avatar=None):
        self.username = username
        if avatar:
            self.user_avatar = avatar
        self.set_screen('main')
    
    def logout_user(self):
        self.username = ""
        self.user_avatar = "resources/images/default_avatar.png"
        self.db.logout_user()
        self.set_screen('welcome')
    
    def on_stop(self):
        # 应用关闭时关闭数据库连接
        self.db.close()

if __name__ == '__main__':
    XingYanAIApp().run()