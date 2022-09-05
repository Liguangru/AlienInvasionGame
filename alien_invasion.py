""" 外星人入侵游戏"""
""" By:Guangru Li"""

import sys
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()  ##初始化背景设置，使得Pygame可以正常工作

        self.screen = pygame.display.set_mode((1200, 800))
        ##调用set_mode来创建显示窗口，宽1200像素，高800像素，并将显示窗口赋给属性self.screen使得类中的每个对象都可以使用它
        pygame.display.set_caption("Alian Invasion")

        ## 设置背景色
        self.bg_color = (230, 230, 230)  ##RBG值表示颜色

    def run_game(self):
        """开始游戏的主循环"""
        while True:  ##不断运行的循环，包含一个事件循环（玩家操作）以及屏幕更新代码
            """监视键盘和鼠标事件"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            """每次循环时都重绘屏幕"""
            self.screen.fill(self.bg_color) ##fill用于填充屏幕，只有一个实参——颜色

            """让最近绘制的屏幕可见"""
            pygame.display.flip()  ##每次while循环都会绘制一个空屏幕，并擦去旧屏幕


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    ai = AlienInvasion()
    ai.run_game()
