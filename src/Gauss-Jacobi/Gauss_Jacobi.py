# OBJETIVO: Implementar em python o metodo de Gauss-Jacobi


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


# FUNÇÃO DE GAUSS-JACOBI
def gauss_jacobi(S,b,Tol,max_iteracoes):
    n = len(S)

    # Aproximações iniciais

    x = [0]*n
    x_novo = [0]*n
    for k in range(max_iteracoes):

        # calcula o novo vetor

        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma += S[i][j]*x[j]
            x_novo[i]=(b[i]-soma)/S[i][i]
    
        # Calcula o erro
        erro = max(abs(x_novo[i]-x[i]) for i in range(n))

        if n == 4:
            print(
            f"Iteração {k+1:2d}: "
            f"x1 = {x_novo[0]:.6f} | "
            f"x2 = {x_novo[1]:.6f} | "
            f"x3 = {x_novo[2]:.6f} | "
            f"x4 = {x_novo[3]:.6f}"
            )
        elif n == 3:
            print(
            f"Iteração {k+1:2d}: "
            f"x1 = {x_novo[0]:.6f} | "
            f"x2 = {x_novo[1]:.6f} | "
            f"x3 = {x_novo[2]:.6f} | "
            )

        # Condição de parada
        if erro < Tol:
            print(f"\nConvergiu em {k+1} iterações")
            return x_novo, k+1, True
        
        x = x_novo.copy()


    print("\nO método não convergiu.")
    print(f"Máximo de {max_iteracoes} iterações atingido.")

    return x_novo, max_iteracoes, False

resolucao,iteracoes,convergiu = gauss_jacobi(B_reorganizado,b3,tolerancia,max_iteracoes)

if convergiu:
    print("Solução:", resolucao)
else:
    print("Última aproximação:", resolucao)