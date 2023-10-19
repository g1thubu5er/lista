#1)Faça um programa que simule um "dado virtual". O dado deve ser modelado como uma classe,
#possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado. O número
#de faces deve ser definido na criação do objeto (construtor com parâmetro). Deve ser instanciado
#um dado com 6, 8 e 12 faces no main(). Cada dado deve ser jogado 3 vezes e o resultado de cada
#jogada deve ser impresso na tela. Não deve ser usado print dentro da classe.

import random

class dado:

    def __init__(self,faces):
        self.faces = faces

def rolar(self):
    num = random.randint(1,self.faces)
    return num

dado1 = dado(6)
dado2 = dado(8)
dado3 = dado(12)
count = 0

while count<3:

    input('Aperte enter para jogar o dado de 6 faces')
    jogada = rolar(dado1)
    print(jogada)
    count+=1

else:
    count = 0

while count<3:

    input('Aperte enter para jogar o dado de 8 faces')
    jogada = rolar(dado2)
    print(jogada)
    count+=1

else:

    count = 0

while count<3:

    input('Aperte enter para jogar o dado de 12 faces')
    jogada = rolar(dado3)
    print(jogada)
    count+=1

else:

    print('Suas jogadas acabaram')


#2) Crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois
#números. Cada um destes métodos recebe por parâmetro dois números reais e retorna o
#resultado da operação com os dois números. Se houver divisão por zero, imprimir um aviso na
#execução do método e retornar -1.



class calculadora:

    def __init__(self,resultado):
        self.resultado = resultado


    def somar(self, num1, num2):
        self.resultado = num1+num2
        return self.resultado


    def subtrair(self,num1,num2):
        self.resultado = num1-num2
        return self.resultado

    def multiplicar(self,num1,num2):
        self.resultado = num1*num2
        return self.resultado

    def dividir(self,num1,num2):
        if num2 == 0:
            print("DIVISÃO POR ZERO")
            self.resultado = -1
            return self.resultado

        else:

            self.resultado = num1/num2
            return self.resultado


calcular = calculadora(0)

num1 = int(input("informe o primeiro número: "))
num2 = int(input("informe o segundo número: "))

calcular.somar(num1,num2)
print("soma = {:.2f}".format(calcular.resultado))

calcular.subtrair(num1,num2)
print("subtração = {:.2f}".format(calcular.resultado))

calcular.multiplicar(num1,num2)
print("multiplicação = {:.2f}".format(calcular.resultado))

calcular.dividir(num1,num2)
print("divisão = {:.2f}".format(calcular.resultado))


#3) Crie uma classe CadastroCliente com os atributos nome, sobrenome, data de nascimento, email,
#CPF e senha. Faça um pequeno programa que permita o cliente se cadastrar e depois consultar
#seus dados. Para consultar seus dados, é necessário que ele faça o login com seu email e senha.
#Se o cliente errar a senha 3x, o cadastro é bloqueado e ele não pode mais acessar


class CadastroCliente:

    def __init__(self,nome,sobrenome,dataNascimento,email,cpf,senha):

        self.nome =nome
        self.sobrenome =sobrenome
        self.dataNascimento =dataNascimento
        self.email =email
        self.cpf =cpf
        self.senha =senha


    def consulta(self):
        print("Nome: ",self.nome," ",self.sobrenome)
        print("Data de nascimento: ",self.dataNascimento)
        print("E-mail: ",self.email)
        print("CPF: ",self.cpf)


    def verificação(self,login1,senha1):

        if login1 == self.email and senha1 == self.senha:

            return True

        else:

            return False


nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
dataNascimento = input("Informe sua data de nascimento: ")
email = input('Informe seu e-mail: ')
cpf = input("Informe seu CPF: ")
senha = input("Informe sua senha: ")


cadastro = CadastroCliente(nome,sobrenome,dataNascimento,email,cpf,senha)

count = 0

while count<3:

    login1 = input("Informe seu e-mail: ")
    senha1 = input("Informe sua senha: ")

    verificacao = cadastro.verificação(login1,senha1)

    if verificacao == True:
        cadastro.consulta()
        break

    else:

        print("Sua senha ou seu nome de usuário está incorreto")
        count+=1
else:

    print("Cadastro bloqueado")


#4)Corrida maluca. Vamos simular uma corrida com 5 competidores...


import random

class Competidor:

    def __init__(self,nome):
        self.nome = nome
        self.posicao = 0

    def get_posicao(self):
        self.posicao +=1
        return self.posicao 


    def atualizar(self,tabuleiro):
        sorteio = random.randint(2,6)
        self.posicao += sorteio

        if self.posicao % 5 == 0 :
            self.posicao -= 1

        elif self.posicao == 7 or self.posicao == 17:
            self.posicao += 2

        elif self.posicao == 13:
            self.posicao == 0

        elif self.posicao >=20:
            pass

        else:
            self.posicao == self.posicao

        for i in range(len(tabuleiro)):
            i += self.posicao 

            if tabuleiro[i] != '*' and tabuleiro[i] != self.nome:
                print(tabuleiro[i],'na mesma posição de ',self.nome)
                sorteio = random.randint(0,10)

                if sorteio % 2==0:
                    print(self.nome,'passou de ',tabuleiro[i])
                    tabuleiro[i] = self.nome
                    print(tabuleiro)
                    break

                else:
                    print(tabuleiro[i],' não mudou de posição')
                    print(tabuleiro)
                    break

            else:    
                tabuleiro[i] = self.nome
                print(tabuleiro)
                break



nome1 = input('Informe o nome do primeiro piloto: ')
piloto1=Competidor(nome1)

nome2 = input('Informe o nome do segundo piloto:')
piloto2 = Competidor(nome2)

nome3 = input('Informe o nome do terceiro piloto: ')
piloto3 = Competidor(nome3)

nome4 = input('Informe o nome do quarto competidor: ')
piloto4 = Competidor(nome4)

nome5 = input('Informe o nome do quinto piloto: ')
piloto5 = Competidor(nome5)

tabuleiro = ['*']*20

tamanho=len(tabuleiro)

while tabuleiro[tamanho-1] == '*':

    print('Jogador:', piloto1.nome)
    piloto1.atualizar(tabuleiro)
    piloto1.get_posicao()
    print("Posição: ", piloto1.posicao)
    print('')

    input("Pressione enter para a próxima rodada")
    print('Jogador:', piloto2.nome)
    piloto2.atualizar(tabuleiro)
    piloto2.get_posicao()
    print("Posição: ", piloto2.posicao)
    print('')

    input("Pressione enter para a próxima rodada")
    print('Jogador:', piloto3.nome)
    piloto3.atualizar(tabuleiro)
    piloto3.get_posicao()
    print("Posição: ", piloto3.posicao)
    print('')

    input("Pressione enter para a próxima rodada")
    print('Jogador: ', piloto4.nome)
    piloto4.atualizar(tabuleiro)
    piloto4.get_posicao()
    print("Posição: ", piloto4.posicao)
    print('')

    input("Pressione enter para a próxima rodada")
    print('Jogador: ', piloto5.nome)
    piloto5.atualizar(tabuleiro)
    piloto5.get_posicao()
    print("Posição: ", piloto5.posicao)
    print(" ")
    input("Pressione enter para a próxima volta")

else:

    print('Posições finais')
    tabuleiro.reverse()
    posFinal=[]

    for a in range(3):
        for i in range(len(tabuleiro)):
            if tabuleiro[i] != '*' and tabuleiro[i] not in(posFinal):    
                posFinal.append(tabuleiro[i])

    for p in range(len(posFinal)):
        print(posFinal[p],'-',p + 1,' lugar!')
