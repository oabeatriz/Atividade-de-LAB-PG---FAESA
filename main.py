# Faça um programa que peça ao usuário seu nome e idade, e imprima uma mensagem de boas-vindas com essas informações.
nome = input("Digite seu nome: ")
print(f"Bem vindo(a), {nome}!")




# Faça um programa que peça ao usuário um número e imprima o dobro desse número.

numero = float(input("Digite um número: "))
dobro = numero * 2
print(f"O dobro de {numero} é: {dobro} ")


# Faça um programa que peça ao usuário uma palavra e imprima essa palavra em maiúsculas

palavra = (input("Digite uma palavra: "))
maiuscula = palavra.upper()
print(f"A palavra em maiúsculo é: {maiuscula}")

# Faça um programa que peça ao usuário o raio de um círculo e calcule a área desse círculo.
# import math --- outra forma
# raio = floar(int("Informe o raio da circunferencia: "))
# area = math.pi * raio * raio
# print(f"A area da circunferencia de raio {raio} é {area}")
raio = float(input("Digite o raio de um círculo: "))
area = 3.14 * raio * raio
print(f"A área deste círculo é: {area}")


#Faça um programa que peça ao usuário um número e calcule a raiz quadrada desse número.
# import math
# numero = float(input("Digite um numero"))
# raiz = math.sqrt(numero)

num = float(input("Digite um número: "))
raiz = float(num) ** 0.5
print(f"A raiz quadrade deste número é: {raiz}")

# faça um programa que peça ao usuario o nome completo e imprima apenas o primeiro nome
nomeCompleto = input("Digite seu nome completo: ")
nomeCompleto = nomeCompleto.split()
print(f"Primeiro nome: {nomeCompleto[0]}")

# faça um programa que peça ao usuário o valor de tres notas e calcule a media ponderada dessas notas considerando os pesos 2, 3 e 5 para as tres notas.a

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

mediaPonderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5))/10
print(f"A média ponderada é igual a {mediaPonderada}")


# faça um programa que peça o usuario o valor de um produto e o percentual de desconto, e calcule o valor final com desconto

valorProduto = float(input("Informe o valor do produto: "))
valorPercentual = float(input("Informe o percentual de desconto: "))

desconto = valorProduto - (valorProduto * (valorPercentual/100))

print(f"O valor final é: {desconto}")

# faça um programa que declare uma variavel do tipo booleano e imprima o valor dessa variavel

var = True # or False
print(var)

# faça um programa q peça ao usuario o raio de uma esfera e calcule o volume da esfera ( V = 4/3 PI R3)

import math
raio = float(input("Digite o raio: "))
volume = (4/3) * math.pi * raio * raio * raio # ou raio ** 3
print(f"O volume da esfera de {raio} é: {volume}")

#peça o usuario um numero e calcule o cubo deste numero

num = float(input("Informe um número: "))
print(f"O cubo de {num} é {num * num * num}") # metodo no print pra n declarar variavel


# faça um prog que peça ao user dois numeros e imprima o quociente e o resto da divisao desses numeros

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
quociente = numero1 / numero2
resto = numero1 % numero2
print(f"O quociente da divisão é: {quociente}")
print(f"O resto da divisão é igual a: {resto}")

# Faça um programa que peça ao usuário o valor de três produtos e seus respectivos preços, e calcule o valor total da compra com desconto de 10% no valor total
prod1 = float(input("Digite o valor do primeiro produto: "))
prod2 =  float(input("Digite o valor do segundo produto: "))
prod3 = float(input("Digite o valor do teceiro produto: "))

total = prod1 + prod2 + prod3
desc = total - (total * 0.1)

print(f"Total: {total}")
print(f"Desconto 1: {desc}")

# Faça um programa que peça ao usuário a base e a altura de um triângulo e calcule a área desse triângulo
base = float(input("Digite o número da base: "))
altura = float(input("Digite a altura: "))

area = (base * altura) / 2
print(f"A area do triângulo é igual a: {area}")

# Faça um programa que peça ao usuário o valor de um produto e o valor pago pelo cliente, e calcule o troco a ser devolvido ao cliente.

valor = float(input("Produto: "))
pago = float(input("Valor pago:"))
troco = valor - pago
print(f"O troco é de: {troco}")

# Faça um programa que peça ao usuário dois valores booleanos e imprima o resultado da operação "xor" entre esses valores
val1 = bool(input("Insira true or false: "))
val2 = bool(input("Insira true or false: "))
xor = val1 ^ val2
print(xor)

# faça um programa que peça a idade do usuário e utilize condicionais if or else para descobrir se está habilitado ou não em ter cnh.
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você está habilitado a ter CNH!")
else:
    print("Você não está habilitado a ter CNH!")