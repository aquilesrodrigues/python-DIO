class Televisor:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1

    def dininuir_canal(self):
        if self.ligada:
            self.canal -=1


televisao = Televisor()

print('Status do self.ligada {}'.format(televisao.ligada))
print('chamando o método televisao.power')
televisao.power()
print('Status do self.ligada {}'.format(televisao.ligada))
print('chamando o método televisao.power')
televisao.power()
print('Status do self.ligada {}'.format(televisao.ligada))
print('canal: {}'.format(televisao.canal))
televisao.power()
print('Status do self.ligada {}'.format(televisao.ligada))
televisao.aumentar_canal()
televisao.aumentar_canal()
print('canal: {}'.format(televisao.canal))
televisao.dininuir_canal()
print('canal: {}'.format(televisao.canal))
