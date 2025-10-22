def input_int(msg, erro='Entrada inválida! Digite um número inteiro.'):
    """_summary_

    Args:
        msg (_type_): _description_
        erro (str, optional): _description_. Defaults to 'Entrada inválida! Digite um número inteiro.'.

    Returns:
        _type_: _description_
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('-' * 80)
            print(erro)
            print('-' * 80)


def input_float(msg, erro='Entrada inálida! Digite um número válido.'):
    """_summary_

    Args:
        msg (_type_): _description_
        erro (str, optional): _description_. Defaults to 'Entrada inálida! Digite um número válido.'.

    Returns:
        _type_: _description_
    """
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('-' * 80)
            print(erro)
            print('-' * 80)
