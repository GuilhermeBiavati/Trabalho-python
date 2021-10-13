# loop que mantem o ciclo para validar se usuario deseja finalizar o app
while True:
    # Recebe nome e armazena na variavel
    nome = input('Informe o nome: ')
    while True:
        # try para validar se foi inserido um inteiro
        try:
            # Recebe a idade e armazena na variavel
            idade = int(input('Informe a idade: '))
            # condicionais para definir o nivel do aluno
            if (idade > 0) and (idade <= 5):
                tipo = 'Educação infantil'
            elif idade > 5 and idade <= 10:
                tipo = 'Educação Fundamental I'
            elif idade > 10 and idade <= 14:
                tipo = 'Educação Fundamental II'
            elif idade > 14:
                tipo = 'Ensino Médio'
            else:
                print('Informe um valor válido')
                continue
            break
        except:
            print('Informe um valor válido')

    # Faz o print do resultado final usando a forma moderna
    print("O aluno {} tem {} anos e está no {}".format(nome, idade, tipo))

    # pergunta ao usuario se deseja finalizar o programa
    while True:
        try:
            continuar = int(input("Deseja continuar? 0 - Não 1 - Sim "))
            break
        except:
            print('Informe um valor válido')
    #  condição que testa e termina o loop e fecha o ciclo
    if continuar == 0:
        break
