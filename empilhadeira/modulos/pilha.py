class Pilha:
    """Representa uma estrutura de dados do tipo pilha (stack).

    A pilha armazena elementos seguindo o princípio LIFO
    (Last In, First Out — o último a entrar é o primeiro a sair).

    Attributes:
        itens (list): Lista que contém os elementos empilhados.
        capacidade (int): Quantidade máxima de elementos que a pilha pode conter.
    """

    def __init__(self, capacidade):
        """Inicializa uma nova pilha vazia com capacidade definida.

        Args:
            capacidade (int): Capacidade máxima de armazenamento da pilha.
        """
        self.itens = []
        self.capacidade = capacidade

    def vazia(self):
        """Verifica se a pilha está vazia.

        Returns:
            bool: True se a pilha estiver vazia, False caso contrário.
        """
        return len(self.itens) == 0

    def cheia(self):
        """Verifica se a pilha atingiu sua capacidade máxima.

        Returns:
            bool: True se a pilha estiver cheia, False caso contrário.
        """
        return len(self.itens) == self.capacidade

    def empilhar(self, valor):
        """Adiciona um novo elemento ao topo da pilha.

        Args:
            valor (any): Valor a ser inserido no topo da pilha.

        Observações:
            - Caso a pilha esteja cheia, exibe uma mensagem de aviso.
        """
        if not self.cheia():
            self.itens.append(valor)
        else:
            print("⚠️ Pilha cheia! Não foi possível empilhar o item.")

    def desempilhar(self):
        """Remove e retorna o elemento do topo da pilha.

        Returns:
            any | None: Valor removido do topo, ou None se a pilha estiver vazia.
        """
        if not self.vazia():
            return self.itens.pop()
        return None

    def topo(self):
        """Retorna o elemento do topo da pilha sem removê-lo.

        Returns:
            any | None: Elemento do topo, ou None se a pilha estiver vazia.
        """
        if not self.vazia():
            return self.itens[-1]
        return None

    def __repr__(self):
        """Retorna uma representação legível da pilha.

        Returns:
            str: Representação textual mostrando os elementos empilhados.
        """
        return f"Pilha({self.itens})"
