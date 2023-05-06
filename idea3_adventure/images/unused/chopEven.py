from pygame import *
from glob import *

x = 4
y = 10
picN = glob("*.png")[0]

pic = image.load(picN)
wid,hi = pic.get_size()
screen = display.set_mode(pic.get_size())
screen.blit(pic,(0,0))
display.flip()

w = pic.get_width()//x
h = pic.get_height()//y

for i in range(x):
    for j in range(y):
        p = pic.subsurface((i*w,j*h,w,h))
        image.save(p, "%s%d%d.png" % (picN.split(".")[0],i,j))
quit()
