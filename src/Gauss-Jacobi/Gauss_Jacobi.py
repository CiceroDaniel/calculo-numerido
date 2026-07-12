# OBJETIVO: Implementar em python o metodo de Gauss-Jacobi

# BIBLIOTECAS

import numpy as np

# Sistema A (4x4)

A = [
    [10,-1,2,0],
    [-1,11,-1,3],
    [2,-1,10,-1],
    [0,3,-1,8]
]

b1 = [6,25,-11,15]

# Sistema B (3x3)

B = [
    [2,8,-1],
    [5,-1,1],
    [-1,1,4]
]

b2 = [11,10,3]


# VARIÁVEIS 

tolerancia = 1e-4
max_iteracoes = 50


# SISTEMAS QUE SERÃO USADOS 

def gauss_jacobi(S,b,Tol,max_interracoes):
    n = len(S)

    # Aproximações iniciais

    x = [0]*n
    x_novo = [0]*n
    

