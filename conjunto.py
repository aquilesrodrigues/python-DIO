conjunto = {1, 2, 3, 4, 6}
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjunto3 = {6, 8, 9}
conjunto4 = {1, 3}
conjunto6 = {5, 6}

conjunto.add(5)
conjunto.discard(6)
# União dos elementos dos 2 conjuntos
conjunto_uniao = conjunto1.union(conjunto2)
# Elementos comuns aos 2 conjuntos
conjunto_interseccao = conjunto1.intersection(conjunto2)
# Elementos diferentes a partir do 1º conjunto
conjunto_diferenca_conj1 = conjunto1.difference(conjunto2)
# Elementos diferentes a partir do 2º conjunto
conjunto_diferenca_conj2 = conjunto2.difference(conjunto1)
# Diferença simétrica - traz elementos distintos de cada conjunto
conjunto_dif_simetrica = conjunto1.symmetric_difference(conjunto2)
# PERTINÊNCIA
# --> Subsequente - todos os elementos de um conjunto menor pertencer ao maior
conjunto_subset = conjunto4.issubset(conjunto1)
print(conjunto_subset)
# --> Subsequente - Todos os elementos do 2º conjunto estão contindos no 1 conjunto
conjunto_superset = conjunto2.issuperset(conjunto6)
print(conjunto_superset)
