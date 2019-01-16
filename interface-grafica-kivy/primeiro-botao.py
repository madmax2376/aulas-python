# Desenvolvendo Janelas com Kivy
from kivy.app import App
from kivy.uix.button import Button


class PrimeiroApp(App):
    def build(self):
        return Button(text='Botão Python+Kivy')

PrimeiroApp().run()
