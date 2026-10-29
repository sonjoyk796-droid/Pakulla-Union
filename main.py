__version__ = "1.0"
from kivy.app import App
from kivy.uix.label import Label

class PakullaApp(App):
    def build(self):
        return Label(text="Pakulla Union")

PakullaApp().run()