import pygame
import random
import time

width = 780
height = 600

white = (255,255,255)
black = (0,0,0)

snake_block = 30

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message(screen):
    screen.fill(white)

    largeText = pygame.font.SysFont('Arial', 30)
    TextSurf, TextRect = text_objects('Game Over', largeText)
    TextRect.center = ((width/2), (height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

def die():
    pass

def snake(screen,x_pos, y_pos, size):
    for i in size:
        pygame.draw.rect(screen, black, [i[0], i[1], snake_block, snake_block])

def food(screen, foodx, foody):
    pygame.draw.rect(screen, black, [foodx, foody, snake_block, snake_block])

def gameloop():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    x = 0
    y = 0

    running = True
    count = 1
    x_change = 0
    y_change = 0

    length_of_snake = 1
    snake_List = [[x, y]]

    foodx = round(random.randrange(0, width-snake_block)/snake_block)*snake_block
    foody = round(random.randrange(0, height-snake_block)/snake_block)*snake_block
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = snake_block
                if event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -snake_block
                if event.key == pygame.K_LEFT and x_change == 0:
                    y_change = 0
                    x_change = -snake_block
                if event.key == pygame.K_RIGHT and x_change == 0:
                    y_change = 0
                    x_change = snake_block


        y += y_change
        x += x_change

        screen.fill(white)

        snake_List.append([x,y])

        if len(snake_List) > length_of_snake:
            del snake_List[0]

        snake(screen, x, y, snake_List)
        food(screen, foodx, foody)

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width-snake_block)/snake_block)*snake_block
            foody = round(random.randrange(0, height-snake_block)/snake_block)*snake_block
            length_of_snake += 1
            print(f'foodx = {foodx}, foody = {foody}')
        #print(x, y)
        pygame.display.update()
        if x > width-snake_block or x < 0 or y > height or y < 0:
            running = False
            message(screen)
        clock.tick(10)          #snake speed or fps
    pygame.quit()

if __name__ == "__main__":

    gameloop()