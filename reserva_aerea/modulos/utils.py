def input_int(msg, erro='Entrada inválida! Tente novamente.'):
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


def input_str(msg, permitir_vazio=False):
    """Lê e valida a entrada de uma string fornecida pelo usuário.

    Args:
        msg (str): Mensagem exibida ao solicitar a entrada do usuário.
        permitir_vazio (bool, optional): Define se é permitido retornar
            uma string vazia. Padrão é False.

    Returns:
        str: Texto digitado pelo usuário, com formatação em Title Case.

    Comportamento:
        - Exibe uma mensagem solicitando a entrada de texto;
        - Remove espaços extras no início e fim (strip);
        - Caso o campo seja obrigatório e o usuário pressione Enter sem digitar nada:
            º Exibe uma mensagem de erro e solicita novamente;
        - Caso seja permitido campo vazio (`permitir_vazio=True`), retorna vazio;
        - O texto retornado é formatado com a primeira letra maiúscula
          (usando o método `.title()`).
    """
    while True:
        valor = input(msg).strip()

        if valor or permitir_vazio:
            return valor.title()

        print('-' * 80)
        print('Entrada inválida! Tente novamente.')
        print('-' * 80)
