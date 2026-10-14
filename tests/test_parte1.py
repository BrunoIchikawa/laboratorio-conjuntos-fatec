"""
Testes automatizados para a Parte 1: Teoria dos Conjuntos.
Valida o Exemplo 1 (caso geral) e o Exemplo 2 (casos de borda) do gabarito.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.parte1_conjuntos import (
    remover_duplicatas,
    pertence_manual,
    uniao_manual,
    intersecao_manual,
    diferenca_manual,
    diferenca_simetrica_manual,
    eh_subconjunto_manual,
    eh_subconjunto_proprio_manual,
    cardinalidade_manual,
    complemento_manual,
    executar_e_comparar_tudo
)


class TestParte1Conjuntos(unittest.TestCase):

    def test_exemplo_1_caso_geral(self):
        """
        Gabarito do Exemplo 1:
        Entrada:
          Conjunto A: 1, 2, 2, 3, 4
          Conjunto B: 3, 4, 5, 6
          Universo U: 1 a 10
        Saída esperada:
          A = {1, 2, 3, 4}          |A| = 4
          B = {3, 4, 5, 6}          |B| = 4
          A ∪ B = {1, 2, 3, 4, 5, 6}
          A ∩ B = {3, 4}
          A − B = {1, 2}
          B − A = {5, 6}
          A Δ B = {1, 2, 5, 6}
          Complemento de A em U = {5, 6, 7, 8, 9, 10}
          3 ∈ A ? Verdadeiro
          5 ∈ A ? Falso
          {3, 4} ⊆ A ? Verdadeiro
          {3, 4} ⊂ A ? Verdadeiro
        """
        a_raw = [1, 2, 2, 3, 4]
        b_raw = [3, 4, 5, 6]
        u_raw = list(range(1, 11))

        # 1. Limpeza de duplicatas
        A = remover_duplicatas(a_raw)
        B = remover_duplicatas(b_raw)
        U = remover_duplicatas(u_raw)

        self.assertEqual(A, [1, 2, 3, 4])
        self.assertEqual(B, [3, 4, 5, 6])
        self.assertEqual(cardinalidade_manual(A), 4)
        self.assertEqual(cardinalidade_manual(B), 4)

        # 2. Operações
        self.assertEqual(uniao_manual(A, B), [1, 2, 3, 4, 5, 6])
        self.assertEqual(intersecao_manual(A, B), [3, 4])
        self.assertEqual(diferenca_manual(A, B), [1, 2])
        self.assertEqual(diferenca_manual(B, A), [5, 6])
        self.assertEqual(diferenca_simetrica_manual(A, B), [1, 2, 5, 6])
        self.assertEqual(complemento_manual(A, U), [5, 6, 7, 8, 9, 10])

        # 3. Pertinência e Inclusão
        self.assertTrue(pertence_manual(3, A))
        self.assertFalse(pertence_manual(5, A))

        sub = [3, 4]
        self.assertTrue(eh_subconjunto_manual(sub, A))
        self.assertTrue(eh_subconjunto_proprio_manual(sub, A))

        # 4. Comparação com solução nativa
        res = executar_e_comparar_tudo(a_raw, b_raw, u_raw)
        self.assertTrue(res["validacao_geral_confere"])

    def test_exemplo_2_casos_de_borda(self):
        """
        Valida a tabela completa do Exemplo 2: casos de borda.
        """
        # Caso 1: Conjunto vazio: A = ∅, B = {1, 2}
        A1 = []
        B1 = [1, 2]
        self.assertEqual(uniao_manual(A1, B1), [1, 2])
        self.assertEqual(intersecao_manual(A1, B1), [])
        self.assertTrue(eh_subconjunto_manual(A1, B1))

        # Caso 2: Conjuntos iguais: A = B = {1, 2, 3}
        A2 = [1, 2, 3]
        B2 = [1, 2, 3]
        self.assertEqual(diferenca_manual(A2, B2), [])
        self.assertEqual(diferenca_simetrica_manual(A2, B2), [])
        self.assertTrue(eh_subconjunto_manual(A2, B2))
        self.assertFalse(eh_subconjunto_proprio_manual(A2, B2))

        # Caso 3: Conjuntos disjuntos: A = {1, 2}, B = {3, 4}
        A3 = [1, 2]
        B3 = [3, 4]
        self.assertEqual(intersecao_manual(A3, B3), [])
        self.assertEqual(uniao_manual(A3, B3), [1, 2, 3, 4])
        self.assertEqual(diferenca_simetrica_manual(A3, B3), [1, 2, 3, 4])

        # Caso 4: Um contido no outro: A = {1, 2}, B = {1, 2, 3}
        A4 = [1, 2]
        B4 = [1, 2, 3]
        self.assertTrue(eh_subconjunto_proprio_manual(A4, B4))
        self.assertFalse(eh_subconjunto_manual(B4, A4))
        self.assertEqual(diferenca_manual(B4, A4), [3])

        # Caso 5: Repetidos na entrada: A = 1, 1, 1, 2
        A5_raw = [1, 1, 1, 2]
        A5 = remover_duplicatas(A5_raw)
        self.assertEqual(A5, [1, 2])
        self.assertEqual(cardinalidade_manual(A5), 2)


if __name__ == '__main__':
    unittest.main()
