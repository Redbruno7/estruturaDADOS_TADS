import os


def cadastrar_aluno(pilha):
    """Cadastra um novo aluno na pilha principal.

    Args:
        pilha (PilhaAlunos): Objeto da classe PilhaAlunos responsável pelo armazenamento.

    Comportamento:
        - Solicita o nome do aluno ao usuário;
        - Valida a entrada, garantindo que o nome não esteja vazio;
        - Gera automaticamente o número identificador e empilha o aluno.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do aluno: ").strip().title()
    if nome:
        pilha.empilhar(nome)
    else:
        print("Nome inválido. Digite novamente.")


def cadastrar_nota(pilha, fila):
    """Cadastra uma nova nota na fila de notas, vinculada a um aluno existente.

    Args:
        pilha (PilhaAlunos): Estrutura contendo os alunos cadastrados.
        fila (FilaNotas): Estrutura FIFO responsável pelas notas.

    Regras:
        - A nota só é cadastrada se o número do aluno existir na pilha;
        - O valor deve ser numérico e estar entre 0 e 10;
        - Caso contrário, uma mensagem de erro é exibida.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        numero = int(input("Digite o número do aluno: "))
        aluno = pilha.buscar(numero)
        if not aluno:
            print("Aluno não encontrado.")
            return

        nota = float(input("Digite a nota (0 a 10): "))
        if 0 <= nota <= 10:
            fila.enfileirar(numero, nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")


def calcular_media(pilha, fila):
    """Calcula e exibe a média das notas de um aluno específico.

    Args:
        pilha (PilhaAlunos): Pilha contendo os alunos cadastrados.
        fila (FilaNotas): Fila contendo as notas registradas.

    Comportamento:
        - Solicita o número do aluno;
        - Caso o aluno exista e tenha notas, calcula e exibe a média aritmética;
        - Caso não haja notas, exibe mensagem de aviso.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        numero = int(input("Digite o número do aluno: "))
        aluno = pilha.buscar(numero)
        if not aluno:
            print("Aluno não encontrado.")
            return

        notas = fila.buscar_notas(numero)
        if not notas:
            print(f"O aluno {aluno['nome']} não possui notas cadastradas.")
            return

        media = sum(notas) / len(notas)
        print(f"Aluno: {aluno['nome']} | Média: {media:.2f}")
    except ValueError:
        print("Entrada inválida.")


def listar_sem_notas(pilha, fila):
    """Lista todos os alunos cadastrados que ainda não possuem notas.

    Args:
        pilha (PilhaAlunos): Estrutura com os alunos cadastrados.
        fila (FilaNotas): Estrutura com as notas existentes.

    Comportamento:
        - Compara os alunos cadastrados com as notas registradas;
        - Exibe apenas os alunos sem nenhuma nota associada;
        - Caso todos possuam notas, exibe uma mensagem informativa.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    alunos = pilha.listar()
    notas = fila.listar()

    alunos_com_nota = {n['aluno'] for n in notas}
    sem_nota = [a for a in alunos if a['numero'] not in alunos_com_nota]

    if sem_nota:
        print("Alunos sem notas:")
        for a in sem_nota:
            print(f"  Nº {a['numero']} - {a['nome']}")
    else:
        print("Todos os alunos possuem notas cadastradas.")


def excluir_aluno(pilha, fila):
    """Remove o aluno do topo da pilha, caso não possua notas associadas.

    Args:
        pilha (PilhaAlunos): Estrutura principal de alunos.
        fila (FilaNotas): Estrutura de notas utilizadas na verificação.

    Regras:
        - O aluno só pode ser removido se estiver no topo da pilha e sem notas;
        - Caso tenha notas, a exclusão é bloqueada e uma mensagem é exibida.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    if pilha.vazia():
        print("Nenhum aluno cadastrado.")
        return

    aluno = pilha.topo()
    notas = fila.buscar_notas(aluno['numero'])

    if notas:
        print(
            f"O aluno {aluno['nome']} não pode ser excluído (possui notas).")
    else:
        removido = pilha.desempilhar()
        print(f"Aluno {removido['nome']} removido com sucesso.")


def excluir_nota(fila):
    """Remove a nota mais antiga da fila, respeitando a ordem FIFO.

    Args:
        fila (FilaNotas): Estrutura de armazenamento de notas.

    Comportamento:
        - Remove a primeira nota inserida (frente da fila);
        - Caso não haja notas, informa o usuário.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    removida = fila.desenfileirar()
    if removida:
        print(
            f"Nota {removida['nota']:.1f} do aluno nº {removida['aluno']} removida.")
