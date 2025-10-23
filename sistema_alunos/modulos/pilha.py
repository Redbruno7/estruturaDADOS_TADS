class PilhaAlunos:
    """Representa uma pilha de alunos utilizando a estrutura LIFO (Last In, First Out).

    Cada elemento da pilha é um dicionário com as seguintes chaves:
        - 'numero': número identificador do aluno (gerado automaticamente);
        - 'nome': nome completo do aluno.

    A pilha armazena os alunos na ordem em que foram cadastrados, permitindo
    a remoção apenas do último elemento inserido (topo da pilha).
    """

    def __init__(self, capacidade=50):
        """Inicializa a pilha de alunos com capacidade e contador de número automático.

        Args:
            capacidade (int, optional): Número máximo de alunos permitidos na pilha.
                Valor padrão: 50.

        Atributos:
            itens (list): Lista de dicionários representando os alunos cadastrados.
            capacidade (int): Limite máximo de alunos na pilha.
            proximo_numero (int): Número sequencial para atribuição automática aos alunos.
        """
        self.itens = []
        self.capacidade = capacidade
        self.proximo_numero = 1

    def vazia(self):
        """Verifica se a pilha está vazia.

        Returns:
            bool: True se não houver alunos cadastrados, False caso contrário.
        """
        return len(self.itens) == 0

    def cheia(self):
        """Verifica se a pilha atingiu sua capacidade máxima.

        Returns:
            bool: True se a pilha estiver cheia, False caso contrário.
        """
        return len(self.itens) == self.capacidade

    def empilhar(self, nome):
        """Adiciona um novo aluno ao topo da pilha.

        Args:
            nome (str): Nome do aluno a ser cadastrado.

        Comportamento:
            - Gera automaticamente o número do aluno;
            - Cria um dicionário {'numero': X, 'nome': 'Y'} e adiciona à pilha;
            - Caso a pilha esteja cheia, exibe mensagem de aviso.

        Observações:
            - O número do aluno é único e incremental;
            - Alunos são sempre adicionados ao final da lista (topo da pilha).
        """
        if self.cheia():
            print("Pilha cheia! Não é possível cadastrar mais alunos.")
            return

        aluno = {"numero": self.proximo_numero, "nome": nome}
        self.itens.append(aluno)
        self.proximo_numero += 1
        print(
            f"Aluno cadastrado com sucesso! Nº {aluno['numero']} - {aluno['nome']}")

    def desempilhar(self):
        """Remove o aluno do topo da pilha (último cadastrado).

        Returns:
            dict | None: Dicionário com os dados do aluno removido, ou None se a pilha estiver vazia.

        Observações:
            - Um aluno só deve ser removido se não possuir notas associadas.
        """
        if not self.vazia():
            return self.itens.pop()
        print("Nenhum aluno para excluir.")
        return None

    def topo(self):
        """Retorna o aluno mais recente (topo) sem removê-lo.

        Returns:
            dict | None: Dicionário do aluno no topo, ou None se a pilha estiver vazia.
        """
        if not self.vazia():
            return self.itens[-1]
        return None

    def listar(self):
        """Retorna a lista completa de alunos cadastrados.

        Returns:
            list[dict]: Lista de dicionários com todos os alunos da pilha.
        """
        return self.itens

    def buscar(self, numero):
        """Procura um aluno pelo número de identificação.

        Args:
            numero (int): Número do aluno.

        Returns:
            dict | None: Dicionário do aluno correspondente, ou None se não encontrado.
        """
        for aluno in self.itens:
            if aluno['numero'] == numero:
                return aluno
        return None
