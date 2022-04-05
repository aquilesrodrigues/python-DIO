# classe

class Calculadora:

    def somar(self, valor1, valor2):
        return valor1 + valor2

    def subtrair(self, valor1, valor2):
        return valor1 - valor2

    def multiplicar(self, valor1, valor2):
        return valor1 * valor2

    def divisao(self, valor1, valor2):
        return valor1 / valor2


calculadora = Calculadora()

print(calculadora.somar(2, 4))
print(calculadora.subtrair(5, 4))
print(calculadora.multiplicar(3, 4))
print(calculadora.divisao(100, 4))
