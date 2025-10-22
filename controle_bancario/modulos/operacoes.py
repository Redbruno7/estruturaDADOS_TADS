import os
from .utils import input_int, input_float


def efetuar_deposito(codigos, saldos):
    """Realiza o depósito de um valor em uma conta existente.

    Args:
        codigos (list[int]): Lista contendo os códigos numéricos das contas cadastradas.
        saldos (list[float]): Lista contendo os saldos correspondentes às contas.

    Comportamento:
        - Solicita ao usuário o código da conta e o valor do depósito;
        - Caso o código informado não exista, exibe mensagem "Conta não encontrada";
        - Caso o valor seja menor ou igual a zero, exibe mensagem "Valor inválido";
        - Caso os dados sejam válidos:
            º Localiza a conta na lista de códigos;
            º Atualiza o saldo somando o valor depositado;
            º Exibe mensagem de confirmação e o novo saldo.

    Observações:
        - A função altera diretamente o valor na lista de saldos, refletindo a mudança
          no sistema principal;
        - Utiliza funções auxiliares de entrada (`input_int` e `input_float`)
          para validar os dados digitados.
    """
    os.system('cls')

    print('=' * 80)
    print('DEPÓSITO'.center(80))
    print('=' * 80)

    codigo = input_int('Informe o código da conta: ')
    print('-' * 80)

    if codigo not in codigos:
        os.system('cls')

        print('-' * 80)
        print('Conta não encontrada.')
        print('-' * 80)
        print()
        return

    valor = input_float('Informe o valor do depósito: ')
    print('-' * 80)

    if valor <= 0:
        os.system('cls')

        print('-' * 80)
        print('Valor inválido.')
        print('-' * 80)
        print()
        return

    i = codigos.index(codigo)
    saldos[i] += valor

    os.system('cls')

    print('-' * 80)
    print('Depósito realizado com sucesso!')
    print(f'Saldo atual: R$ {saldos[i]:.2f}')
    print('-' * 80)
    print()


def efetuar_saque(codigos, saldos):
    """Realiza o saque de um valor em uma conta existente.

    Args:
        codigos (list[int]): Lista contendo os códigos numéricos das contas cadastradas.
        saldos (list[float]): Lista contendo os saldos correspondentes às contas.

    Comportamento:
        - Solicita ao usuário o código da conta e o valor a ser sacado;
        - Caso o código informado não exista, exibe "Conta não encontrada";
        - Caso o valor seja menor ou igual a zero, exibe "Valor inválido";
        - Caso o saldo da conta seja insuficiente, exibe "Saldo insuficiente";
        - Caso tudo esteja correto:
            º Subtrai o valor do saldo da conta;
            º Exibe mensagem de confirmação e o saldo atualizado.

    Observações:
        - A conta não pode ficar com saldo negativo;
        - A função altera a lista de saldos diretamente, mantendo a atualização global.
    """
    os.system('cls')

    print('=' * 80)
    print('SAQUE'.center(80))
    print('=' * 80)

    codigo = input_int('Digite o código da conta: ')
    print('-' * 80)

    if codigo not in codigos:
        os.system('cls')

        print('-' * 80)
        print('Conta não encontrada.')
        print('-' * 80)
        print()
        return

    valor = input_float('Informe o valor do saque: ')
    i = codigos.index(codigo)
    print('-' * 80)

    if valor <= 0:
        os.system('cls')

        print('-' * 80)
        print('Valor inválido.')
        print('-' * 80)
        print()
    elif saldos[i] < valor:
        os.system('cls')

        print('-' * 80)
        print('Saldo insuficiente.')
        print('-' * 80)
        print()
    else:
        os.system('cls')

        saldos[i] -= valor

        print('-' * 80)
        print('Saque realizado com sucesso!')
        print(f'Saldo atual: R$ {saldos[i]:.2f}')
        print('-' * 80)
        print()


def consultar_ativo_bancario(saldos):
    """Calcula e exibe o total do ativo bancário do sistema.

    Args:
        saldos (list[float]): Lista contendo os saldos de todas as contas.

    Comportamento:
        - Soma todos os valores da lista de saldos;
        - Exibe o total acumulado, representando o ativo financeiro do banco;
        - Retorna ao menu principal após exibir o resultado.

    Observações:
        - O cálculo é feito em tempo real com base nos saldos atuais;
        - Serve apenas para consulta, não altera nenhuma informação do sistema.
    """
    os.system('cls')

    total = sum(saldos)

    print('=' * 80)
    print('ATIVO BANCÁRIO'.center(80))
    print('-' * 80)
    print(f'O banco possui um total de R$ {total:.2f} disponíveis.')
    print('=' * 80)
    print()
