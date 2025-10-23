class No:
    """
    Representa um nó de uma árvore binária.

    Atributos:
        valor (int | float): Valor armazenado no nó.
        esquerda (No | None): Referência para o nó filho à esquerda.
        direita (No | None): Referência para o nó filho à direita.
    """

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return f"No({self.valor})"
