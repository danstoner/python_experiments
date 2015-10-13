# https://www.youtube.com/watch?v=ZVWAKzR63ig
# Kivy crash course 4

## Kivy language

from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout   # puts child widget in a row vertically or horizontally

class ScatterTextWidget(BoxLayout):
    pass

class TutorialApp(App):   # kivy looks for a kivy file that matches the name of the app, e.g. the first part of "TutorialApp"
    def build(self):
        # b = BoxLayout(orientation='vertical')
        # t = TextInput(font_size=150,
        #               size_hint_y=None,
        #               height=200,
        #               text='default')

        # f = FloatLayout()
        # s = Scatter()    # Scatter for touch and pinch properties
        # l = Label (text="Hello!",
        #          font_size=150)

        # t.bind(text=l.setter('text'))

        # f.add_widget(s)   # everything is added to the float layer
        # f.add_widget(l)

        # b.add_widget(t)  # order is important in vertical layout
        # b.add_widget(f)
        # return b   # b is the new root widget to contain the other widgets
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()

