import pymysql.cursors


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Amil@2020',
                             db='estoque',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class Produto:
    def __init__(self, tipo,genero,tamanho,cor,marca,quantidade):
        self.tipo = tipo
        self.genero = genero
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca
        self.quantidade = quantidade


def consulta_produto():
    with connection.cursor() as cursor:
            
            sql = "SELECT * FROM PRODUTO WHERE `QUANTIDADE`>=%s"
            cursor.execute(sql, ('0',))
            for item in cursor.fetchall():
               print(item)
    connection.close()

def cadastra_produto():
    
    tipo = input("Qual o tipo do produto: ")
    genero = input("Qual o gênero do produto: ")
    tamanho = input('Qual o tamanho: ')
    cor = input('Digite a cor: ')
    marca = input('Qual a marca: ')
    estoq_var = int(input('Qual a quantidade: '))

    prod1 = Produto(tipo,genero,tamanho,cor,marca,estoq_var)

    with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `PRODUTO` (`TIPO`, `GENERO`,`TAMANHO`,`MARCA`,`COR`,`QUANTIDADE`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (prod1.tipo,prod1.genero,prod1.tamanho,prod1.marca,prod1.cor,prod1.quantidade))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
    connection.commit()