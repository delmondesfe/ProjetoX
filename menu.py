import os
import cadastro
import consulta
import pymysql.cursors

def menu():
    print('Digite: 1-Cadastro 2-Consulta\n')

    escolha = int(input("Escolha: "))

    if (escolha == 1):
        cadastro.cadastra_produto()
        print('Produto cadastrado com sucesso!!')
        input('Continuar')


    elif (escolha ==2):
        consulta.consulta_produto()
        input('Continuar')

clear = lambda: os.system('clear')
        
clear()

while True:
    #print("\033[2;1H")
    print('**Controle de estoque**')
    opt = int(input('1 - Menu cadastro\n2 - Sair\nEscolha: ' ))

    if opt ==1:
        menu()
        clear()
    elif opt ==2:
        clear()
        break