'''Faça um programa que receba o custo de um espetáculo teatral e o preço do convite
desse espetáculo. Esse programa deve calcular e mostrar:
a) A quantidade de convites que devem ser vendidos para que pelo menos o custo
do espetáculo seja alcançado.
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de
23%.'''

import math

print("Digite o custo do espetáculo teatral: ")
custoTeatro = float(input())
print("Digite o preço do convite do espetáculo: ")
preco = float(input())

qtd = custoTeatro/preco
print("A quantidade de convites deve ser de: ", math.ceil(qtd), "convites.")
qtdLucro = 23/100*qtd+qtd
print("E devem ser vendidos", math.ceil(qtdLucro), "convites, para se obter o lucro de 23%") 
