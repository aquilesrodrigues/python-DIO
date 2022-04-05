class Error(Exception):
    pass

class EntradaError(Error):
    # Classe que erdada de Erro

    def __init__(self, message):
        self.message = message

while True:

    try:
        x = int(input('Entre com a nota de 0 à 10: '))
        print(x)
        if x > 10:
            # raise força uma excessão
            raise EntradaError('Nota não pode ser maior que 10')
        elif x <0:
            # raise força uma excessão
            raise EntradaError('Nota não pode ser menor que 0')

        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números válidos')

    except EntradaError as ex:
        print(ex)
