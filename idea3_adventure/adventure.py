'''
adventure.py
Mr. McKenzie
MasseyHacks IX - Intro to Python II workshop
---------
This example shows how to set up a story-based program. There is extensive
use of lists. Each location in the story has a number, this number is used
as an index into various lists. e.g.
    - index 0 is the cabin.
    - names[0] is its name
    - pics[0] is its image
    - links[0] is where you can go from the cabin i.e. [1,2,3]

'''



from pygame import *
from random import *

init()
screen = display.set_mode((1080, 384))

names = ["cabin","fort","tavern","ship"]
pics = []
for n in names:
    p = image.load("images/"+n+".png")
    pics.append(p)

links = [[1,2,3],[0,2],[0,1],[0]]
rects = [Rect(50, 50, 100, 40),Rect(50, 120, 100, 40),Rect(50, 190, 100, 40)]
location = 0
fnt = font.SysFont("Arial", 24)
running = True
while running:
    for e in event.get():
        if e.type==QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            if over > -1:
                location = links[location][over]
        
    over = -1
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
        
    # draw everything
    screen.blit(pics[location], (0,0))
    for i in range(len(links[location])):
        button = rects[i]
        if button.collidepoint(mx,my):
            draw.rect(screen, (211,211,255), button)
            draw.rect(screen, (255,0,0), button,2)
            over = i
        else:
            draw.rect(screen, (111,111,155), button)
            draw.rect(screen, (255,255,0), button,2)
        dest = links[location][i]
        txt = fnt.render(names[dest], True, 0)
        screen.blit(txt, (button.x+10, button.y+5))
    display.flip()

quit()
