from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=25))
    

class Trf(App):
    def build(self):
        return Tarefas(['Fazer Compras','Buscar Filho','Beber Água'],orientation='horizontal')

Trf().run()
