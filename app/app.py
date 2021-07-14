from servicos import *

while True:
    print('#' * 34)
    print('# 1 - Novo cadastro -------------#')
    print('# 2 - Buscar cadastro por nome---#')
    print('# 3 - Alterar cadastro-----------#')
    print('# 4 - Mostrar todos--------------#')
    print('# 5 - Excluir cadastro-----------#')
    print('# 6 - Buscar por matricula-------#')
    print('# 7 - Sair-----------------------#')
    print('#' * 34)

    op = input( 'Informe a operação: ')

    if op == '1':
        nome = input('Informe o nome: ')
        matricula = int(input('Informe sua matricula: '))
        nome_mae = input('Informe o nome da mãe: ')
        idade = input('Informe sua idade: ')
        telefone = input('Informe um telefone: ')
        sexo = input('Informe seu sexo: ')
        endereço = input('Informe seu endereço: ')
        novo_cadastro(nome, matricula, nome_mae, idade, telefone, sexo, endereço)
        gerar_log("Um aluno foi cadastrado com sucesso!")


    elif op == '2':
        nome = input('Informe o nome do aluno  cadastro: ')
        nome_buscas = buscar_por_nome(nome)
        for nome_busca in nome_buscas:
            print('')
            print('Nome:', nome_busca[0])
            print('Matricula:', nome_busca[1])
            print('Nome mãe:', nome_busca[2])
            print('Idade:', nome_busca[3])
            print('Telefone:', nome_busca[4])
            print('Sexo:', nome_busca[5])
            print('Endereço:', nome_busca[6])
            print('')

        gerar_log( "Busca foi feita com sucesso!")

    elif op == '3':
        matricula = int(input('Informe matricula do contato que você quer alterar: '))
        novo_nome = (input('Informe seu nome: '))
        novo_nome_mae = input('Informe o nome da mae: ')
        nova_idade = (input('Informe sua idade: '))
        novo_sexo = input('Informe seu sexo: ')
        novo_telefone = (input('Informe seu telefone: '))
        novo_endereço = input('Informe seu endereço: ')
        alterar_cadastro(novo_nome, novo_nome_mae,nova_idade, novo_telefone, novo_sexo, novo_endereço, matricula)
        gerar_log("Cadastro foi alterado com sucesso!")

    elif op == '4':
        alunos = mostrar_todos()
        for aluno in alunos:
            print('')
            print('Nome:', aluno[0])
            print('Matricula:', aluno[1])
            print('Nome mãe:', aluno[2])
            print('Idade:', aluno[3])
            print('Sexo:', aluno[4])
            print('Telefone:', aluno[5])
            print('Endereço:', aluno[6])
            print('')
    elif op == '5':
        matricula = input( 'Informe a matricula do aluno: ')
        excluir_cadastro(matricula)
        gerar_log("Cadastro excluido com sucesso!")

    elif op == '6':
        matricula_busca = int(input('Informe sua matricula: '))
        matricula = buscar_por_matricula(matricula_busca)
        print('')
        print('Nome:', matricula[0])
        print('Matricula:', matricula[1])
        print('Nome mãe:', matricula[2])
        print('Idade:', matricula[3])
        print('Sexo:', matricula[4])
        print('Telefone:', matricula[5])
        print('Endereço:', matricula[6])
        print('')
        gerar_log('Buscar_por_matricula feita com sucesso!')


    elif op == '7':
        print('Obrigado por usar nosso sistema! ')
        break
    else:
        print('Opção inválida!')
