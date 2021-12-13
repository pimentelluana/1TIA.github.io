print("Bem-vindo à Assistência técnica InfoTec")

print("Escolha a lista de opções abaixo (1 = SIM, 0 = NÃO)")

op1 = int(input("Problemas com CPU (Dependendo do problema o preço irá variar): "))

op2 = int(input("Problemas com GPU (Dependendo do problema o preço irá variar): "))

op3 = int(input("Limpeza completa: "))

op5 = int(input("Deseja realizar uma troca de componentes? Digite quantos componentes deseja trocar (Nenhuma = 0): "))

import random

ip1 = random.randint(120,150)

print(ip1)

ip2 = random.randint(200,300)

print(ip2)

p1 = op1 * ip1

p2 = op2 * ip2

p3 = op3 * 50

p5 = op5 * 100

Total = p2 + p1 + p3 + p5

if(op5<=0):
    print("Certo, nenhuma peça será trocada.")
elif(op5>=1):
    print(f"A(s) {op5} peça(s) serão trocada(s), o preço de {p5} reais será somado no final.")



for Intervalo in range(1,11,1):
    print(f"Aguarde um pouco... {Intervalo}")

print(f"O preço total aproximado será: {Total} reais.")