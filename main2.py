import pygame
import sys

# مقداردهی اولیه
pygame.init()

# تنظیمات صفحه
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("بازی ساده با pygame")

# رنگ‌ها
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# مشخصات مربع
square_size = 40
x, y = WIDTH // 2, HEIGHT // 2
speed = 5

# حلقه بازی
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)  # فریم بر ثانیه

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حرکت با کلیدهای جهت‌دار
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # بررسی برخورد با لبه‌ها
    if x < 0 or x + square_size > WIDTH or y < 0 or y + square_size > HEIGHT:
        print("Game Over!")
        running = False

    # رسم
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, square_size, square_size))
    pygame.display.flip()

pygame.quit()
sys.exit()
