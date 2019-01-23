from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ContadorApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button1 = Button(text='Volume +' ,font_size=25,on_release=self.increase)
        button2 = Button(text='Volume -' ,font_size=25,on_release=self.decrease)
        self.label = Label(text='1' ,font_size=25)
        box.add_widget(button1)
        box.add_widget(button2)
        box.add_widget(self.label)
        return box

    def increase(self, button1):
        self.label.text = str(int(self.label.text)+1)

    def decrease(self, button2):
        self.label.text = str(int(self.label.text)-1)

ContadorApp().run()
