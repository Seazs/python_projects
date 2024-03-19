# Example file showing a basic pygame "game loop"
import pygame
from math import sin, cos, pi, tan

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
running = True

x = 350
y = 250

x_speed = 5
y_speed = 5
position = (x, y)

length = 300
w = 0.05
t = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255, 255, 255))

    
    x0 = 350
    y0 = 50

    t += 1
    theta = cos(w*t)/(1 + t**3/1000000000)
    # update the position of the pendulum
    x = x0 + length * sin(theta)
    y = y0 + length * cos(theta) 

    if event.type == pygame.MOUSEBUTTONDOWN:
        y = pygame.mouse.get_pos()[1]
        t = 0
        
    
    position = (x, y)




    # RENDER YOUR GAME HERE
    # draw a pendulum
    pygame.draw.circle(screen, (0, 0, 255), position, 30)
    pygame.draw.line(screen, (0, 0, 255), (x0, y0), position, 5)

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()