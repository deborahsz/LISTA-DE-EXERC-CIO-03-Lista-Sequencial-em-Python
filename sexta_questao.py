# criação da lista de strings
palavras = ["elefante", "gato", "hipopotamo", "cachorro", "rato"]

# exibição da lista de palavras
print("Lista de palavras:", palavras)

# encontrar a palavra mais longa
if palavras:
    palavra_mais_longa = max(palavras, key=len)
    # exibição da palavra mais longa
    print("A palavra mais longa na lista é:", palavra_mais_longa)
else:
    print("A lista está vazia. Não há palavras para verificar.")
