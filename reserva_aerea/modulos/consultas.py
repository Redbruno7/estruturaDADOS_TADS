import os
from .utils import input_int, input_str


def consultar_numero(voos):
    """Realiza a consulta de um voo específico pelo número.

    Args:
        voos (list): Lista de dicionários contendo os dados de todos os voos.

    Comportamento:
        - Solicita ao usuário o número do voo desejado;
        - Busca o voo correspondente na lista;
        - Exibe as informações do voo, caso encontrado;
        - Caso o número não exista, informa que o voo é inexistente.
    """
    os.system('cls')

    print('=' * 80)
    numero = input_int('Digite o número do voo: ')
    print('-' * 80)

    voo = next((v for v in voos if v['numero'] == numero), None)

    if voo:
        print(
            f"Voo {voo['numero']} | {voo['origem']} -> {voo['destino']} | Lugares: {voo['lugares']}")
        print('=' * 80)
        print()
    else:
        print('Voo inexistente.')
        print('=' * 80)
        print()


def consulta_origem(voos):
    """Realiza a consulta de voos com base na origem informada.

    Args:
        voos (list): Lista de dicionários contendo os dados de todos os voos.

    Comportamento:
        - Solicita a cidade de origem ao usuário;
        - Lista todos os voos que partem dessa origem;
        - Caso nenhum voo seja encontrado, exibe mensagem informativa.
    """
    os.system('cls')

    print('=' * 80)
    origem = input_str('Digite a origem: ')
    print('-' * 80)

    encontrados = [v for v in voos if v['origem'] == origem]

    if encontrados:
        for v in encontrados:
            print(
                f"{v['numero']} | {v['origem']} → {v['destino']} | Lugares: {v['lugares']}")
        print('=' * 80)
        print()
    else:
        print('Nenhum voo encontrado com essa origem.')
        print('=' * 80)
        print()


def consultar_destino(voos):
    """Realiza a consulta de voos com base no destino informado.

    Args:
        voos (list): Lista de dicionários contendo os dados de todos os voos.

    Comportamento:
        - Solicita a cidade de destino ao usuário;
        - Lista todos os voos que têm esse destino;
        - Caso nenhum voo seja encontrado, exibe mensagem informativa.
    """
    os.system('cls')

    print('=' * 80)
    destino = input_str('Digite o destino: ')
    print('-' * 80)

    encontrados = [v for v in voos if v['destino'] == destino]

    if encontrados:
        for v in encontrados:
            print(
                f"{v['numero']} | {v['origem']} → {v['destino']} | Lugares: {v['lugares']}")
        print('=' * 80)
        print()
    else:
        print('Nenhum voo encontrado com esse destino.')
        print('=' * 80)
        print()


def consultar_todos(voos):
    """Exibe uma listagem completa de todos os voos disponíveis.

    Args:
        voos (list): Lista de dicionários contendo os dados de todos os voos.

    Comportamento:
        - Exibe todos os voos cadastrados em formato de tabela;
        - Mostra número, origem, destino e quantidade de lugares disponíveis;
        - Após exibir a tabela, aguarda o usuário pressionar ENTER
          antes de retornar ao menu.
    """
    os.system('cls')

    print('=' * 80)
    print('LISTA COMPLETA DE VOOS'.center(80))
    print('=' * 80)
    print(f"{'N°':<6}{'Origem':<25}{'Destino':<25}{'Lugares':<10}")
    print('-' * 80)

    for v in voos:
        print(
            f"{v['numero']:<6}{v['origem']:<25}{v['destino']:<25}{v['lugares']:<10}")

    print('=' * 80)
    input("\nPressione ENTER para voltar ao menu...")

    os.system('cls')


def menu_consulta(voos):
    """Exibe o menu de consultas e direciona para a função apropriada.

    Args:
        voos (list): Lista de dicionários contendo os dados de todos os voos.

    Comportamento:
        - Exibe um menu com as opções de consulta disponíveis:
            1. Consultar por número
            2. Consultar por origem
            3. Consultar por destino
            4. Consultar todos os voos
            5. Voltar ao menu principal
        - Redireciona o usuário conforme a opção escolhida;
        - Mantém o menu em loop até que o usuário escolha "Voltar".
    """
    os.system('cls')

    while True:
        print('=' * 80)
        print('CONSULTAR VOOS'.center(80))
        print('=' * 80)
        print('1. Número')
        print('2. Origem')
        print('3. Destino')
        print('4. Todos os voos')
        print('5. Voltar')
        print('-' * 80)
        opcao = input('Escolha uma opção (1-5): ')

        if opcao == '1':
            consultar_numero(voos)
        elif opcao == '2':
            consulta_origem(voos)
        elif opcao == '3':
            consultar_destino(voos)
        elif opcao == '4':
            consultar_todos(voos)
        elif opcao == '5':
            os.system('cls')
            break
        else:
            os.system('cls')

            print('-' * 80)
            print('Opção inválida! Tente novamente.')
            print('-' * 80)
            print()
