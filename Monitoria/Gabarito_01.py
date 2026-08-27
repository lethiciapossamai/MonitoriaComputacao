# 1. (Questão 8 - Lista): Lembra-se da fórmula para o cálculo da soma dos n primeiros 
# números naturais? Sn = n(n + 1)/2. 
# Tarefa: Criar um programa que receba via input() um inteiro positivo n, calcula a 
# soma de todos os inteiros positivos de 1 a n e dá um print() indicando o valor de n 
# e o resultado da soma[cite: 3].

n = int(input("Digite n: "))
soma_gauss = (n * (n + 1)) // 2
print("Para n =", n, "a soma é:", soma_gauss)


# 2. (Questão 9 - Lista): Criar um programa que recebe via input() um número inteiro de 
# 4 dígitos (do tipo string) e imprime a soma desses dígitos. Por exemplo, se o número 
# for 2023, seu programa deverá retornar 7 (resultado de 2+0+2+3)[cite: 3].
# (Nota: a resolução usa a abordagem matemática para desconstruir o número).

numero = int(input("Digite um número de 4 dígitos: "))
soma_digitos = 0

while numero > 0:
    soma_digitos += numero % 10
    numero //= 10

print("A soma dos dígitos é:", soma_digitos)


# 3. (Questão 13 - Lista): As regras para determinar se um ano é ou não um bissexto são:
# - Qualquer ano divisível por 400 é um ano bissexto.
# - Dos anos restantes, qualquer ano divisível por 100 não é um ano bissexto.
# - Dos anos restantes, qualquer ano divisível por 4 é um ano bissexto.
# - Todos os outros anos não são anos bissextos.
# Tarefa: Criar a função bissexto(ano) que retorne True ou False[cite: 3].

def bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False


# 4. (Questão 20 - Lista): Criar um script em Python que peça ao usuário para informar 
# um número e retorne uma mensagem na tela indicando se o número (i) é par; (ii) é 
# ímpar; ou (iii) é divisível por 6 (apenas uma dessas mensagens)[cite: 3].

num = int(input("Informe um número: "))
if num % 6 == 0:
    print("É divisível por 6")
elif num % 2 == 0:
    print("É par")
else:
    print("É ímpar")


# 5. (Questão 21 - Lista): Usando a função criada na última aula para calcular a soma 
# dos divisores de um número, criar uma função em Python chamada conferePrimo que 
# receba como parâmetro de entrada um número natural p e retorne True se for primo 
# e False caso contrário[cite: 3].

def conferePrimo(p):
    soma_divisores = 0
    for i in range(1, p + 1):
        if p % i == 0:
            soma_divisores += i
    
    return soma_divisores == p + 1


# 6. (Questão 22 - Lista): Criar uma função chamada quantosPrimos que receba 
# como parâmetros de entrada dois números naturais n1 e n2 e retorne a 
# quantidade de números primos que há entre eles (incluídos no intervalo)[cite: 3].

def quantosPrimos(n1, n2):
    contador = 0
    for num in range(n1, n2 + 1):
        if conferePrimo(num):
            contador += 1
    return contador


# 7. (Questão 23 - Lista): Dois números constituem um par de primos gêmeos se ambos 
# são primos e a diferença entre eles é de duas unidades.
# Tarefa: Criar uma função chamada gemeos(p) que retorne a quantidade de pares de primos 
# gêmeos que existem até p (inclusive)[cite: 3].

def gemeos(p):
    contador = 0
    for i in range(3, p - 1):
        if conferePrimo(i) and conferePrimo(i + 2):
            contador += 1
    return contador


# 8. (Ex. integral-while - Aula 2): Podemos aproximar numericamente a integral de uma 
# função f entre os limites a e b com a fórmula [soma de retângulos]. Implemente 
# essa aproximação[cite: 2].

def integral(f, a, b, dx=0.001):
    r = 0
    a = a + dx
    while a < b:
        r += f(a)
        a += dx
    return r * dx

cubica = lambda x: x**3
print("Aproximação da integral:", integral(cubica, 0, 1))
b = 0.0 == 0.0
print(b)