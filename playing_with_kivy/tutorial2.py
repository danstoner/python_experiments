# https://www.youtube.com/watch?v=F7UKmK9eQLY

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

#from kivy.uix.button import Button

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()    # Scatter for touch and pinch properties
        l = Label (text="Hello!",
                 font_size=150)

        f.add_widget(s)   # everything is added to the float layer
        f.add_widget(l)
        return f

if __name__ == "__main__":
    TutorialApp().run()

