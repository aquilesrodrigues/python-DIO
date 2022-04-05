
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 2
    numero = lista[1]
    x = a

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')

# ex é o álias que receberá mensagem do método BaseException
except BaseException as ex:
    print('Erro desconhecido! Erro: {}'.format(ex))

else:
    print('Executa quando não houver nenhuma excessão')
    print('utilizamos esta opção para os códigos que só podem ser executado quando não houver excessões')

    arquivo.close()