"""
Criando 1º Classe em python
sempre que você quiser criar uma classe, vai fazer:
    class nome_Classe(object):
Dentro da classe, você vai criar a "função"(método) __init__
Esse método é quem define o que acontece quando você cria uma instância da Classe

exemplo : tv

"""
#toda função que está dentro de uma classe é um método

class TV:
    def __init__(self):
    #caracteristica
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'netflix'
        self.volume = 10

#instancia da tv 
tv_sala = TV()
tv_quarto = TV()

print(tv_sala.cor)
print(tv_quarto.canal)

#mudando a cor da tv da sala

tv_sala.cor = 'branca'
print(tv_sala.cor)
print(tv_quarto.cor)

#mudando o tamanho da tv do quarto
tv_quarto.tamanho = 30
print(tv_quarto.tamanho)
print(tv_sala.tamanho)
