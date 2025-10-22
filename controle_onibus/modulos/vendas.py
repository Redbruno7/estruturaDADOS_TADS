import os
from .utils import input_int, input_str
from .poltronas import exibir_disponiveis, poltronas_disponiveis


def vender_passagem(janela, corredor):
    """Realiza o processo de venda de uma passagem.

    Args:
        janela (list[int]): Lista das poltronas da janela.
        corredor (list[int]): Lista das poltronas do corredor.
    """
    os.system('cls')

    if not poltronas_disponiveis(janela, corredor):
        print('=' * 80)
        print('ônibus lotado!')
        print('=' * 80)

        input('\nPressione ENTER para voltar ao menu: ')

        os.system('cls')
        return
    
    print('=' * 80)
    print('VENDA DE PASSAGEM'.center(80))
    print('=' * 80)

    tipo = input_str('Deseja uma poltrona na janela ou no corredor? ').lower()

    if tipo not in ['janela', 'corredor']:
        os.system('cls')

        print('-' * 80)
        print('Tipo inválido. Digite "janela" ou "corredor".')
        print('-' * 80)
        print()
        return
    
    exibir_disponiveis(janela, corredor, tipo)
    print('-' * 80)

    num = input_int(f'Digite o número da poltrona desejada (1-24): ')
    if num < 1 or num > 24:
        os.system('cls')

        print('-' * 80)
        print('Número inválido.')
        print('-' * 80)
        print()
        return
    
    lista = janela if tipo == 'janela' else corredor

    if lista[num -1] == 1:
        os.system('cls')

        print('-' * 80)
        print('Poltrona já ocupada!')
    else:
        os.system('cls')

        lista[num - 1] = 1

        print('-' * 80)
        print('Passagem confirmada! Boa viagem!')
    print('-' * 80)
    print()