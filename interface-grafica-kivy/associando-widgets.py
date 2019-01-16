from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class PrimeiroApp(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')
        button = Button(text='Botao1')
        label = Label(text='Texto1')
        box.add_widget(button)
        box.add_widget(label)
        return box

PrimeiroApp().run()
