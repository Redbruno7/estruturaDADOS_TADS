import os
from modulos.pilha import PilhaAlunos
from modulos.fila import FilaNotas
from modulos.operacoes import (
    cadastrar_aluno,
    cadastrar_nota,
    calcular_media,
    listar_sem_notas,
    excluir_aluno,
    excluir_nota
)


def main():
    """Função principal do sistema de cadastro e controle de alunos e notas.

    Descrição geral:
        Este programa gerencia alunos e suas notas utilizando estruturas de dados clássicas:
            - Pilha (LIFO) para armazenar alunos;
            - Fila (FIFO) para armazenar notas.

    Funcionalidades:
        1. Cadastrar novos alunos com numeração automática;
        2. Associar notas válidas (0 a 10) aos alunos já cadastrados;
        3. Calcular a média individual de um aluno;
        4. Listar alunos que ainda não possuem notas;
        5. Excluir o aluno mais recente, desde que não tenha notas;
        6. Excluir a nota mais antiga cadastrada;
        7. Encerrar o programa.

    Observações:
        - As estruturas seguem rigorosamente as regras de empilhamento e enfileiramento;
        - Todas as entradas são validadas para evitar erros de execução;
        - O sistema opera em modo interativo, exibindo menus e mensagens informativas.
    """
    pilha = PilhaAlunos()
    fila = FilaNotas()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 80)
        print('SISTEMA DE CADASTRO DE ALUNOS E NOTAS'.center(80))
        print('=' * 80)
        print('1. Cadastrar aluno')
        print('2. Cadastrar nota')
        print('3. Calcular média de um aluno')
        print('4. Listar alunos sem notas')
        print('5. Excluir aluno (pilha)')
        print('6. Excluir nota (fila)')
        print('7. Sair')
        print('-' * 80)

        opcao = input('Escolha uma opção (1-7): ').strip()

        if opcao == '1':
            cadastrar_aluno(pilha)
        elif opcao == '2':
            cadastrar_nota(pilha, fila)
        elif opcao == '3':
            calcular_media(pilha, fila)
        elif opcao == '4':
            listar_sem_notas(pilha, fila)
        elif opcao == '5':
            excluir_aluno(pilha, fila)
        elif opcao == '6':
            excluir_nota(fila)
        elif opcao == '7':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção inválida!')

        input('\nPressione ENTER para continuar...')


if __name__ == "__main__":
    main()
