def insertion(v):
    for i in range(1, len(v)):
        aux = v[i]
        j = i - 1 
        while j >= 0 and aux < v[j]:
            v[j + 1] =  v[j]
            j -= 1
        v[j+ 1] = aux

vet = [9, 1, 2, 7, 6, 0, 5, 11, 12, 8, 3, 4, 10]
insertion(vet)
print(vet)