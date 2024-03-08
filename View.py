from Controller import *
from os import system


ctrlCadastro = CadastroController()

while True:
  system('cls')
  nome = input('Digite seu nome: ')
  email = input('Digite seu email: ')
  senha = input('Digite uma senha: ')
  confirmarSenha = input('Confirme a senha: ')
  print('-' * 30)

  if senha == confirmarSenha:
    cadastroFeito = ctrlCadastro.adicionarUsuario(nome, email, senha)
    if cadastroFeito:
      break
  else:
    print(">> As senhas não conferem!")
  input('\nPressione "Enter" para continuar...')