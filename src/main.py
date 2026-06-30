'''
TRABALHO DE CALCULO NUMÉRICO - 2026.1
ALUNO: CÍCERO DANIEL BARBOSA DOS SANTOS
PROFESSOR:
'''

'''
OBJETIVO: Implemetntar o metodo da falsa posicao para encontrar a raiz de uma função.
'''
import math


print("TRABALHO DE CALCULO NUMÉRICO - 2026.1")

tolerancia = 0.000001
max_iteracoes = 100


def f(x):
    return math.sin(x)



while True: 

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    if f(a) * f(b) > 0:
        print("Erro!")
        print("O intervalo escolhido não possue uma raiz")
        print("Escolha outro intervalo")
    else: break

print("\n")
print("="*20)
print("METODO DA FALSA POSIÇÃO")
print("="*20)

op = int(input())


for i in range(1, max_iteracoes+1):
    xr = (a*f(b)-b*f(a))/(f(b)-f(a))

    fxr = f(xr)

    print("\n")
    print("="*20)
    print(f"\nInterações:{i}")
    print(f"Valor de a: {a:.6f}")
    print(f"Valor de b: {b:.6f}")
    print(f"Valor de xr: {xr:.6f}")
    print(f"Valor de f(xr): {fxr:.6f}")
    print("="*20)

    if abs(fxr)<tolerancia:
        print(f"\nRaiz encontrada!")
        print(f"x = {xr:.6f}")
        break

    if f(a) * fxr < 0:
        b = xr
    else:
        a = xr

else: 
    print("\nNúmero máximo de iterações atingido.")
    print(f"Aproximação encontrada: {xr:.6f}")