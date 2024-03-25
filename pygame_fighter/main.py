import pygame
import random

# 初始化Pygame
pygame.init()

# 设置屏幕大小
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏窗口标题
pygame.display.set_caption("Mini Fighter")

# 设置时钟
clock = pygame.time.Clock()

# 载入背景图像
background = pygame.image.load("background.png")

# 载入飞机图像
player = pygame.image.load("player.png")
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = (screen_width / 2) - (player_width / 2)
player_y_pos = screen_height - player_height

# 载入敌人图像
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 设置子弹
bullet = pygame.image.load("bullet.png")
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]
bullet_x_pos = 0
bullet_y_pos = 0
bullet_speed = 20
bullet_state = "ready"  # ready - 不能看见子弹；fire - 子弹正在移动

# 子弹发射函数
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + player_width / 2 - bullet_width / 2, y - bullet_height))

# 碰撞检测函数
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**0.5
    if distance < 27:
        return True
    else:
        return False

# 游戏主循环
running = True
while running:
    # 设置游戏帧率
    clock.tick(60)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 键盘控制
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x_pos = player_x_pos
                    bullet_y_pos = player_y_pos
                    fire_bullet(bullet_x_pos, bullet_y_pos)

    # 更新游戏状态
    if bullet_y_pos <= 0:
        bullet_y_pos = player_y_pos
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x_pos, bullet_y_pos)
        bullet_y_pos -= bullet_speed

    collision = is_collision(enemy_x_pos, enemy_y_pos, bullet_x_pos, bullet_y_pos)
    if collision:
        bullet_y_pos = player_y_pos
        bullet_state = "ready"
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

    enemy_y_pos += enemy_speed

    # 绘制背景和飞机
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 更新显示
    pygame.display.update()

# 结束Pygame
pygame.quit()
