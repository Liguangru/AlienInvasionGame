""" 外星人入侵游戏"""
""" By:Guangru Li"""
import sys
import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def_init_(self):
    """ 初始化游戏并创建游戏资源"""
    pygame.init()

    self.screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alian Invasion")