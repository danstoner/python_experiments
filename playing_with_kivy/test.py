# test kivy app button and text input box

from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class testWidget(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        return testWidget()

if __name__ == "__main__":
    # most of the app description is in test.kv kivy language file
    TestApp().run()
