"""
星妍AI应用的通用样式定义
"""

# 颜色定义
COLORS = {
    'primary': '#6E8CA0',  # 主色调（蓝灰色）
    'primary_light': '#A5BFD3',  # 浅主色调
    'secondary': '#78C4D4',  # 次要色调（浅蓝色）
    'background': '#F5F7FA',  # 背景色（浅灰色）
    'text': '#333333',  # 文本颜色（深灰色）
    'text_light': '#888888',  # 浅文本颜色
    'white': '#FFFFFF',  # 白色
    'success': '#4CAF50',  # 成功色（绿色）
    'warning': '#FFC107',  # 警告色（黄色）
    'error': '#F44336',  # 错误色（红色）
    'border': '#E0E0E0',  # 边框颜色
}

# 字体大小
FONT_SIZES = {
    'h1': '26sp',
    'h2': '22sp',
    'h3': '18sp',
    'body': '16sp',
    'small': '14sp',
    'tiny': '12sp',
}

# 间距
SPACING = {
    'xs': '5dp',
    'sm': '10dp',
    'md': '15dp',
    'lg': '20dp',
    'xl': '30dp',
}

# 圆角
RADIUS = {
    'small': '5dp',
    'medium': '10dp',
    'large': '15dp',
    'circle': '50dp',
}

# 阴影
ELEVATION = {
    'none': '0dp',
    'small': '2dp',
    'medium': '4dp',
    'large': '8dp',
}

# 按钮样式
BUTTON_STYLES = {
    'primary': {
        'background_color': COLORS['primary'],
        'color': COLORS['white'],
        'font_size': FONT_SIZES['body'],
        'height': '50dp',
        'border_radius': RADIUS['medium'],
    },
    'secondary': {
        'background_color': COLORS['secondary'],
        'color': COLORS['white'],
        'font_size': FONT_SIZES['body'],
        'height': '50dp',
        'border_radius': RADIUS['medium'],
    },
    'text': {
        'background_color': (0, 0, 0, 0),
        'color': COLORS['primary'],
        'font_size': FONT_SIZES['body'],
        'height': '40dp',
        'border_radius': RADIUS['small'],
    }
}

# 输入框样式
INPUT_STYLES = {
    'default': {
        'height': '50dp',
        'background_color': COLORS['white'],
        'border_color': COLORS['border'],
        'border_width': '1dp',
        'padding': SPACING['sm'],
        'font_size': FONT_SIZES['body'],
        'border_radius': RADIUS['medium'],
    }
}

# 卡片样式
CARD_STYLES = {
    'default': {
        'background_color': COLORS['white'],
        'border_radius': RADIUS['medium'],
        'padding': SPACING['md'],
        'elevation': ELEVATION['small'],
    }
}