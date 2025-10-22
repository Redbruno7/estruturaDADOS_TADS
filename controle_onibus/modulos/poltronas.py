def inicializar_poltronas():
    """Cria e retorna duas listas representando as poltronas do ônibus.

    Returns:
        tuple: Duas listas contendo:
            - janela (list[int]): 24 posições com 0 (livre) representando poltronas na janela.
            - corredor (list[int]): 24 posições com 0 (livre) representando poltronas no corredor.

    Observações:
        - Cada posição do vetor representa uma poltrona.
        - O valor 0 indica poltrona livre.
        - O valor 1 indica poltrona ocupada.
    """
    janela = [0] * 24
    corredor = [0] * 24
    return janela, corredor


def exibir_disponiveis(janela, corredor, tipo):
    """Exibe as poltronas disponíveis conforme o tipo escolhido.

    Args:
        janela (list[int]): Lista com as poltronas da janela.
        corredor (list[int]): Lista com as poltronas do corredor.
        tipo (str): 'janela' ou 'corredor', indicando o tipo de poltrona.

    Comportamento:
        - Mostra os números das poltronas livres (valor 0);
        - Caso todas as poltronas estejam ocupadas, exibe uma mensagem informando.
    """
    lista = janela if tipo == 'janela' else corredor
    livres = [i + 1 for i, v in enumerate(lista) if v == 0]

    if livres:
        print(f'Poltronas disponíveis {[tipo]}: {livres}')
    else:
        print(f'Não há poltronas livres no(a) {tipo}.')


def poltronas_disponiveis(janela, corredor):
    """Verifica se ainda existem poltronas livres em qualquer tipo.

    Args:
        janela (list[int]): Lista de poltronas da janela.
        corredor (list[int]): Lista de poltronas do corredor.

    Returns:
        bool: True se houver pelo menos uma poltrona livre, False caso contrário.
    """
    return 0 in janela or 0 in corredor