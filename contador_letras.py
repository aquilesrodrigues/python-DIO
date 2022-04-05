def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        # A função len() fornece o tamanha de
        # cada palavra encontrada pelo ponteiro x
        quantidade = len(x)
        contador.append(quantidade)
    return contador


if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
