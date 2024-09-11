# criação das duas listas de números inteiros
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

# exibição das listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# encontrar os números que estão presentes em ambas as listas
numeros_comuns = [numero for numero in lista1 if numero in lista2]

# exibição dos números comuns
print("Números presentes em ambas as listas:", numeros_comuns)
