from collections import deque

def soma_nos_niveis_impares(raiz):
    """
    Soma os valores dos nós que estão em níveis ímpares na árvore.
    """
    if not raiz:
        return 0

    fila = deque([(raiz, 0)])
    soma = 0

    while fila:
        no, nivel = fila.popleft()
        if nivel % 2 == 1:
            soma += no.valor
        if no.esquerda:
            fila.append((no.esquerda, nivel + 1))
        if no.direita:
            fila.append((no.direita, nivel + 1))

    return soma


def tamanho_nao_recursivo(raiz):
    """
    Calcula o tamanho (número total de nós) de uma árvore binária
    utilizando uma abordagem iterativa.
    """
    if not raiz:
        return 0

    fila = deque([raiz])
    tamanho = 0

    while fila:
        no = fila.popleft()
        tamanho += 1
        if no.esquerda:
            fila.append(no.esquerda)
        if no.direita:
            fila.append(no.direita)

    return tamanho


def eh_estritamente_binaria(raiz):
    """
    Verifica se a árvore é estritamente binária.
    Uma árvore é estritamente binária se cada nó tem 0 ou 2 filhos.
    """
    if not raiz:
        return True

    fila = deque([raiz])

    while fila:
        no = fila.popleft()
        filhos = sum([no.esquerda is not None, no.direita is not None])

        if filhos == 1:
            return False

        if no.esquerda:
            fila.append(no.esquerda)
        if no.direita:
            fila.append(no.direita)

    return True
