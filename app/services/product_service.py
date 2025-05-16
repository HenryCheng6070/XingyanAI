class ProductService:
    def __init__(self):
        # 产品数据库，实际应用中可能从数据库或API获取
        self.products = {
            "SY001": {
                "name": "星妍控油精华液",
                "description": "针对油性皮肤，有效控制油脂分泌，保持肌肤清爽不油腻。",
                "price": 199.00,
                "image": "resources/images/product_sy001.png",
                "tags": ["控油", "精华液"]
            },
            "SY002": {
                "name": "星妍祛痘凝胶",
                "description": "温和祛痘，不刺激皮肤，有效改善痘痘问题。",
                "price": 168.00,
                "image": "resources/images/product_sy002.png",
                "tags": ["祛痘", "凝胶"]
            },
            "SY003": {
                "name": "星妍美白精华",
                "description": "有效淡化色斑，提亮肤色，改善暗沉问题。",
                "price": 258.00,
                "image": "resources/images/product_sy003.png",
                "tags": ["美白", "精华"]
            },
            "SY004": {
                "name": "星妍保湿面霜",
                "description": "深层滋润，长效保湿，改善干燥缺水问题。",
                "price": 188.00,
                "image": "resources/images/product_sy004.png",
                "tags": ["保湿", "面霜"]
            }
        }
    
    def get_product_by_id(self, product_id):
        """根据产品ID获取产品信息"""
        return self.products.get(product_id)
    
    def get_all_products(self):
        """获取所有产品"""
        return self.products
    
    def recommend_products(self, skin_analysis):
        """根据皮肤分析结果推荐产品"""
        recommendations = []
        
        # 根据皮肤类型和问题推荐产品
        if skin_analysis.get("oil", 0) > 60:
            recommendations.append(self.products["SY001"])  # 控油精华液
            
        if skin_analysis.get("acne", {}).get("count", 0) > 0:
            recommendations.append(self.products["SY002"])  # 祛痘凝胶
            
        if skin_analysis.get("pigmentation", {}).get("level") in ["中度", "严重"]:
            recommendations.append(self.products["SY003"])  # 美白精华
            
        if skin_analysis.get("moisture", 0) < 50:
            recommendations.append(self.products["SY004"])  # 保湿面霜
            
        # 如果没有推荐产品，返回所有产品
        if not recommendations:
            return list(self.products.values())
            
        return recommendations