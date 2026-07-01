
TRABALHO DE CALCULO NUMÉRICO - 2026.01

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