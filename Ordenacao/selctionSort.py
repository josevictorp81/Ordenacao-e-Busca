def selection(v):
    for i in range(0, len(v) - 1):
        menor = i
        for j in range(i + 1, len(v)):
            if v[j] < v[menor]:
                menor = j
        v[i], v[menor] = v[menor], v[i]


vet = [9, 1, 2, 7, 6, 0, 5, 11, 12, 8, 3, 4, 10]
selection(vet)
print(vet)