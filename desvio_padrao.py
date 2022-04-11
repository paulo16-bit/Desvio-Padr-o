amostra = input("Digite as amostas (a1 a2 a3): ")  # coleta as amostras
amostra = amostra.split()  # coloca os valores em uma lista
rol = sorted(list(map(float, amostra)))  # transforma os valores em números do tipo float e organiza


# função que calcula e retorna a média das amostras
def media(lista):
    media = sum(lista) / len(lista)
    return media


# função que calcula e retorna a variância das amostras
def variancia(lista):
    S = 0
    for i in lista:
        S += (i - media(rol)) ** 2
    S = S / len(lista)
    return S


# função que calcula e retorna o desvio padrão das amostras
def desvio():
    dp = (variancia(rol)) ** 0.5
    return dp


# função que calcula e retorna coeficiente de variância das amostras
def cv():
    cv = desvio() / media(rol) * 100
    return cv


print()
print("Média Aritimética: ", media(rol))
print("Variância: ", variancia(rol))
print("Desvio Padrão: ", desvio())
print("Coeficiente de Variação: ", cv())
