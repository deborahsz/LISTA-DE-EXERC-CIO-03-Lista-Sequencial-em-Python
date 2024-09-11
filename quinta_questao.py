# criação da lista de palavras
palavras = ["Abacaxi", "banana", "Ameixa", "maçã", "Açúcar", "pêssego"]

# exibição da lista de palavras
print("Lista de palavras:", palavras)

# contagem das palavras que começam com a letra 'A'
contador = sum(1 for palavra in palavras if palavra.lower().startswith('a'))

# exibição da quantidade de palavras que começam com a letra 'A'
print("Quantidade de palavras que começam com a letra 'A':", contador)
