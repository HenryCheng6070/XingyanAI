from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)
        
        # 创建主布局
        self.layout = BoxLayout(orientation='vertical', padding=10)
        
        # 添加返回按钮
        self.back_button = Button(
            text='返回',
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'left': 1}
        )
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)
        
        # 添加标题
        self.title_label = Label(
            text='历史记录',
            font_size='24sp',
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.title_label)
        
        # 创建滚动视图
        self.scroll_view = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False,
            do_scroll_y=True
        )
        
        # 创建网格布局用于显示历史记录
        self.history_grid = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None,
            padding=10
        )
        # 确保网格布局可以滚动
        self.history_grid.bind(minimum_height=self.history_grid.setter('height'))
        
        # 添加历史记录到网格布局
        self.scroll_view.add_widget(self.history_grid)
        self.layout.add_widget(self.scroll_view)
        
        # 将布局添加到屏幕
        self.add_widget(self.layout)
    
    def on_enter(self):
        """屏幕进入时的回调"""
        # 清空现有历史记录
        self.history_grid.clear_widgets()
        
        # 获取应用实例
        app = App.get_running_app()
        
        # 从数据库加载历史记录
        # 这里应该从app.db获取历史记录
        # 这里只是示例数据
        history_data = [
            {"date": "2025-05-15", "skin_type": "混合性皮肤", "issues": ["轻微痘痘", "黑头"]},
            {"date": "2025-05-10", "skin_type": "干性皮肤", "issues": ["干燥", "细纹"]},
            {"date": "2025-05-05", "skin_type": "油性皮肤", "issues": ["油光", "毛孔粗大"]}
        ]
        
        # 显示历史记录
        self.display_history(history_data)
    
    def go_back(self, instance):
        """返回上一屏幕"""
        self.manager.current = 'main'
    
    def display_history(self, history_data):
        """显示历史记录"""
        if not history_data:
            # 如果没有历史记录，显示提示信息
            no_data_label = Label(
                text="暂无历史记录",
                size_hint_y=None,
                height=50
            )
            self.history_grid.add_widget(no_data_label)
            return
        
        # 添加历史记录项
        for item in history_data:
            # 创建历史记录项布局
            item_layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=150,
                padding=10,
                spacing=5
            )
            
            # 添加日期
            date_label = Label(
                text=f"日期: {item['date']}",
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(400, None)
            )
            item_layout.add_widget(date_label)
            
            # 添加皮肤类型
            skin_type_label = Label(
                text=f"皮肤类型: {item['skin_type']}",
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(400, None)
            )
            item_layout.add_widget(skin_type_label)
            
            # 添加皮肤问题
            issues_label = Label(
                text=f"皮肤问题: {', '.join(item['issues'])}",
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(400, None)
            )
            item_layout.add_widget(issues_label)
            
            # 添加查看详情按钮
            details_button = Button(
                text="查看详情",
                size_hint_y=None,
                height=40
            )
            details_button.bind(on_press=lambda btn, item=item: self.view_details(item))
            item_layout.add_widget(details_button)
            
            # 添加分隔线
            separator = BoxLayout(
                size_hint_y=None,
                height=1
            )
            # 添加背景颜色
            with separator.canvas.before:
                Color(0.8, 0.8, 0.8, 1)  # 设置颜色 (灰色)
                Rectangle(pos=separator.pos, size=separator.size)  # 绘制矩形
            
            # 绑定更新函数以确保矩形跟随分隔线的位置和大小
            def update_rect(instance, value):
                instance.canvas.before.clear()
                with instance.canvas.before:
                    Color(0.8, 0.8, 0.8, 1)
                    Rectangle(pos=instance.pos, size=instance.size)
            
            separator.bind(pos=update_rect, size=update_rect)
            
            # 将历史记录项添加到网格布局
            self.history_grid.add_widget(item_layout)
            self.history_grid.add_widget(separator)
    
    def view_details(self, item):
        """查看历史记录详情"""
        # 在实际应用中，这里应该跳转到详情页面
        # 这里只是打印信息
        print(f"查看详情: {item}")
        
        # 可以跳转到分析页面并传递历史数据
        app = App.get_running_app()
        # 设置当前分析数据
        # app.current_analysis = item
        # 跳转到分析页面
        self.manager.current = 'analysis'