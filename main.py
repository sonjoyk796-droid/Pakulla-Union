from kivy.app import App
from kivy.uix.label import Label

class PakullaApp(App):
    def build(self):
        return Label(text="Pakulla Union - Welcome", font_size='20sp')

PakullaApp().run()