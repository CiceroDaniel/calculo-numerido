# TRABALHO DE CALCULO NUMÉRICO - 2026.1

ALUNO: CÍCERO DANIEL BARBOSA DOS SANTOS

OBJETIVO: Implemetntar o metodo da falsa posicao para encontrar a raiz de uma função.

 --- 
## Método da Falsa posição
### Ideia simples

Temos dois pontos: $(a, f(a))$ e $(b, f(b))$.
Queremos descobrir onde a reta que passa por esses dois pontos e intercepta o eixo $x$. Nesse ponto, temos $y = 0$

A ideia é simples:

1. Escolha um intervalo $[a,b]$ em que a função muda de sinal:
    - $f(a)⋅f(b)<0$.
2. Trace a reta que liga os pontos $(a,f(a))$ e $(b,f(b))$.
3. O ponto onde essa reta cruza o eixo $x$ é a aproximação da raiz.

A fórmula é:

$$
x = \frac{a f(b) - b f(a)}{f(b) - f(a)}.
$$


Depois:

- Se $f(a)⋅f(x)<0$, substitua $b=x$.
- Caso contrário, substitua $a=x$.
- Repita até atingir a precisão desejada.

---
## Pseudocódigo


```
Função Falsa_Posicao(f, a, b, tolerancia, max_iteracoes)
    xr_ant ← NULO
    Para i de 0 até max_iteracoes faça
        xr ← (a·f(b) - b·f(a)) / (f(b) - f(a))
        Se xr_ant ≠ NULO então
            Se |xr - xr_ant| < tolerancia então
                Retorne xr
            Fim-Se
        Fim-Se
        xr_ant ← xr
        fxr ← f(xr)
        Se f(a) · fxr < 0 então
            b ← xr
        Senão
            a ← xr
        Fim-Se
    Fim-Para
    Escreva "Número máximo de iterações atingido."
    Retorne xr
Fim-Função
```
---

## Método de Gauss-Jacobi

O método de Gauss-Jacobi é um método iterativo utilizado para resolver sistemas de equações lineares. A ideia consiste em isolar cada variável do sistema e, a partir de uma aproximação inicial, calcular sucessivas aproximações para a solução.

Considere o **Sistema A**:

$$
\begin{aligned}
x_1 &= \frac{6+x_2-2x_3}{10}\\
x_2 &= \frac{25+x_1+x_3-3x_4}{11}\\
x_3 &= \frac{-11-2x_1+x_2+x_4}{10}\\
x_4 &= \frac{15-3x_2+x_3}{8}
\end{aligned}
$$

Isolando cada variável, obtemos:
$$x_1=\frac{6+x_2-2x_3}{10}$$
$$x_2=\frac{25+x_1+x_3-3x_4}{11}$$
$$x_3=\frac{-11-2x_1+x_2+x_4}{10} $$
$$x_4=\frac{15-3x_2+x_3}{8} $$
Como aproximação inicial, utiliza-se

$$x^{(0)}=[0,0,0,0]^T.$$

Na primeira iteração, substituindo esses valores nas equações:

$$x_1^{(1)}=\frac{6+0-2(0)}{10}=0,6  $$

$$x_2^{(1)}=\frac{25+0+0-3(0)}{11}=2,2727$$  

$$x_3^{(1)}=\frac{-11-2(0)+0+0}{10}=-1,1$$

$$x_4^{(1)}=\frac{15-3(0)+0}{8}=1,875  $$

Obtém-se a primeira aproximação:

$$x^{(1)}=[0.6,2.2727,-1.1,1.875]^T.$$

Na iteração seguinte, todos esses valores são utilizados para calcular uma nova aproximação. Esse processo é repetido até que o erro entre duas iterações consecutivas seja menor que a tolerância estabelecida ou seja atingido o número máximo de iterações.

> No método de Gauss-Jacobi, todas as variáveis de uma iteração são calculadas utilizando exclusivamente os valores da iteração anterior. Os novos valores só são utilizados na próxima iteração.

