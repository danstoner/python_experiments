# https://www.youtube.com/watch?v=OkW-1uzP5Og
# Kivy crash course 6
# Kivy properties

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout   # puts child widget in a row vertically or horizontally

# import random

class ScatterTextWidget(BoxLayout):
    # def change_label_colour(self, *args):
    #     colour = [random.random() for i in xrange(3)] + [1]
    #     label = self.ids['my_label']
    #     label.color = colour
    pass

class Tutorial6App(App):   # kivy looks for a kivy file that matches the name of the app, e.g. the first part of "TutorialApp"
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    Tutorial6App().run()

