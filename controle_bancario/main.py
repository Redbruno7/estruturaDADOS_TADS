import os
from modulos.contas import criar_contas
from modulos.operacoes import efetuar_deposito, efetuar_saque, consultar_ativo_bancario


def main():
    """Função principal do sistema de controle bancário.

    Comportamento:
        - Limpa a tela e realiza o cadastro inicial das contas bancárias
          chamando a função `criar_contas()` do módulo `contas`;
        - Armazena os códigos e saldos retornados em duas listas paralelas;
        - Exibe o menu principal com as seguintes opções:
            1. Efetuar depósito
            2. Efetuar saque
            3. Consultar ativo bancário
            4. Sair
        - Direciona o fluxo para as funções correspondentes de acordo
          com a opção selecionada pelo usuário:
            ▪ `efetuar_deposito(codigos, saldos)`
            ▪ `efetuar_saque(codigos, saldos)`
            ▪ `consultar_ativo_bancario(saldos)`
        - Encerra o programa quando a opção “4. Sair” é escolhida;
        - Exibe mensagens informativas e de erro para cada ação inválida.

    Observações:
        - O sistema utiliza limpeza de tela (`os.system('cls')`) para
          manter a interface organizada;
        - As listas `codigos` e `saldos` permanecem ativas durante
          todo o ciclo de execução, refletindo todas as operações realizadas.
    """
    os.system('cls')

    codigos, saldos = criar_contas()
    os.system('cls')

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
            os.system('cls')

            print('-' * 80)
            print('Opção inválida! Tente novamente.')
            print('-' * 80)
            print()


if __name__ == '__main__':
    main()
