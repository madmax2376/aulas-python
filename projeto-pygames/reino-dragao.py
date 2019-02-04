import random
import time

def displayIntro():
    print('Você está em uma terra cheia de dragões e na sua frente')
    print('você vê duas cavernas. Em uma caverna, o dragão é amigo')
    print('e irá compartilhar seu tesouro com você. Já o outro dragão')
    print('é ganancioso, feroz e está com fome. Irá devorá-lo.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Qual caverna você vai entrar (caverna 1 ou caverna 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('Você está se aproximando da caverna...')
    time.sleep(3)
    print('A caverna é escura e assustadora...')
    time.sleep(2)
    print('Um grande dragão pula em sua frente! Ele abre sua enorme boca e com seus dentes afiados...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Parabéns!!! Você ganhou o tesouro!!!')
    else:
        print('Você foi engolido pelo dragão feroz!!!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    
    caveNumber = chooseCave()

    checkCave (caveNumber)

    print('Você deseja jogar novamente (yes or no)')
    playAgain = input()
