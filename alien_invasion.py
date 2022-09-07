""" 外星人入侵游戏"""
""" By:Guangru Li"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()  # 初始化背景设置，使得Pygame可以正常工作
        self.settings = Settings()

        """自定义屏幕模式"""
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

        """创建飞船和子弹实例"""
        self.ship = Ship(self)          # 创建一个ship实例，()里的self指向当前AlienInvasion实例，使得Ship可以访问游戏资源（屏幕等）
        self.bullets = pygame.sprite.Group()  # 创建用于存储子弹的数组，此为Group类的一个实例，类似于列表

        """设置背景色"""
        self.bg_color = (230, 230, 230)  # RBG值表示颜色

    def run_game(self):
        """开始游戏的主循环"""
        while True:  # 不断运行的循环，包含一个事件循环（玩家操作）以及屏幕更新代码
            """监视键盘和鼠标事件"""
            self._check_events()
            self.ship.update()      # 飞船位置将在键盘事件之后更新，但是早于屏幕刷新
            self._update_bullets()
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
        if event.key == pygame.K_RIGHT:    # 按下右箭头向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:   # 按下左箭头向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:      # 按下Q键就退出
            sys.exit()
        elif event.key == pygame.K_SPACE:  # 按下空格键调用_fire_bullet函数发射子弹
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # 如果按键松开，就将self.moving_right设为False，停止向右移动
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   # 如果按键松开，就将self.moving_left设为False，停止向右移动

    def _fire_bullet(self):
        """创建新子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:  # 判断子弹是否已经用尽
            new_bullet = Bullet(self)     # 创建Bullet实例并赋给new_bullet
            self.bullets.add(new_bullet)  # 使用add()将new_bullet加入编组bullets,add类似append

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()  # 更新子弹的位置

        # 删除飞出屏幕的子弹
        for bullet in self.bullets.copy():  # 创建一个副本，使用for循环遍历副本。原因是for循环遍历列表或编组时，要求列表长度不变。
            # 因此不可以在for循环遍历的列表或者编组中删除元素。
            if bullet.rect.bottom <= 0:  # 检查子弹的rect的bottom属性，如果小于等于0，则子弹已经飞出屏幕
                self.bullets.remove(bullet)  # 如果是，就将其从编组bullets中删除
        # print(len(self.bullets))            # 显示子弹数量，如果逐渐变为0，则说明飞出的子弹已经删除。注意：此print仅作为测试。

    def _update_screen(self):  # 更新屏幕移到方法_update_screen()中
        """ 每次循环时都重绘屏幕 """
        self.screen.fill(self.settings.bg_color)  # fill用于填充屏幕，只有一个实参——颜色
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        # bullets.sprites()返回一个列表，其中包含编组bullets中的所有sprite。
                                        # 为了绘制所有的子弹，遍历编组中的所有sprite并对每个sprite调用draw_bullet

        """让最近绘制的屏幕可见"""
        pygame.display.flip()  # 每次while循环都会绘制一个空屏幕，并擦去旧屏幕


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
