def particao(array, inicio, fim):
    pivo = array[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if array[j] <= pivo:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[fim]) = (array[fim], array[i + 1])

    return i + 1


def quickSort(array, inicio, fim):
    if inicio < fim:

        pi = particao(array, inicio, fim)

        # ordena os elementos à esquerda do pivô
        quickSort(array, inicio, pi - 1)

        # ordena os elementos à direita do pivô
        quickSort(array, pi + 1, fim)


data = [10, 80, 30, 90, 40, 50, 70]
tam = len(data)
quickSort(data, 0, tam - 1)
print(data)