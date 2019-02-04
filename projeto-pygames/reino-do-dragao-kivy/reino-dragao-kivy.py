from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Reinos(ScrollView):
    def __init__(self, reinos, **kwargs):
        super().__init__(**kwargs)
        for reino in reinos:
            self.ids.box.add_widget(Label(text=reino, font_size=20, size_hint_y=None, height=25))
    

class Ren(App):
    def build(self):#Método de construção do título     
        return Reinos(['Você está em uma terra cheia de dragões!!! Inesperadamente à sua frente,',
        'você vê duas cavernas. Em uma caverna, o dragão é amigo',
        'e irá compartilhar seu tesouro com você. Já o outro dragão',
        'é ganancioso, feroz e está com muita fome. Ele quer muito devorá-lo!',
        'Qual caverna você vai entrar (caverna 1 ou caverna 2)'])

Ren().run()
