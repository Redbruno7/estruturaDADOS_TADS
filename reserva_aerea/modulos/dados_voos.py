def criar_voos():
    """Cria e retorna a lista inicial de voos disponíveis no sistema.

    Returns:
        list: Lista de dicionários, onde cada dicionário representa um voo.

    Estrutura de cada voo:
        {
            "numero"  (int): Número identificador do voo,
            "origem"  (str): Cidade de origem do voo,
            "destino" (str): Cidade de destino do voo,
            "lugares" (int): Quantidade de lugares disponíveis.
        }

    Comportamento:
        - Esta função é responsável apenas por fornecer os dados iniciais
          que simulam um banco de dados de voos;
        - A lista retornada é utilizada por outros módulos do sistema
          (consultas e reservas);
        - Os voos são fixos, pré-cadastrados, e podem ser modificados
          conforme necessidade de testes.
    """
    return [
        {"numero": 101, "origem": "Juiz De Fora",
            "destino": "São Paulo", "lugares": 5},
        {"numero": 102, "origem": "Juiz De Fora",
            "destino": "Belo Horizonte", "lugares": 3},
        {"numero": 103, "origem": "Rio De Janeiro",
            "destino": "Brasília", "lugares": 8},
        {"numero": 104, "origem": "São Paulo", "destino": "Recife", "lugares": 0},
        {"numero": 105, "origem": "Belo Horizonte",
            "destino": "Salvador", "lugares": 2},
        {"numero": 106, "origem": "Curitiba", "destino": "Fortaleza", "lugares": 6},
        {"numero": 107, "origem": "Brasília", "destino": "Manaus", "lugares": 1},
        {"numero": 108, "origem": "Recife", "destino": "São Paulo", "lugares": 7},
        {"numero": 109, "origem": "Salvador",
            "destino": "Rio De Janeiro", "lugares": 4},
        {"numero": 110, "origem": "Fortaleza",
            "destino": "Curitiba", "lugares": 0},
        {"numero": 111, "origem": "Manaus", "destino": "Recife", "lugares": 3},
        {"numero": 112, "origem": "São Paulo",
            "destino": "Rio De Janeiro", "lugares": 9},
    ]
