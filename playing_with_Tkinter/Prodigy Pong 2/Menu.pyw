#------------------------------------------------------------------------------#
    #PRODIGY PONG 2
    #v1.00
    #Copyright (C) 2011  Muhammad Ahmad Tirmazi

    # Prodigy Pong 2
    # is distributed under the terms of the GNU General Public License

    # This file is part of Prodigy Pong 2.

    #Prodigy Pong 2 is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.
  
    #You should have received a copy of the GNU General Public License         
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#------------------------------------------------------------------------------#

#The Title, Main Menu, Options Menu and Other Sub-Menus
import pygame
from pygame.locals import *
from Objects import *
from pgu import gui
import easygui

black = pygame.image.load('gfx/black.BMP').convert()
icon = pygame.image.load('gfx/ball.PNG').convert_alpha()
pygame.display.set_caption('BURNING PRODIGY Tech.')
pygame.display.set_icon(icon)


def check_quit(tmp):
    if get_surface == 'fullscreen':
        pygame.quit()
        sys.exit(0)
    else:
        check = easygui.ynbox('Are you sure you want to quit?')
        if check:
            pygame.quit()
            sys.exit(0)
        else:
            return

def Game_Start(tmp):
    Game()
    Menu()

def goback(tmp):
        Options(5)

def setmode(tmp):
    screen.blit(black,(0,0))
    modeapp = gui.App()
    modeapp.connect(gui.QUIT,check_quit,None)
    button_space = gui.Button('SPACE MODE')
    button_grass = gui.Button('STADIUM MODE')
    button_return = gui.Button('RETURN TO OPTIONS MENU')
    def setspace(tmp):
        settings.set_mode('space')
        return
    def setgrass(tmp):
        settings.set_mode('grass')
        return
    button_space.connect(gui.CLICK,setspace,None)
    button_grass.connect(gui.CLICK,setgrass,None)
    button_return.connect(gui.CLICK,goback,None)
    modetable = gui.Table(width = 800, height = 600)
    modetable.td(button_space)
    modetable.tr()
    modetable.td(button_grass)
    modetable.tr()
    modetable.td(button_return)
    modeapp.run(modetable)

def difficulty(tmp):
    diffapp = gui.App()
    diffapp.connect(gui.QUIT,check_quit,None)
    screen.blit(black,(0,0))
    difftable = gui.Table(width = 800, height = 600)
    button_easy = gui.Button('EASY')
    button_normal = gui.Button('NORMAL')
    button_hard = gui.Button('HARD')
    button_return = gui.Button('RETURN TO OPTIONS MENU')
    def seteasy(tmp):
        settings.set_difficulty('easy')
    def setnormal(tmp):
        settings.set_difficulty('normal')
    def sethard(tmp):
        settings.set_difficulty('hard')
    button_easy.connect(gui.CLICK,seteasy,None)
    button_normal.connect(gui.CLICK,setnormal,None)
    button_hard.connect(gui.CLICK,sethard,None)
    button_return.connect(gui.CLICK,goback,None)
    difftable.td(button_easy)
    difftable.tr()
    difftable.td(button_normal)
    difftable.tr()
    difftable.td(button_hard)
    difftable.tr()
    difftable.td(button_return)
    difftable.tr()
    diffapp.run(difftable)

def players(tmp):
    plyapp = gui.App()
    plyapp.connect(gui.QUIT,check_quit,None)
    screen.blit(black,(0,0))
    button_p1 = gui.Button('SINGLE PLAYER')
    button_p2 = gui.Button('2 PLAYERS')
    button_return = gui.Button('RETURN TO OPTIONS MENU')
    def setp1(tmp):
        settings.set_players(1)
    def setp2(tmp):
        settings.set_players(2)
    button_p1.connect(gui.CLICK,setp1,None)
    button_p2.connect(gui.CLICK,setp2,None)
    button_return.connect(gui.CLICK,goback,None)
    plytable = gui.Table(width = 800, height = 600)
    plytable.td(button_p1)
    plytable.tr()
    plytable.td(button_p2)
    plytable.tr()
    plytable.td(button_return)
    plyapp.run(plytable)

def device(tmp):
    devapp = gui.App()
    devapp.connect(gui.QUIT,check_quit,None)
    screen.blit(black,(0,0))
    button_key = gui.Button('KEYBOARD')
    button_mouse = gui.Button('MOUSE')
    button_return = gui.Button('RETURN TO OPTIONS MENU')
    def setkey(tmp):
        settings.set_device('keyboard')
    def setmouse(tmp):
        settings.set_device('mouse')
    button_key.connect(gui.CLICK,setkey,None)
    button_mouse.connect(gui.CLICK,setmouse,None)
    button_return.connect(gui.CLICK,goback,None)
    devtable = gui.Table(width = 800, height = 600)
    devtable.td(button_key)
    devtable.tr()
    devtable.td(button_mouse)
    devtable.tr()
    devtable.td(button_return)
    devapp.run(devtable)
    
    
def end(tmp):
    Menu()

def Options(tmp):
    optapp = gui.App()
    optapp.connect(gui.QUIT,check_quit,None)
    screen.blit(black,(0,0))
    opttable = gui.Table(width =800, height = 600)
    button_setmode = gui.Button('SET GAME MODE')
    button_difficulty = gui.Button('SET DIFFICULTY')
    button_players = gui.Button('SET PLAYERS')
    button_device = gui.Button('SET INPUT DEVICE')
    button_return = gui.Button('RETURN TO MAIN MENU')
    button_setmode.connect(gui.CLICK,setmode,None)
    button_difficulty.connect(gui.CLICK,difficulty,None)
    button_players.connect(gui.CLICK,players,None)
    button_device.connect(gui.CLICK,device,None)
    button_return.connect(gui.CLICK,end,None)
    opttable.td(button_setmode)
    opttable.tr()
    opttable.td(button_difficulty)
    opttable.tr()
    opttable.td(button_players)
    opttable.tr()
    opttable.td(button_device)
    opttable.tr()
    opttable.td(button_return)
    optapp.run(opttable)
    



def Menu():
    app = gui.App()
    screen.blit(black,(0,0))
    app.connect(gui.QUIT,check_quit,None)
    table = gui.Table(width = 800, height = 600)
    button_start = gui.Button('START GAME')
    button_options = gui.Button('OPTIONS')
    button_quit = gui.Button('EXIT')
    button_start.connect(gui.CLICK,Game_Start,None)
    button_options.connect(gui.CLICK,Options,None)
    button_quit.connect(gui.CLICK,check_quit,None)
    table.td(button_start)
    table.tr()
    table.td(button_options)
    table.tr()
    table.td(button_quit)
    app.run(table)

def TMenu():
    title = pygame.image.load('gfx/title.BMP')
    screen.blit(title,(0,0))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                check_quit()
            elif event.type == KEYDOWN:
                Menu()
        pygame.display.update()
    
TMenu()
