##
## Code patterns and snippets from:
##   -   Making Games with Python and Pygame by Al Sweigart, 2012
##         http://inventwithpython.com/pygame
##   -   Making games with Pygame by (Tom Chance?), 2003
##         https://www.pygame.org/docs/tut/tom/games6.html



import pygame
# SDL_FBDEV environment variable is required for the Raspberry Pi PiTFT by AdaFruit
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"

def quit_program():
    print "QUIT requested. Shutting down..."
    raise SystemExit

def poll(code,status):
    print "** poll() **"
    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms
    for event in pygame.event.get():
        if status.status == "alarming":
            if event.type == pygame.QUIT:
                quit_program()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                code.reset()
                status.change_to_Scanning()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    code.reset()
                    status.change_to_Scanning()
        elif status.status == "scanning":
            if event.type == pygame.QUIT:
                quit_program()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_program()
                elif event.key == pygame.K_RETURN:
                    code.found = code.check_code()
                    if code.found:
                        status.change_to_Alarming()
                        code.reset()
                    else:
                        code.reset()
                elif chr(event.key).isalnum():
                    code.append(chr(event.key))
                    print "debug - code ======= ", code.word        
    return True


# Constants to be used for RPi with TFT
FPS = 15
WIDTH = 320
HEIGHT = 240
WINDOW_SIZE = (WIDTH,HEIGHT)
YOFFSET = 15


# colors are specified using RGB or friendly names such as "white" or "gray"
# see: https://drafts.csswg.org/css-color/
# COLOR = (Red, Green, Blue [,alpha])
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (32, 32, 32)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# Customize
TITLE_TEXT = "CDS"
SCANNING_TEXT = "Waiting for..."
ALERT_TEXT = "MONKEY!!!"

CODES = ("12345", "abcde")

class Status:

    def __init__ (self):
        self.change_to_Alarming()

    def change_to_Scanning (self):
        self.textcolor = GREEN
        self.backgroundcolor = DARK_GRAY
        self.statustext = SCANNING_TEXT
        self.status = "scanning"

    def change_to_Alarming (self):
        self.textcolor = WHITE
        self.backgroundcolor = RED
        self.statustext = ALERT_TEXT
        self.status = "alarming"

        
class Code:

    def __init__ (self):
        self.reset()

    def reset (self):
        self.word = ""
        self.found = False

    def check_code (self):
        if self.word in CODES:
            self.found = True
            return True
        else:
            self.found = False
            return False

    def append (self,letter):
        self.word += letter

        
def paint (surface, statusobject):
    newtext = font.render(statusobject.statustext, 1, statusobject.textcolor)
    newtextpos = newtext.get_rect()
    newtextpos.centerx = surface.get_rect().centerx
    newtextpos.centery = surface.get_rect().centery
    pygame.draw.rect(surface, statusobject.backgroundcolor, (0, YOFFSET, WIDTH, HEIGHT))
    surface.blit(newtext, newtextpos)

if __name__=="__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()
    DisplaySurface = pygame.display.set_mode(WINDOW_SIZE)
    DisplaySurface.fill(WHITE)
    font = pygame.font.Font(None, 36)
    title = font.render(TITLE_TEXT, 1, BLACK)
    titlepos = title.get_rect()
    titlepos.centerx = DisplaySurface.get_rect().centerx
    DisplaySurface.blit(title, titlepos)

    MyStatus = Status()
    MyCode = Code()

    MyStatus.change_to_Alarming()
    print MyStatus.statustext
    paint(DisplaySurface,MyStatus)
    pygame.display.flip()

    # Main Loop!
    while True:
        poll(MyCode,MyStatus)
        paint(DisplaySurface,MyStatus)
        pygame.display.flip()
        pygame.time.wait(50)  # time in ms
        fpsClock.tick(FPS)

    raise SystemExit

