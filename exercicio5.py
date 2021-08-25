''' 5) Escreva um programa que receba três números quaisquer e apresente:
a) a soma dos quadrados dos três números;
b) o quadrado da soma dos três números.'''

import math

print("Digite o primeiro número: ")
num1 = float(input())
print("Digite o segundo número: ")
num2 = float(input())
print("Digite o terceiro número: ")
num3 = float(input())

somaA = math.pow(num1,2)+ math.pow(num2,2)+ math.pow(num3, 2)
print("A soma dos quadrados dos três números é: ", somaA)

somaB = math.pow(somaA,2)
print("O quadrado da soma dos três números é: ", somaB)
