import os
from modulos.pilha import Pilha
from modulos.deposito import chega_no_deposito


def main():
    """Função principal interativa do sistema de empilhamento de caixas.

    Comportamento:
        - Inicializa três pilhas (A, B e C);
        - Exibe um menu com as opções disponíveis;
        - Permite ao usuário informar o peso da caixa (3, 5 ou 7 toneladas);
        - Controla o empilhamento conforme as regras de prioridade decrescente;
        - Exibe o estado atual das pilhas após cada operação;
        - Permite encerrar o programa quando desejado.
    """
    pilhaA = Pilha(10)
    pilhaB = Pilha(10)
    pilhaC = Pilha(10)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=' * 80)
        print('SISTEMA DE EMPILHAMENTO DE CAIXAS'.center(80))
        print('=' * 80)
        print('1. Adicionar caixa (3, 5 ou 7 toneladas)')
        print('2. Exibir estado das pilhas')
        print('3. Sair')
        print('-' * 80)

        opcao = input('Escolha uma opção (1-3): ').strip()

        if opcao == '1':
            try:
                peso = int(input('Digite o peso da caixa (3, 5 ou 7): '))
                if peso not in [3, 5, 7]:
                    print('Peso inválido! Use apenas 3, 5 ou 7.')
                    input('\nPressione ENTER para continuar...')
                else:
                    chega_no_deposito(peso, pilhaA, pilhaB, pilhaC)
            except ValueError:
                print('Entrada inválida! Digite um número inteiro.')
                input('\nPressione ENTER para continuar...')

        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('=' * 80)
            print('ESTADO ATUAL DAS PILHAS'.center(80))
            print('=' * 80)
            print(f"Pilha A: {pilhaA.itens}")
            print(f"Pilha B: {pilhaB.itens}")
            print(f"Pilha C: {pilhaC.itens}")
            print('=' * 80)
            input('\nPressione ENTER para voltar ao menu...')

        elif opcao == '3':
            print('-' * 80)
            print('Sistema encerrado. Obrigado por utilizar!')
            print('-' * 80)
            break

        else:
            print('Opção inválida! Tente novamente.')
            input('\nPressione ENTER para continuar...')


if __name__ == "__main__":
    main()
