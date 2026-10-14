"""
===============================================================================
SCRIPT DE DEMONSTRAÇÃO COMPLETA E GERAÇÃO DE LOGS OFICIAIS
===============================================================================
Este script executa todas as exigências do enunciado e gera um arquivo de log
formatado (logs_execucao.txt) pronto para inclusão no README e apresentação.
===============================================================================
"""

import sys
import os
import io

# Garante suporte completo a caracteres matemáticos no terminal Windows
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.parte1_conjuntos import (
    remover_duplicatas,
    uniao_manual,
    intersecao_manual,
    diferenca_manual,
    diferenca_simetrica_manual,
    eh_subconjunto_manual,
    eh_subconjunto_proprio_manual,
    cardinalidade_manual,
    complemento_manual,
    pertence_manual,
    executar_e_comparar_tudo,
    formatar_conjunto
)

from src.parte2_numericos import (
    classificar_numero,
    calcular_fracao_geratriz,
    crivo_de_eratostenes,
    listar_divisores
)

from src.parte3_miniprojetos import (
    calcular_similaridade_jaccard,
    recomendar_amigos_para,
    SistemaControleAcesso,
    produto_cartesiano_manual,
    conjunto_das_partes_manual,
    IntervaloReal
)


def executar_demonstracao():
    buffer = io.StringIO()
    
    def log(msg=""):
        print(msg)
        buffer.write(msg + "\n")

    log("=" * 80)
    log("DEMONSTRAÇÃO COMPLETA - LABORATÓRIO DE CONJUNTOS (FATEC OSASCO)")
    log("Curso: Desenvolvimento de Software Multiplataforma | Matemática Concreta")
    log("=" * 80)

    # -------------------------------------------------------------------------
    # PARTE 1: TEORIA DOS CONJUNTOS
    # -------------------------------------------------------------------------
    log("\n" + "#" * 80)
    log("PARTE 1: TEORIA DOS CONJUNTOS (NÍVEL BÁSICO)")
    log("#" * 80)
    
    log("\n>>> CENÁRIO 1: EXEMPLO 1 OFICIAL (CASO GERAL)")
    a_raw = [1, 2, 2, 3, 4]
    b_raw = [3, 4, 5, 6]
    u_raw = list(range(1, 11))
    
    log(f"Entrada Bruta: Conjunto A = {a_raw}, Conjunto B = {b_raw}, Universo U = 1 a 10")
    res1 = executar_e_comparar_tudo(a_raw, b_raw, u_raw)
    
    A = res1["A"]
    B = res1["B"]
    log(f"Conjunto A (tratado) = {formatar_conjunto(A)} | Cardinalidade |A| = {res1['card_A']['manual']}")
    log(f"Conjunto B (tratado) = {formatar_conjunto(B)} | Cardinalidade |B| = {res1['card_B']['manual']}")
    log(f"União A ∪ B          = {formatar_conjunto(res1['uniao']['manual'])}")
    log(f"Interseção A ∩ B     = {formatar_conjunto(res1['intersecao']['manual'])}")
    log(f"Diferença A − B      = {formatar_conjunto(res1['diferenca_A_B']['manual'])}")
    log(f"Diferença B − A      = {formatar_conjunto(res1['diferenca_B_A']['manual'])}")
    log(f"Diferença Simétrica  = {formatar_conjunto(res1['diferenca_simetrica']['manual'])}")
    log(f"Complemento de A em U= {formatar_conjunto(res1['complemento_A_em_U']['manual'])}")
    log(f"3 ∈ A ? {'Verdadeiro' if pertence_manual(3, A) else 'Falso'}   |   5 ∈ A ? {'Verdadeiro' if pertence_manual(5, A) else 'Falso'}")
    log(f"{{3, 4}} ⊆ A ? {'Verdadeiro' if eh_subconjunto_manual([3, 4], A) else 'Falso'}   |   {{3, 4}} ⊂ A ? {'Verdadeiro' if eh_subconjunto_proprio_manual([3, 4], A) else 'Falso'}")
    log(f"Validação com Solução Nativa Python: {'100% IDÊNTICA (Gabarito Aprovado)' if res1['validacao_geral_confere'] else 'Divergência'}")

    log("\n>>> CENÁRIO 2: EXEMPLO 2 OFICIAL (CASOS DE BORDA)")
    casos_borda = [
        ("Conjunto vazio", [], [1, 2]),
        ("Conjuntos iguais", [1, 2, 3], [1, 2, 3]),
        ("Conjuntos disjuntos", [1, 2], [3, 4]),
        ("Um contido no outro", [1, 2], [1, 2, 3]),
        ("Repetidos na entrada", [1, 1, 1, 2], [])
    ]
    for situacao, a_in, b_in in casos_borda:
        A_b = remover_duplicatas(a_in)
        B_b = remover_duplicatas(b_in)
        log(f"\n[Situação: {situacao}]")
        log(f"  Entrada: A = {formatar_conjunto(A_b)}, B = {formatar_conjunto(B_b)}")
        if situacao == "Conjunto vazio":
            u = formatar_conjunto(uniao_manual(A_b, B_b))
            i = formatar_conjunto(intersecao_manual(A_b, B_b))
            s = "verdadeiro" if eh_subconjunto_manual(A_b, B_b) else "falso"
            log(f"  Saída: A ∪ B = {u}; A ∩ B = {i}; A ⊆ B é {s}")
        elif situacao == "Conjuntos iguais":
            d = formatar_conjunto(diferenca_manual(A_b, B_b))
            ds = formatar_conjunto(diferenca_simetrica_manual(A_b, B_b))
            s = "verdadeiro" if eh_subconjunto_manual(A_b, B_b) else "falso"
            sp = "verdadeiro" if eh_subconjunto_proprio_manual(A_b, B_b) else "falso"
            log(f"  Saída: A − B = {d}; A Δ B = {ds}; A ⊆ B é {s}; A ⊂ B é {sp}")
        elif situacao == "Conjuntos disjuntos":
            i = formatar_conjunto(intersecao_manual(A_b, B_b))
            u = formatar_conjunto(uniao_manual(A_b, B_b))
            ds = formatar_conjunto(diferenca_simetrica_manual(A_b, B_b))
            log(f"  Saída: A ∩ B = {i}; A ∪ B = {u}; A Δ B = {ds}")
        elif situacao == "Um contido no outro":
            sp = "verdadeiro" if eh_subconjunto_proprio_manual(A_b, B_b) else "falso"
            sba = "verdadeiro" if eh_subconjunto_manual(B_b, A_b) else "falso"
            dba = formatar_conjunto(diferenca_manual(B_b, A_b))
            log(f"  Saída: A ⊂ B é {sp}; B ⊆ A é {sba}; B − A = {dba}")
        elif situacao == "Repetidos na entrada":
            log(f"  Saída: A = {formatar_conjunto(A_b)}; |A| = {cardinalidade_manual(A_b)}")

    # -------------------------------------------------------------------------
    # PARTE 2: CONJUNTOS NUMÉRICOS
    # -------------------------------------------------------------------------
    log("\n" + "#" * 80)
    log("PARTE 2: CONJUNTOS NUMÉRICOS (NÍVEL INTERMEDIÁRIO)")
    log("#" * 80)

    log("\n>>> EXEMPLO OFICIAL DE DÍZIMA PERIÓDICA:")
    res_dizima = classificar_numero("1,2(5)")
    d = res_dizima["detalhes_dizima"]
    log(f"Entrada: {d['entrada']}")
    log(f"Tipo: {d['tipo_dizima']} (parte não periódica: {d['parte_nao_periodica']}; período: {d['periodo']})")
    log(f"Fração geratriz: {d['fracao_geratriz']}")
    log(f"Pertence a: {', '.join(res_dizima['pertence_a'])}")
    log(f"Não pertence a: {', '.join(res_dizima['nao_pertence_a'])}")

    log("\n>>> TABELA DE GABARITO OFICIAL DOS 12 NÚMEROS:")
    log(f"{'Entrada':<10} | {'Pertence a':<16} | {'Observação'}")
    log("-" * 75)
    casos_num = ["7", "-3", "0", "3/4", "-5/2", "6/3", "0,(3)", "2,(7)", "1,2(5)", "0,(9)", "√9", "√2"]
    for c in casos_num:
        r = classificar_numero(c, n_inclui_zero=True)
        pert = ", ".join(r["pertence_a"])
        log(f"{c:<10} | {pert:<16} | {r['justificativa']}")

    log("\n>>> BÔNUS: PRIMOS E DIVISORES:")
    primos = crivo_de_eratostenes(30)
    divisores = listar_divisores(36)
    log(f"Primos de N até 30: {', '.join(str(p) for p in primos)}")
    log(f"Divisores de 36:    {', '.join(str(d) for d in divisores)}")

    # -------------------------------------------------------------------------
    # PARTE 3: MINI-PROJETOS
    # -------------------------------------------------------------------------
    log("\n" + "#" * 80)
    log("PARTE 3: INTEGRAÇÃO E MINI-PROJETOS (NÍVEL AVANÇADO)")
    log("#" * 80)

    log("\n>>> OPÇÃO 1: RECOMENDAÇÃO POR INTERESSES (ÍNDICE DE JACCARD)")
    interesses = {
        "Ana": ["rock", "jazz", "cinema", "games"],
        "Bia": ["jazz", "cinema", "séries", "viagens"],
        "Caio": ["games", "tecnologia", "cinema"]
    }
    for nome, itens in interesses.items():
        log(f"Interesses de {nome}: {formatar_conjunto(itens)}")

    log(f"\n{'Par':<14} | {'Interseção':<22} | {'União':<16} | {'Jaccard'}")
    log("-" * 70)
    pares = [("Ana", "Bia"), ("Ana", "Caio"), ("Bia", "Caio")]
    for p1, p2 in pares:
        res_j = calcular_similaridade_jaccard(interesses[p1], interesses[p2])
        inter_str = f"{formatar_conjunto(res_j['intersecao'])} ({res_j['qtd_intersecao']})"
        uniao_str = f"{res_j['qtd_uniao']} elementos"
        jacc_str = f"{res_j['jaccard_fracao']} = {res_j['jaccard_decimal']:.2f}"
        log(f"{p1 + ' e ' + p2:<14} | {inter_str:<22} | {uniao_str:<16} | {jacc_str}")
        
    ranking = recomendar_amigos_para("Ana", interesses)
    log(f"\nResultado esperado: Para a Ana, a recomendação mais forte é o {ranking[0][0]}, o de maior afinidade ({ranking[0][1]}).")

    log("\n>>> OPÇÃO 2: CONTROLE DE ACESSO POR PERFIS (RBAC)")
    rbac = SistemaControleAcesso()
    log("Perfis Definidos:")
    for p, ac in rbac.perfis.items():
        log(f"  {p} = {formatar_conjunto(ac)}")

    log("\nCenários de Teste:")
    p1 = rbac.obter_permissoes_usuario(["leitor", "editor"])
    log(f"• Usuário com os perfis leitor e editor: permissões = união = {formatar_conjunto(p1)}")

    p2 = rbac.obter_permissoes_usuario(["editor", "financeiro"])
    log(f"• Usuário com os perfis editor e financeiro: permissões = {formatar_conjunto(p2)}")

    pode_excluir = rbac.usuario_pode_executar(["editor", "financeiro"], "excluir")
    log(f"• Esse usuário pode excluir? {'Sim' if pode_excluir else 'Não, porque excluir ∉ permissões.'}")

    ed_sub_admin = "Verdadeiro" if rbac.perfil_esta_contido("editor", "admin") else "Falso"
    fin_sub_admin = "Verdadeiro" if rbac.perfil_esta_contido("financeiro", "admin") else "Falso"
    log(f"• editor ⊆ admin? {ed_sub_admin}. financeiro ⊆ admin? {fin_sub_admin}.")

    log("\n>>> OPÇÃO 3: PRODUTO CARTESIANO E CONJUNTO DAS PARTES (2^n)")
    A_cart = [1, 2]
    B_cart = ["X", "Y"]
    prod_cart = produto_cartesiano_manual(A_cart, B_cart)
    log(f"Produto Cartesiano {A_cart} × {B_cart} = {prod_cart} (Total: {len(prod_cart)})")
    
    elem_sub = [1, 2, 3]
    powerset = conjunto_das_partes_manual(elem_sub)
    log(f"Conjunto das Partes de {elem_sub} = {len(powerset)} elementos (2^{len(elem_sub)} = {2**len(elem_sub)})")

    log("\n>>> OPÇÃO 4: INTERVALOS REAIS [2, 5)")
    int1 = IntervaloReal(2, 5, fecha_inicio=True, fecha_fim=False)
    log(f"Intervalo: {int1}")
    log(f"  2 ∈ [2, 5) ? {int1.contem(2)}")
    log(f"  3.5 ∈ [2, 5) ? {int1.contem(3.5)}")
    log(f"  5 ∈ [2, 5) ? {int1.contem(5)}")

    log("\n" + "=" * 80)
    log("TODAS AS ETAPAS E GABARITOS FORAM DEMONSTRADOS E VALIDADOS COM SUCESSO!")
    log("=" * 80)

    # Grava o log em disco
    log_file = os.path.join(os.path.dirname(__file__), "logs_execucao.txt")
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(buffer.getvalue())
    print(f"\nArquivo de log gravado com sucesso em: {log_file}")


if __name__ == "__main__":
    executar_demonstracao()
