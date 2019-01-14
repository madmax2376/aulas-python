import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.1')

class PrimeiroApp(App):
    def build(self):
        return Label(text='O meu ficou mais foda!!!')

if __name__ == '__main__':
    PrimeiroApp().run()
