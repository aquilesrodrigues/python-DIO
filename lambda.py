
contador_letras = lambda lista: [len(x) for x in lista]

# criar um DICIONÁRIO
calculadora = {
    'somar': lambda a, b: a + b,
    'subtrair': lambda a, b: a - b,
    'multiplicar': lambda a, b: a * b,
    'dividir': lambda a, b: a / b,
}


if __name__ == '__main__':

    lista_animais = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista_animais))

    soma = calculadora['somar']
    subtracao = calculadora['subtrair']
    print('A soma é: {}'.format(soma(10, 5)))
