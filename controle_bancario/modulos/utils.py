def input_int(msg, erro='Entrada inválida! Digite um número inteiro.'):
    """Lê e valida a entrada de um número inteiro fornecido pelo usuário.

    Args:
        msg (str): Mensagem exibida ao solicitar a entrada do usuário.
        erro (str, optional): Mensagem exibida quando ocorre erro de digitação.
            Por padrão, 'Entrada inválida! Tente novamente.'.

    Returns:
        int: Valor inteiro digitado corretamente pelo usuário.

    Comportamento:
        - Exibe uma mensagem solicitando a entrada de um valor inteiro;
        - Caso o usuário digite algo que não seja um número, o programa:
            º Captura a exceção ValueError;
            º Exibe uma mensagem de erro personalizada;
            º Repete a solicitação até uma entrada válida ser fornecida;
        - Retorna o valor inteiro convertido.
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('-' * 80)
            print(erro)
            print('-' * 80)


def input_float(msg, erro='Entrada inálida! Digite um número válido.'):
    """Lê e valida a entrada de um número inteiro fornecido pelo usuário.

    Args:
        msg (str): Mensagem exibida ao solicitar a entrada do usuário.
        erro (str, optional): Mensagem exibida quando ocorre erro de digitação.
            Por padrão, 'Entrada inválida! Tente novamente.'.

    Returns:
        float: Valor em ponto flutuante digitado corretamente pelo usuário.

    Comportamento:
        - Exibe uma mensagem solicitando a entrada de um valor inteiro;
        - Caso o usuário digite algo que não seja um número, o programa:
            º Captura a exceção ValueError;
            º Exibe uma mensagem de erro personalizada;
            º Repete a solicitação até uma entrada válida ser fornecida;
        - Retorna o valor inteiro convertido.
    """
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('-' * 80)
            print(erro)
            print('-' * 80)
