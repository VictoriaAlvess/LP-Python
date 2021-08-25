'''3) Escreva um programa que lê dois valores em ponto flutuante e exibe o resultado do
primeiro dividido pelo segundo, com exatamente seis dígitos depois da vírgula.
'''


print ("Digite o primeiro número: ")
num1 = float(input())
print("Digite o segundo número: ")
num2 = float(input())
result = num1/num2
print("O resultado da divisão é: %.6f" %result)
