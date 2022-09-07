""" 外星人入侵游戏"""
""" By:Guangru Li"""

import sys
from time import sleep  # 飞船撞到后游戏暂停片刻

import pygame

from settings import Settings
from game_stats import Gamestats
from button import  Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()  # 初始化背景设置，使得Pygame可以正常工作
        self.settings = Settings()

        """自定义屏幕模式"""
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screem_height))
        # self.screen = pygame.display.set_mode((1200, 800))
        # # 调用set_mode来创建显示窗口，宽1200像素，高800像素，并将显示窗口赋给属性self.screen使得类中的每个对象都可以使用它

        """实现全屏模式"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width    # 无法预先知道屏幕宽度和高度，所以创建屏幕后要更新设置
        self.settings.screem_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        """创建统计游戏信息的实例"""
        self.stats = Gamestats(self)

        """创建飞船,子弹和外星人实例"""
        self.ship = Ship(self)          # 创建ship实例，()里的self指向当前AlienInvasion实例，使得Ship可以访问游戏资源（屏幕等）
        self.bullets = pygame.sprite.Group()  # 创建用于存储子弹的数组，此为Group类的一个实例，类似于列表
        self.aliens = pygame.sprite.Group()   # 创建用于存储外星人群的编组
        self._creat_fleet()                   # 调用_creat_fleet()方法

        """设置背景色"""
        self.bg_color = (230, 230, 230)  # RBG值表示颜色

        """创建Play按钮"""
        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏的主循环"""
        while True:  # 不断运行的循环，包含一个事件循环（玩家操作）以及屏幕更新代码
            """监视键盘和鼠标事件"""
            self._check_events()

            if self.stats.game_active:
                self.ship.update()      # 飞船位置将在键盘事件之后更新，但是早于屏幕刷新
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()   # 返回一个元组，其中包含玩家单击时鼠标的x和y坐标
                self._check_play_button(mouse_pos)   # 将坐标传递给方法_check_play_button

    def _check_play_button(self, mouse_pos):
        """玩家单击Play时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)  # collidepoint可以检查鼠标坐标是否在Play按钮的rect内
        if button_clicked and not self.stats.game_active:   # 游戏仅在game_active为False即游戏处于非活动状态并单击Play按钮时开始，
                                                            # 因为Play按钮即使不可见，单击其所在区域时也会响应
            # 重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并让飞船居中
            self._creat_fleet()
            self.ship.center_ship()

            # 游戏进行时隐藏鼠标
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:    # 按下右箭头向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:   # 按下左箭头向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:      # 按下Q键就退出
            sys.exit()
        elif event.key == pygame.K_SPACE:  # 按下空格键调用_fire_bullet函数发射子弹
            self._fire_bullet()

    def _check_keyup_events(self, event):
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
        for bullet in self.bullets.copy():    # 创建一个副本，使用for循环遍历副本。原因是for循环遍历列表或编组时，要求列表长度不变。
                                              # 因此不可以在for循环遍历的列表或者编组中删除元素。
            if bullet.rect.bottom <= 0:       # 检查子弹的rect的bottom属性，如果小于等于0，则子弹已经飞出屏幕
                self.bullets.remove(bullet)   # 如果是，就将其从编组bullets中删除
        # print(len(self.bullets))            # 显示子弹数量，如果逐渐变为0，则说明飞出的子弹已经删除。注意：此print仅作为测试。

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中外星人
        # 如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)    # 这里的True的作用是删除对应的实例（即子弹或者外星人），设为false则为不删除

        if not self.aliens:   # 检查aliens是否为空，若为空。相当于False，就删除子弹并更新外星人
            # 删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._creat_fleet()

    def _update_aliens(self):
        """检查是否碰到屏幕边缘并更新外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船是否碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # spritecollideany接受两个实参：一个精灵和一个编组，
                                                                    # 其作用是检查编组成员是否和精灵碰撞
                                                                    # 如果碰撞则停止遍历编组成员，并返回碰撞成员
            self._ship_hit_()

        # 检查是否有外星人到达屏幕底部
            self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """检查是否有外星人到了屏幕底部"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 和飞船被撞到一样处理
                self._ship_hit_()
                break

    def _ship_hit_(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            # 将ships_left减1
            self.stats.ships_left -= 1

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建新的外星人并将飞船放到屏幕底部中央
            self._creat_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.get_visible(True)    # 游戏进入非活动状态后鼠标可见

    def _creat_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳为多少个外星人
        # 外星人横向间距为外星人宽度
        alien = Alien(self)     # 创建一个外星人实例,用于获取宽度和高度，因此不加入编组中
        alien_width, alien_height = alien.rect.size   # 获取外星人宽度和高度
        available_space_x = self.settings.screen_width - (2 * alien_width)  # 计算可用于放置外星人的空间：屏幕宽度减去外星人宽度的两倍
        number_aliens_x = available_space_x // (2 * alien_width)   # 计算每行可容纳的外星人数量：可用空间除以外星人宽度的两倍（外星人之间留出一个宽度作为间距）

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screem_height - (3 * alien_height) - ship_height)
        # 计算可用的垂直空间：屏幕高度减去第一行外星人的上边距（外星人高度）、飞船高度以及外星人群最初与飞船之间的距离（外星人高度的两倍），从而在飞船上方留出一定的空白区域，留出射杀外星人的时间
        number_rows = available_space_y // (2 * alien_height)
        # 计算可容纳的行数：可用垂直空间除以外星人高度的两倍，使得相邻行之间的空白间距为外星人的高度

        # 创建外星人群
        for row_number in range(number_rows):
            # 创建第一行外星人
            for alien_number in range(number_aliens_x):
                self._creat_alien(alien_number, row_number)

    def _creat_alien(self, alien_number, row_number):
        # 创建一个外星人并放入当前行
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number  # 注意此处为什么使用alien.x，因为其可以存储小数值，见alien.py，下面的alien.y则不可以
        alien.rect.x = alien.x  # 每个外星人都向右推1个宽度，并将宽度乘以2以得到每个外星人占据的空间（外星人本身宽度加上右边的空白）
                                # 由此得到当前外星人在当前行的位置
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number  # 修改外星人的y坐标
        self.aliens.add(alien)  # 将其添加到用于存储外星人的编组中，外星人位置从左上角开始

    def _check_fleet_edges(self):
        """有外星人到达屏幕边缘后采取相应措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():    # 如果碰到屏幕边缘就会返回True，就会调用_change_fleet_direction()并退出循环
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移并改变移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # 方向值乘以-1，下次移动时会向反方向移动

    def _update_screen(self):   # 更新屏幕移到方法_update_screen()中
        """ 每次循环时都重绘屏幕 """
        self.screen.fill(self.settings.bg_color)  # fill用于填充屏幕，只有一个实参——颜色
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()        # bullets.sprites()返回一个列表，其中包含编组bullets中的所有sprite。
                                        # 为了绘制所有的子弹，遍历编组中的所有sprite并对每个sprite调用draw_bullet
        self.aliens.draw(self.screen)   # 绘制外星人  # draw()使用时，Pygame会将编组中的每个元素都绘制到属性rect指定的地方

        """ 如果游戏处于非活动状态就绘制Play按钮"""
        if not self.stats.game_active:
            self.play_button.draw_button()

        """让最近绘制的屏幕可见"""
        pygame.display.flip()  # 每次while循环都会绘制一个空屏幕，并擦去旧屏幕


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
