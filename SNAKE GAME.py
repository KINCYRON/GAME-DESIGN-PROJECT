import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Set up the display
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set up the fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Set up the snake game variables
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    dis.blit(value, [10, 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close:
            dis.fill(BLUE)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(BLUE)
        pygame.draw.rect(dis, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

        clock.tick(snake_speed)


# Set up the menu options
main_options = ["Start Game", "Game Level"]
selected_option = 0

# Set up the sub-menu options
level_options = ["Level 1 (Speed: 5)", "Level 2 (Speed: 10)", "Level 3 (Speed: 15)"]
selected_level = 0

# Set up the menu fonts
menu_font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Clear the screen
    dis.fill(BLACK)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if selected_option == 1:
                if event.key == pygame.K_UP:
                    selected_level = (selected_level - 1) % len(level_options)
                elif event.key == pygame.K_DOWN:
                    selected_level = (selected_level + 1) % len(level_options)
                elif event.key == pygame.K_RETURN:
                    if selected_level == 0:
                        snake_speed = 5
                        game_loop()
                    elif selected_level == 1:
                        snake_speed = 10
                        game_loop()
                    elif selected_level == 2:
                        snake_speed = 15
                        game_loop()
            else:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(main_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(main_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        print("Starting game...")
                        game_loop()
                    elif selected_option == 1:
                        selected_level = 0
                        selected_option = 1


    # Draw the menu options
    for i, option in enumerate(main_options):
        if i == selected_option:
            text = menu_font.render(option, True, RED)
        else:
            text = menu_font.render(option, True, WHITE)
        text_rect = text.get_rect(center=(dis_width // 2, 200 + i * 70))
        dis.blit(text, text_rect)

    # Draw the sub-menu options if "Game Level" is selected
    if selected_option == 1:
        for i, level in enumerate(level_options):
            if i == selected_level:
                text = menu_font.render(level, True, RED)
            else:
                text = menu_font.render(level, True, WHITE)
            text_rect = text.get_rect(center=(dis_width // 2, 340 + i * 70))
            dis.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()