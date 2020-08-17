class Produto:
    def __init__(self, tipo,genero,tamanho,marca,quantidade):
        self.tipo = tipo
        self.genero = genero
        self.tamanho = tamanho
        self.marca = marca
        self.quantidade = input('Digite a quantidade: ')