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

#Basic Classes and Game Objects
#Includes The Game Loop    
import pygame
from pygame.locals import *
import random
import fullscreen
from Settings import *
from Sounds import *
import Title
import easygui

pygame.init()
get_surface = Title.title()
screen = pygame.display.set_mode((800,600),SWSURFACE)
clock = pygame.time.Clock()
settings = Settings()
if get_surface == 'fullscreen':
    screen = fullscreen.fullscreen()

class Bat(pygame.sprite.Sprite):
    def __init__(self,p2 = False,pos = 1):
        self.p2 = p2
        self.pos = pos
        self.mode = settings.get_mode()
        if self.mode == 'space':
            image = 'spacebat.PNG'
        elif self.mode == 'grass':
            image = 'grassbat.PNG'
        image = 'gfx/' + image
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 10
        if p2:
            if pos == 2:
                self.upkey = K_UP
                self.downkey = K_DOWN
                w = screen.get_width() - self.image.get_width()/2 - 32
                h = screen.get_height()/2 - self.image.get_height()/2
            else:
                if settings.get_device() == 'mouse':
                    self.upkey = K_UP
                    self.downkey = K_DOWN
                else:
                    self.upkey = K_w
                    self.downkey = K_s
                w = self.image.get_width()/2 + 32
                h = screen.get_height()/2 - self.image.get_height()/2
            self.rect.center = (w,h)
        else:
            self.upkey = K_UP
            self.downkey = K_DOWN
            w = self.image.get_width()/2 + 32
            h = screen.get_height()/2 - self.image.get_height()/2
            self.rect.center = (w,h)

    def update(self):
        if settings.get_device() == 'mouse' and self.pos == 2:
            mousex,mousey = pygame.mouse.get_pos()
            self.rect.centery = mousey
        elif settings.get_device() == 'mouse' and self.p2 is False:
            mousex,mousey = pygame.mouse.get_pos()
            self.rect.centery = mousey
        else:
            key = pygame.key.get_pressed()
            if key[self.upkey]:
                self.rect.centery -= self.speed
            elif key[self.downkey]:
                self.rect.centery += self.speed
        self.check_coll()

    def check_coll(self):
        if self.rect.colliderect(horwall):
            self.rect.top = horwall.rect.bottom
        if self.rect.colliderect(horwall2):
            self.rect.bottom = horwall2.rect.top
class Comp_Bat(Bat):
    def __init__(self):
        Bat.__init__(self)
        w = screen.get_width() - self.image.get_width()/2 - 32
        h = screen.get_height()/2 - self.image.get_height()/2
        self.rect.center = (w,h)
        if settings.get_difficulty() == 'easy':
            self.speed = 4
        elif settings.get_difficulty() == 'normal':
            self.speed = 8
        elif settings.get_difficulty() == 'hard':
            self.speed = 12

    def update(self):
        if ball.rect.centery > self.rect.centery:
            self.rect.centery += self.speed
        elif ball.rect.centery < self.rect.centery:
            self.rect.centery -= self.speed
        self.check_coll()


class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,horiz = False):
        pygame.sprite.Sprite.__init__(self)
        self.mode = settings.get_mode()
        if self.mode == 'space':
            if horiz:
                self.image = pygame.image.load('gfx/hor_wall.PNG').convert_alpha()
            else:
                self.image = pygame.image.load('gfx/ver_wall.PNG').convert_alpha()

        elif self.mode == 'grass':
            if horiz:
                self.image = pygame.image.load('gfx/hor_fence.PNG').convert_alpha()
            else:
                self.image = pygame.image.load('gfx/ver_fence.PNG').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        
class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.mode = settings.get_mode()
        pygame.sprite.Sprite.__init__(self)
        if self.mode == 'space':
            self.image = pygame.image.load('gfx/space.PNG').convert()
        elif self.mode == 'grass':
            self.image = pygame.image.load('gfx/grass.BMP').convert()
        self.rect = self.image.get_rect()
        self.speed = 8

    if settings.get_mode() == 'space':
        def update(self):
            self.rect.bottom += self.speed
            if self.rect.top >= 0:
                self.rect.bottom = screen.get_height()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('gfx/ball.PNG').convert_alpha()
        self.rect = self.image.get_rect()

    def set_pos(self):
        posx = screen.get_width()/2 - self.image.get_width()/2
        posy = screen.get_height()/2 - self.image.get_height()/2
        self.rect.center = (posx,posy)
        self.speedx = random.randint(-10.0,10.0)
        self.speedy = random.randint(-5.0,5.0)
        if self.speedx in range(-2,2) or self.speedy in range(-2,2):
            self.set_pos()

    def update(self):
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        self.check_coll()

    def check_coll(self):
        if self.rect.colliderect(horwall) or self.rect.colliderect(horwall2):
            wallsound.play()
            self.speedy = -self.speedy
            self.speed_incr()
            
        if self.rect.colliderect(bat) or self.rect.colliderect(bat2):
            if settings.get_mode() == 'grass':
                if self.rect.colliderect(bat):
                    gbatsound.play()
                elif self.rect.colliderect(bat2):
                    gbatsound2.play()
            elif settings.get_mode() == 'space':
                if self.rect.colliderect(bat):
                    sbatsound.play()
                elif self.rect.colliderect(bat2):
                    sbatsound2.play()
            self.speedx = -self.speedx
            self.speed_incr()
            
        if self.rect.colliderect(verwall) or self.rect.colliderect(verwall2):
            if settings.get_players() == 1:
                if self.rect.colliderect(verwall):
                    score.P1()
                elif self.rect.colliderect(verwall2):
                    score.P2()
            elif settings.get_players() == 2:
                if self.rect.colliderect(verwall):
                    score.P1()
                elif self.rect.colliderect(verwall2):
                    score.P2()
            self.set_pos()

    def speed_incr(self):
        if self.speedy < 0:
            self.speedy -= 0.5
        elif self.speedy > 0:
            self.speedy += 0.5
        if self.speedx < 0:
            self.speedx-=0.5
        elif self.speedx > 0:
            self.speedx += 0.5
            
        self.speed_check()
        
    def speed_check(self):
        if self.speedx < -18:
            self.speedx = -18
        elif self.speedx > 18:
            self.speedx = 18
        if self.speedy < -18:
            self.speedy = -18
        elif self.speedy > 18:
            self.speedy = 18

class Score():
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.font = pygame.font.Font('freesansbold.TTF',20)
        self.gameend = False

    def P1(self):
        self.score1 += 1
        if self.check_winner():
            if self.winner() == 'P1':
                if get_surface == 'fullscreen':
                    img = pygame.image.load('gfx/winp1.GIF')
                    screen.blit(img,(0,0))
                    pygame.display.update()
                    pygame.time.delay(3000)
                else:
                    Title.winp1()
                self.gameend = True
    def P2(self):
        self.score2 += 1
        if self.check_winner():
            if self.winner() == 'P2':
                if get_surface == 'fullscreen':
                    img = pygame.image.load('gfx/winp2.GIF')
                    screen.blit(img,(0,0))
                    pygame.display.update()
                    pygame.time.delay(3000)
                else:
                    Title.winp2()
                self.gameend = True
    def check_winner(self):
        if self.score1 > 15 or self.score2 > 15:
            return True
    def winner(self):
        if self.score1 > 15:
            return 'P1'
        elif self.score2 > 15:
            return 'P2'
        else:
            return
    def update(self):
        self.score_img = self.font.render(str(self.score1),True,(255,255,255))
        self.score2_img = self.font.render(str(self.score2),True,(255,255,255))
        if settings.get_players() == 2:
            posx = bat.rect.centerx - self.score2_img.get_width()/2
            posy = bat.rect.centery - self.score2_img.get_height()/2
            screen.blit(self.score2_img,(posx,posy))
            posx2 = bat2.rect.centerx - self.score_img.get_width()/2
            posy2 = bat2.rect.centery - self.score_img.get_height()/2
            screen.blit(self.score_img,(posx2,posy2))

        else:    
            posx = bat.rect.centerx - self.score2_img.get_width()/2
            posy = bat.rect.centery - self.score2_img.get_height()/2
            screen.blit(self.score2_img,(posx,posy))
            posx2 = bat2.rect.centerx - self.score_img.get_width()/2
            posy2 = bat2.rect.centery - self.score_img.get_height()/2
            screen.blit(self.score_img,(posx2,posy2))


        
    
def Game():
    pygame.mouse.set_visible(0)
    players = settings.get_players()
    global ball,bat,bat2,horwall,horwall2,verwall,verwall2,score,screen
    if players == 2:
        bat = Bat(p2 = True, pos = 1)
    else:
        bat = Bat()
    if players == 2:
        bat2 = Bat(p2 = True,pos = 2)
    else:
        bat2 = Comp_Bat()

    ball = Ball()
    verwall = Wall(0,0)
    verwall2 = Wall(784,0)
    horwall = Wall(0,0,horiz = True)
    horwall2 = Wall(0,584,horiz = True)
    background = Background()

    ball.set_pos()
    
    BgSprites = pygame.sprite.Group(background,verwall,verwall2,horwall,horwall2)
    ActiveSprites = pygame.sprite.Group(ball,bat,bat2)
    score = Score()

    if settings.get_mode() == 'space':
        startbgm('space')
    else:
        startbgm('grass')

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if score.gameend:
                running = False
                    
        BgSprites.update()
        ActiveSprites.update()
        BgSprites.draw(screen)
        ActiveSprites.draw(screen)
        score.update()
        pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mouse.set_visible(1)




    


    


        


