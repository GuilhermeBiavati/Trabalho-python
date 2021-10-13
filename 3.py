passou = True


def pergunta(text, quartos):
    while True:
        try:
            res = int(input('Em qual posição quer alocar o {}? '.format(text)))

            if not (res in quartos):
                print('Você deve escolher entre {}'.format(quartos))
                continue
            return res
        except:
            print('Você deve escolher entre {}'.format(quartos))
            continue


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
quartos = [3, 6]
rato = pergunta('Rato',  quartos)
quartos.remove(rato)
gato = pergunta('Gato', quartos)

if rato == 3 or gato == 6:
    passou = False
    print('Você perdeu!')


print('Bem vindos a fase 2!')
print('Na fase 2, o jogador deve alocar um CÃO, CÃO e OSSO na seguinte matriz que representa os quartos: ')
print('+---------+')
print('| - * * * |')
print('| * C - - |')
print('+---------+')
quartos = [1, 7, 8]
cao = pergunta('CÃO',  quartos)
quartos.remove(cao)
cao2 = pergunta('CÃO',  quartos)
quartos.remove(cao2)
osso = pergunta('OSSO',  quartos)

if osso == 7:
    passou = False
    print('Você perdeu!')

print('Bem vindos a fase 3!')
print('Na fase 3, o jogador deve alocar um GATO, RATO e OSSO na seguinte matriz que representa os quartos: ')
print('+---------+')
print('| - * * * |')
print('| - G - * |')
print('+---------+')
quartos = [1, 5, 7]
gato = pergunta('GATO',  quartos)
quartos.remove(gato)
rato = pergunta('RATO',  quartos)
quartos.remove(rato)
osso = pergunta('OSSO',  quartos)
if rato == 7 or rato == 5:
    passou = False
    print('Você perdeu!')
print('Bem vindos a fase 4!')
print('Na fase 4, o jogador deve alocar um QUEIJO, QUEIJO e OSSO na seguinte matriz que representa os quartos: ')
print('+---------+')
print('| - - - * |')
print('| * R * * |')
print('+---------+')
quartos = [1, 2, 3]
queijo = pergunta('QUEIJO',  quartos)
quartos.remove(queijo)
queijo2 = pergunta('QUEIJO',  quartos)
quartos.remove(queijo2)
osso = pergunta('OSSO',  quartos)

if queijo == 2 or queijo2 == 2:
    passou = False
    print('Você perdeu!')

if(passou):
    print('Você ganhou!')
    print('Parabéns!!! você conseguiu alocar todo mundo!')
