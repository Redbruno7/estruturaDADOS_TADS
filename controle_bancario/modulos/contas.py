def criar_contas():
    """_summary_

    Returns:
        _type_: _description_
    """
    codigos = []
    saldos = []

    print('=' * 80)
    print('CADASTRO INICIAL DE CONTAS'.center(80))
    print('=' * 80)

    for i in range(10):
        while True:
            try:
                codigo = int(input(f'Digite o código da {i+1}ª conta: '))
                print('-' * 80)

                if codigo in codigos:
                    print('Código já cadastrado! Tente novamente.')
                    print('-' * 80)
                elif codigo <= 0:
                    print('Entrada inválida! Digite apenas números inteiros positivos.')
                    print('-' * 80)
                else:
                    codigos.append(codigo)
                    break
            except ValueError:
                print('-' * 80)
                print('Entrada inválida! Digite apenas números inteiros positivos.')
                print('-' * 80)

        while True:
            try:
                saldo = float(input(f'Digite o saldo inicial da conta {codigo}: '))
                print('-' * 80)

                if saldo < 0:
                    print('Saldo não pode ser negativo.')
                    print('-' * 80)
                else:
                    saldos.append(saldo)
                    print('=' * 80)
                    break
            except ValueError:
                print('-' * 80)
                print('Entrada inválida! Digite um valor numérico.')
                print('-' * 80)

    return codigos, saldos