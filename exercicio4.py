''' 4) Calcule e apresente o volume de uma lata de óleo. v = pi.r².altura'''
import math

print ("Digite o raio da sua lata de óleo: ")
raio = float(input())
print("Digite a altura da sua lata de óleo: ")
altura = float(input())
volume = math.pi * math.pow(raio,2) * altura
print("O volume da sua lata de óleo é de %.2f: " %volume)
