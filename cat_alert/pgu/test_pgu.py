### started from example gui12.py from https://github.com/parogers/pgu
import sys
sys.path.insert(0, '..')


import pygame
from pygame.locals import *
from pgu import gui
# SDL_FBDEV change is required for the Raspberry Pi PiTFT by AdaFruit
import os
os.environ["SDL_FBDEV"] = "/dev/fb1"


# def open_file_browser(arg):
#     d = gui.FileDialog()
#     d.connect(gui.CHANGE, handle_file_browser_closed, d)
#     d.open()
    

# def handle_file_browser_closed(dlg):
#     if dlg.value: input_file.value = dlg.value

def checker():
    print "checked"

# def quitall():
#     raise SystemExit

#gui.theme.load('../data/themes/default')
app = gui.Desktop()
app.connect(gui.QUIT,app.quit,None)

main = gui.Container(width=320, height=240, background=(40, 40, 40) )

main.add(gui.Label("Example", cls="h1"), 20, 20)

e = gui.Button("Quit")
e.connect(gui.CLICK,app.quit,None)
top = gui.Table()
top.tr()
top.td(e)
    
td_style = {'padding_right': 1}
t = gui.Table()
t.tr()
t.td( gui.Label('Ready to Scan:') , style=td_style )
t.tr()
input_string = gui.Input()
t.td( input_string, style=td_style )
#b = gui.Button("Browse...")
#t.td( b, style=td_style )
#b.connect(gui.CLICK, open_file_browser, None)
input_string.connect(gui.KEYDOWN,checker)

main.add(top, 250, 180)
main.add(t, 20, 100)
#line = gui.Input(size=49)

input_string.focus()
app.run(main)


#import profile
#profile.run('app.run(main)')
