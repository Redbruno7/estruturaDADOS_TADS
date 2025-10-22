from .utils import input_int, input_float


def efetuar_deposito(codigos, saldos):
    """_summary_

    Args:
        codigos (_type_): _description_
        saldos (_type_): _description_
    """
    print('=' * 80)
    print('DEPÓSITO'.center(80))
    print('=' * 80)

    codigo = input_int('Informe o código da conta: ')
    print('-' * 80)

    if codigo not in codigos:
        print('Conta não encontrada.')
        print('=' * 80)
        print()
        return

    valor = input_float('Informe o valor do depósito: ')
    print('-' * 80)

    if valor <= 0:
        print('Valor inválido.')
        print('=' * 80)
        print()
        return

    i = codigos.index(codigo)
    saldos[i] += valor
    print('Depósito realizado com sucesso!')
    print(f'Saldo atual: R$ {saldos[i]:.2f}')


def efetuar_saque(codigos, saldos):
    """_summary_

    Args:
        codigos (_type_): _description_
        saldos (_type_): _description_
    """
    print('=' * 80)
    print('SAQUE'.center(80))
    print('=' * 80)

    codigo = input_int('Digite o código da conta: ')
    print('-' * 80)

    if codigo not in codigos:
        print('Conta não encontrada.')
        print('=' * 80)
        print()
        return

    valor = input_float('Informe o valor do saque: ')
    i = codigos.index(codigo)
    print('-' * 80)

    if valor <= 0:
        print('Valor inválido.')
        print('-' * 80)
    elif saldos[i] < valor:
        print('Saldo insuficiente.')
        print('-' * 80)
    else:
        saldos[i] -= valor

        print('Saque realizado com sucesso!')
        print(f'Saldo atual: R$ {saldos[i]:.2f}')
        print('=' * 80)
        print()


def consultar_ativo_bancario(saldos):
    """_summary_

    Args:
        saldos (_type_): _description_
    """
    total = sum(saldos)

    print('=' * 80)
    print('ATIVO BANCÁRIO'.center(80))
    print('=' * 80)
    print(f'O banco possui um total de R$ {total:.2f} disponíveis.')
    print('=' * 80)
    print()
