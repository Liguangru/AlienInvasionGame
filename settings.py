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
