print('Saiba se você está obeso ou se está em forma')
name = str(input('Por favor digite seu nome '))
age = int(input('Por favor digite sua idade '))
weight = float(input('Por favor digite seu peso '))
if weight <= 60:
    print('Olá! '+name+' você está em forma para alguém da sua idade')
    print('*********FIM**********')
else:
    print('Olá! '+name+' você tem obesidade morbida, cuidado, Você morrerrá!')
    print('*********FIM**********')
