# AlienInvasionGame
《Python编程-入门到实践》书中的实例项目1
## alien_invasion.py
包含**AlienInvasion**类，这个类创建一系列游戏中所需要的属性：赋给self.settings的设置，赋给screen中的主显示surface，以及飞船、子弹等实例。  
此外还包含游戏的主循环，即while循环。while循环中调用_check_events()、ship.update()和_update_screen()。  
方法_check_events()检测相关的事件（例如按下和松开按键），并通过调用方法_check_keydown_events()和_check_keyup_events()处理这些事件。这些方法主要负责飞船的移动。  
**玩游戏时只需运行文件alian_invasion.py**

## settings.py
文件setteings.py包含**Settings**类，这个类只包含方法__int__()，用于初始化控制游戏外观和飞船速度的属性。  

## ship.py
文件ship.py包含**Ship**类，这个类包含方法__int__()、管理飞船位置的方法update()和在屏幕上绘制飞船的方法blitme()。飞船图形位于images文件夹的ship.bmp。  

