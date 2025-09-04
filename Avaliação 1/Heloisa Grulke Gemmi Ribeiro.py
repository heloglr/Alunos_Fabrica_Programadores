# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# ENTREGA ATÉ 04/09/2025

# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR
# Heloisa Grulke Gemmi Ribeiro
print("ola mundo seja bem vindo ")
nome = str(input("digite seu nome: "))
peso = float(input("digite seu peso: "))
altura = float (input("digite sua altura: "))
imc = peso / (altura**2)

print("seu imc equevale a:", imc)


if imc <= 18.5:
    print("Abaixo do peso.")
elif imc <= 24.9: 
    print("Peso normal.")
elif imc <= 29.9:
    print("Sobrepeso.") 
elif imc <= 34.9:
    print("Obesidade Grau 1")
elif imc <= 39.9:
    print("Obesidade Grau 2")
else:
    print("obesidade de grau 3")