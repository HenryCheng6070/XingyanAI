from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty, NumericProperty
from app.ui.styles import COLORS, RADIUS

class RoundedTextInput(TextInput):
    border_color = ListProperty([0.9, 0.9, 0.9, 1])
    border_radius = NumericProperty(10)
    
    def __init__(self, **kwargs):
        super(RoundedTextInput, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_active = ''
        self.background_color = [1, 1, 1, 1]  # 白色背景
        self.padding = [15, 10, 15, 10]
        self.bind(size=self._update_canvas, pos=self._update_canvas)
        
    def _update_canvas(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            # 背景
            Color(1, 1, 1, 1)  # 白色
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.border_radius])
            # 边框
            Color(*self.border_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.border_radius], width=1.5)