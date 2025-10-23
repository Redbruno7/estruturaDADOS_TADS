def input_int(msg, erro='Entrada inválida! Digite um número inteiro.'):
    """Solicita um valor inteiro do usuário com tratamento de erro.

    Args:
        msg (str): Mensagem exibida ao usuário solicitando o valor.
        erro (str, optional): Mensagem exibida em caso de erro. Defaults to 'Entrada inválida! Digite um número inteiro.'.

    Returns:
        int: Valor inteiro digitado pelo usuário.
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('-' * 80)
            print(erro)
            print('-' * 80)


def input_positive_int(msg):
    """Solicita um número inteiro positivo, garantindo que seja maior que zero.

    Args:
        msg (str): Mensagem exibida ao usuário.

    Returns:
        int: Número inteiro positivo fornecido pelo usuário.
    """
    while True:
        valor = input_int(msg)
        if valor > 0:
            return valor
        print('-' * 80)
        print('Digite um valor positivo!')
        print('-' * 80)
