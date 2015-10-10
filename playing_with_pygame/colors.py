import pygame
import time

screen = pygame.display.set_mode((640, 400))

running =1

event = pygame.event.poll()
#while running:
#    if event.type == pygame.QUIT:
#        running = 0

def pollforquit():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        raise SystemExit

i = 0
j = 0
k = 0

while (i < 256) and (running):
    pollforquit()
    for i in range (0,256,15):
        pollforquit()
        for j in range (0,256,15):
            pollforquit()
            for k in range (0,256,15):
                print (i, j, k)
                pollforquit()
                screen.fill((i, j, k))
                pygame.display.flip()
                time.sleep(0.05)
                
            


