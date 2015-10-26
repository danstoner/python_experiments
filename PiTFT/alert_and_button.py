import pygame
import time

import sys
# SDL_FBDEV change is required for the Raspberry Pi PiTFT by AdaFruit
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"

debug = False
if len(sys.argv) > 1:
    if "debug" in sys.argv:
        debug=True

pygame.init()
window = pygame.display.set_mode((300, 200))
pygame.display.set_caption('Alerter with Snooze Button')


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

backgroundcolor = (DARK_GRAY)

# Initial screen decorations
#window.fill(backgroundcolor)
# See: https://www.pygame.org/docs/tut/tom/games2.html
# Fill background
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill(backgroundcolor)

font = pygame.font.Font(None, 36)
text = font.render("My Application Title", 1, BLUE)
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)
window.blit(background, (0, 0))

pygame.display.flip()

def pollforquit():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        raise SystemExit

## if not alarming, we want the text box to have focus and read lines of input from keyboard.
## if alarming, we only want to listen for a click or touch event.

def repeat_alarm(alarming):
    alarm_state = alarming
    text = font.render("ALARMING!!!", 1, RED)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    window.blit(background, (0, 0))

#    background.blit(text,textpos)
    pygame.display.update()

    # put the process to sleep to share CPU and reduce resource consumption while idling

    while alarm_state:
        print "ALARM!"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            
        # stop alarm on click touch or keypress
            if (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.KEYDOWN):
                alarm_state = False
        if alarm_state:
            pygame.time.wait(15)  # time in ms
    return alarm_state

# Default application state
running = True
alarming = True

print "Started..."
# Main Event Loop
while running:
    if alarming:
        alarming = repeat_alarm(alarming)
    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms
    if not debug:
        pollforquit();
    



raise SystemExit


