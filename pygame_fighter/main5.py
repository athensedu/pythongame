"""
enemy spawns randomly
fighter can shoot
add explosion sound effect when shooting an enemy and get exploded
"""
import pygame
import random

# init Pygame
pygame.init()

# init music
pygame.mixer.init()

# screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Mini Space Fighter")

# Clock
clock = pygame.time.Clock()

# Bg img
background = pygame.image.load("background.png")

# Player img
player = pygame.image.load("player.png")
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = (screen_width / 2) - (player_width / 2)
player_y_pos = screen_height - player_height
player_speed = 10

# Enemy img
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 3

# Bullet
bullet = pygame.image.load("bullet.png")
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]
bullet_x_pos = 0
bullet_y_pos = player_y_pos
bullet_speed = 15
bullet_state = "ready"

# Sound effects - explosion
explosion_sound = pygame.mixer.Sound("explosion.wav")

# fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"

# collision detecting
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**0.5
    if distance < 27:
        return True
    else:
        return False


# main loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x_pos -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x_pos += player_speed
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_x_pos = player_x_pos
            bullet_y_pos = player_y_pos
            fire_bullet(bullet_x_pos, bullet_y_pos)

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x_pos, player_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    if bullet_state == "fire":
        screen.blit(bullet, (bullet_x_pos + player_width / 2 - bullet_width / 2, bullet_y_pos))
        bullet_y_pos -= bullet_speed

    if bullet_y_pos < 0:
        bullet_y_pos = player_y_pos
        bullet_state = "ready"

    collision = is_collision(enemy_x_pos, enemy_y_pos, bullet_x_pos, bullet_y_pos)
    if collision:
        explosion_sound.play()  # 播放爆炸声音
        bullet_y_pos = player_y_pos
        bullet_state = "ready"
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

    pygame.display.update()

pygame.quit()
