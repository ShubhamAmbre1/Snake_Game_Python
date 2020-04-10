import pygame
pygame.init()
(width, height) = (500,500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

x = 250
y = 250
width = 40
height = 40
vel = 5
# clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
    
    pygame.draw.rect(screen, (255,0,0), (x,y, width, height))
    pygame.display.update()
pygame.quit()
