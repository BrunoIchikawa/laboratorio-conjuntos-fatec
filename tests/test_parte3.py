"""
Testes automatizados para a Parte 3: Mini-projetos.
Valida o gabarito oficial da Opção 1 (Jaccard) e da Opção 2 (Perfis de Acesso).
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.parte3_miniprojetos import (
    calcular_similaridade_jaccard,
    recomendar_amigos_para,
    SistemaControleAcesso,
    produto_cartesiano_manual,
    conjunto_das_partes_manual,
    IntervaloReal
)


class TestParte3MiniProjetos(unittest.TestCase):

    def setUp(self):
        # Base de dados oficial da Opção 1
        self.interesses = {
            "Ana": ["rock", "jazz", "cinema", "games"],
            "Bia": ["jazz", "cinema", "séries", "viagens"],
            "Caio": ["games", "tecnologia", "cinema"]
        }
        self.sistema_rbac = SistemaControleAcesso()

    def test_opcao1_jaccard_tabela_oficial(self):
        """
        Valida a tabela oficial da Opção 1:
        | Par        | Interseção          | União        | Jaccard    |
        | Ana e Bia  | {jazz, cinema} (2)  | 6 elementos  | 2/6 = 0,33 |
        | Ana e Caio | {games, cinema} (2) | 5 elementos  | 2/5 = 0,40 |
        | Bia e Caio | {cinema} (1)        | 6 elementos  | 1/6 = 0,17 |
        """
        # 1. Ana e Bia
        res_ab = calcular_similaridade_jaccard(self.interesses["Ana"], self.interesses["Bia"])
        self.assertEqual(res_ab["qtd_intersecao"], 2)
        self.assertEqual(set(res_ab["intersecao"]), {"jazz", "cinema"})
        self.assertEqual(res_ab["qtd_uniao"], 6)
        self.assertEqual(res_ab["jaccard_decimal"], 0.33)

        # 2. Ana e Caio
        res_ac = calcular_similaridade_jaccard(self.interesses["Ana"], self.interesses["Caio"])
        self.assertEqual(res_ac["qtd_intersecao"], 2)
        self.assertEqual(set(res_ac["intersecao"]), {"games", "cinema"})
        self.assertEqual(res_ac["qtd_uniao"], 5)
        self.assertEqual(res_ac["jaccard_decimal"], 0.40)

        # 3. Bia e Caio
        res_bc = calcular_similaridade_jaccard(self.interesses["Bia"], self.interesses["Caio"])
        self.assertEqual(res_bc["qtd_intersecao"], 1)
        self.assertEqual(set(res_bc["intersecao"]), {"cinema"})
        self.assertEqual(res_bc["qtd_uniao"], 6)
        self.assertEqual(res_bc["jaccard_decimal"], 0.17)

        # 4. Resultado esperado: para a Ana, a recomendação mais forte é o Caio
        ranking_ana = recomendar_amigos_para("Ana", self.interesses)
        melhor_amigo = ranking_ana[0][0]
        self.assertEqual(melhor_amigo, "Caio")

    def test_opcao2_rbac_casos_oficiais(self):
        """
        Valida os 4 casos de teste da Opção 2:
        - Usuário com perfis leitor e editor: permissões = união = {ler, editar}.
        - Usuário com perfis editor e financeiro: permissões = {ler, editar, ver_relatorios}.
        - Esse usuário pode excluir? Não, porque excluir ∉ permissões.
        - editor ⊆ admin? Verdadeiro. financeiro ⊆ admin? Falso.
        """
        # Caso 1: Usuário leitor + editor
        p1 = self.sistema_rbac.obter_permissoes_usuario(["leitor", "editor"])
        self.assertEqual(set(p1), {"ler", "editar"})

        # Caso 2: Usuário editor + financeiro
        p2 = self.sistema_rbac.obter_permissoes_usuario(["editor", "financeiro"])
        self.assertEqual(set(p2), {"ler", "editar", "ver_relatorios"})

        # Caso 3: Esse usuário pode excluir?
        pode_excluir = self.sistema_rbac.usuario_pode_executar(["editor", "financeiro"], "excluir")
        self.assertFalse(pode_excluir)

        # Caso 4: Inclusão de perfis
        self.assertTrue(self.sistema_rbac.perfil_esta_contido("editor", "admin"))
        self.assertFalse(self.sistema_rbac.perfil_esta_contido("financeiro", "admin"))

    def test_opcao3_produto_cartesiano_e_partes(self):
        """Valida o Produto Cartesiano e Conjunto das Partes (2^n)."""
        A = [1, 2]
        B = ["x", "y"]
        prod = produto_cartesiano_manual(A, B)
        self.assertEqual(len(prod), 4)

        partes = conjunto_das_partes_manual([1, 2, 3])
        self.assertEqual(len(partes), 2 ** 3)  # 2^3 = 8

    def test_opcao4_intervalos_reais(self):
        """Valida o Intervalo Real [2, 5) com pertinência e interseção."""
        interv = IntervaloReal(2, 5, fecha_inicio=True, fecha_fim=False)
        self.assertTrue(interv.contem(2))
        self.assertTrue(interv.contem(4.99))
        self.assertFalse(interv.contem(5))
        self.assertFalse(interv.contem(1.99))

        interv2 = IntervaloReal(4, 7, fecha_inicio=True, fecha_fim=True)
        inter = interv.intersecao(interv2)
        self.assertIsNotNone(inter)
        self.assertEqual(inter.inicio, 4)
        self.assertEqual(inter.fim, 5)


if __name__ == '__main__':
    unittest.main()
