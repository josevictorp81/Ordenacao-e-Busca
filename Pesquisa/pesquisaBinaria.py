def pesquisa(vetor, chave, inicio, fim):
    if inicio <= fim:
        meio = (inicio + fim) // 2 # divide pela metade a cada iteracao = log n
        if vetor[meio] == chave:
            return meio
        if chave < vetor[meio]:
            return pesquisa(vetor, chave, inicio, meio - 1)
        else:
            return pesquisa(vetor, chave, meio + 1, fim)
    return None


vet = [1, 2, 4, 5, 6, 9] # 
ch = int(input('chave: '))
p = pesquisa(vet, ch, 0, len(vet)- 1)

if p is None:
    print('Item buscado nao esta na lista')
else:
    print('A chave {} esta na posicao {} da lista'.format(ch, p))