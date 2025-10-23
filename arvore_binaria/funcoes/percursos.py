from collections import deque


def pre_ordem_iterativo(raiz):
    """
    Percorre a árvore em pré-ordem (Raiz → Esquerda → Direita) de forma não recursiva.
    """
    if not raiz:
        return []
    pilha = [raiz]
    resultado = []

    while pilha:
        no = pilha.pop()
        resultado.append(no.valor)
        if no.direita:
            pilha.append(no.direita)
        if no.esquerda:
            pilha.append(no.esquerda)
    return resultado


def em_ordem_iterativo(raiz):
    """
    Percorre a árvore em ordem (Esquerda → Raiz → Direita) de forma não recursiva.
    """
    pilha, resultado = [], []
    atual = raiz
    while True:
        if atual:
            pilha.append(atual)
            atual = atual.esquerda
        elif pilha:
            atual = pilha.pop()
            resultado.append(atual.valor)
            atual = atual.direita
        else:
            break
    return resultado


def pos_ordem_iterativo(raiz):
    """
    Percorre a árvore em pós-ordem (Esquerda → Direita → Raiz) sem recursão.
    """
    if not raiz:
        return []
    pilha1, pilha2 = [raiz], []
    while pilha1:
        no = pilha1.pop()
        pilha2.append(no)
        if no.esquerda:
            pilha1.append(no.esquerda)
        if no.direita:
            pilha1.append(no.direita)
    return [n.valor for n in reversed(pilha2)]


def percurso_em_nivel(raiz):
    """
    Percorre a árvore em nível (largura), visitando os nós nível a nível.
    """
    if not raiz:
        return []
    fila = deque([raiz])
    resultado = []
    while fila:
        no = fila.popleft()
        resultado.append(no.valor)
        if no.esquerda:
            fila.append(no.esquerda)
        if no.direita:
            fila.append(no.direita)
    return resultado
