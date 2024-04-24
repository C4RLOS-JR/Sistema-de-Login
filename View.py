from Controller import *
from termcolor import cprint
from os import system

ctrl_cadastro = CadastroController()
ctrl_login = LoginController()

while True:
  system('clear')
  cprint(' SISTEMA DE LOGIN PYTHONFULL! ', color='light_blue')
  print('-' * 30)
  print('1- LOGIN\n'
        '2- CADASTRO\n'
        '3- SAIR')
  print('-' * 30)
  opcao = input('OPÇÃO: ')

  if opcao == '1':
    system('clear')
    cprint(f'{"LOGIN":^30}', color='light_blue')      
    print('-' * 30)
    email = input('DIGITE UM EMAIL: ')
    senha = input('DIGITE UMA SENHA: ')
    print('-' * 30)

    login_efetuado = ctrl_login.validaLogin(email, senha)
    input('\nPressione "Enter" para continuar...')

  if opcao == '2':
    system('clear')
    cprint(f'{"CADASTRO":^30}', color='light_blue')
    print('-' * 30)
    nome = input('DIGITE SEU NOME: ')
    email = input('DIGITE SEU EMAIL: ')
    senha = input('DIGITE UMA SENHA: ')
    confirmar_senha = input('CONFIRME A SENHA: ')
    print('-' * 30)

    if senha == confirmar_senha:
      ctrl_cadastro.adicionarUsuario(nome, email, senha)
    else:
      cprint(">> AS SENHAS NÃO CONFEREM!", color='light_red')
    input('\nPressione "Enter" para continuar...')
  
  if opcao == '3':
    system('clear')
    print('PROGRAMA FINALIZADO!\n')
    break