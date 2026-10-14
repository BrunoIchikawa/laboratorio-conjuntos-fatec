"""
Testes automatizados para a Parte 2: Conjuntos Numéricos.
Valida todas as 12 entradas da tabela de gabarito, além da dízima periódica e do bônus.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.parte2_numericos import (
    classificar_numero,
    calcular_fracao_geratriz,
    crivo_de_eratostenes,
    listar_divisores
)


class TestParte2Numericos(unittest.TestCase):

    def test_exemplo_dizima_periodica_oficial(self):
        """
        Gabarito do enunciado:
          Entrada: 1,2(5)
          Tipo: dízima periódica (parte não periódica: 2; período: 5)
          Fração geratriz: 113/90
          Pertence a: Q, R
          Não pertence a: N, Z, I
        """
        res = classificar_numero("1,2(5)")
        d = res["detalhes_dizima"]

        self.assertIsNotNone(d)
        self.assertEqual(d["parte_nao_periodica"], "2")
        self.assertEqual(d["periodo"], "5")
        self.assertEqual(d["fracao_geratriz"], "113/90")
        self.assertEqual(res["pertence_a"], ["Q", "R"])
        self.assertEqual(res["nao_pertence_a"], ["N", "Z", "I"])

    def test_tabela_oficial_numeros_sugeridos(self):
        """
        Testa cada uma das 12 entradas da tabela de gabarito:
        | Entrada | Pertence a | Observação |
        | 7       | N, Z, Q, R | Número natural. |
        | −3      | Z, Q, R    | Inteiro negativo, não é natural. |
        | 0       | N, Z, Q, R | Definam no README se N inclui o zero. |
        | 3/4     | Q, R       | Fração equivalente ao decimal exato 0,75. |
        | −5/2    | Q, R       | Fração negativa, equivale a −2,5. |
        | 6/3     | N, Z, Q, R | A fração simplifica para 2. |
        | 0,(3)   | Q, R       | Dízima periódica, fração geratriz 1/3. |
        | 2,(7)   | Q, R       | Dízima periódica, fração geratriz 25/9. |
        | 1,2(5)  | Q, R       | Dízima periódica composta, geratriz 113/90. |
        | 0,(9)   | N, Z, Q, R | Caso curioso: a geratriz é 9/9 = 1. |
        | √9      | N, Z, Q, R | A raiz é exata e vale 3. |
        | √2      | I, R       | Raiz não exata, portanto irracional. |
        """
        casos = [
            ("7", ["N", "Z", "Q", "R"]),
            ("-3", ["Z", "Q", "R"]),
            ("0", ["N", "Z", "Q", "R"]),
            ("3/4", ["Q", "R"]),
            ("-5/2", ["Q", "R"]),
            ("6/3", ["N", "Z", "Q", "R"]),
            ("0,(3)", ["Q", "R"]),
            ("2,(7)", ["Q", "R"]),
            ("1,2(5)", ["Q", "R"]),
            ("0,(9)", ["N", "Z", "Q", "R"]),
            ("√9", ["N", "Z", "Q", "R"]),
            ("√2", ["I", "R"]),
        ]

        for entrada, esperados in casos:
            res = classificar_numero(entrada, n_inclui_zero=True)
            self.assertEqual(
                res["pertence_a"], esperados,
                f"Erro na classificação de {entrada}: esperado {esperados}, obteve {res['pertence_a']}"
            )

    def test_fracoes_geratrizes(self):
        """Verifica os cálculos das frações geratrizes."""
        self.assertEqual(calcular_fracao_geratriz("0,(3)")["fracao_geratriz"], "1/3")
        self.assertEqual(calcular_fracao_geratriz("2,(7)")["fracao_geratriz"], "25/9")
        self.assertEqual(calcular_fracao_geratriz("1,2(5)")["fracao_geratriz"], "113/90")
        self.assertEqual(calcular_fracao_geratriz("0,(9)")["fracao_geratriz"], "1/1")

    def test_bonus_primos_e_divisores(self):
        """
        Gabarito do bônus:
          Primos de N até 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
          Divisores de 36: 1, 2, 3, 4, 6, 9, 12, 18, 36.
        """
        primos_esperados = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        divisores_36_esperados = [1, 2, 3, 4, 6, 9, 12, 18, 36]

        self.assertEqual(crivo_de_eratostenes(30), primos_esperados)
        self.assertEqual(listar_divisores(36), divisores_36_esperados)


if __name__ == '__main__':
    unittest.main()
