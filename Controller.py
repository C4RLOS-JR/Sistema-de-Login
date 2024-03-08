from sqlalchemy import exists
from Model import Session, Cadastro
from hashlib import sha256
import re

session = Session()


class CadastroController:

  def adicionarUsuario(self, nome, email, senha):
    emailExiste = CadastroController.verificarEmail(email)
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
            'A senha tem que ter 8 ou mais digitos,\n'
            'possuir letra maiúscula, minúscula,\n'
            'números e caracteres especiais.')
    return False
  
  def verificarEmail(email):
    usuarios = session.query(Cadastro).all()

    for usuario in usuarios:
      if usuario.email == email:
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
  
    
class LoginController:

  def validaLogin(self, email, senha):
    senha = sha256(senha.encode()).hexdigest()  















