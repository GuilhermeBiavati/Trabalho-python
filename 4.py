# importa as bibliotecas
from random import seed
from random import randint
# inicia a lista
lista = []
# Loop que faz repetir o ciclo de perguntas
while True:
    # mostra as opções para os usarios
    print('------------------------------ Menu de opções ------------------------------')
    print('1 - Nova inscrição')
    print('2 - Visualizar inscrições')
    print('0 - Encerrar')
    # Armazena a opção desejada
    try:
        opcao = int(input('Escolha uma opção: '))

        # caso seja 0 ele encerra o loop e consequentemente o app
        if opcao == 0:
            break
        # caso seja ele ele pergunta as informações
        elif opcao == 1:
            # cria um numero aleatorio
            # seed(999)
            voucher = randint(0, 999)
            nome = input('Insira seu nome: ')
            email = input('Insira seu email: ')
            telefone = input('Insira seu telefone: ')
            curso = input('Insira seu curso: ')

            # adiciona o dicionario com as informações na lista
            lista.append({'voucher': voucher, 'nome': nome,
                          'email': email, 'telefone': telefone, 'curso': curso})
        # caso seja 2 ele faz um loop em cada item da lista imprimindo os dados cadastrados
        elif opcao == 2:
            print(
                '------------------------------ Lista de inscritos ------------------------------')
            for item in lista:
                print('Voucher: {}'.format(item['voucher']))
                print('Nome: {}'.format(item['nome']))
                print('Email: {}'.format(item['email']))
                print('Telefone: {}'.format(item['telefone']))
                print('Curso: {}'.format(item['curso']))
                print(
                    '-------------------------------------------------------------------')
        # caso a opção não existe ele imprime o erro e começa o loop novamente
        else:
            print('Erro, Insira um valor válido')
    except:
        # caso ocorra algum erro ele imprime o erro e começa o loop novamente
        print('Erro, Insira um valor válido')
