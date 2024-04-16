from Controller import *
from termcolor import cprint
from os import system

ctrlCadastro = CadastroController()
ctrlLogin = LoginController()

while True:
  system('cls')
  cprint(' SISTEMA DE LOGIN PYTHONFULL! ', color='light_blue')
  print('-' * 30)
  print('1- LOGIN\n'
        '2- CADASTRO\n'
        '3- SAIR')
  print('-' * 30)
  opcao = input('OPÇÃO: ')

  if opcao == '1':
    system('cls')
    cprint(f'{"LOGIN":^30}', color='light_blue')      
    print('-' * 30)
    email = input('DIGITE UM EMAIL: ')
    senha = input('DIGITE UMA SENHA: ')
    print('-' * 30)

    loginEfetuado = ctrlLogin.validaLogin(email, senha)
    input('\nPressione "Enter" para continuar...')

  if opcao == '2':
    system('cls')
    cprint(f'{"CADASTRO":^30}', color='light_blue')
    print('-' * 30)
    nome = input('DIGITE SEU NOME: ')
    email = input('DIGITE SEU EMAIL: ')
    senha = input('DIGITE UMA SENHA: ')
    confirmarSenha = input('CONFIRME A SENHA: ')
    print('-' * 30)

    if senha == confirmarSenha:
      cadastroFeito = ctrlCadastro.adicionarUsuario(nome, email, senha)
    else:
      cprint(">> AS SENHAS NÃO CONFEREM!", color='light_red')
    input('\nPressione "Enter" para continuar...')
  
  if opcao == '3':
    system('cls')
    print('PROGRAMA FINALIZADO!')
    break