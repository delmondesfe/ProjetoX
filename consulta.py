from produto_class import Produto
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Amil@2020',
                             db='estoque',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def consulta_produto():
    with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM produtos WHERE `quantidade`>%s"
            cursor.execute(sql, ('0',))
            for  item in cursor.fetchall():
                print(item)

    connection.close()
