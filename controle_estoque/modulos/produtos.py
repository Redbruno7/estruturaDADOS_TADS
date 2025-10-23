from .utils import input_positive_int


def cadastrar_produtos():
    """Realiza o cadastro inicial dos produtos e seus respectivos estoques.

    Returns:
        tuple[list[int], list[int]]: 
            - Lista de códigos dos produtos (inteiros e únicos);
            - Lista de estoques correspondentes (quantidades inteiras e positivas).

    Funcionamento:
        - São cadastrados 10 produtos;
        - Cada produto é identificado por um código único (sem repetições);
        - O estoque inicial é informado pelo usuário;
        - O índice de ambos os vetores é sincronizado:
            o produto na posição `i` tem seu estoque na mesma posição `i`.
    """
    codigos = []
    estoques = []

    print('=' * 80)
    print('CADASTRO DE PRODUTOS'.center(80))
    print('=' * 80)

    for i in range(1, 11):
        while True:
            codigo = input_positive_int(f'Digite o código do {i}º produto: ')
            if codigo in codigos:
                print('-' * 80)
                print('Código já cadastrado! Digite outro.')
                print('-' * 80)
            else:
                codigos.append(codigo)
                break

        estoque = input_positive_int(
            f'Digite a quantidade em estoque do produto {codigo}: ')
        estoques.append(estoque)

        print('-' * 80)

    print('=' * 80)
    print('Cadastro concluído com sucesso!')
    print('=' * 80)
    print()

    return codigos, estoques
