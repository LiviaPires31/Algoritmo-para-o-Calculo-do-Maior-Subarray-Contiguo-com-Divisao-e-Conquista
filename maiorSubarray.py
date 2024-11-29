# Função para encontrar a soma máxima de um subarray que cruza o meio do array
def encontra_soma_maior_subarray(array, baixo, meio, alto):
    soma_atual = 0
    soma_maior_esquerda = float('-inf')
    subarray_maior_esquerda = []

    # Itera da metade para a esquerda do array
    for i in range(meio, baixo - 1, -1):
        soma_atual += array[i]
        # Se a soma atual for maior que a soma máxima encontrada até agora, atualiza a soma máxima e o subarray
        if soma_atual > soma_maior_esquerda:
            soma_maior_esquerda = soma_atual
            subarray_maior_esquerda = array[i:meio + 1]

    soma_atual = 0
    soma_maior_direita = float('-inf')
    subarray_maior_direita = []

    # Itera da metade para a direita do array
    for i in range(meio + 1, alto + 1):
        soma_atual += array[i]
        # Se a soma atual for maior que a soma máxima encontrada até agora, atualiza a soma máxima e o subarray
        if soma_atual > soma_maior_direita:
            soma_maior_direita = soma_atual
            subarray_maior_direita = array[meio + 1:i + 1]

    # Retorna a soma máxima e o subarray que cruza o meio do array
    return soma_maior_esquerda + soma_maior_direita, subarray_maior_esquerda + subarray_maior_direita

def encontra_soma_maior_divisao_conquista(arr, baixo, alto):
    # Caso base: se o array contém apenas um elemento
    if baixo == alto:
        return arr[baixo], [arr[baixo]]

    meio = (baixo + alto) // 2

    # Recursivamente encontra a soma máxima no lado esquerdo e direito do array
    soma_maior_esquerda, subarray_maior_esquerda = encontra_soma_maior_divisao_conquista(arr, baixo, meio)
    soma_maior_direita, subarray_maior_direita = encontra_soma_maior_divisao_conquista(arr, meio + 1, alto)

    # Encontra a soma máxima que cruza o meio do array
    soma_maior_cruzado, subarray_maior_cruzado = encontra_soma_maior_subarray(arr, baixo, meio, alto)

    # Retorna a maior das três somas e o respectivo subarray
    if soma_maior_esquerda >= soma_maior_direita and soma_maior_esquerda >= soma_maior_cruzado:
        return soma_maior_esquerda, subarray_maior_esquerda
    elif soma_maior_direita >= soma_maior_esquerda and soma_maior_direita >= soma_maior_cruzado:
        return soma_maior_direita, subarray_maior_direita
    else:
        return soma_maior_cruzado, subarray_maior_cruzado

# Loop principal que continua pedindo entradas até que 'sair' seja digitado
while True:
    entrada = input("Digite os números separados por espaço (ou 'sair' para terminar): ")

    # Se 'sair' for digitado, termina o loop
    if entrada.lower() == 'sair':
        break

    # Converte a entrada em uma lista de inteiros
    array = list(map(int, entrada.split()))

    n = len(array)

    # Encontra a soma máxima e o subarray correspondente
    maior_soma, maior_subarray = encontra_soma_maior_divisao_conquista(array, 0, n - 1)

    print("A soma máxima contígua é", maior_soma)
    print("O subarray com a soma máxima é", maior_subarray)

