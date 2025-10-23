# Pacote 'funcoes'
# Reúne os percursos e operações sobre a árvore binária.

from .percursos import (
    pre_ordem_iterativo,
    em_ordem_iterativo,
    pos_ordem_iterativo,
    percurso_em_nivel
)

from .propriedades import (
    soma_nos_niveis_impares,
    tamanho_nao_recursivo,
    eh_estritamente_binaria
)
