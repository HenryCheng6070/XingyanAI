from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.app import App

class AnalysisScreen(Screen):
    def __init__(self, **kwargs):
        super(AnalysisScreen, self).__init__(**kwargs)
        
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
            text='皮肤分析结果',
            font_size='24sp',
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.title_label)
        
        # 添加图片显示区域
        self.image_display = Image(
            source='',  # 将在显示分析时设置
            size_hint=(1, 0.5)
        )
        self.layout.add_widget(self.image_display)
        
        # 添加分析结果区域
        self.result_label = Label(
            text='正在加载分析结果...',
            size_hint=(1, 0.3),
            halign='left',
            valign='top',
            text_size=(400, None)
        )
        self.layout.add_widget(self.result_label)
        
        # 添加产品推荐按钮
        self.product_button = Button(
            text='查看推荐产品',
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0.7, 0.3, 1)
        )
        self.product_button.bind(on_press=self.view_products)
        self.layout.add_widget(self.product_button)
        
        # 将布局添加到屏幕
        self.add_widget(self.layout)
        
    def on_enter(self):
        """屏幕进入时的回调"""
        # 获取应用实例
        app = App.get_running_app()
        
        # 在实际应用中，这里应该从应用状态获取分析结果
        # 这里只是示例
        self.display_analysis_result({
            "skin_type": "混合性皮肤",
            "oil_level": "T区油性较高",
            "hydration": "两颊偏干",
            "issues": ["轻微痘痘", "黑头"]
        })
    
    def go_back(self, instance):
        """返回上一屏幕"""
        self.manager.current = 'main'
    
    def display_analysis_result(self, result):
        """显示分析结果"""
        # 在实际应用中，这里应该显示从API获取的分析结果
        # 这里只是示例
        result_text = f"""
皮肤类型: {result['skin_type']}
油脂分泌: {result['oil_level']}
水分状况: {result['hydration']}
皮肤问题: {', '.join(result['issues'])}

建议:
1. 使用温和的洁面产品
2. 注意T区控油
3. 两颊需要补充水分
4. 使用含有水杨酸的产品改善痘痘问题
        """
        
        self.result_label.text = result_text
    
    def view_products(self, instance):
        """查看推荐产品"""
        self.manager.current = 'product'