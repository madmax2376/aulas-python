from Pessoa_Fisica import pessoafisica
from Pessoa_Juridica import pessoajuridica

a = pessoafisica('105.568.057-80', nome='Mauricio', idade='33 anos')

print(a.getCPF())
print(a.getNome())
print(a.getIdade())

b = pessoajuridica('64.614.527/0001-99', nome='DevInside', idade='02 anos')

print(b.getCNPJ())
print(b.getNome())
print(b.getIdade())
