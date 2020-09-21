# operadores da divisão (/) e resto da divisão (%)
#divisao = 15 / 2
#resto = 15 % 2

#print('divisao', divisao)
#print('resto', resto)

# Ler um numero para ver se ele é par ou impar
numero = int(input('Informe um numero:'))
# calcula o resto da divisão do numero par por 2
resto = numero % 2
# olha para o valor do resto
if resto == 0:
  print(numero, 'par!')
else:
  print(numero, 'impar!')
