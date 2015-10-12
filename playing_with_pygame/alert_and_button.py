import pygame
import time


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

#backgroundcolor = (80,80,80)
backgroundcolor = (DARK_GRAY)



def pollforquit():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        raise SystemExit
    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms



# Initial screen decorations
#window.fill(backgroundcolor)
# See: https://www.pygame.org/docs/tut/tom/games2.html
# Fill background
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill(backgroundcolor)

font = pygame.font.Font(None, 36)
text = font.render("Stuff goes here", 1, BLUE)
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)
window.blit(background, (0, 0))

pygame.display.flip()




# Main Event Loop
running = True

while running:
    pollforquit();
    



raise SystemExit


