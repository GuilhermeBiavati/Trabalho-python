# Recebe nome e armazena na variavel
nome = input('Informe o nome: ')
# Transforma string para maiusculo, e substitui as vogais pelos caracteres requiridos
retorno = nome.upper().replace('A', '@').replace('E', '&').replace('I',
                                                                   '!').replace('O', '#').replace('U', '*')
#  Retorno dos resultados
print(nome)
print(retorno)
