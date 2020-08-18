import os
import produto_class


def menu():
    print('Digite: 1-Cadastrar 2-Consulta\n')

    escolha = int(input("Escolha: "))

    if (escolha == 1):
        produto_class.cadastra_produto()
        print('Produto cadastrado com sucesso!!')
        input('Continuar')


    elif (escolha ==2):
        produto_class.consulta_produto()
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