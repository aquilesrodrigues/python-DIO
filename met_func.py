
# classe

class Calculadora:

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b



calculadora = Calculadora(10, 2)

print(calculadora.a)
print(calculadora.b)
print(calculadora.somar())