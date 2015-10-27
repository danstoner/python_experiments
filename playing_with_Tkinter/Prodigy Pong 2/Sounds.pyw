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
#Handles Game Sound Effects and Background Music
    
import pygame
from pygame.locals import *
import random

pygame.init()

wallsound = pygame.mixer.Sound('sfx/Wall.WAV')
gbatsound = pygame.mixer.Sound('sfx/Bat_1.WAV')
gbatsound2 = pygame.mixer.Sound('sfx/Bat_2.WAV')
sbatsound = pygame.mixer.Sound('sfx/Bat_1.WAV')
sbatsound2 = pygame.mixer.Sound('sfx/Bat_2.WAV')
wallsound.set_volume(20)
gbatsound.set_volume(20)
gbatsound2.set_volume(20)
sbatsound.set_volume(20)
sbatsound2.set_volume(20)

bg1 = 'sfx/heartofthesea.OGG'
bg2 = 'sfx/cautiouspath.OGG'
bg3 = 'sfx/destination.OGG'
bgm_set = [bg1,bg2,bg3]

def startbgm(no):
    if no == 1:
        pygame.mixer.music.load(bg1)
    elif no == 2:
        pygame.mixer.music.load(bg2)
    elif no == 3:
        pygame.mixer.music.load(bg3)
    elif no == 'random':
        x = random.randint(0,len(bgm_set))
        x = x-1
        pygame.mixer.music.load(bgm_set[x])
    elif no == 'space':
        x = random.randint(0,1)
        x = x+1
        pygame.mixer.music.load(bgm_set[x])
    elif no == 'grass':
        x = 0
        pygame.mixer.music.load(bgm_set[x])

    pygame.mixer.music.play(-1)

