from estruturas.arvore import ArvoreBinaria
from funcoes import *

def main():
    """
    Programa principal de demonstração dos algoritmos sobre árvore binária.
    """
    arvore = ArvoreBinaria()

    # Inserindo valores na árvore
    for valor in [10, 5, 15, 3, 7, 12, 18]:
        arvore.inserir(valor)

    print("\n🌳 RESULTADOS DA ÁRVORE BINÁRIA\n")
    print("Soma dos nós nos níveis ímpares:", soma_nos_niveis_impares(arvore.raiz))
    print("Tamanho (não recursivo):", tamanho_nao_recursivo(arvore.raiz))
    print("Pré-Ordem:", pre_ordem_iterativo(arvore.raiz))
    print("Em-Ordem:", em_ordem_iterativo(arvore.raiz))
    print("Pós-Ordem:", pos_ordem_iterativo(arvore.raiz))
    print("Percurso em nível:", percurso_em_nivel(arvore.raiz))
    print("É estritamente binária?", "Sim" if eh_estritamente_binaria(arvore.raiz) else "Não")

if __name__ == "__main__":
    main()
