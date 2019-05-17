tp = (1,2,3)
for i in tp:
    print(i)

lista = ["Leite", "Pão", "Queijo"]
for i in lista:
    print(i)

for contador in range(0,5):
    print(contador)

lista1 = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista1:
    if (num % 2 == 0):
        print(num)

for i in range(0,101,2):
    print(i)

for i in range(0,5):
    for a in range(0,5):
        print(a)

lista2 = (12,14,16,18)
soma = 0
for i in lista2:
    dobro = i * 2
    soma += dobro
print(soma)

lista3 = [[1,2,3,4],[11,12,13,14],[21,22,23,24]]
for i in lista3:
    print(i)

lista3 = [[1,2,3,4],[11,12,13,14],[21,22,23,24]]
count = 0
for i in lista3:
    count += 1
print(count)

tp1 = ("Joao", "Maria", "Pelé")
for i in tp1:
    if i == "Joao":
        print("Item Encontrado!")
    else:
        print("Item nao encontrado!")