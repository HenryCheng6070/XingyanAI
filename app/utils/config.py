import json
import os

CONFIG_FILE = 'resources/config.json'

def get_config():
    """
    获取应用配置
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"读取配置文件出错: {str(e)}")
    
    # 返回默认配置
    return {
        "coze_api_key": "your_api_key_here",
        "coze_api_url": "https://api.coze.com",
        "app_name": "星妍AI",
        "version": "1.0.0"
    }

def save_config(config):
    """
    保存应用配置
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"保存配置文件出错: {str(e)}")
        return False