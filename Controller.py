from Model import Session, Cadastro
from hashlib import sha256
import re


session = Session()

x = session.query(Cadastro).all()
for i in x:
  if i.senha == '654321':
    print(f'Nome: {i.nome}\n'
          f'Email: {i.email}\n'
          f'Senha: {i.senha}')



class CadastroController:

  def validarEmail(email):
    return True

  def validarSenha(senha):
    if len(senha) >= 8:
      if re.search('[A-Z]', senha) or re.search('[a-z]', senha):
        if re.search('[0-9]', senha):
          if re.search('[!@#$%^&*]', senha):
            senha = sha256(senha.encode()).hexdigest()
            print(f'Hash da senha: {senha}')
            return senha
    return False

  def adicionarUsuario(nome, email, senha):
    email = CadastroController.validarEmail(email)
    senha = CadastroController.validarSenha(senha)

    user = Cadastro(nome=nome,
                    email=email, 
                    senha=senha)
    
    



class LoginController:

  def validaLogin(email, senha):
    senha = sha256(senha.encode()).hexdigest()  








# while True:
#   senha = input('Digite uma senha: ')

#   if CadastroController.validarSenha(senha):
#     print('Senha válida')
    
#     break
#   else:
#     print('Senha inválida')







