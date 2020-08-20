class Funcionarios:
    def __init__(self, cpf, nome, cargo):
        self.cpf = cpf
        self.nome = nome
        self.cargo = cargo

def cadastra_func():

    cpf = input('Digite o CPF do Funcionario para cadastro: ')
    nome = input('Digite o nome completo: ')
    cargo = input('Digite a função dentro da empresa: ')

    funcs = Funcionarios(cpf,nome,cargo)

    print('Funcionário {} cadastrado'.format(funcs.nome))
    


    
