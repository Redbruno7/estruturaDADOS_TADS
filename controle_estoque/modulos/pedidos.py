from .utils import input_int, input_positive_int
import os


def processar_pedidos(codigos, estoques):
    """Gerencia o processamento dos pedidos de compra de clientes.

    Args:
        codigos (list[int]): Lista dos códigos de produtos cadastrados.
        estoques (list[int]): Lista com o estoque atual de cada produto.

    Funcionamento:
        - O programa solicita continuamente:
            * Código do cliente (0 encerra o programa);
            * Código do produto desejado;
            * Quantidade solicitada.
        - Para cada pedido:
            * Verifica se o produto existe;
            * Caso exista, verifica se há estoque suficiente;
            * Atualiza o estoque apenas se o pedido puder ser atendido integralmente.
        - Mensagens informativas são exibidas para cada situação.

    O loop encerra quando o código do cliente for igual a 0.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print('=' * 80)
    print('PROCESSAMENTO DE PEDIDOS'.center(80))
    print('=' * 80)

    while True:
        codigo_cliente = input_int('Código do cliente (0 para encerrar): ')
        if codigo_cliente == 0:
            break

        codigo_produto = input_int('Código do produto desejado: ')
        quantidade = input_positive_int('Quantidade desejada: ')

        print('-' * 80)

        # Verifica se o produto existe
        if codigo_produto not in codigos:
            print('Código inexistente.')
            print('-' * 80)
            continue

        indice = codigos.index(codigo_produto)

        # Verifica se há estoque suficiente
        if estoques[indice] < quantidade:
            print('Não temos estoque suficiente desta mercadoria.')
        else:
            estoques[indice] -= quantidade
            print('Pedido atendido. Obrigado e volte sempre!')

        print('-' * 80)

    print('=' * 80)
    print('FIM DO PROCESSAMENTO DE PEDIDOS')
    print('=' * 80)
    print()


def exibir_estoque_atual(codigos, estoques):
    """Exibe o estoque final atualizado de todos os produtos.

    Args:
        codigos (list[int]): Lista de códigos de produtos.
        estoques (list[int]): Lista de estoques correspondentes.

    Exibição:
        - Cada linha mostra o código do produto e o estoque atual;
        - Formatação limpa e alinhada para melhor leitura.
    """
    print('=' * 80)
    print('ESTOQUE FINAL ATUALIZADO'.center(80))
    print('=' * 80)

    for codigo, estoque in zip(codigos, estoques):
        print(f'Produto {codigo:<10} | Estoque: {estoque:>3}')

    print('=' * 80)
    print()
