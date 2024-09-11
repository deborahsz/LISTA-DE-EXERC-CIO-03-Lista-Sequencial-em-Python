# criação da lista de números inteiros
numeros = [10, 15, 22, 33, 40, 55, 62]

# exibição da lista de números
print("Lista de números:", numeros)

# encontrar e exibir os números ímpares da lista
numeros_impares = [numero for numero in numeros if numero % 2 != 0]

# exibição dos números ímpares
print("Números ímpares na lista:", numeros_impares)
