import os
from modulos.poltronas import inicializar_poltronas
from modulos.vendas import vender_passagem


def main():
    """Função principal do sistema de controle de passagens."""
    os.system('cls')

    janela, corredor = inicializar_poltronas()

    while True:
        print('=' * 80)
        print('SISTEMA DE VENDA DE PASSAGENS'.center(80))
        print('=' * 80)
        print('1. Comprar passagem')
        print('2. Sair')
        print('-' * 80)

        opcao = input('Escolha uma opção (1-2): ')

        if opcao == '1':
            vender_passagem(janela, corredor)
        elif opcao == '2':
            print('=' * 80)
            print('Sistema encerrado.')
            print('=' * 80)
            print()
            break
        else:
            os.system('cls')
            print('-' * 80)
            print('Opção inválida! Tente novamente.')
            print('-' * 80)
            print()


if __name__ == '__main__':
    main()