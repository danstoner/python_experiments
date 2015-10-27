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

#Game Title and other Dialogs
    
import easygui
import sys


def title():
    image = "gfx/title.GIF"
    msg = 'BURNING PRODIGY Tech.'
    choices = ["START FULLSCREEN GAME","START WINDOWED GAME"]
    reply = easygui.buttonbox(msg,image=image,choices = choices)
    if reply == choices[0]:
        return 'fullscreen'
    elif reply == choices[1]:
        return 'windowed'
    else:
        return

def winp1():
    image = "gfx/winp1.GIF"
    msg = "BURNING PRODIGY Tech."
    choices = ["PLAY AGAIN", "EXIT"]
    reply = easygui.buttonbox(msg,image = image,choices = choices)
    if reply == 'PLAY AGAIN':
        return
    else:
        sys.exit()
        
def winp2():
    image = "gfx/winp2.GIF"
    msg = "BURNING PRODIGY Tech."
    choices = ["PLAY AGAIN", "EXIT"]
    reply = easygui.buttonbox(msg,image = image,choices = choices)
    if reply == 'PLAY AGAIN':
        return
    else:
        sys.exit()
