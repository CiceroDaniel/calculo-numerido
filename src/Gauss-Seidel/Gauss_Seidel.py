# OBJETIVO: Implementar em python o metodo de Gauss-Seidel


# SISTEMAS QUE SERÃO USADOS 
# Sistema A (4x4)

A = [
    [10,-1,2,0],
    [-1,11,-1,3],
    [2,-1,10,-1],
    [0,3,-1,8]
]

b1 = [6,25,-11,15]

# Sistema B (3x3)
# Original
B = [
    [2,8,-1],
    [5,-1,1],
    [-1,1,4]
]

b2 = [11,10,3]

# Reorganizado
B_reorganizado = [
    [5, -1, 1],
    [2, 8, -1],
    [-1, 1, 4]
]

b3 = [10, 11, 3]

# VARIÁVEIS 

tolerancia = 1e-4
max_iteracoes = 50