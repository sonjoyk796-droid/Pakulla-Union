from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase
import os

# বাংলা ফন্ট থাকলে লোড করবে, না থাকলেও অ্যাপ চলবে
if os.path.exists("NotoSansBengali.ttf"):
    LabelBase.register(name="Bangla", fn_regular="NotoSansBengali.ttf")
    FONT = "Bangla"
else:
    FONT = "Roboto"

class PakullaApp(App):
    def build(self):
        return Label(
            text="পাকুল্লা ইউনিয়ন\nডিজিটাল সেবা কেন্দ্র\n\nস্বাগতম!",
            font_name=FONT,
            font_size="24sp",
            halign="center"
        )

PakullaApp().run()