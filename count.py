def counting_sort(arr):
    # Encontra o valor máximo no array
    max_value = max(arr)

    # Inicializa um array auxiliar com zeros
    count = [0] * (max_value + 1)

    # Conta o número de ocorrências de cada valor no array
    for i in arr:
        count[i] += 1

    # Calcula a posição de cada elemento no array ordenado
    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    # Cria um array ordenado
    sorted_arr = [0] * len(arr)
    for i in arr:
        sorted_arr[count[i] - 1] = i
        count[i] -= 1

    return sorted_arr

arr = [3, 1, 4, 2, 3, 1, 4, 2, 3, 5]
sorted_arr = counting_sort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
