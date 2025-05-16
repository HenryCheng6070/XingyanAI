from kivy.config import Config

# 在导入其他模块之前设置
Config.set('kivy', 'default_font', ['Chinese', 'resources/fonts/msyh.ttf'])

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase

# 导入自定义模块
from app.models.database import Database
from app.ui.screens.login_screen import LoginScreen
from app.ui.screens.main_screen import MainScreen
from app.ui.screens.camera_screen import CameraScreen
from app.ui.screens.analysis_screen import AnalysisScreen
from app.ui.screens.history_screen import HistoryScreen
from app.ui.screens.product_screen import ProductScreen
from app.ui.screens.register_screen import RegisterScreen

# 注册中文字体
LabelBase.register(name='Chinese', 
                  fn_regular='resources/fonts/msyh.ttf')  # 使用微软雅黑或其他中文字体

# 设置窗口大小模拟手机屏幕
Window.size = (400, 700)

class XingYanAIApp(App):
    def build(self):
        # 初始化数据库
        self.db = Database()
        
        # 创建屏幕管理器
        self.sm = ScreenManager()
        
        # 添加各个屏幕
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(CameraScreen(name='camera'))
        self.sm.add_widget(AnalysisScreen(name='analysis'))
        self.sm.add_widget(HistoryScreen(name='history'))
        self.sm.add_widget(ProductScreen(name='product'))
        
        # 设置初始屏幕
        return self.sm
    
    def on_stop(self):
        # 应用关闭时关闭数据库连接
        self.db.close()

if __name__ == '__main__':
    XingYanAIApp().run()