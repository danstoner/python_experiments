# https://www.youtube.com/watch?v=-NvpKDReKyg
# Kivy crash course 3

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
# BoxLayout puts child widget in a row vertically or horizontally
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

class TutorialApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=150,
                      size_hint_y=None,
                      height=200,
                      text='default')

        f = FloatLayout()
        # Scatter for touch and pinch properties
        s = Scatter()

        l = Label (text="Hello!",
                 font_size=150)

        t.bind(text=l.setter('text'))

        f.add_widget(s)
        f.add_widget(l)

        b.add_widget(t)  # order here controls order on screen
        b.add_widget(f)
        return b   # b is the new root widget to contain the other widgets

if __name__ == "__main__":
    TutorialApp().run()

