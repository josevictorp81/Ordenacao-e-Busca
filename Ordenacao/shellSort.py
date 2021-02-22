def shellSort(vet):

    intervalo = len(vet) // 2
    while intervalo > 0:
        for i in range(intervalo, len(vet)):
            temp = vet[i]
            j = i
            while j >= intervalo and vet[j - intervalo] > temp:
                vet[j] = vet[j - intervalo]
                j -= intervalo

            vet[j] = temp
        intervalo //= 2  

vet = [2, 1, 7, 0, 6, 9, 4, 3]
shellSort(vet)
print(vet)