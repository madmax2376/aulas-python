from Pessoa_Fisica import pessoafisica
from Pessoa_Juridica import pessoajuridica

a = pessoafisica('CPF: 105.568.057-80', nome='Mauricio', idade='33 anos')

print(a.getNome())
print(a.getCPF())
print(a.getIdade())

b = pessoajuridica('CNPJ: 64.614.527/0001-99', nome='Empresa: DevInside', idade='02 anos')

print(b.getNome())
print(b.getCNPJ())
print(b.getIdade())
