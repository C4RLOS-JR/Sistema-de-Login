from sqlalchemy import exists
from Model import Session, Cadastro
from hashlib import sha256
from os import system
import re


session = Session()

class CadastroController:

  def validarEmail(email):
    x = session.query(Cadastro).all()

    for i in x:
      if i.email == email:
        return True
    return False
  

  def validarSenha(senha):
    if len(senha) >= 8:
      if re.search('[A-Z]', senha) or re.search('[a-z]', senha):
        if re.search('[0-9]', senha):
          if re.search('[!@#$%^&*]', senha):
            senha = sha256(senha.encode()).hexdigest()
            return senha
    return False

  def adicionarUsuario(self, nome, email, senha):

    emailExiste = CadastroController.validarEmail(email)
    senhaValida = CadastroController.validarSenha(senha)

    if not emailExiste and senhaValida:
      usuario = Cadastro(nome=nome,
                      email=email, 
                      senha=senhaValida)
      session.add(usuario)
      session.commit()
      print('>> Cadastro realizado com sucesso!')
      return True
    elif emailExiste:
      print('>> Email já cadastrado!\n'
            'Esse email já existe em nosso banco de dados.')
    elif not senhaValida:
      print('>> Esta senha não é válida!\n'
            'A senha tem que ter 8 ou mais digitos\n'
            'Possuir letra maiúscula, minúscula, números e caracteres especiais.')
    return False
    
    



class LoginController:

  def validaLogin(email, senha):
    senha = sha256(senha.encode()).hexdigest()  






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





  # if CadastroController.validarSenha(senha):
  #   print('Senha válida')
    
  #   break
  # else:
  #   print('Senha inválida')







