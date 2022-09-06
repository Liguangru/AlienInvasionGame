import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 使用方法get_rect访问屏幕的属性rect（矩形对象）并将其赋给self.screen_rect，使得飞船可以放置在屏幕的正确位置

        """加载飞船图像并获取外接矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小孩值
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False  # 添加属性self.moving_right并将其初始值设为False
        self.moving_left = False   # 同上

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:  # self.rect.right是飞船外接矩形右边缘的x坐标，限制飞船活动范围
            # self.moving_right为True时向右移动飞船，update通过Ship实例来调用
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:                         # self.rect.left是飞船外接矩形左边缘的x坐标，限制飞船活动范围
            # self.moving_left为True时向左移动飞船，update通过Ship实例来调用
            self.x -= self.settings.ship_speed
        """ 此处使用if而非elif，原因在于：如果玩家同时按下左右箭头键，将先增加再减少rect.x值，此时飞船位置保持不变。因为从向左切换到向右时，玩家会同时按下左右箭头键，这样飞船保持不动会更好"""
        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 定义方法blitme，将图像绘制到self.rect指定的位置
