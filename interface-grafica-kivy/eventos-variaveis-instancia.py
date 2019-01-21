from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class PrimeiroApp(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')
        button = Button(text='Botao1' ,font_size=30,on_release=self.increase)
        label = Label(text='Texto1' ,font_size=30)
        box.add_widget(button)
        box.add_widget(label)
        return box

    def increase(self, button):
        button.text = 'Soltei'

PrimeiroApp().run()
