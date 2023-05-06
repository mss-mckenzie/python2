from pygame import *
from random import *

screen = display.set_mode((800, 600))

tarx = randint(0,750)
tary = randint(0,550)
target = Rect(tarx, tary, 50, 50)

running = True
while running:
    for e in event.get():
        if e.type==QUIT:
            running = False

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    
    if mb[0] and target.collidepoint(mx,my):
        tarx = randint(0,750)
        tary = randint(0,550)
        target = Rect(tarx, tary, 50, 50)
        
    # draw everything
    screen.fill((0,0,0))
    draw.rect(screen, (255,255,255), (tarx,tary,50,50))
   
    display.flip()
    time.wait(10)

quit()
