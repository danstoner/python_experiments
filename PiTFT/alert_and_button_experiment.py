import pygame
import time
import eztext
import sys
# SDL_FBDEV change is required for the Raspberry Pi PiTFT by AdaFruit
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()
window = pygame.display.set_mode((300, 200))
pygame.display.set_caption('caption goes here')

# colors are specified using RGB or friendly names such as "white" or "grey"
# see: https://drafts.csswg.org/css-color/#named-colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (32, 32, 32)
RED = (255, 0, 0)
GREEN = (34, 139, 34)  # forestgreen
BLUE = (30, 144, 255)  # dodgerblue

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

txtbx=eztext.Input(maxlength=10, color=WHITE,y=3,prompt='Ready to Scan: ')
txtbx.color=WHITE
txtbx.focus=True

txtbx.draw(window)
background.blit(text, textpos)
window.blit(background, (0, 0))
pygame.display.flip()

def pollforquit():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        raise SystemExit

## if not alarming, we want the text box to have focus and read lines of input from keyboard.
## if alarming, we only want to listen for a click or touch event.

def repeat_alarm(alarming,alarm_text):
    alarm_state = alarming
    alarm_text = font.render("ALARMING!!!", 1, RED)
    alarm_textpos = text.get_rect()
    alarm_textpos.centerx = background.get_rect().centerx
    alarm_textpos.centery = background.get_rect().centery
    background.blit(alarm_text, alarm_textpos)
    window.blit(background, (0, 0))

#    background.blit(text,textpos)
    pygame.display.flip()

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
                reset_alarm(alarm_text)
        if alarm_state:
            pygame.time.wait(15)  # time in ms
    return alarm_state


# Default application state
running = True
alarming = True

def reset_alarm(alarm_text):
    alarm_text = font.render("READY", 1, GREEN)
    return alarm_text

alarm_text = font.render("READY", 1, GREEN)

print "Started..."
# Main Event Loop
while running:
    events = pygame.event.get()
    txtbx.update(events)
    txtbx.draw(window)
    if alarming:
        
        alarming = repeat_alarm(alarming,alarm_text)
    else:
        alarm_textpos = alarm_text.get_rect()
        alarm_textpos.centerx = background.get_rect().centerx
        alarm_textpos.centery = background.get_rect().centery
        background.blit(alarm_text, alarm_textpos)
        window.blit(background, (0, 0))
        pygame.display.flip()

    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms
    pollforquit();
    



raise SystemExit


