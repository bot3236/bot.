# meu primeiro codigo funcional,ele conferi se o usuario tem ou não a senha correta para ser um usuario um vip ou não tem autorização.
usuario = input("qual o seu nome? ")
senha= input("digite uma senha:")
usuario_vip = (senha == '123456')
if senha == "123456":
    print (f'parabens {usuario} voce é um usuario VIP')
elif senha == '1234':
    print (f'vem vindo {usuario}')
else:
    print (f'{usuario} voce não está autorizado!!!')
