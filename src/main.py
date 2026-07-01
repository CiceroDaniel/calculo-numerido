'''
TRABALHO DE CALCULO NUMÉRICO - 2026.1
ALUNO: CÍCERO DANIEL BARBOSA DOS SANTOS
PROFESSOR:
'''

'''
OBJETIVO: Implemetntar o metodo da falsa posicao para encontrar a raiz de uma função.
'''
# BIBLIOTECAS
import math
import matplotlib.pyplot as plt
import numpy as np

# TÍTULO
print("TRABALHO DE CALCULO NUMÉRICO - 2026.1")

# VARIÁVEIS DE TOLERÂNCIA DE ERRO E O MÁXIMO DE ITERAÇÕES PARA NAO ESTOURAR A MEMÓRIA

tolerancia = 0.000001
max_iteracoes = 100

# FUNÇÃO QUE SERÁ USADA

def f(x):
    return x**3-x-2

# FUNÇÃO PARA CRIAR E IMPRIMIR O O GRÁFICO

def Plotar_funcao(a, b, raiz):

    # GERA VERIOS PONTOS PARA CRIAR A CURVA

    x = np.linspace(a-1,b+1,400)

    # CALCULO f(x) DE TODOS OS PONTOS ANTERIORES

    y = f(x)

    # CRIA A FIGURA

    plt.figure(figsize=(8,5))

    # DESENHA A FUNÇÃO

    plt.plot(x,y,label="f(x) = x³ - x - 2")

    # IMPRIME O EIXO X

    plt.axhline(0)

    # MARCA A RAIZ ENCONTRADA

    plt.scatter(raiz,f(raiz),s=80,label="raiz")

    # LINHA VERTICAL PASSANDO PELA RAIZ

    plt.axvline(raiz, linestyle="--")

    # TÍTULO

    plt.title("MÉTODO DA FALSA POSIÇÃO")

    # NOME DOS EIXOS

    plt.xlabel("x")
    plt.ylabel("f(x)")

    # GRADE PARA VIZUALIZAÇÃO

    plt.grid(True)

    # LEGENDA

    plt.legend()

    # IMPRIME O GRÁFICO

    plt.show()


# LAÇO DE REPETIÇÃO PARA PARA RECEBER O INTERVALO [a,b] SÓ PARA QUANDO A CONDIÇÃO f(a)*f(b) < 0 FOR VERDADEIRA

while True: 

    # RESCEBE O LIMITE INFERIOR E O SUPERIOR DO INTERVÁLO [a,b]

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    # VERIFICA SE A CONDIÇÃO f(a)*f(b) < 0 É FALSA, SE HÁ MUDANÇA DE SINAL
    
    if f(a) * f(b) > 0: # SE NÃO HOUVER MUNDANÇA DE SINAL O INTERVALO NÃO POSSUE UMA RAIZ
        print("Erro!")
        print("O intervalo escolhido não possue uma raiz")
        print("Escolha outro intervalo")
    else:
        break

# MÉTODO

print("\n")
print("="*20)
print("METODO DA FALSA POSIÇÃO")
print("="*20)

# ALGORITIMO DO MÉTODO DA FALSA POSIÇÃO

for i in range(1, max_iteracoes+1):

    # CALCULO O VALOR DE X APLICANDO A FORMULA DO MÉTODO 
    xr = (a*f(b)-b*f(a))/(f(b)-f(a))
    # CALCULA O VALOR DE f(x) COM O X OBTIDO ACIMA
    fxr = f(xr)

    # IMPRIME OS VALORES DA ITERAÇÃO

    print("\n")
    print("="*20)
    print(f"ITERAÇÃO {i}")
    print("="*20)
    print(f"Valor de a: {a:.6f}")
    print(f"Valor de b: {b:.6f}")
    print(f"Valor de xr: {xr:.6f}")
    print(f"Valor de f(xr): {fxr:.6f}")
    print("="*20)

    # VERIFICA SE O MÓDULO DE f(x) É MENOR QUE A TOLERÂNCIA

    if abs(fxr)<tolerancia: # SE O MÓDULO DE f(x) FOR MENOR QUE A TOLERÂNCIA ENTÃO A RAIZ FOI ENCONTRADA
        print(f"\nRaiz encontrada!")
        print(f"x = {xr:.6f}")

        Plotar_funcao(a,b,xr)

        break

    # VERIFICA SE É NESCESSÁRIO SUBSTITUIR OS VALORES DE A OU B

    if f(a) * fxr < 0: # SE f(a)*f(x) < 0, TROCA O VALOR DE B:  b = x
        b = xr
    else: # SE f(a)*f(x) > 0, TROCA O VALOR DE A:  a = x
        a = xr

else: # CASO O NÚMERO MÁXIMO DE ITERÇÕES FOR ANTINGIDO, PRINTA O ULTIMO VALOR DE X OBTIDO
    print("\n|Número máximo de iterações atingido.")
    print(f"|Aproximação encontrada: {xr:.6f}\n")