import sys
import re

cpf_inserido = input('Insira os nove primeiros digitos numéricos do seu CPF: ')
cpf_corrigido = re.sub(
    r'[^0-9]',  
    '', 
    cpf_inserido
)

nove_digitos = cpf_corrigido[:9]
contador_regressivo1 = 10

if len(cpf_corrigido) != 9:
    print('Você inseriu um CPF inválido!')
    sys.exit()

#elif cpf_corrigido[0] * 11:
    print('O CPF não pode ser um digito repetido diversas vezes.')
    sys.exit()



resultado_digito1 = 0
for digito1 in nove_digitos:
    resultado_digito1 += int(digito1) * contador_regressivo1
    contador_regressivo1 -= 1

digito1 = (resultado_digito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
##Separador do Primeiro e do Segundo digito.

dez_digitos = cpf_corrigido[:9] + str(digito1)

contador_regressivo2 = 11
resultado_digito2 = 0

for digito2 in dez_digitos:
    resultado_digito2 += int(digito2) * contador_regressivo2
    contador_regressivo2 -= 1

digito2 = (resultado_digito2 * 10) % 11
digito2 = digito2 if digito2 <=9 else 0

print(f'O primeiro digito do seu CPF é {digito1} e o segundo {digito2}. \n \
O seu CPF completo é: {cpf_inserido}-{digito1}{digito2}.')




        