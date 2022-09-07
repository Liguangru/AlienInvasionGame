class Settings:
    """存储游戏《外形人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screem_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 2  # 速度设置为小数方便调节，但是rect.x之可以存储整数值。所以需要在Ship类中修改

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    # 创建宽3像素，高15像素的深灰色子弹
        self.bullets_allowed = 8  # 设置最大子弹数，对同时出现在屏幕上的子弹进行限制，鼓励玩家有目标的射击敌人
