# Função que recebe o objeto da pergunta e quais os quartos que podem ser alocados
def pergunta(text, quartos):
    while True:
        #  try para fazer a verificação se está sendo inserido os quartos corretos e numeros inteiros
        try:
            # Pergunta o quarto desejado e armazena na variavel
            res = int(input('Em qual posição quer alocar o {}? '.format(text)))
            # verifica se o quarto esta disponivel caso esteja incoreto ele pergunta novamente
            if not (res in quartos):
                print('Você deve escolher entre {}'.format(quartos))
                continue
            return res
        except:
            print('Você deve escolher entre {}'.format(quartos))
            continue


while True:
    # Indica como o jogo funciona
    print('Especificando a posição:')
    print('+---------+')
    print('| 1 2 3 4 |')
    print('| 5 6 7 8 |')
    print('+---------+')

    print('Bem vindos a fase 1!')
    print('Na fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos: ')
    print('+---------+')
    print('| * * - G |')
    print('| R - * * |')
    print('+---------+')
    # variavel q contem os quartos disponiveis
    quartos = [3, 6]
    # pergunta onde o objeto deve ser alocado
    rato = pergunta('Rato',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(rato)
    # pergunta onde o objeto deve ser alocado
    gato = pergunta('Gato', quartos)
    # verifica se os objetos foram alocados corretamente e termina o programa
    if rato == 3 or gato == 6:
        passou = False
        print('Você perdeu!')
        break

    print('Bem vindos a fase 2!')
    print('Na fase 2, o jogador deve alocar um CÃO, CÃO e OSSO na seguinte matriz que representa os quartos: ')
    print('+---------+')
    print('| - * * * |')
    print('| * C - - |')
    print('+---------+')
    # variavel q contem os quartos disponiveis
    quartos = [1, 7, 8]
    # pergunta onde o objeto deve ser alocado
    cao = pergunta('CÃO',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(cao)
    # pergunta onde o objeto deve ser alocado
    cao2 = pergunta('CÃO',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(cao2)
    # pergunta onde o objeto deve ser alocado
    osso = pergunta('OSSO',  quartos)

    # verifica se os objetos foram alocados corretamente e termina o programa
    if osso == 7:
        passou = False
        print('Você perdeu!')
        break

    print('Bem vindos a fase 3!')
    print('Na fase 3, o jogador deve alocar um GATO, RATO e OSSO na seguinte matriz que representa os quartos: ')
    print('+---------+')
    print('| - * * * |')
    print('| - G - * |')
    print('+---------+')
    # variavel q contem os quartos disponiveis
    quartos = [1, 5, 7]
    # pergunta onde o objeto deve ser alocado

    gato = pergunta('GATO',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(gato)
    # pergunta onde o objeto deve ser alocado

    rato = pergunta('RATO',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(rato)
    # pergunta onde o objeto deve ser alocado

    osso = pergunta('OSSO',  quartos)

    # verifica se os objetos foram alocados corretamente e termina o programa
    if rato == 7 or rato == 5:
        passou = False
        print('Você perdeu!')
        break

    print('Bem vindos a fase 4!')
    print('Na fase 4, o jogador deve alocar um QUEIJO, QUEIJO e OSSO na seguinte matriz que representa os quartos: ')
    print('+---------+')
    print('| - - - * |')
    print('| * R * * |')
    print('+---------+')
    # variavel q contem os quartos disponiveis
    quartos = [1, 2, 3]
    # pergunta onde o objeto deve ser alocado

    queijo = pergunta('QUEIJO',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(queijo)
    # pergunta onde o objeto deve ser alocado
    queijo2 = pergunta('QUEIJO',  quartos)
    # remove o item selecionado dos quartos disponiveis
    quartos.remove(queijo2)
    # pergunta onde o objeto deve ser alocado
    osso = pergunta('OSSO',  quartos)

    # verifica se os objetos foram alocados corretamente e termina o programa
    if queijo == 2 or queijo2 == 2:
        passou = False
        print('Você perdeu!')
        break

    # Indica que conseguiu alocar todos os niveis e termina o programa
    print('Você ganhou!')
    print('Parabéns!!! você conseguiu alocar todo mundo!')
    break
