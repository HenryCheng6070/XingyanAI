from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, ColorProperty
from kivy.graphics import Color, Line, Ellipse
from kivy.metrics import dp
import math

class CircularProgress(Widget):
    """
    圆形进度指示器组件
    用于显示皮肤检测进度或结果的百分比
    """
    progress = NumericProperty(0)  # 进度值 (0-100)
    thickness = NumericProperty(dp(5))  # 圆环厚度
    cap_style = StringProperty('round')  # 线条端点样式
    cap_precision = NumericProperty(10)  # 端点精度
    progress_color = ColorProperty([0.4, 0.6, 0.8, 1])  # 进度条颜色
    background_color = ColorProperty([0.9, 0.9, 0.9, 1])  # 背景颜色
    text_color = ColorProperty([0.2, 0.2, 0.2, 1])  # 文字颜色
    text = StringProperty('')  # 显示的文本
    
    def __init__(self, **kwargs):
        super(CircularProgress, self).__init__(**kwargs)
        self.bind(
            progress=self.update_canvas,
            size=self.update_canvas,
            pos=self.update_canvas,
            thickness=self.update_canvas,
            progress_color=self.update_canvas,
            background_color=self.update_canvas
        )
        self.update_canvas()
    
    def update_canvas(self, *args):
        self.canvas.clear()
        
        # 计算圆的中心和半径
        center_x = self.center_x
        center_y = self.center_y
        radius = min(self.width, self.height) / 2 - self.thickness
        
        # 绘制背景圆环
        with self.canvas:
            Color(*self.background_color)
            Line(
                circle=(center_x, center_y, radius),
                width=self.thickness,
                cap=self.cap_style
            )
            
            # 绘制进度圆弧
            if self.progress > 0:
                Color(*self.progress_color)
                # 计算角度 (0度在右侧，逆时针方向)
                angle_start = 0
                angle_end = self.progress / 100 * 360
                
                # 使用Line绘制圆弧
                Line(
                    ellipse=(center_x - radius, center_y - radius, radius * 2, radius * 2, 
                            angle_start, angle_end),
                    width=self.thickness,
                    cap=self.cap_style
                )