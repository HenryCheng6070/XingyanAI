from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.app import App

class ProductScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductScreen, self).__init__(**kwargs)
        
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
            text='推荐产品',
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
        
        # 创建网格布局用于显示产品
        self.product_grid = GridLayout(
            cols=2,
            spacing=10,
            size_hint_y=None,
            padding=10
        )
        # 确保网格布局可以滚动
        self.product_grid.bind(minimum_height=self.product_grid.setter('height'))
        
        # 添加产品到网格布局
        self.scroll_view.add_widget(self.product_grid)
        self.layout.add_widget(self.scroll_view)
        
        # 将布局添加到屏幕
        self.add_widget(self.layout)
    
    def on_enter(self):
        """屏幕进入时的回调"""
        # 清空现有产品
        self.product_grid.clear_widgets()
        
        # 获取应用实例
        app = App.get_running_app()
        
        # 从数据库或API加载推荐产品
        # 这里只是示例数据
        product_data = [
            {
                "id": "p001",
                "name": "控油洁面乳",
                "price": "¥128",
                "image": "resources/product1.png",
                "description": "温和清洁，控制T区油脂分泌"
            },
            {
                "id": "p002",
                "name": "水杨酸精华",
                "price": "¥198",
                "image": "resources/product2.png",
                "description": "改善痘痘和黑头问题"
            },
            {
                "id": "p003",
                "name": "保湿面霜",
                "price": "¥168",
                "image": "resources/product3.png",
                "description": "深层滋润，改善干燥"
            },
            {
                "id": "p004",
                "name": "修复精华液",
                "price": "¥258",
                "image": "resources/product4.png",
                "description": "修复受损肌肤，增强屏障"
            }
        ]
        
        # 显示产品
        self.display_products(product_data)
    
    def go_back(self, instance):
        """返回上一屏幕"""
        self.manager.current = 'main'
    
    def display_products(self, product_data):
        """显示产品"""
        if not product_data:
            # 如果没有产品，显示提示信息
            no_data_label = Label(
                text="暂无推荐产品",
                size_hint_y=None,
                height=50
            )
            self.product_grid.add_widget(no_data_label)
            return
        
        # 添加产品项
        for product in product_data:
            # 创建产品项布局
            product_layout = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=300,
                padding=5,
                spacing=5
            )
            
            # 添加产品图片
            # 注意：如果图片不存在，将显示默认图片或空白
            product_image = Image(
                source=product.get("image", ""),
                size_hint=(1, 0.6)
            )
            product_layout.add_widget(product_image)
            
            # 添加产品名称
            name_label = Label(
                text=product["name"],
                size_hint_y=None,
                height=30,
                font_size='16sp'
            )
            product_layout.add_widget(name_label)
            
            # 添加产品价格
            price_label = Label(
                text=product["price"],
                size_hint_y=None,
                height=30,
                color=(0.8, 0.2, 0.2, 1)  # 红色价格
            )
            product_layout.add_widget(price_label)
            
            # 添加产品描述
            desc_label = Label(
                text=product["description"],
                size_hint_y=None,
                height=40,
                font_size='12sp',
                text_size=(150, None),
                halign='center'
            )
            product_layout.add_widget(desc_label)
            
            # 添加购买按钮
            buy_button = Button(
                text="立即购买",
                size_hint_y=None,
                height=40,
                background_color=(0.2, 0.7, 0.3, 1)
            )
            buy_button.bind(on_press=lambda btn, prod=product: self.buy_product(prod))
            product_layout.add_widget(buy_button)
            
            # 将产品项添加到网格布局
            self.product_grid.add_widget(product_layout)
    
    def buy_product(self, product):
        """购买产品"""
        # 在实际应用中，这里应该跳转到购买页面或添加到购物车
        # 这里只是打印信息
        print(f"购买产品: {product['name']}")
        
        # 可以跳转到购买页面
        # self.manager.current = 'purchase'