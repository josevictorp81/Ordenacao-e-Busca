def pesquisa(vetor, chave):
    for i in range(len(vetor)):
        #print(i)
        if vetor[i] == chave:
            return i
    
    return None


vet = [2, 4, 6, 1, 9, 10]

ch = int(input('Chave: '))
p = pesquisa(vet, ch)

if p is None:
    print('Item buscado nao esta na lista')
else:
    print('A chave {} esta na posicao {} da lista'.format(ch, p))