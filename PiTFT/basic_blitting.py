#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
From....
012_text.py
displaying and moving text
url: http://thepythongamebook.com/en:part2:pygame:step012
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

This program demonstrate how to render and blit text into a surface

works with pyhton3.4 and python2.7
"""

import pygame
# SDL_FBDEV change is required for the Raspberry Pi PiTFT by AdaFruit
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"




def flytext(msg="hello world", duration=5):
    """blinking text bouncing around the screen"""

    def newcolour():
        # any colour but black or white 
        return (random.randint(10,250), random.randint(10,250), random.randint(10,250))

    def write(msg="pygame is cool"):
        myfont = pygame.font.SysFont("None", random.randint(20,40))
        mytext = myfont.render(msg, True, newcolour())
        mytext = mytext.convert_alpha()
        return mytext
        
    pygame.init()
    x = 60
    y = 60
    dx = 5
    dy = 5

    screen = pygame.display.set_mode((320,240))
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background.fill((255,255,255)) # white
    background = background.convert()
    screen.blit(background, (0,0)) # clean whole screen
    clock = pygame.time.Clock()
    mainloop = True
    FPS = 15 # desired framerate in frames per second.
    while mainloop:
        milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
        seconds = milliseconds / 1000.0 # seconds passed since last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False # user pressed ESC
        textsurface = write("hello world")
        #screen.blit(background, (0,0)) # clean whole screen
        x += dx
        y += dy
        if x < 0:
           x = 0
           dx *= -1
           screen.blit(background, (0,0)) # clean whole screen
        elif x + textsurface.get_width() > screen.get_width():
            x = screen.get_width() - textsurface.get_width()
            dx *= -1
        if y < 0:
            y = 0
            dy *= -1
        elif y + textsurface.get_height() > screen.get_height():
            y = screen.get_height() - textsurface.get_height()
            dy *= -1
            
        screen.blit(textsurface, (x,y))
        pygame.display.flip()
        # put the process to sleep to share CPU and reduce resource consumption while idling
        pygame.time.wait(15)  # time in ms

    pygame.quit()


def scanloop(screen,background):
    print "scanloop"
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def alarmloop(screen,background):
    print "alarmloop"
    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms
    #event = pygame.event.poll()
    #if event.type == pygame.MOUSEBUTTONDOWN:
    #    return False
    # stop alarm on mouse button or Escape key
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            change_to_scanning(screen,background,"Ready to Scan...")
            return False
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    change_to_scanning(screen,background,"Ready to Scan...")
                    return False
    return True

def poll_for_quit():
    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def change_to_alerting(screen,background,status):
    background.fill(RED)
    background = background.convert()
    font = pygame.font.Font(None, 36)
    text = font.render(status, 1, WHITE)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
    screen.blit(background,(0,30))
    print "changed to alerting"
    

def change_to_scanning(screen,background,status):
    background.fill(DARK_GRAY)
    background = background.convert()
    font = pygame.font.Font(None, 36)
    text = font.render(status, 1, GREEN)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
    screen.blit(background,(0,30))
    print "changed to scanning"

# colors are specified using RGB or friendly names such as "white" or "grey"
# see: https://drafts.csswg.org/css-color/
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (32, 32, 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

if __name__=="__main__":
    running = True
    alarming = True
    scanning = True
    pygame.init()
    screen = pygame.display.set_mode((320,240))
    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)
    background = background.convert()
    screen.blit(background,(0,0)) # initial clear screen
    # set the title
    font = pygame.font.Font(None, 36)
    text = font.render("My Application Title", 1, BLACK)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    screen.blit(background,(0,0))
    pygame.display.flip()
    change_to_alerting(screen,background,"ALERT!!!")
    pygame.display.flip()
    while running:
        # TO DO: probably only need to do the fill once? pygame hung the PiTFT
        while alarming and running:
            alarming = alarmloop(screen,background)
            pygame.display.flip()
        while scanning and running:
            scanning = scanloop(screen,background)
            running = poll_for_quit()
            pygame.display.flip()
    raise SystemExit
