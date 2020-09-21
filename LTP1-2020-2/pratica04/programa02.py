# pede para o usuario digitar uma senha e valida ela com a senha secreta
# cria uma variavel para guardar uma senha
senha_secreta = '123456'

#pede para o usuario digitar uma senha
senha = input ('Informe uma senha')

#verifica se a senha do usuario esta corrreta
if senha == senha_secreta:
  print('Bem vindo Hackman')

if senha != senha_secreta:
  print('acesso negado!')
