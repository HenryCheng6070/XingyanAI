"""
星妍AI应用的通用样式定义
"""

def hex_to_rgba(hex_color):
    """将十六进制颜色代码转换为RGBA格式（0-1范围）"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4))
        return (r, g, b, 1)
    elif len(hex_color) == 8:
        r, g, b, a = tuple(int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4, 6))
        return (r, g, b, a)
    else:
        raise ValueError(f"无效的十六进制颜色代码: {hex_color}")

# 十六进制颜色定义（用于参考）
HEX_COLORS = {
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
    'text_secondary': '#757575',
}

# 颜色定义（Kivy兼容的RGBA格式）
COLORS = {
    'primary': hex_to_rgba('#6E8CA0'),
    'primary_light': hex_to_rgba('#A5BFD3'),
    'secondary': hex_to_rgba('#78C4D4'),
    'background': hex_to_rgba('#F5F7FA'),
    'text': hex_to_rgba('#333333'),
    'text_light': hex_to_rgba('#888888'),
    'white': hex_to_rgba('#FFFFFF'),
    'success': hex_to_rgba('#4CAF50'),
    'warning': hex_to_rgba('#FFC107'),
    'error': hex_to_rgba('#F44336'),
    'border': hex_to_rgba('#E0E0E0'),
    'text_secondary': hex_to_rgba('#757575'),
    'text_primary': hex_to_rgba('#333333'),  # 添加这一行，使用与'text'相同的颜色值
}

# 字体大小
FONT_SIZES = {
    'h1': '26sp',
    'h2': '22sp',
    'h3': '18sp',
    'body': '16sp',
    'small': '14sp',
    'tiny': '12sp',
    'button': '18sp',
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