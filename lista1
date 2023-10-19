#1. Adicione mais 2 atributos e 2 métodos à classe Mago. 
#2. Instancie 3 objetos da classe mago e invoque seus métodos.

# Definição da classe Mago 

class Mago:
    # Atributos de classe
    possuiMagia = True
    possuiPoderFogo = True
    possuiPoderGelo = True

    # Método construtor
    def __init__(self, nome, idade, escola):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        print('Mago ', self.nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')

    def correr(self):
        print('Estou correndo')

    def descansar(self):
        print('Estou descansando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def cumprimentar(self,nome):
        print('Ola, ', nome)

    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 
        
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts')
gd = Mago('Gandalf', 2000, 'Magia Cinza')
pl = Mago('Patolino', 80, 'Looney Tunes')
yen = Mago('Yennefer', 100, 'Aretusa')
ci = Mago('Ciri', 21, 'Kaer Morhen')

#Acessando atributos públicos
print(hp.nome)
print(hp.idade)
print(hp.escola)

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()
hp.cumprimentar("Rossana")

gd.falar()
gd.cumprimentar("Gabriel")

pl.falar()
pl.andar()
pl.cumprimentar("Perna Longa")

yen.falar()
yen.invocarMagia()
yen.correr()

ci.correr()
ci.cumprimentar("Geralt")

del hp
del gd


#3. Crie uma classe Data, com os seguintes atributos: dia, mês e ano. Além do construtor padrão, a
#classe deverá ter um construtor personalizado que recebe dia, mês e ano por parâmetro. Essa classe
#deve ter também dois métodos: imprimirData, que não recebe parâmetro, e
#imprimirDataPorExtenso, que recebe o nome de uma cidade por parâmetro. Ambos os métodos
#não retornam dados. 

class Data:
    #Atributo da classe
    nomesMeses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    #Método construtor
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimirData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def imprimirDataPorExtenso(self,cidade):

        nomeMes = self.nomesMeses[int(self.mes)-1]

        if self.mes == 1:
            nomeMes = 'Janeiro'
        elif self.mes == 2:
            nomeMes = 'Fevereiro'
        elif self.mes == 3:
            nomeMes = 'Marco'
        elif self.mes == 4:
            nomeMes = 'Abril'
        elif self.mes == 5:
            nomeMes = 'Maio'
        elif self.mes == 6:
            nomeMes = 'Junho'
        elif self.mes == 7:
            nomeMes = 'Julho'
        elif self.mes == 8:
            nomeMes = 'Agosto'
        elif self.mes == 9:
            nomeMes = 'Setembro'
        elif self.mes == 10:
            nomeMes = 'Outubro'
        elif self.mes == 11:
            nomeMes = 'Novembro'
        elif self.mes == 12:
            nomeMes = 'Dezembro'
        print(cidade,' , ',self.dia, ' de ', nomeMes, ' de ', self.ano)    

data = Data(31,8,2023)

data.imprimirData()
data.imprimirDataPorExtenso('Porto Alegre')


#4. Adapte o exercício de revisão (mini-spotify), propondo uma classe Musica. Quais seriam seus
#atributos? Quais seriam alguns dos seus possíveis métodos? Como poderíamos representar uma
#playlist? 

class Musica:

    versaoAcustica = True
    possuiLetra = True

    def __init__(self, nome, artista, genero, ano, duracao):

        self.nome = nome
        self.artista = artista
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

        print('A música:', self.nome, 'de', self.artista, 'foi adicionada à sua playlist!')

    def tocar(self):
         print('Tocando música')

    def pausar(self):
        print('Música pausada')

    def aumentarSom(self):
        print('O som foi aumentado')

    def diminuirSom(self):
        print('O som foi diminuido')


    def __del__(self):
        print('A música foi deletada!')


ff = Musica('Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05')
sp = Musica('Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58')
rr = Musica('Rock n Rolo', 'The Buns','Rock',	1984, '4:01')
gg = Musica( 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25')
om = Musica('Outra musica', 'Anira', 'Funk', 2019, '3:05')

print(ff.nome)
print(sp.artista)
print(rr.genero)
print(gg.ano)
print(om.duracao)

ff.tocar()
ff.pausar()

sp.tocar()
sp.aumentarSom()

rr.tocar()

gg.tocar()
gg.diminuirSom()

om.tocar()
om.aumentarSom()
om.pausar()


del ff
del sp
del rr
del gg
del om
