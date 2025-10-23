class FilaNotas:
    """Representa uma fila de notas utilizando a estrutura FIFO (First In, First Out).

    Cada elemento da fila é um dicionário com as chaves:
        - 'aluno': número do aluno associado à nota;
        - 'nota': valor numérico da nota (float entre 0 e 10).

    As notas são processadas na ordem de inserção, mantendo o controle sequencial.
    """

    def __init__(self, capacidade=100):
        """Inicializa a fila de notas com capacidade máxima.

        Args:
            capacidade (int, optional): Quantidade máxima de notas permitidas. Padrão: 100.

        Atributos:
            itens (list): Lista contendo as notas cadastradas.
            capacidade (int): Limite máximo de elementos na fila.
        """
        self.itens = []
        self.capacidade = capacidade

    def vazia(self):
        """Verifica se a fila está vazia.

        Returns:
            bool: True se não houver notas, False caso contrário.
        """
        return len(self.itens) == 0

    def cheia(self):
        """Verifica se a fila atingiu sua capacidade máxima.

        Returns:
            bool: True se a fila estiver cheia, False caso contrário.
        """
        return len(self.itens) == self.capacidade

    def enfileirar(self, numero_aluno, nota):
        """Adiciona uma nova nota ao final da fila.

        Args:
            numero_aluno (int): Número do aluno ao qual a nota pertence.
            nota (float): Valor da nota (entre 0 e 10).

        Comportamento:
            - Insere a nota no final da fila;
            - Caso a fila esteja cheia, exibe aviso e não insere o elemento.
        """
        if self.cheia():
            print("Fila cheia! Não é possível cadastrar mais notas.")
            return
        self.itens.append({"aluno": numero_aluno, "nota": nota})
        print(f"✅ Nota {nota:.1f} cadastrada para o aluno nº {numero_aluno}.")

    def desenfileirar(self):
        """Remove e retorna a nota mais antiga cadastrada (primeira da fila).

        Returns:
            dict | None: Dicionário da nota removida, ou None se a fila estiver vazia.
        """
        if not self.vazia():
            return self.itens.pop(0)
        print("Nenhuma nota para excluir.")
        return None

    def listar(self):
        """Retorna todas as notas cadastradas na fila.

        Returns:
            list[dict]: Lista contendo dicionários com número do aluno e valor da nota.
        """
        return self.itens

    def buscar_notas(self, numero_aluno):
        """Filtra e retorna todas as notas pertencentes a um aluno específico.

        Args:
            numero_aluno (int): Número do aluno a ser pesquisado.

        Returns:
            list[float]: Lista com todas as notas encontradas para o aluno informado.
        """
        return [n['nota'] for n in self.itens if n['aluno'] == numero_aluno]
