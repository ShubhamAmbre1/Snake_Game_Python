import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game')

x = 250                                     #snake's position on x
y = 250                                     #snake's position on y

width = 20                                  #snake width
height = 20                                 #snake height

x1_change = 0                               #change in position
y1_change = 0                               #change in position

clock = pygame.time.Clock()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change != 10:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change != -10:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change != 10:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN and y1_change != -10:
                x1_change = 0
                y1_change = 10
        if x >= 500 or x <= 0 or y >= 500 or y <= 0:
            run = False

    x += x1_change
    y += y1_change
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), [x,y, width, height])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
