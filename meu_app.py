# print('meu primeiro programa em Python')
#
# a = 3
# b = 5
# soma = a + b
# print(soma)
#
# a = int(input('1 valor: '))
# b = int(input('2 valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#
#     print('todos são pares')
# else:
#     print('alguém não é par')

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# a = int(input('\nDigite um número: '))
#
# for num in range(a+1):
#     print('contador do 1º for', num)
#     divisivel = 0
#     for x in range(1, num+1):
#         print('contador do 2º for {} e fim do range {}'.format(x, num+1))
#         resto = num % x
#         if resto == 0 :
#             divisivel +=1
#     if divisivel == 2:
#         print('Foi divisível em 2x - {}'.format(num))

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#
# a = int(input('\nDigite um número: '))
#
# for num in range(a+1):
#     print('contador do 1º for', num)
#     divisivel = 0
#     for x in range(1, num+1):
#         print('contador do 2º for {} e fim do range {}'.format(x, num+1))
#         resto = num % x
#         if resto == 0 :
#             divisivel +=1
#     if divisivel == 2:
#         print('Foi divisível em 2x - {}'.format(num))

lista_numero = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
soma = 0
for x in lista_numero:
    print(x)
    soma += x
print('fim de for! \nprint de soma {}'.format(soma))


print('\nSoma da lista sem o uso do for! \nFunção sum() {}'.format(sum(lista_numero)))

print('\nMaior valor da lista numérica! \nFunção max() {}'.format(max(lista_numero)))

print('\nMaior valor da lista numérica! \nFunção max() {}'.format(max(lista_animal)))


if 'gato' in lista_animal:
    print('\nExiste um gato')
else:
    print('\nNão existe um gato na lista')

# criar uma nova lista

nova_lista_animal = lista_animal * 3
print('\nLista multiplicada por 3 {}'.format(nova_lista_animal))


# criar um novo elemento a lista
lista_animal.append('lobo')

if 'lobo' in lista_animal:
    print('\nInserido elemento {} a Lista Animal'.format(lista_animal))
else:
    print('\nNão foi inserido elemento')
