from produto_class import Produto
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Amil@2020',
                             db='estoque',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


print ('Controle de estoque')

print('Digite: 1-Cadastro 2-Consulta\n')

escolha = int(input("Escolha: "))

if (escolha == 1):
    tipo = input("Qual o tipo do produto: ")
    genero = input("Qual o gênero do produto: ")
    tamanho = input('Qual o tamanho: ')
    cor = input('Digite a cor: ')
    marca = input('Qual a marca: ')
    estoq_var = input('Qual a quantidade: ')

    prod1 = Produto(tipo,genero,tamanho,cor,marca,estoq_var)

    with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `produtos` (`tipo`, `genero`,`tamanho`,`marca`,`cor`,`quantidade`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (prod1.tipo,prod1.genero,prod1.tamanho,prod1.marca,prod1.cor,prod1.quantidade))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
    connection.commit()


    print ('Cadastro efetuado com sucesso')
elif (escolha ==2):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM produtos WHERE `quantidade`>%s"
        cursor.execute(sql, ('0',))
        for  item in cursor.fetchall():
            print(item)

    connection.close()