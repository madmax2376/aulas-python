from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=25, size_hint_y=None, height=200))
    

class Scrvw(App):
    def build(self):
        return Tarefas(['Fazer Compras','Buscar Filho','Beber Água','Pagar Contas','Corrida da Manhã','Estudar Python','Estudar Economia'])

Scrvw().run()
