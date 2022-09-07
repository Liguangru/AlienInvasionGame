import pygame.font


class Button:

    def __init__(self, ai_game, msg):  # msg是按钮中显示的文本
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # 指定文本字体

        # 创建按钮的rect对象并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  # 按钮center属性，居中在屏幕中央

        # 按钮的标签只需创建一次
        self._prep_msg(msg)   # 调用_prep_msg来渲染

    def _prep_msg(self, msg):  # 接受实参self和需要渲染为图像的文本（msg）
        """将msg渲染为图像，并位于按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # font.render将msg中的文本转换为图像并存储在self.msg_image中
        # font.render还接受一个布尔实参，制定开启还是关闭反锯齿功能（反锯齿使得文本边缘更加平滑）
        # 余下的两个实参分别是文本颜色和背景色
        self.msg_image_rect = self.msg_image.get_rect()   # 根据文本图像创建一个rect
        self.msg_image_rect.center = self.rect.center     # 将其center属性设置为按钮的center属性

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

