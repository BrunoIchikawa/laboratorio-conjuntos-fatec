 """
===============================================================================
PARTE 1: TEORIA DOS CONJUNTOS (NÍVEL BÁSICO)
===============================================================================
Este módulo implementa operações fundamentais sobre conjuntos matemáticos.

OBJETIVO DIDÁTICO:
------------------
O desafio proposto pelo professor exige NÃO utilizar os operadores prontos
do Python (como |, &, -, ^, issubset) na implementação principal.
Portanto, implementamos cada operação "na mão" utilizando apenas laços de
repetição (for) e testes condicionais (if).

Para validar e demonstrar o aprendizado, cada operação manual é acompanhada
de sua contraparte que utiliza os recursos nativos do Python (tipo set),
permitindo comparar e comprovar que ambas chegam exatamente ao mesmo resultado.

CONCEITOS EXPLICADOS DE FORMA SIMPLES:
- Conjunto: Uma coleção de elementos únicos (sem repetições).
- Elemento: Um item individual que pode ou não pertencer a um conjunto.
===============================================================================
"""

from typing import List, Any, Set, Tuple, Dict


def remover_duplicatas(lista: List[Any]) -> List[Any]:
    """
    Remove elementos duplicados de uma lista, preservando a primeira ocorrência.
    
    Por que isso é necessário?
    Na matemática, um conjunto NÃO possui elementos repetidos.
    Se o usuário digitar '1, 2, 2, 3, 4', o conjunto real é '{1, 2, 3, 4}'.
    
    Como funciona:
    1. Criamos uma nova lista vazia chamada 'unicos'.
    2. Percorremos cada item da lista original.
    3. Se o item ainda não estiver em 'unicos', nós o colocamos lá.
    4. Ao final, retornamos a lista contendo apenas itens únicos.
    """
    unicos = []
    for item in lista:
        if not pertence_manual(item, unicos):
            unicos.append(item)
    return unicos


def ordenar_elementos(lista: List[Any]) -> List[Any]:
    """
    Ordena os elementos para apresentação visual organizada.
    Se forem números, ordena numericamente (ex: 5 vem antes de 10).
    Se forem strings, ordena alfabeticamente.
    """
    def chave(x):
        try:
            return (0, float(x))
        except (ValueError, TypeError):
            return (1, str(x))
    return sorted(lista, key=chave)


# =============================================================================
# OPERAÇÃO 1: PERTINÊNCIA (x ∈ A)
# =============================================================================

def pertence_manual(elemento: Any, conjunto: List[Any]) -> bool:
    """
    Verifica se um elemento pertence a um conjunto (x ∈ A).
    
    Explicação para leigos:
    Imagine que você tem uma caixa com vários objetos etiquetados.
    Para saber se um objeto específico está na caixa, você olha um por um.
    Se achar, responde Verdadeiro (True).
    Se olhar todos e não achar, responde Falso (False).
    """
    for item in conjunto:
        if item == elemento:
            return True
    return False


def pertence_nativo(elemento: Any, conjunto: Set[Any]) -> bool:
    """Solução nativa do Python usando o operador 'in'."""
    return elemento in conjunto


# =============================================================================
# OPERAÇÃO 2: UNIÃO (A ∪ B)
# =============================================================================

def uniao_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
    """
    Calcula a união entre dois conjuntos (A ∪ B).
    
    Definição Matemática:
    A ∪ B = { x | x ∈ A ou x ∈ B }
    (Todos os elementos que estão em A, em B ou em ambos).
    
    Como funciona o passo a passo:
    1. Começamos com uma lista vazia chamada 'resultado'.
    2. Copiamos todos os elementos de A para 'resultado' (sem duplicar).
    3. Percorremos cada elemento de B:
       - Se ele já estiver no 'resultado', ignoramos.
       - Se ele NÃO estiver no 'resultado', adicionamos.
    4. Retornamos a lista com todos os elementos reunidos.
    """
    resultado = []
    
    # Adiciona os elementos de A
    for item in conjunto_a:
        if not pertence_manual(item, resultado):
            resultado.append(item)
            
    # Adiciona os elementos de B que ainda não estão no resultado
    for item in conjunto_b:
        if not pertence_manual(item, resultado):
            resultado.append(item)
            
    return ordenar_elementos(resultado)


def uniao_nativa(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
    """Solução nativa do Python usando o operador | ou union()."""
    return conjunto_a.union(conjunto_b)


# =============================================================================
# OPERAÇÃO 3: INTERSEÇÃO (A ∩ B)
# =============================================================================

def intersecao_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
    """
    Calcula a interseção entre dois conjuntos (A ∩ B).
    
    Definição Matemática:
    A ∩ B = { x | x ∈ A e x ∈ B }
    (Apenas os elementos que estão presentes SIMULTANEAMENTE em A e em B).
    
    Como funciona o passo a passo:
    1. Começamos com uma lista vazia chamada 'resultado'.
    2. Percorremos cada elemento de A.
    3. Para cada elemento de A, perguntamos: "Ele também está em B?"
       - Se SIM, nós o colocamos em 'resultado' (caso ainda não esteja lá).
       - Se NÃO, não fazemos nada.
    4. Retornamos 'resultado'.
    """
    resultado = []
    for item in conjunto_a:
        if pertence_manual(item, conjunto_b) and not pertence_manual(item, resultado):
            resultado.append(item)
            
    return ordenar_elementos(resultado)


def intersecao_nativa(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
    """Solução nativa do Python usando o operador & ou intersection()."""
    return conjunto_a.intersection(conjunto_b)


# =============================================================================
# OPERAÇÃO 4: DIFERENÇA (A − B e B − A)
# =============================================================================

def diferenca_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
    """
    Calcula a diferença entre A e B (A − B).
    
    Definição Matemática:
    A − B = { x | x ∈ A e x ∉ B }
    (Elementos que pertencem a A, mas NÃO pertencem a B).
    
    Como funciona o passo a passo:
    1. Criamos a lista 'resultado'.
    2. Percorremos cada item de A.
    3. Se o item NÃO estiver presente em B, ele entra no 'resultado'.
    """
    resultado = []
    for item in conjunto_a:
        if not pertence_manual(item, conjunto_b) and not pertence_manual(item, resultado):
            resultado.append(item)
            
    return ordenar_elementos(resultado)


def diferenca_nativa(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
    """Solução nativa do Python usando o operador - ou difference()."""
    return conjunto_a.difference(conjunto_b)


# =============================================================================
# OPERAÇÃO 5: DIFERENÇA SIMÉTRICA (A Δ B)
# =============================================================================

def diferenca_simetrica_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> List[Any]:
    """
    Calcula a diferença simétrica entre A e B (A Δ B).
    
    Definição Matemática:
    A Δ B = (A − B) ∪ (B − A)
    (Elementos que estão em A OU em B, mas NÃO em ambos).
    
    Como funciona o passo a passo:
    1. Pegamos os elementos exclusivos de A (calculando A − B).
    2. Pegamos os elementos exclusivos de B (calculando B − A).
    3. Juntamos (unimos) esses dois grupos.
    """
    apenas_a = diferenca_manual(conjunto_a, conjunto_b)
    apenas_b = diferenca_manual(conjunto_b, conjunto_a)
    return uniao_manual(apenas_a, apenas_b)


def diferenca_simetrica_nativa(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> Set[Any]:
    """Solução nativa do Python usando o operador ^ ou symmetric_difference()."""
    return conjunto_a.symmetric_difference(conjunto_b)


# =============================================================================
# OPERAÇÃO 6: INCLUSÃO - SUBCONJUNTO (A ⊆ B) e SUBCONJUNTO PRÓPRIO (A ⊂ B)
# =============================================================================

def eh_subconjunto_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> bool:
    """
    Verifica se A é subconjunto de B (A ⊆ B).
    
    Definição Matemática:
    Para todo x, se x ∈ A então x ∈ B.
    (Todos os elementos de A estão contidos em B. A pode ser igual a B).
    
    Como funciona o passo a passo:
    1. Olhamos cada elemento de A.
    2. Se encontrarmos QUALQUER elemento de A que NÃO esteja em B,
       já sabemos imediatamente que A não está contido em B. Retornamos False.
    3. Se o laço terminar e todos os elementos de A estavam em B, retornamos True.
    * Nota: O conjunto vazio (∅) é subconjunto de qualquer conjunto!
    """
    for item in conjunto_a:
        if not pertence_manual(item, conjunto_b):
            return False
    return True


def eh_subconjunto_proprio_manual(conjunto_a: List[Any], conjunto_b: List[Any]) -> bool:
    """
    Verifica se A é subconjunto próprio de B (A ⊂ B).
    
    Definição Matemática:
    A ⊆ B E A ≠ B.
    (Todos os elementos de A estão em B, MAS B tem pelo menos um elemento a mais).
    
    Como funciona:
    1. Primeiro verifica se A ⊆ B (todos de A estão em B).
    2. Depois verifica se a quantidade de elementos de A é menor que a de B.
       Se for menor, significa que B tem elementos que A não tem.
    """
    esta_contido = eh_subconjunto_manual(conjunto_a, conjunto_b)
    eh_estritamente_menor = cardinalidade_manual(conjunto_a) < cardinalidade_manual(conjunto_b)
    return esta_contido and eh_estritamente_menor


def eh_subconjunto_nativo(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> bool:
    """Solução nativa usando issubset() ou <=."""
    return conjunto_a.issubset(conjunto_b)


def eh_subconjunto_proprio_nativo(conjunto_a: Set[Any], conjunto_b: Set[Any]) -> bool:
    """Solução nativa usando operador < (estritamente menor)."""
    return conjunto_a < conjunto_b


# =============================================================================
# OPERAÇÃO 7: CARDINALIDADE (|A|)
# =============================================================================

def cardinalidade_manual(conjunto: List[Any]) -> int:
    """
    Calcula a quantidade de elementos únicos de um conjunto (|A|).
    
    Como funciona:
    1. Garantimos que não haja itens repetidos.
    2. Contamos os elementos usando um contador simples iniciado em 0.
    """
    unicos = remover_duplicatas(conjunto)
    contador = 0
    for _ in unicos:
        contador += 1
    return contador


def cardinalidade_nativa(conjunto: Set[Any]) -> int:
    """Solução nativa usando len()."""
    return len(conjunto)


# =============================================================================
# OPERAÇÃO 8: COMPLEMENTO DE A EM RELAÇÃO AO UNIVERSO U
# =============================================================================

def complemento_manual(conjunto_a: List[Any], conjunto_universo: List[Any]) -> List[Any]:
    """
    Calcula o complemento de A em relação ao Universo U (U − A ou Aᶜ).
    
    Definição Matemática:
    Tudo que pertence ao universo U, mas NÃO pertence ao conjunto A.
    
    Como funciona:
    É exatamente a diferença entre o Universo e o conjunto A: U − A.
    """
    return diferenca_manual(conjunto_universo, conjunto_a)


def complemento_nativo(conjunto_a: Set[Any], conjunto_universo: Set[Any]) -> Set[Any]:
    """Solução nativa usando U.difference(A)."""
    return conjunto_universo.difference(conjunto_a)


# =============================================================================
# FUNÇÃO DE COMPARAÇÃO E VALIDAÇÃO (MANUAL VS NATIVO)
# =============================================================================

def executar_e_comparar_tudo(
    a_raw: List[Any],
    b_raw: List[Any],
    u_raw: List[Any],
    teste_elemento_pertence: Any = None,
    teste_subconjunto: List[Any] = None
) -> Dict[str, Any]:
    """
    Executa todas as operações de teoria dos conjuntos utilizando TANTO a
    implementação manual QUANTO a solução nativa do Python, comparando
    os resultados lado a lado para garantir que o gabarito confere 100%.
    """
    # 1. Tratamento das entradas (remover duplicatas)
    A_list = remover_duplicatas(a_raw)
    B_list = remover_duplicatas(b_raw)
    U_list = remover_duplicatas(u_raw)
    
    A_set = set(A_list)
    B_set = set(B_list)
    U_set = set(U_list)
    
    # 2. Execuções Manuais
    res_uniao_man = uniao_manual(A_list, B_list)
    res_inter_man = intersecao_manual(A_list, B_list)
    res_dif_ab_man = diferenca_manual(A_list, B_list)
    res_dif_ba_man = diferenca_manual(B_list, A_list)
    res_dif_sim_man = diferenca_simetrica_manual(A_list, B_list)
    res_comp_man = complemento_manual(A_list, U_list)
    card_a_man = cardinalidade_manual(A_list)
    card_b_man = cardinalidade_manual(B_list)
    
    # Inclusões (A em B e subconjunto de teste em A)
    a_sub_b_man = eh_subconjunto_manual(A_list, B_list)
    a_proprio_b_man = eh_subconjunto_proprio_manual(A_list, B_list)
    
    # 3. Execuções Nativas
    res_uniao_nat = ordenar_elementos(list(uniao_nativa(A_set, B_set)))
    res_inter_nat = ordenar_elementos(list(intersecao_nativa(A_set, B_set)))
    res_dif_ab_nat = ordenar_elementos(list(diferenca_nativa(A_set, B_set)))
    res_dif_ba_nat = ordenar_elementos(list(diferenca_nativa(B_set, A_set)))
    res_dif_sim_nat = ordenar_elementos(list(diferenca_simetrica_nativa(A_set, B_set)))
    res_comp_nat = ordenar_elementos(list(complemento_nativo(A_set, U_set)))
    card_a_nat = cardinalidade_nativa(A_set)
    card_b_nat = cardinalidade_nativa(B_set)
    
    a_sub_b_nat = eh_subconjunto_nativo(A_set, B_set)
    a_proprio_b_nat = eh_subconjunto_proprio_nativo(A_set, B_set)
    
    # 4. Verificação de correspondência
    iguais = (
        res_uniao_man == res_uniao_nat and
        res_inter_man == res_inter_nat and
        res_dif_ab_man == res_dif_ab_nat and
        res_dif_ba_man == res_dif_ba_nat and
        res_dif_sim_man == res_dif_sim_nat and
        res_comp_man == res_comp_nat and
        card_a_man == card_a_nat and
        card_b_man == card_b_nat and
        a_sub_b_man == a_sub_b_nat and
        a_proprio_b_man == a_proprio_b_nat
    )
    
    return {
        "A": A_list,
        "B": B_list,
        "U": U_list,
        "card_A": {"manual": card_a_man, "nativo": card_a_nat},
        "card_B": {"manual": card_b_man, "nativo": card_b_nat},
        "uniao": {"manual": res_uniao_man, "nativo": res_uniao_nat},
        "intersecao": {"manual": res_inter_man, "nativo": res_inter_nat},
        "diferenca_A_B": {"manual": res_dif_ab_man, "nativo": res_dif_ab_nat},
        "diferenca_B_A": {"manual": res_dif_ba_man, "nativo": res_dif_ba_nat},
        "diferenca_simetrica": {"manual": res_dif_sim_man, "nativo": res_dif_sim_nat},
        "complemento_A_em_U": {"manual": res_comp_man, "nativo": res_comp_nat},
        "A_subconjunto_B": {"manual": a_sub_b_man, "nativo": a_sub_b_nat},
        "A_subconjunto_proprio_B": {"manual": a_proprio_b_man, "nativo": a_proprio_b_nat},
        "validacao_geral_confere": iguais
    }


def formatar_conjunto(conjunto: List[Any]) -> str:
    """Formata visualmente uma lista no estilo matemático: {1, 2, 3} ou ∅ para vazio."""
    if not conjunto:
        return "∅"
    itens = ", ".join(str(x) for x in conjunto)
    return f"{{{itens}}}"
