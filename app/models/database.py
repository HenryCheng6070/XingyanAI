import sqlite3
import os
import json
from datetime import datetime

class Database:
    def __init__(self, db_path="resources/xingyan.db"):
        self.db_path = db_path
        self.conn = None
        self.init_db()
        self.migrate_db()
    
    def init_db(self):
        """初始化数据库"""
        # 确保目录存在
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        
        # 创建用户表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            age INTEGER,
            skin_type TEXT,
            is_logged_in INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # 创建分析记录表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            image_path TEXT,
            analysis_result TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''')
        
        self.conn.commit()
    
    def register_user(self, username, password, age=None, skin_type=None):
        """注册新用户"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password, age, skin_type) VALUES (?, ?, ?, ?)",
                (username, password, age, skin_type)
            )
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None  # 用户名已存在
    
    def login_user(self, username, password):
        """用户登录"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        
        if user and self.verify_password(password, user[2]):  # 假设第3列是密码
            # 更新登录状态
            cursor.execute("UPDATE users SET is_logged_in = 0")  # 先将所有用户设为未登录
            cursor.execute("UPDATE users SET is_logged_in = 1 WHERE id = ?", (user[0],))
            self.conn.commit()
            return True
        return False

    def logout_user(self):
        """用户退出登录"""
        cursor = self.conn.cursor()
        cursor.execute("UPDATE users SET is_logged_in = 0")
        self.conn.commit()
        
        def save_analysis(self, user_id, image_path, analysis_result):
            """保存分析结果"""
            cursor = self.conn.cursor()
            # 如果analysis_result是字典，转换为JSON字符串
            if isinstance(analysis_result, dict):
                analysis_result = json.dumps(analysis_result)
                
            cursor.execute(
                "INSERT INTO analysis_records (user_id, image_path, analysis_result) VALUES (?, ?, ?)",
                (user_id, image_path, analysis_result)
            )
            self.conn.commit()
            return cursor.lastrowid
    
    def get_user_history(self, user_id):
        """获取用户历史分析记录"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT id, image_path, analysis_result, created_at FROM analysis_records WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,)
        )
        records = cursor.fetchall()
        result = []
        for record in records:
            # 将JSON字符串转换回字典
            try:
                analysis = json.loads(record[2])
            except:
                analysis = record[2]
                
            result.append({
                'id': record[0],
                'image_path': record[1],
                'analysis': analysis,
                'created_at': record[3]
            })
        return result
    
    def get_analysis_by_id(self, analysis_id):
        """根据ID获取分析记录"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT image_path, analysis_result FROM analysis_records WHERE id = ?",
            (analysis_id,)
        )
        record = cursor.fetchone()
        if record:
            try:
                analysis = json.loads(record[1])
            except:
                analysis = record[1]
            return {
                'image_path': record[0],
                'analysis': analysis
            }
        return None
    
    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()

    def migrate_db(self):
            """数据库迁移，添加新列"""
            cursor = self.conn.cursor()
            
            # 检查 is_logged_in 列是否存在
            cursor.execute("PRAGMA table_info(users)")
            columns = [column[1] for column in cursor.fetchall()]
            
            # 如果 is_logged_in 列不存在，则添加
            if 'is_logged_in' not in columns:
                cursor.execute("ALTER TABLE users ADD COLUMN is_logged_in INTEGER DEFAULT 0")
                self.conn.commit() 
    def get_logged_in_user(self):
        """获取当前登录用户信息"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE is_logged_in = 1 LIMIT 1")
        user = cursor.fetchone()
        
        if user:
            # 返回用户信息字典
            return {
                'id': user[0],
                'username': user[1],
                # 不返回密码
                'age': user[3],
                'skin_type': user[4],
                'created_at': user[5]
            }
        return None