# Indexação com Strings
s = 'Mauricio de Andrade Junior'
#print(s.find('c'))
#print(s.count('A'))
#print(s.split('a'))
#print(s.lower())
#print(s.upper())
#print(s[0])
#print(s[0],s[12],s[20])
#print(s[3:])
#print(s[:20])

# Slice (Fatiamento :  ::)
#print(s[::1])
#print(s[::2])

# Indexação com Números
num = [1,2,3,4,5,6,7]
num[0] = "x"
num[2] = "y"
print(num)
#print(num[0], num[2], num[4])

#lista = [1, 2, 3, 4, 5]
#indice = len(lista) -2
#print(indice)

print("Python" == "R")
print("Python" == "Python")

listamercado1 = "Biscoitos", "Arroz", "Feijão", "Manteiga"
#print(listamercado1)

listamercado2 = ["Ovos", "Farinha", "Leite Ninho", "Pão"]
listamercado2[3] = "Chocolate"
#print(listamercado2)

item1 = listamercado1[0], listamercado1[3]
item2 = listamercado2[2], listamercado2[3]
del listamercado2[1]
print(listamercado2)
print(item1, item2)

# Listas dentro de Listas
l1 = [[1,2,3,4],["Mauricio de Andrade Junior"],[5.5, 6.8]]
# Retorna elemento Linha x Coluna
print(l1[2][1]+10)
indice = len(l1)
print(indice)
print(2 in l1)


l2 = [[20, 21, 22, 23, 24],[30, 31, 32, 33, 34],[40, 41, 42, 43, 44]]
l2.append("Carne")
l2.append("Carne")
print(l2.count("Arroz"))
print(l2.insert(2, "Arroz"))
print(l2)
#print(min(l2))
#print(min(l2[1]))
#print(max(l2[2]))
#print(max(l2[0]))
#print(min(l2[1]))

l3 = []
l3.append(53)
l3.append(54)
l3.append(55)
print(l3)
print(l3.index(54))

# Criando Dicionários
estudantes_dict = {"Matheus":24, "José":22, "Tatiana":26, "Madruga":34}
print(estudantes_dict)
print(estudantes_dict["Tatiana"])
estudantes_dict["Pedrinho"]=17
print(estudantes_dict)

estudantes = {"Mauricio":24, "Fernanda":22, "Tamires":26, "Cristiano":25}
estudantes["Chiquinha"]=12
print(estudantes)
print(len(estudantes))
print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())
print(estudantes_dict.update(estudantes))

dic1 = {}
dic1["Feijão"] = "R$5,00"
dic1["Arroz"] = "R$9,90"
print(dic1)
print(dic1.keys())
print(dic1.values())

dic2 = {}
dic2["Patinho"] = "12,00"
dic2["Alcatra"] = "17,00"
dic2["Cortes"] = ["Especiais", "Nobres", "Burgueses"]
print(dic2)
print(dic2["Patinho"])
print(dic2["Cortes"][1])
print(len(dic2))

#Estudo de Tuplas
t1 = ("Geografia", 23, "Elefante")
print(t1[2])
print(len(t1))