import os
from .pilha import Pilha

def chega_no_deposito(pNova, pilhaA, pilhaB, pilhaC):
    """Gerencia o empilhamento decrescente de caixas no depósito.

    Args:
        pNova (int): Peso da nova caixa a ser empilhada (7, 5 ou 3 toneladas).
        pilhaA (Pilha): Pilha principal, onde as caixas são armazenadas.
        pilhaB (Pilha): Pilha auxiliar destinada a caixas de 5 toneladas.
        pilhaC (Pilha): Pilha auxiliar destinada a caixas de 3 toneladas.

    Comportamento:
        - Se a nova caixa tiver peso maior que a do topo da pilha A,
          todas as caixas menores são temporariamente movidas para pilhas auxiliares;
        - Após abrir espaço, a nova caixa é empilhada em A;
        - Em seguida, as caixas removidas são retornadas à pilha principal (A);
        - A operação mantém o empilhamento em ordem decrescente (7 > 5 > 3).

    Exemplo:
        Entrada de caixas em sequência: 3, 5, 7
        Resultado final da pilha A: [7, 5, 3]
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * 80)
    print(f"CHEGOU UMA NOVA CAIXA DE {pNova} TONELADAS".center(80))
    print('=' * 80)

    # Move caixas menores para pilhas auxiliares
    while not pilhaA.vazia() and pilhaA.topo() < pNova:
        caixa = pilhaA.desempilhar()

        if caixa == 5:
            pilhaB.empilhar(caixa)
            print(f"Movendo caixa {caixa}t → Pilha B (5t)")
        elif caixa == 3:
            pilhaC.empilhar(caixa)
            print(f"Movendo caixa {caixa}t → Pilha C (3t)")

    # Empilha a nova caixa
    pilhaA.empilhar(pNova)
    print(f"Empilhando caixa {pNova}t → Pilha A")

    # Retorna as caixas das pilhas auxiliares
    while not pilhaB.vazia():
        caixa = pilhaB.desempilhar()
        pilhaA.empilhar(caixa)
        print(f"Retornando caixa {caixa}t → Pilha A")

    while not pilhaC.vazia():
        caixa = pilhaC.desempilhar()
        pilhaA.empilhar(caixa)
        print(f"Retornando caixa {caixa}t → Pilha A")

    print('-' * 80)
    print(f"Pilha A atual: {pilhaA.itens}")
    print('-' * 80)
    input("\nPressione ENTER para continuar...")
