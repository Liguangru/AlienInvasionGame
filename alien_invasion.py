""" 外星人入侵游戏"""
""" By:Guangru Li"""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()  # 初始化背景设置，使得Pygame可以正常工作
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screem_height)
        # )
        # self.screen = pygame.display.set_mode((1200, 800))
        # # 调用set_mode来创建显示窗口，宽1200像素，高800像素，并将显示窗口赋给属性self.screen使得类中的每个对象都可以使用它

        """实现全屏模式"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width    # 无法预先知道屏幕宽度和高度，所以创建屏幕后要更新设置
        self.settings.screem_height = self.screen.get_rect().height

        pygame.display.set_caption("Alian Invasion")

        self.ship = Ship(self)
        # 设置背景色
        self.bg_color = (230, 230, 230)  # RBG值表示颜色

    def run_game(self):
        """开始游戏的主循环"""
        while True:  # 不断运行的循环，包含一个事件循环（玩家操作）以及屏幕更新代码
            """监视键盘和鼠标事件"""
            self._check_events()
            self.ship.update()   # 飞船位置将在键盘事件之后更新，但是早于屏幕刷新
            self._update_screen()

    def _check_events(self):  # 管理事件移到方法_check_events()中
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # 按下Q键就退出
            sys.exit()

    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # 如果按键松开，就将self.moving_right设为False，停止向右移动
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   # 如果按键松开，就将self.moving_left设为False，停止向右移动

    def _update_screen(self):  # 更新屏幕移到方法_update_screen()中
        """ 每次循环时都重绘屏幕 """
        self.screen.fill(self.settings.bg_color)  # fill用于填充屏幕，只有一个实参——颜色
        self.ship.blitme()
        """让最近绘制的屏幕可见"""
        pygame.display.flip()  # 每次while循环都会绘制一个空屏幕，并擦去旧屏幕


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
