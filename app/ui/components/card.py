from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty, NumericProperty
from app.ui.styles import COLORS, RADIUS

class Card(BoxLayout):
    background_color = ListProperty([1, 1, 1, 1])  # 白色背景
    border_radius = NumericProperty(10)
    elevation = NumericProperty(2)
    
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)
        self.padding = [15, 15, 15, 15]
        self.bind(size=self._update_canvas, pos=self._update_canvas)
        
    def _update_canvas(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            # 阴影效果（简化版）
            Color(0.9, 0.9, 0.9, 0.5)
            RoundedRectangle(pos=[self.pos[0]+self.elevation, self.pos[1]-self.elevation], 
                             size=self.size, radius=[self.border_radius])
            # 背景
            Color(*self.background_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.border_radius])