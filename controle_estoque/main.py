import os
from modulos.produtos import cadastrar_produtos
from modulos.pedidos import processar_pedidos, exibir_estoque_atual


def main():
    """Função principal do sistema de controle de estoque de mercadorias.

    Descrição geral:
        O programa simula o controle de estoque de uma empresa,
        permitindo o cadastro inicial de produtos e o processamento
        de pedidos de compra feitos por clientes.

    Etapas do funcionamento:
        1. Cadastrar os produtos (código e quantidade em estoque);
        2. Ler e processar pedidos até que o código do cliente seja 0;
        3. Atualizar o estoque somente para pedidos totalmente atendidos;
        4. Exibir o estoque final após o término das operações.

    Observações:
        - Um produto é identificado unicamente pelo seu código;
        - Caso o código informado não exista, o pedido é ignorado;
        - O sistema lida com quantidades inteiras positivas apenas.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    codigos, estoques = cadastrar_produtos()
    processar_pedidos(codigos, estoques)
    exibir_estoque_atual(codigos, estoques)


if __name__ == '__main__':
    main()
