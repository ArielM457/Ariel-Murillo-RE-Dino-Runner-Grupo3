from  pygame import *
import sys
init()
screen = display.set_mode((800,600))
fondo = image.load("dino.png")
fondo =transform.scale(fondo, (800,600))
while True:
            screen.fill((255, 255, 255))
            for e in event.get():
                if e.type ==  QUIT:sys.exit()
            screen.blit(fondo, (0,0))
            display.flip()
