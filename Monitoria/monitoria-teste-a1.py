# 1. (Questão 21 - Lista): No ensino médio você deve ter aprendido que se um certo
# número P é primo, a soma dos seus divisores é igual a P + 1, pois seus únicos
# divisores são 1 e ele próprio.
# Tarefa: Usando a função para calcular a soma dos divisores de um número, criar uma
# função em Python chamada conferePrimo que receba como parâmetro de entrada um
# número natural p e retorne como parâmetro de saída True se o número for primo e
# False caso contrário.

def conferePrimo(p):
    if p < 2:
        return False
    soma = 0
    for divisor in range(1, p + 1):
        if p % divisor == 0:
            soma += divisor
    if soma == p + 1:
        return True
    else:
        return False


# 2. (Questão 22 - Lista): Criar uma função em Python chamada quantosPrimos que
# receba como parâmetros de entrada dois números naturais n1 e n2 e retorne como
# parâmetro de saída a quantidade de números primos que há entre eles (considere-os
# incluídos no intervalo).

def quantosPrimos(n1, n2):
    quantidade_de_primos = 0
    for numero_testado in range(n1, n2 + 1):
        if conferePrimo(numero_testado):
            quantidade_de_primos += 1
    return quantidade_de_primos


# 3. (Questão 40 - Lista): Criar uma função em Python chamada primoAntes que receba
# como parâmetro de entrada um número natural n e retorne como parâmetro de saída o
# último número primo menor ou igual a n. Por exemplo, se a entrada for 100, a saída
# deverá ser 97. Se a entrada for 23, a saída deverá ser 23.

def primoAntes(n):
    candidato = n
    while candidato >= 2:
        if conferePrimo(candidato):
            return candidato
        candidato -= 1
    return None


# 4. (Questão 39 - Lista): Criar uma função em Python chamada primoDepois que
# receba como parâmetro de entrada um número natural n e retorne como parâmetro
# de saída o primeiro número primo superior a n. Por exemplo, se a entrada for
# 90, a saída deve ser 97.

def primoDepois(n):
    candidato = n + 1
    while not conferePrimo(candidato):
        candidato += 1
    return candidato


# 5. (Questão 19 - Lista): Criar um script em Python que peça ao usuário para
# informar um número e retorne uma mensagem na tela indicando se o número contém
# ou não contém o algarismo 2.

numero = input('Informe um número: ')
contem_dois = False

for algarismo in numero:
    if algarismo == '2':
        contem_dois = True

if contem_dois:
    print(f'O número {numero} contém o algarismo 2')
else:
    print(f'O número {numero} não contém o algarismo 2')


# 6. (Questão 16 - Lista): Uma boa senha possui pelo menos 8 caracteres, contém
# pelo menos uma letra maiúscula, pelo menos uma letra minúscula e pelo menos um
# número.
# Tarefa: Criar uma função em Python chamada boaSenha que receba como parâmetro de
# entrada uma string e retorne como parâmetro de saída True se é uma boa senha e
# False caso contrário.

def boaSenha(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tamanho_suficiente = len(senha) >= 8
    for caractere in senha:
        if str.isupper(caractere):
            tem_maiuscula = True
        if str.islower(caractere):
            tem_minuscula = True
        if str.isdigit(caractere):
            tem_numero = True
    if tamanho_suficiente and tem_maiuscula and tem_minuscula and tem_numero:
        return True
    else:
        return False


# 7. (Questão 17 - Lista): Uma data mágica é uma data em que o dia multiplicado pelo
# mês é igual ao ano de dois dígitos. Por exemplo, 10 de junho de 1960 é uma data
# mágica porque 6 vezes 10 é 60, que é igual ao ano de dois dígitos.
# Tarefa: Criar uma função em Python chamada dataMagica que receba como parâmetro de
# entrada uma data (string no formato ddmmaaaa ou dd/mm/aaaa) e retorne como
# parâmetro de saída True se é uma data mágica e False caso contrário.

def dataMagica(data):
    apenas_digitos = str.replace(data, '/', '')
    dia = int(apenas_digitos[0:2])
    mes = int(apenas_digitos[2:4])
    ano_curto = int(apenas_digitos[6:8])
    if dia * mes == ano_curto:
        return True
    else:
        return False


# 8. (Questão 30 - Lista): Criar uma função em Python chamada meiaString que receba
# como parâmetro de entrada uma string x e retorne como parâmetros de saída duas
# strings resultantes da divisão ao meio da string original. Se esta tiver
# quantidade ímpar de caracteres, a primeira parte deve ficar com um elemento a
# mais que a segunda.
# Por exemplo, 'walter' -> 'wal' e 'ter'; 'bruno' -> 'bru' e 'no'.

def meiaString(x):
    meio = (len(x) + 1) // 2
    primeira_metade = x[0:meio]
    segunda_metade = x[meio:len(x)]
    return primeira_metade, segunda_metade


# 9. (Questão 24 - Lista): Criar uma função em Python chamada invertePalavra que
# receba como parâmetro de entrada uma string x e retorne como parâmetro de saída
# uma string com os caracteres de x em ordem invertida.

def invertePalavra(x):
    invertida = ''
    for letra in x:
        invertida = letra + invertida
    return invertida


# 10. (Questão 15 - Lista): Um palíndromo é uma palavra, frase ou qualquer outra
# sequência de unidades que tem a propriedade de poder ser lida tanto da direita
# para a esquerda como da esquerda para a direita. Alguns exemplos: aibofobia,
# luz azul, Hanah e 20/02/2002.
# Tarefa: Criar uma função em Python chamada palindromo que receba como parâmetro
# de entrada uma string ou um número e retorne como parâmetro de saída True se é
# um palíndromo e False caso contrário.

def palindromo(x):
    texto = str.lower(str(x))
    texto = str.replace(texto, ' ', '')
    invertido = ''
    for caractere in texto:
        invertido = caractere + invertido
    if texto == invertido:
        return True
    else:
        return False
