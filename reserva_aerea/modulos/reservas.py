import os
from .utils import input_int


def efetuar_reserva(voos):
    """Realiza a reserva de assento em um voo específico.

    Args:
        voos (list): Lista de dicionários contendo os dados de todos os voos.

    Comportamento:
        - Limpa a tela e exibe o cabeçalho da seção de reservas;
        - Solicita ao usuário o número do voo desejado;
        - Verifica se o voo informado existe na lista de voos;
        - Caso o voo não exista, exibe mensagem informando "Voo inexistente";
        - Caso o voo exista mas esteja lotado, informa "Voo lotado";
        - Caso o voo possua lugares disponíveis:
            º Diminui em 1 o número de lugares;
            º Confirma a reserva ao usuário, mostrando quantos lugares restam.

    Observações:
        - A atualização é feita diretamente na lista recebida como parâmetro,
          garantindo que a alteração seja refletida globalmente no sistema;
        - Não há persistência em banco de dados, pois trata-se de simulação.
    """
    os.system('cls')

    print('=' * 80)
    print('EFETUAR RESERVA'.center(80))
    print('=' * 80)
    print()

    print('=' * 80)
    numero = input_int('Digite o número do voo desejado: ')
    print('-' * 80)

    voo = next((v for v in voos if v['numero'] == numero), None)

    if not voo:
        print('Voo inexistente.')
        print('=' * 80)
        print()
    elif voo['lugares'] == 0:
        print('Voo lotado.')
        print('=' * 80)
        print()
    else:
        voo['lugares'] -= 1
        print(f'Reserva confirmada! Lugares restantes: {voo['lugares']}')
        print('=' * 80)
        print()
