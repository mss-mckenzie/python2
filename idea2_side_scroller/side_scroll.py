from pygame import *
from random import *

screen = display.set_mode((800, 600))

badguys = []
for i in range(10):
    badguys.append(Rect(randint(800,1600), randint(0,500), 70, 70))

running = True
while running:
    for e in event.get():
        if e.type==QUIT:
            running = False

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()

    #move Bad Guys        
    for bad in badguys:
        bad.x -= 10
        if bad.x < -80:
            bad.x = randint(800,1600)
        
    # draw everything
    screen.fill((0,0,0))
    for bad in badguys:
        draw.rect(screen, (255,0,0), bad)
    draw.rect(screen,(255,255,0),(mx-35,my-35,70,70))
    display.flip()
    time.wait(10)

quit()
