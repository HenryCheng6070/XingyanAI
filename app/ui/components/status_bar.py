from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
from kivy.properties import StringProperty
from app.ui.styles import COLORS, FONT_SIZES

class StatusBar(BoxLayout):
    time_text = StringProperty('9:41')
    
    def __init__(self, **kwargs):
        super(StatusBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = '30dp'
        self.padding = [10, 0, 10, 0]
        
        # 创建时间标签
        self.time_label = Label(
            text=self.time_text,
            size_hint_x=None,
            width='50dp',
            font_size=FONT_SIZES['small'],
            color=[0.2, 0.2, 0.2, 1]
        )
        self.add_widget(self.time_label)
        
        # 创建空白区域
        self.add_widget(BoxLayout())
        
        # 创建信号图标（简化为文本）
        signal_label = Label(
            text='●●●●',
            size_hint_x=None,
            width='50dp',
            font_size=FONT_SIZES['small'],
            color=[0.2, 0.2, 0.2, 1]
        )
        self.add_widget(signal_label)
        
        # 创建电池图标（简化为文本）
        battery_label = Label(
            text='100%',
            size_hint_x=None,
            width='50dp',
            font_size=FONT_SIZES['small'],
            color=[0.2, 0.2, 0.2, 1]
        )
        self.add_widget(battery_label)
        
        # 更新时间
        Clock.schedule_interval(self.update_time, 60)
        self.update_time(0)
    
    def update_time(self, dt):
        current_time = datetime.now()
        self.time_text = current_time.strftime('%H:%M')
        self.time_label.text = self.time_text