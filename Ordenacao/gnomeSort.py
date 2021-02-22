def gonme(v):
    p = 0
    while p < len(v):
        if p == 0 or v[p] >= v[p - 1]:
            p += 1
        else:
            v[p], v[p - 1] = v[p - 1], v[p]
            p -= 1

vet = [9, 1, 2, 7, 6, 0, 5, 11, 12, 8, 3, 4, 10]
gonme(vet)
print(vet)