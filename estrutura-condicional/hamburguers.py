print('**********BEM VINDO A NOSSA HAMBURGUERIA, CONHEÇA NOSSO CARDÁPIO**********')
print('PEÇA PELO NÚMERO "1" DOGÃO BOLADO - PREÇO: R$4,00')
print('PEÇA PELO NÚMERO "2" X-SALADA - PREÇO: R$4,50')
print('PEÇA PELO NÚMERO "3" X- BACON - PREÇO: R$5,00')
print('PEÇA PELO NÚMERO "4" TORRADINHA - PREÇO: R$2,00')
print('PEÇA PELO NÚMERO "5" DOLLY GUARANÁ - PREÇO: R$1,50')
cq = 4.00
xs = 4.50
xb = 5.00
tr = 2.00
rf = 1.50
qtd = cq, xs, xb, tr, rf
num = int(input('Digite o número do seu lanche: '))
qtd = int(input('Quantos dele você deseja? '))

if (num==1):
    totalcq = qtd * cq
    print('O TOTAL A SER PAGO É: R$', totalcq)
    print('**********OBRIGADO PELA PREFERÊNCIA E VOLTE SEMPRE**********')

if (num==2):
    totalxs = qtd * xs
    print('O TOTAL A SER PAGO É: R$', totalxs)
    print('**********OBRIGADO PELA PREFERÊNCIA E VOLTE SEMPRE**********')

if (num==3):
    totalxb = qtd * xb
    print('O TOTAL A SER PAGO É: R$', totalxb)
    print('**********OBRIGADO PELA PREFERÊNCIA E VOLTE SEMPRE**********')

if (num==4):
    totaltr = qtd * tr
    print('O TOTAL A SER PAGO É: R$', totaltr)
    print('**********OBRIGADO PELA PREFERÊNCIA E VOLTE SEMPRE**********')

if (num==5):
    totalrf = qtd * rf
    print('O TOTAL A SER PAGO É: R$', totalrf)
    print('**********OBRIGADO PELA PREFERÊNCIA E VOLTE SEMPRE**********')
