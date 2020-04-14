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
blue = (0,0,255)


#Display
screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

snake_body = 10
snake_speed = 30

clock = pygame.time.Clock()                 #For Referesh rate/ Snake's speed
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_width/3, dis_height/3])

def gameloop():
    close = False
    run = False

    x = dis_width/2                                     #snake's position on x
    y = dis_height/2                                     #snake's position on y

    x1_change = 0                               #change in position
    y1_change = 0                               #change in position


    fx = round(random.randrange(0, 800 - 10)/ 10.0)* 10.0
    fy = round(random.randrange(0, 800 - 10)/ 10.0)* 10.0


    while not run:
        while close == True:
            screen.fill(white)
            message("you lost noob!", red)
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
                if event.key == pygame.K_LEFT and x1_change != 10:
                    x1_change = -snake_body
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -10:
                    x1_change = snake_body
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != 10:
                    x1_change = 0
                    y1_change = -snake_body
                elif event.key == pygame.K_DOWN and y1_change != -10:
                    x1_change = 0
                    y1_change = snake_body

        if x >= dis_width or x <= 0 or y >= dis_height or y <= 0:
            run = True

        x += x1_change
        y += y1_change

        screen.fill(white)


        pygame.draw.rect(screen, blue, [fx,fy, snake_body, snake_body])               #food
        pygame.draw.rect(screen, black, [x,y, snake_body, snake_body])                   #snake
        pygame.display.update()

        if x == fx and y == fy:
            print("food")
        clock.tick(snake_speed)                          #snake's speed

    pygame.quit()
    quit()

gameloop()
