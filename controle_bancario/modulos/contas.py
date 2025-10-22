def criar_contas():
    """Realiza o cadastro inicial das contas bancárias e seus respectivos saldos.

    Returns:
        tuple: Duas listas paralelas contendo:
            - codigos (list[int]): Lista com os códigos numéricos das contas;
            - saldos (list[float]): Lista com os saldos correspondentes a cada conta.

    Comportamento:
        - Solicita ao usuário o cadastro de um número fixo de contas (definido pelo `range`);
        - Para cada conta:
            º Solicita o código numérico e valida se é positivo e não duplicado;
            º Solicita o saldo inicial e valida se não é negativo;
        - Cada conta e seu respectivo saldo são armazenados na mesma posição
          nas listas `codigos` e `saldos`, mantendo a correspondência direta;
        - Retorna as duas listas para serem utilizadas pelas operações do sistema bancário.

    Observações:
        - Caso o usuário insira dados inválidos, o sistema exibe mensagens de erro
          e solicita nova entrada até receber valores válidos.
    """
    codigos = []
    saldos = []

    print('=' * 80)
    print('CADASTRO INICIAL DE CONTAS'.center(80))

    for i in range(10):
        while True:
            try:
                print('=' * 80)
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
                saldo = float(
                    input(f'Digite o saldo inicial da conta {codigo}: '))

                if saldo < 0:
                    print('Saldo não pode ser negativo.')
                    print('-' * 80)
                else:
                    saldos.append(saldo)
                    print('=' * 80)
                    print()
                    break
            except ValueError:
                print('-' * 80)
                print('Entrada inválida! Digite um valor numérico.')
                print('-' * 80)

    return codigos, saldos
