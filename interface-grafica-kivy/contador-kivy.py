from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Increase(BoxLayout):
    pass

class ContadorApp(App):
    def build(self):
        return Increase()

ContadorApp().run()
