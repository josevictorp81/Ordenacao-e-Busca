def bubble(v):
    for i in range(len(v)):# percorre todo a lista
        for j in range(len(v) - 1):# percorre a lista varias vezes
            if v[j] > v[j + 1]:# compara cada posicao da lista
                v[j], v[j + 1] = v[j + 1], v[j]# troca se o proximo for menos que o anterior

vet = [9, 1, 2, 7, 6, 0, 5, 11, 12, 8, 3, 4, 10]
bubble(vet)
print(vet)