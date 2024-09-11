# criação da lista de números inteiros
numeros = [10, 20, 30, 40, 50]

# exibição da lista de números
print("Lista de números:", numeros)

# verifica se a lista não está vazia para evitar divisão por zero
if len(numeros) > 0:
    # cálculo da soma de todos os números na lista
    soma_total = sum(numeros)
    
    # cálculo da média dos números na lista
    media = soma_total / len(numeros)
    
    # exibição da média
    print("Média dos números na lista:", media)
else:
    print("A lista está vazia. Não é possível calcular a média.")
