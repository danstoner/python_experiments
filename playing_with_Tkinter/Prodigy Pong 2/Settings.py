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

#The Settings Class (To store game settings)
    
class Settings:
    mode = 'space'
    difficulty = 'normal'
    players = 1
    device = 'keyboard'
    
    def set_mode(self,mode):
        self.mode = mode

    def get_mode(self):
        return self.mode
        
    def set_difficulty(self,diff):
        self.difficulty = diff

    def get_difficulty(self):
        return self.difficulty

    def set_screen(self,scr):
        self.screen = scr

    def get_screen(self,scr):
        return self.screen

    def set_players(self,players):
        self.players = players

    def get_players(self):
        return self.players

    def set_device(self,dev):
        self.device = dev

    def get_device(self):
        return self.device
