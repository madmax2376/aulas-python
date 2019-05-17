# Exercícios de Condicionais

# Condicional If
num = int(input("Digite um número inteiro qualquer: "))
if (num > 2):
    print("O numero digitado é maior que 2")
else:
    print("O numero digitado é menor que 2")

nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua Idade: "))
if (nome == "Bob") and (idade >=18):
    print("Acesso autorizado")
else:
    print("Acesso Negado")

dia = str(input("Digite um dia da semana: "))
if (dia == "Segunda"):
    print("Hoje o tempo é de muito Sol!")
elif (dia == "Terça"):
    print("Hoje o tempo é de muita chuva!")
else:
    print("Não há previsão de tempo para o dia escolhido.")

# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input(str("Digite o nome da disciplina: "))
nota_final = input(int("Digite a sua nota final entre 0 e 100: "))
semestre = input(int("Digite o semestre entre 1 e 4: "))

if (disciplina == "Geografia") and (nota_final >= 50) and int(semestre != 1):
    print("Voce foi aprovado em %s com média final %r!" %(disciplina, nota_final))
else:
    print("Voce foi reprovado, precisa estudar mais!")