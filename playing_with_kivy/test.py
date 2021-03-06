# test kivy app button and text input box

from kivy.app import App
from kivy.config import Config

import os
os.environ["SDL_FBDEV"] = "/dev/fb1"


# set app size for smaller screens
Config.set('graphics', 'width', 320)
Config.set('graphics', 'height', 240)


from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class testWidget(BoxLayout):
    alarming_now = False
    
    # define some colors using RGB (Red, Green, Blue, Opacity)    
    white = (224, 224, 224, 1)
    red = (255, 0, 0, 1)
    green = (0, 102, 0, 1)

    catcodes = ("02225937",
                "01435009",
                "01907121",
                "01661313",
                "02026993"
                )



    def alert_color(self):
        if self.alarming_now:
            return self.red
        else:
            return self.green

    def check_and_reset(self, text):
        if self.is_cat(text):
            # reset the text box to empty and give it focus
            # ?
            self.sound_alarm()
            return True
        else:
            # reset the text box to empty and give it focus
            return False
    
    def is_cat(self, text):
        for cat in self.catcodes:
            if cat in text:
                print "Cat Found!"
                self.alarming_now = True
                return True
        print "Input Received: no cats found."
        return False
            

    def sound_alarm(self):
        if self.alarming_now:
            print "ALARM!"

    def snooze_alarm(self):
        print "Snooze Button pressed."
        self.alarming_now = False



    pass

class TestApp(App):    
    def build(self):
        return testWidget()

if __name__ == "__main__":
    # most of the app description is in test.kv kivy language file
    TestApp().run()
