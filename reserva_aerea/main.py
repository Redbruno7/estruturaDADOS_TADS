import os
from modulos.dados_voos import criar_voos
from modulos.consultas import menu_consulta
from modulos.reservas import efetuar_reserva


def main():
    """Função principal do sistema de reserva de voos.

    Responsável por:
    - Limpar a tela inicial;
    - Criar a lista de voos disponíveis (chamando a função criar_voos());
    - Exibir o menu principal do programa;
    - Direcionar o usuário para as opções:
        1. Consultar voos;
        2. Efetuar reserva;
        3. Encerrar o sistema.

    O loop principal permanece ativo até o usuário escolher a opção "Sair".
    """
    os.system('cls')

    voos = criar_voos()

    while True:
        print('=' * 80)
        print('MENU PRINCIPAL'.center(80))
        print('=' * 80)
        print('1. Consultar voos')
        print('2. Efetuar reserva')
        print('3. Sair')
        print('-' * 80)
        opcao = input('Escolha uma opção (1-3): ')

        if opcao == '1':
            menu_consulta(voos)
        elif opcao == '2':
            efetuar_reserva(voos)
        elif opcao == '3':
            print('=' * 80)
            print()
            print('=' * 80)
            print('SISTEMA ENCERRADO')
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
