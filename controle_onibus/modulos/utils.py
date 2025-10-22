def input_int(msg):
    """Lê e valida um número inteiro informado pelo usuário."""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Entrada inválida! Digite um número inteiro.')
            print('-' * 80)


def input_str(msg, permitir_vazio=False):
    """Lê e retorna uma string não vazia."""
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        print('Entrada vazia! Tente novamente.')
        print('-' * 80)
