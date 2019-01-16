from tkinter import *

def comando1 ():
    print('Led Azul Ligado')
def comando2 ():
    print('Led Vermelho Ligado')

janela = Tk()
janela.title('Raspiberry Controller')
janela.geometry('500x500')
texto1 = Label(text='Pressione o Botão do Led que deseja ligar')
texto1.pack()
botao1 = Button(text='Ligar Led Azul', command = comando1).pack()
botao2 = Button(text='Ligar Led Vermelho', command = comando2).pack()
janela.mainloop()
