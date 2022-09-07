class Settings:
    """存储游戏《外形人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screem_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 2  # 速度设置为小数方便调节，但是rect.x之可以存储整数值。所以需要在Ship类中修改
        self.ship_limit = 5  # 玩家拥有的飞船数量

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    # 创建宽3像素，高15像素的深灰色子弹
        self.bullets_allowed = 8  # 设置最大子弹数，对同时出现在屏幕上的子弹进行限制，鼓励玩家有目标的射击敌人

        # 外星人设置
        self.alien_speed = 1.0   # 设置外星人速度
        self.fleet_drop_speed = 10
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1  # 设为2表示玩家每提高一个等级游戏节奏就翻一倍，设为1表示节奏不变

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的节奏"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 represents right; = -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
