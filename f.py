import pygame

x = 500
y = 500

racketWidth = 100
racketHeight = 15

racketX = 200
racketY = 450

speed = 0

ballX = int(x/2)
ballY = int(y/2)

ballRadius = 15

def moveRacket():
    global racketX
    racketX += speed

def racketBlock():
    global speed
    if racketX <= 0 or racketX >= x - racketWidth:
        speed = 0
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and racketX >= 0:
            speed = -2
        if event.key == pygame.K_RIGHT and racketX <= x - racketWidth:
            speed = 2

title = "Pong"

run = True
pygame.init()
screen = pygame.display.set_mode((x, y))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    moveRacket()
    racketBlock()
    pygame.draw.circle(screen, (255, 255, 0), (ballX, ballY), ballRadius, 0)

    pygame.draw.rect(screen, (255, 40, 0), (racketX, racketY, racketWidth, racketHeight), 0)

    pygame.display.flip()

    pygame.time.delay(5)




        

