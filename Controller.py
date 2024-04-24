from Model import Session, Cadastro
from hashlib import sha256
from termcolor import cprint
from os import system
import re

session = Session()
usuarios = session.query(Cadastro).all()

def verificarEmail(email):
    for usuario in usuarios:
      if usuario.email == email:
        return True
    return False

def verificarSenha(senha):
  for usuario in usuarios:
    if usuario.senha == senha:
      return True
  return False
  
def validarSenha(senha):
  if len(senha) >= 8:
    if re.search('[A-Z]', senha) and re.search('[a-z]', senha) and re.search('[0-9]', senha) and re.search('[!@#$%^&*]', senha):
          senha = sha256(senha.encode()).hexdigest()
          return senha
  return False


class CadastroController:

  def adicionarUsuario(self, nome, email, senha):
    email_existe = verificarEmail(email)
    senha_valida = validarSenha(senha)

    if not email_existe and senha_valida:
      usuario = Cadastro( nome=nome,
                          email=email, 
                          senha=senha_valida)
      session.add(usuario)
      session.commit()
      system('clear')
      cprint('>> CADASTRO REALIZADO COM SUCESSO!', color='light_green')
      print('Faça o login para entrar!')
      return True
    elif email_existe:
      cprint('>> EMAIL JÁ CADASTRADO!', color='light_red')
      print('Esse email já existe em nosso banco de dados.')
    elif not senha_valida:
      cprint('>> SENHA INVÁLIDA!', color='light_red')
      print('A senha tem que ter 8 ou mais digitos,\n'
            'possuir letra maiúscula, minúscula,\n'
            'números e caracteres especiais.')
    return False
  
 
class LoginController:

  def validaLogin(self, email, senha):
    senha = sha256(senha.encode()).hexdigest()
    email_existe = verificarEmail(email)
    senha_existe = verificarSenha(senha)

    if email_existe:
      if senha_existe:
        system('clear')
        cprint('LOGIN EFETUADO COM SUCESSO!', color='light_green')
        print('Seja bem vindo!')
        return True
      else:
        cprint('>> SENHA NÃO CONFERE!', color='light_red')
        print('Tente outra senha ou cadastre-se!')
    else:
      cprint('>> EMAIL NÃO EXISTE!', color='light_red')
      print('Não existe usuário com este email!\n'
            'Tente novamente ou cadastre-se!')
    return False