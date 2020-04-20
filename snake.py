import pygame
import time
import random

pygame.init()

dis_width = 800
dis_height = 600

#Colors
white =(255, 255,255)
black =(0,0,0)
red= (255,0,0)
green = (50,205,50)


#Display
screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

snake_block = 20
snake_speed = 15

clock = pygame.time.Clock()                 #For Referesh rate/ Snake's speed

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("Hack",35)

def Your_score(score):
    value = score_font.render("Your Score: "+ str(score), True, red)
    screen.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, red, [x[0],x[1],snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width/3, dis_height/3])

def gameloop():
    close = False
    run = False

    x1 = dis_width/2                                     #snake's position on x
    y1 = dis_height/2                                     #snake's position on y

    x1_change = 0                               #change in position
    y1_change = 0                               #change in position

    snake_list = []
    length_of_snake = 1

    fx = round(random.randrange(0, dis_width -snake_block)/10.0)* 10.0
    fy = round(random.randrange(0, dis_width -snake_block)/10.0)* 10.0

    while not run:
        while close == True:
            screen.fill(white)
            message("you lost noob!", red)
            Your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = True
                        close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 <= 0 or y1 >= dis_height or y1 <= 0:
            run = True

        x1 += x1_change
        y1 += y1_change

        screen.fill(white)
        pygame.draw.rect(screen, green, [fx,fy, snake_block,snake_block])     #food

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == fx and y1 == fy:
            fx = round(random.randrange(0, dis_width -snake_block)/10.0)* 10.0
            fy = round(random.randrange(0, dis_width -snake_block)/10.0)* 10.0
            length_of_snake += 1

        clock.tick(snake_speed)                          #snake's speed

    pygame.quit()
    quit()





gameloop()
