import os
from modulos.contas import criar_contas
from modulos.operacoes import efetuar_deposito, efetuar_saque, consultar_ativo_bancario


def main():

    os.system('cls')

    codigos, saldos = criar_contas()

    while True:
        print('=' * 80)
        print('MENU PRINCIPAL - CONTROLE BANCÁRIO'.center(80))
        print('=' * 80)
        print('1. Efetuar depósito')
        print('2. Efetuar saque')
        print('3. Consultar ativo bancário')
        print('4. Sair')
        print('-' * 80)

        opcao = input('Escolha uma opção: (1-4): ')

        if opcao == '1':
            efetuar_deposito(codigos, saldos)
        elif opcao == '2':
            efetuar_saque(codigos, saldos)
        elif opcao == '3':
            consultar_ativo_bancario(saldos)
        elif opcao == '4':
            print('-' * 80)
            print('Sistema encerrado.')
            print('=' * 80)
            print()
            break
        else:
            print('-' * 80)
            print('Opção inválida! Tente novamente.')
            print('-' * 80)


if __name__ == '__main__':
    main()