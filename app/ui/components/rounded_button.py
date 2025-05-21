from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty, NumericProperty, StringProperty
from app.ui.styles import COLORS, RADIUS

class RoundedButton(Button):
    background_color = ListProperty([0, 0, 0, 0])  # 透明背景
    border_radius = NumericProperty(10)
    btn_color = ListProperty([0.6, 0.7, 0.8, 1])
    
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = [0, 0, 0, 0]  # 透明背景
        self.bind(size=self._update_canvas, pos=self._update_canvas)
        
    def _update_canvas(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.btn_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.border_radius])