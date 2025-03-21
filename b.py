import pygame

pygame.init()
import random


win = pygame.display.set_mode((500, 500)) # Dies erzeugt ein Fenster von 500 Breite und 500 Höhe.
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 50
height = 50
vel = 6
color = (238, 130, 238)

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel  
    if keys[pygame.K_SPACE]:
        isJump = True

    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

        
    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height))
    pygame.display.update()

    

pygame.quit() # Wenn wor die Schleife verlassen. wird dis ausgeführt und unser Spiel beendet. 
