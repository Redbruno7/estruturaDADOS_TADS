from estruturas.no import No

class ArvoreBinaria:
    """
    Representa uma árvore binária simples (não balanceada).

    Métodos:
        inserir(valor): Insere um novo valor na árvore.
        mostrar_em_ordem(): Exibe os valores em ordem crescente.
    """

    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """Insere um novo nó na árvore de forma iterativa."""
        novo = No(valor)

        if self.raiz is None:
            self.raiz = novo
            return

        atual = self.raiz
        while True:
            if valor < atual.valor:
                if atual.esquerda:
                    atual = atual.esquerda
                else:
                    atual.esquerda = novo
                    break
            else:
                if atual.direita:
                    atual = atual.direita
                else:
                    atual.direita = novo
                    break

    def mostrar_em_ordem(self):
        """Percorre a árvore em ordem e imprime os valores."""
        def _em_ordem(no):
            if no:
                _em_ordem(no.esquerda)
                print(no.valor, end=" ")
                _em_ordem(no.direita)

        _em_ordem(self.raiz)
        print()
