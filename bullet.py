import pygame
from pygame.sprite import Sprite  # 继承了从模块pygame.sprite导入的Sprite类（精灵类）


class Bullet(Sprite):
    """管理飞船所发射子弹的类"""

    def __init__(self, ai_game):
        """在飞船当前位置创建一个子对象"""
        super().__init__()  # 调用super来继承Sprite，super函数可以自动搜索所有的父类方法并导入self，完成初始化
                            # 在这里，就是使用Sprite中的__init__来初始化Bullet

        # 定义用于存储屏幕以及设置对象和子弹颜色的属性
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在（0，0）创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,  # 创建子弹属性rect，子弹并非基于图像，因此使用pygame.Rect()从头开始创建。
                                self.settings.bullet_height)       # 设置初始位置（0， 0）,宽度和高度由self.settings获取。
        self.rect.midtop = ai_game.ship.rect.midtop                # 这里设置真正的子弹位置，即飞船的顶部。

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)     # y坐标存储为小数值，以便可以微调子弹的速度

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed   # 子弹向上移动，所以其x坐标不变，y坐标的值不断减小，因为左上角为（0，0）
        # 更新表示子弹位置的rect的位置
        self.rect.y = self.y                   # 将self.rect.y设置为self.y的值

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)   # draw.rect()函数使用存储在self.color中的颜色填充子弹的rect区域

