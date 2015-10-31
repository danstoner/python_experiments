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

def scanloop(screen,background):
    print "** scanloop **"
    looking_for_codes = True
    read_a_line = False
    code = ""

    while looking_for_codes:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_RETURN:
                    read_a_line = True
                if chr(event.key).isalnum():
                    code += chr(event.key)
                    print "debug - code ======= ", code
        # by this point code should be a string triggered by return / enter.... e.g. equivalent to a readline
        if read_a_line:
            read_a_line = False
            if code == "12345":
                change_to_alerting(screen,background,"ALERT!!!")
                pygame.display.flip()
            return False
    return True

def alarmloop(screen,background):
    print "** alarmloop **"
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

def quit_program():
    print "QUIT requested. Shutting down..."
    raise SystemExit

def poll_for_quit():
    print "** poll_for_quit() **"
    # put the process to sleep to share CPU and reduce resource consumption while idling
    pygame.time.wait(15)  # time in ms
    for event in pygame.event.get():
#        print event
        if event.type == pygame.QUIT:
            #return False
            quit_program()
        elif  event.type == pygame.MOUSEBUTTONDOWN:
            quit_program()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #return False
                quit_program()
    return True

def change_to_alerting(screen,background,status):
    print "** change_to_alerting() **"
    background.fill(RED)
    background = background.convert()
    font = pygame.font.Font(None, 36)
    text = font.render(status, 1, WHITE)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
    screen.blit(background, INTERNAL_UPPER_LEFT_CORNER)

    

def change_to_scanning(screen,background,status):
    print "** change_to_scanning() **"
    background.fill(DARK_GRAY)
    background = background.convert()
    font = pygame.font.Font(None, 36)
    text = font.render(status, 1, GREEN)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)
    screen.blit(background,INTERNAL_UPPER_LEFT_CORNER)


# colors are specified using RGB or friendly names such as "white" or "grey"
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

FPS = 15

TITLE_TEXT = "Cat Defense System"
SCANNING_TEXT = "Ready to Scan..."
ALERT_TEXT = "ALERT!!!"

WIDTH = 320
HEIGHT = 240
WINDOW_SIZE = (WIDTH,HEIGHT)
YOFFSET = 30
#INTERNAL_UPPER_LEFT_CORNER = (0,YOFFSET)

class Status:

    def __init__ (self):
        self.change_to_Alarming()

    def change_to_Scanning (self):
        self.textcolor = GREEN
        self.backgroundcolor = LIGHT_GRAY
        self.statustext = SCANNING_TEXT

    def change_to_Alarming (self):
        self.textcolor = WHITE
        self.backgroundcolor = RED
        self.statustext = ALERT_TEXT

        
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
    print MyStatus.statustext
    MyStatus.statustext = SCANNING_TEXT
    print MyStatus.statustext
    MyStatus.change_to_Alarming()
    print MyStatus.statustext
    MyStatus.change_to_Scanning()
    print MyStatus.statustext
    
    while True:
        MyStatus.change_to_Scanning()
        paint(DisplaySurface,MyStatus)
        pygame.display.flip()

        # put the process to sleep to share CPU and reduce resource consumption while idling
        pygame.time.wait(25)  # time in ms

    # font = pygame.font.Font(None, 36)
    # text = font.render(status, 1, WHITE)
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos.centery = background.get_rect().centery
    # background.blit(text, textpos)
    # screen.blit(background, INTERNAL_UPPER_LEFT_CORNER)


        MyStatus.change_to_Alarming()
        paint(DisplaySurface,MyStatus)
        pygame.display.flip()
        # put the process to sleep to share CPU and reduce resource consumption while idling
        pygame.time.wait(25)  # time in ms

        poll_for_quit()
        fpsClock.tick(FPS)

    raise SystemExit



    running = True
    alarming = True
    scanning = True
    pygame.init()
    #pygame.mouse.set_visible(False)
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
    while running:
        print "** main running **"
        if alarming:
            change_to_alerting(screen,background,"ALERT!!!")
            pygame.display.flip()
        while alarming and running:
            print "** alarming and running **"
            alarming = alarmloop(screen,background)
#            pygame.display.flip()
#        letterstack = "" # reset the letter stack whenever we are outside the scanning loop
#        alarming = False
        scanning = True
        change_to_scanning(screen,background,"Ready to Scan...")
        pygame.display.flip()
        while scanning and running:
            print "** scanning and running **"
#            line = sys.stdin.readline()
#           print "debug: ", line
            # if (line == "quit") or (line == "exit"):
            #     print "Quitting..."
            #     raise SystemExit
            # if line == "12345":
            #     print "code found!"
            #     scanning = False
            #     alarming = True
            #     change_to_alerting(screen,background,"ALERT!!!")
            scanning = scanloop(screen,background)
            pygame.display.flip()
            running = poll_for_quit()
        alarming = True
#        scanning = True
    raise SystemExit
