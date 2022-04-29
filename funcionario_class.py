import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Amil@2020',
                             db='estoque',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class Funcionarios:
    def __init__(self, cpf, nome, cargo):
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo

def cadastro_funcionario():

    cpf = input('Digite o CPF do Funcionario para cadastro: ')
    nome = input('Digite o nome completo: ')
    cargo = input('Digite a função dentro da empresa: ')

    funcs = Funcionarios(cpf,nome,cargo)

    with connection.cursor() as cursor:
        sql = "INSERT INTO `FUNCIONARIOS` (`CPF`,`NOME`,`CARGO`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (funcs.cpf,funcs.nome,funcs.cargo))

    connection.commit()

def consulta_funcionario():
    with connection.cursor() as cursor:
            
            sql = "SELECT * FROM FUNCIONARIOS WHERE `ID_FUNC`>=%s"
            cursor.execute(sql, ('0',))
            for item in cursor.fetchall():
               print(item)
    connection.close()


    
