import pygame
import sys
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutlarını ayarla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Yılan Oyunu")

# Renkler
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Yılan ayarları
snake_block = 20
snake_speed = 15

# Font ayarları
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Meyve konumu
    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("Kaybettin! C - Tekrar, Q - Çıkış", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()