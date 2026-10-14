"""
===============================================================================
PARTE 3: INTEGRAÇÃO E MINI-PROJETOS (NÍVEL AVANÇADO)
===============================================================================
Neste módulo, aplicamos a Teoria dos Conjuntos na resolução de problemas reais
do desenvolvimento de software.

Implementamos as 4 opções sugeridas pelo professor:
  1. Sistema de Recomendação Simples (Índice de Similaridade de Jaccard)
  2. Controle de Acesso Baseado em Perfis / RBAC (União e Subconjuntos)
  3. Produto Cartesiano e Conjunto das Partes (Power Set & Análise de 2^n)
  4. Intervalos Reais (Classe Intervalo com União, Interseção e Pertinência)

As Opções 1 e 2 são destacadas com o gabarito oficial do enunciado.
===============================================================================
"""

from typing import Set, Dict, List, Tuple, Any
from src.parte1_conjuntos import (
    uniao_manual,
    intersecao_manual,
    cardinalidade_manual,
    eh_subconjunto_manual,
    pertence_manual
)


# =============================================================================
# OPÇÃO 1: SISTEMA DE RECOMENDAÇÃO (ÍNDICE DE JACCARD)
# =============================================================================

def calcular_similaridade_jaccard(
    interesses_a: List[str],
    interesses_b: List[str]
) -> Dict[str, Any]:
    """
    Calcula a similaridade entre duas pessoas usando o Índice de Jaccard.
    
    O QUE É O ÍNDICE DE JACCARD?
    ---------------------------
    É uma métrica matemática criada por Paul Jaccard para medir o grau de
    afinidade entre dois conjuntos. A fórmula é:
    
                     |A ∩ B|       (Quantos interesses eles têm em COMUM)
      Jaccard(A, B) = ───────   =  ──────────────────────────────────────
                     |A ∪ B|       (Quantos interesses DISTINTOS existem no total)
                     
    - Se não tiverem nada em comum: 0 / Total = 0 (0% de afinidade).
    - Se tiverem exatamente os mesmos interesses: Total / Total = 1 (100% de afinidade).
    """
    intersecao = intersecao_manual(interesses_a, interesses_b)
    uniao = uniao_manual(interesses_a, interesses_b)
    
    qtd_intersecao = cardinalidade_manual(intersecao)
    qtd_uniao = cardinalidade_manual(uniao)
    
    coeficiente = (qtd_intersecao / qtd_uniao) if qtd_uniao > 0 else 0.0
    
    return {
        "intersecao": intersecao,
        "qtd_intersecao": qtd_intersecao,
        "uniao": uniao,
        "qtd_uniao": qtd_uniao,
        "jaccard_fracao": f"{qtd_intersecao}/{qtd_uniao}",
        "jaccard_decimal": round(coeficiente, 2),
        "jaccard_exato": coeficiente
    }


def recomendar_amigos_para(
    alvo: str,
    base_interesses: Dict[str, List[str]]
) -> List[Tuple[str, float, Dict[str, Any]]]:
    """
    Dada uma base de usuários e um usuário-alvo, ranqueia todos os outros
    da maior para a menor afinidade pelo índice de Jaccard.
    """
    if alvo not in base_interesses:
        raise ValueError(f"Usuário {alvo} não encontrado na base!")
        
    interesses_alvo = base_interesses[alvo]
    ranking = []
    
    for outro_usuario, interesses_outro in base_interesses.items():
        if outro_usuario == alvo:
            continue
            
        dados_jaccard = calcular_similaridade_jaccard(interesses_alvo, interesses_outro)
        ranking.append((outro_usuario, dados_jaccard["jaccard_decimal"], dados_jaccard))
        
    # Ordena do maior Jaccard para o menor
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking


# =============================================================================
# OPÇÃO 2: CONTROLE DE ACESSO POR PERFIS (RBAC)
# =============================================================================

class SistemaControleAcesso:
    """
    Sistema de permissões e controle de acesso baseado em Teoria dos Conjuntos.
    
    CONEXÃO COM A TEORIA DOS CONJUNTOS:
    - Cada perfil (ex: leitor, editor, admin) é um CONJUNTO de permissões.
    - Se um usuário recebe 2 perfis, suas permissões totais são a UNIÃO (P1 ∪ P2).
    - Para saber se um perfil 'editor' está contido em 'admin', testamos se
      editor ⊆ admin (SUBCONJUNTO).
    - Para saber se o usuário pode executar uma ação (ex: 'excluir'), testamos
      se 'excluir' ∈ Permissões (PERTINÊNCIA).
    """
    
    def __init__(self, definicao_perfis: Dict[str, List[str]] = None):
        if definicao_perfis is None:
            # Perfis padrão do gabarito oficial
            self.perfis = {
                "leitor": ["ler"],
                "editor": ["ler", "editar"],
                "admin": ["ler", "editar", "excluir", "gerir_usuarios"],
                "financeiro": ["ver_relatorios"]
            }
        else:
            self.perfis = definicao_perfis

    def obter_permissoes_usuario(self, perfis_atribuidos: List[str]) -> List[str]:
        """Calcula o conjunto total de permissões pela UNIÃO dos perfis atribuídos."""
        permissoes_totais = []
        for nome_perfil in perfis_atribuidos:
            if nome_perfil in self.perfis:
                permissoes_totais = uniao_manual(permissoes_totais, self.perfis[nome_perfil])
        return permissoes_totais

    def usuario_pode_executar(self, perfis_atribuidos: List[str], acao: str) -> bool:
        """Verifica se a ação PERTENCE ao conjunto de permissões do usuário (x ∈ P)."""
        permissoes = self.obter_permissoes_usuario(perfis_atribuidos)
        return pertence_manual(acao, permissoes)

    def perfil_esta_contido(self, perfil_origem: str, perfil_destino: str) -> bool:
        """Verifica se perfil_origem é subconjunto de perfil_destino (P1 ⊆ P2)."""
        p1 = self.perfis.get(perfil_origem, [])
        p2 = self.perfis.get(perfil_destino, [])
        return eh_subconjunto_manual(p1, p2)


# =============================================================================
# OPÇÃO 3: PRODUTO CARTESIANO E CONJUNTO DAS PARTES (POWER SET)
# =============================================================================

def produto_cartesiano_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Calcula o produto cartesiano A × B = { (a, b) | a ∈ A e b ∈ B }.
    Cardinalidade: |A × B| = |A| * |B|.
    """
    resultado = []
    for a in conjunto_a:
        for b in conjunto_b:
            resultado.append((a, b))
    return resultado


def conjunto_das_partes_manual(conjunto: List[Any]) -> List[List[Any]]:
    """
    Gera o Conjunto das Partes (Power Set) P(A).
    
    PROPRIEDADE MATEMÁTICA E DESEMPENHO:
    Se um conjunto tem n elementos, o seu conjunto das partes terá exatamente 2^n subconjuntos!
      - n = 3  -> 2^3 = 8 subconjuntos
      - n = 10 -> 2^10 = 1.024 subconjuntos
      - n = 20 -> 2^20 = 1.048.576 subconjuntos
      - n = 30 -> 2^30 = 1.073.741.824 (mais de 1 bilhão!)
    Isso ilustra o crescimento exponencial na complexidade computacional (O(2^n)).
    """
    partes = [[]]
    for elemento in conjunto:
        novas_partes = []
        for subconjunto in partes:
            novas_partes.append(subconjunto + [elemento])
        partes.extend(novas_partes)
    return partes


# =============================================================================
# OPÇÃO 4: INTERVALOS REAIS [a, b)
# =============================================================================

class IntervaloReal:
    """
    Representa um intervalo na reta real, com suporte a limites abertos ou fechados.
    Exemplo: [2, 5) -> 2 <= x < 5.
    """
    def __init__(self, inicio: float, fim: float, fecha_inicio: bool = True, fecha_fim: bool = False):
        if inicio > fim:
            raise ValueError("O início do intervalo não pode ser maior que o fim!")
        self.inicio = inicio
        self.fim = fim
        self.fecha_inicio = fecha_inicio
        self.fecha_fim = fecha_fim

    def contem(self, x: float) -> bool:
        """Verifica se x ∈ Intervalo (pertinência)."""
        maior_que_inicio = (x >= self.inicio) if self.fecha_inicio else (x > self.inicio)
        menor_que_fim = (x <= self.fim) if self.fecha_fim else (x < self.fim)
        return maior_que_inicio and menor_que_fim

    def intersecao(self, outro: 'IntervaloReal') -> 'IntervaloReal':
        """Calcula a interseção entre dois intervalos reais."""
        novo_inicio = max(self.inicio, outro.inicio)
        novo_fim = min(self.fim, outro.fim)
        
        if novo_inicio > novo_fim:
            return None  # Interseção vazia
            
        fecha_ini = self.fecha_inicio if novo_inicio == self.inicio else outro.fecha_inicio
        fecha_f = self.fecha_fim if novo_fim == self.fim else outro.fecha_fim
        return IntervaloReal(novo_inicio, novo_fim, fecha_ini, fecha_f)

    def __repr__(self) -> str:
        esq = "[" if self.fecha_inicio else "("
        dir_ = "]" if self.fecha_fim else ")"
        return f"{esq}{self.inicio}, {self.fim}{dir_}"
