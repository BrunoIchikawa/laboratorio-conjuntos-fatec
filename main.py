"""
===============================================================================
LABORATÓRIO DE CONJUNTOS - PROGRAMA PRINCIPAL
===============================================================================
Fatec Osasco - Curso: Desenvolvimento de Software Multiplataforma
Disciplina: Matemática Concreta (MC)

Menu interativo didático unificado para demonstração das Partes 1, 2 e 3.
Projetado para facilitar a explicação e demonstração por qualquer membro do grupo!
===============================================================================
"""

import sys
import os
from typing import List

# Garante suporte completo a caracteres matemáticos no terminal Windows
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Garante a importação dos módulos da pasta src
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


def limpar_tela():
    """Limpa o console para manter a interface organizada."""
    pass  # Não limpa para preservar histórico caso o usuário queira copiar logs


def cabecalho(titulo: str):
    print("\n" + "=" * 70)
    print(f" {titulo.center(68)} ")
    print("=" * 70)


def pausar():
    input("\nPressione [ENTER] para continuar...")


# =============================================================================
# FLUXO DA PARTE 1
# =============================================================================

def parse_conjunto_input(texto: str) -> List[Any]:
    """Converte uma entrada de texto como '1, 2, 3' ou 'a, b, c' em lista tratada."""
    texto = texto.strip()
    if not texto or texto.lower() in ['vazio', '{}', '∅', 'none']:
        return []
    partes = [p.strip() for p in texto.split(',') if p.strip()]
    resultado = []
    for p in partes:
        try:
            val = int(p)
        except ValueError:
            try:
                val = float(p)
            except ValueError:
                val = p
        resultado.append(val)
    return remover_duplicatas(resultado)


def menu_parte1():
    while True:
        cabecalho("PARTE 1: TEORIA DOS CONJUNTOS (NÍVEL BÁSICO)")
        print("1. Executar com o Exemplo 1 Oficial (Gabarito do Enunciado)")
        print("2. Executar os Casos de Borda do Exemplo 2 (Gabarito Oficial)")
        print("3. Digitar meus próprios conjuntos A e B manualmente")
        print("0. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            demonstrar_exemplo_1_oficial()
            pausar()
        elif opcao == "2":
            demonstrar_exemplo_2_oficial()
            pausar()
        elif opcao == "3":
            demonstrar_conjuntos_usuario()
            pausar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")


def demonstrar_exemplo_1_oficial():
    cabecalho("EXEMPLO 1: CASO GERAL (OFICIAL DO ENUNCIADO)")
    a_raw = [1, 2, 2, 3, 4]
    b_raw = [3, 4, 5, 6]
    u_raw = list(range(1, 11))
    
    print(f"Entrada Bruta:")
    print(f"  Conjunto A: {a_raw}")
    print(f"  Conjunto B: {b_raw}")
    print(f"  Universo U: 1 a 10")
    
    res = executar_e_comparar_tudo(a_raw, b_raw, u_raw)
    
    A = res["A"]
    B = res["B"]
    
    print(f"\nConjuntos Tratados (duplicatas descartadas):")
    print(f"  A = {formatar_conjunto(A):<30} |A| = {res['card_A']['manual']}")
    print(f"  B = {formatar_conjunto(B):<30} |B| = {res['card_B']['manual']}")
    
    print("\nResultados das Operações:")
    print(f"  A ∪ B = {formatar_conjunto(res['uniao']['manual'])}")
    print(f"  A ∩ B = {formatar_conjunto(res['intersecao']['manual'])}")
    print(f"  A − B = {formatar_conjunto(res['diferenca_A_B']['manual'])}")
    print(f"  B − A = {formatar_conjunto(res['diferenca_B_A']['manual'])}")
    print(f"  A Δ B = {formatar_conjunto(res['diferenca_simetrica']['manual'])}")
    print(f"  Complemento de A em U = {formatar_conjunto(res['complemento_A_em_U']['manual'])}")
    
    print(f"\nPertinência e Inclusão:")
    p3 = "Verdadeiro" if pertence_manual(3, A) else "Falso"
    p5 = "Verdadeiro" if pertence_manual(5, A) else "Falso"
    print(f"  3 ∈ A ? {p3:<15} 5 ∈ A ? {p5}")
    
    sub = [3, 4]
    sub_proprio = "Verdadeiro" if eh_subconjunto_proprio_manual(sub, A) else "Falso"
    sub_comum = "Verdadeiro" if eh_subconjunto_manual(sub, A) else "Falso"
    print(f"  {{3, 4}} ⊆ A ? {sub_comum:<15} {{3, 4}} ⊂ A ? {sub_proprio}")
    
    print("\n" + "-" * 70)
    print("VALIDAÇÃO COM A SOLUÇÃO NATIVA DO PYTHON (set):")
    if res["validacao_geral_confere"]:
        print("  [OK] Todos os resultados manuais coincidem 100% com a solução nativa!")
    else:
        print("  [AVISO] Houve divergência em alguma operação.")
    print("-" * 70)


def demonstrar_exemplo_2_oficial():
    cabecalho("EXEMPLO 2: CASOS DE BORDA (OFICIAL DO ENUNCIADO)")
    
    casos = [
        ("Conjunto vazio", [], [1, 2]),
        ("Conjuntos iguais", [1, 2, 3], [1, 2, 3]),
        ("Conjuntos disjuntos", [1, 2], [3, 4]),
        ("Um contido no outro", [1, 2], [1, 2, 3]),
        ("Repetidos na entrada", [1, 1, 1, 2], [])
    ]
    
    for situacao, a_in, b_in in casos:
        print(f"\n--- Situação: {situacao} ---")
        A = remover_duplicatas(a_in)
        B = remover_duplicatas(b_in)
        print(f"Entrada: A = {formatar_conjunto(A)}, B = {formatar_conjunto(B)}")
        
        if situacao == "Conjunto vazio":
            uniao = formatar_conjunto(uniao_manual(A, B))
            inter = formatar_conjunto(intersecao_manual(A, B))
            sub = "verdadeiro" if eh_subconjunto_manual(A, B) else "falso"
            print(f"Resultado: A ∪ B = {uniao}; A ∩ B = {inter}; A ⊆ B é {sub}")
            
        elif situacao == "Conjuntos iguais":
            dif = formatar_conjunto(diferenca_manual(A, B))
            dif_sim = formatar_conjunto(diferenca_simetrica_manual(A, B))
            sub = "verdadeiro" if eh_subconjunto_manual(A, B) else "falso"
            sub_p = "verdadeiro" if eh_subconjunto_proprio_manual(A, B) else "falso"
            print(f"Resultado: A − B = {dif}; A Δ B = {dif_sim}; A ⊆ B é {sub}; A ⊂ B é {sub_p}")
            
        elif situacao == "Conjuntos disjuntos":
            inter = formatar_conjunto(intersecao_manual(A, B))
            uniao = formatar_conjunto(uniao_manual(A, B))
            dif_sim = formatar_conjunto(diferenca_simetrica_manual(A, B))
            print(f"Resultado: A ∩ B = {inter}; A ∪ B = {uniao}; A Δ B = {dif_sim}")
            
        elif situacao == "Um contido no outro":
            sub_p = "verdadeiro" if eh_subconjunto_proprio_manual(A, B) else "falso"
            sub_b_a = "verdadeiro" if eh_subconjunto_manual(B, A) else "falso"
            dif_ba = formatar_conjunto(diferenca_manual(B, A))
            print(f"Resultado: A ⊂ B é {sub_p}; B ⊆ A é {sub_b_a}; B − A = {dif_ba}")
            
        elif situacao == "Repetidos na entrada":
            print(f"Resultado: A = {formatar_conjunto(A)}; |A| = {cardinalidade_manual(A)}")


def demonstrar_conjuntos_usuario():
    cabecalho("ENTRADA PERSONALIZADA DE CONJUNTOS")
    print("Digite os elementos separados por vírgula (ex: 1, 2, 3 ou a, b, c).")
    raw_a = input("Conjunto A: ")
    raw_b = input("Conjunto B: ")
    raw_u = input("Universo U (pressione enter para 1 a 10): ")
    
    A = parse_conjunto_input(raw_a)
    B = parse_conjunto_input(raw_b)
    U = parse_conjunto_input(raw_u) if raw_u.strip() else list(range(1, 11))
    
    res = executar_e_comparar_tudo(A, B, U)
    
    print(f"\nConjunto A = {formatar_conjunto(res['A'])} (|A| = {res['card_A']['manual']})")
    print(f"Conjunto B = {formatar_conjunto(res['B'])} (|B| = {res['card_B']['manual']})")
    print(f"Universo U  = {formatar_conjunto(res['U'])}")
    
    print("\nOperações (Implementação Manual):")
    print(f"  A ∪ B = {formatar_conjunto(res['uniao']['manual'])}")
    print(f"  A ∩ B = {formatar_conjunto(res['intersecao']['manual'])}")
    print(f"  A − B = {formatar_conjunto(res['diferenca_A_B']['manual'])}")
    print(f"  B − A = {formatar_conjunto(res['diferenca_B_A']['manual'])}")
    print(f"  A Δ B = {formatar_conjunto(res['diferenca_simetrica']['manual'])}")
    print(f"  Complemento de A em U = {formatar_conjunto(res['complemento_A_em_U']['manual'])}")
    print(f"  A ⊆ B ? {'Verdadeiro' if res['A_subconjunto_B']['manual'] else 'Falso'}")
    print(f"  A ⊂ B ? {'Verdadeiro' if res['A_subconjunto_proprio_B']['manual'] else 'Falso'}")
    print(f"\nComparação com solucão nativa: {'CONFIRMADA' if res['validacao_geral_confere'] else 'DIVERGÊNCIA'}")


# =============================================================================
# FLUXO DA PARTE 2
# =============================================================================

def menu_parte2():
    while True:
        cabecalho("PARTE 2: CONJUNTOS NUMÉRICOS (NÍVEL INTERMEDIÁRIO)")
        print("1. Classificar um número qualquer (inteiro, fração, decimal, dízima ou raiz)")
        print("2. Demonstrar o Exemplo Oficial de Dízima Periódica (1,2(5))")
        print("3. Executar a Tabela Completa dos 12 Números do Enunciado")
        print("4. Bônus: Crivo de Eratóstenes (Primos até 30) e Divisores de 36")
        print("0. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            entrada = input("\nDigite um número (ex: 7, -3, 3/4, 0.75, 1,2(5), √9, √2): ").strip()
            try:
                res = classificar_numero(entrada)
                print(f"\nNúmero: {res['entrada']}")
                print(f"Tipo detectado: {res['tipo_detectado']}")
                print(f"Pertence a: {', '.join(res['pertence_a'])}")
                print(f"Não pertence a: {', '.join(res['nao_pertence_a'])}")
                print(f"Justificativa: {res['justificativa']}")
                if res['detalhes_dizima']:
                    d = res['detalhes_dizima']
                    print(f"Fração Geratriz: {d['fracao_geratriz']}")
            except Exception as e:
                print(f"Erro ao processar: {e}")
            pausar()
            
        elif opcao == "2":
            cabecalho("DÍZIMA PERIÓDICA OFICIAL: 1,2(5)")
            res = classificar_numero("1,2(5)")
            d = res["detalhes_dizima"]
            print(f"Entrada: {d['entrada']}")
            print(f"Tipo: {d['tipo_dizima']} (parte não periódica: {d['parte_nao_periodica']}; período: {d['periodo']})")
            print(f"Fração geratriz: {d['fracao_geratriz']}")
            print(f"Pertence a: {', '.join(res['pertence_a'])}")
            print(f"Não pertence a: {', '.join(res['nao_pertence_a'])}")
            pausar()
            
        elif opcao == "3":
            cabecalho("TABELA DE GABARITO COMPLETA (12 NÚMEROS)")
            casos = ["7", "-3", "0", "3/4", "-5/2", "6/3", "0,(3)", "2,(7)", "1,2(5)", "0,(9)", "√9", "√2"]
            print(f"{'Entrada':<10} | {'Pertence a':<16} | {'Observação / Justificativa'}")
            print("-" * 70)
            for c in casos:
                res = classificar_numero(c)
                pert_str = ", ".join(res["pertence_a"])
                print(f"{c:<10} | {pert_str:<16} | {res['justificativa'][:40]}...")
            pausar()
            
        elif opcao == "4":
            cabecalho("BÔNUS: PRIMOS E DIVISORES")
            primos = crivo_de_eratostenes(30)
            divisores = listar_divisores(36)
            print(f"Primos de N até 30: {', '.join(str(p) for p in primos)}")
            print(f"Divisores de 36: {', '.join(str(d) for d in divisores)}")
            pausar()
            
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")


# =============================================================================
# FLUXO DA PARTE 3
# =============================================================================

def menu_parte3():
    while True:
        cabecalho("PARTE 3: INTEGRAÇÃO E MINI-PROJETOS (NÍVEL AVANÇADO)")
        print("1. Opção 1: Recomendação por Interesses (Índice de Jaccard - Gabarito)")
        print("2. Opção 2: Controle de Acesso por Perfis (RBAC - Gabarito)")
        print("3. Opção 3: Produto Cartesiano e Conjunto das Partes (2^n)")
        print("4. Opção 4: Intervalos Reais [2, 5)")
        print("0. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            cabecalho("OPÇÃO 1: RECOMENDAÇÃO POR INTERESSES (ÍNDICE DE JACCARD)")
            interesses = {
                "Ana": ["rock", "jazz", "cinema", "games"],
                "Bia": ["jazz", "cinema", "séries", "viagens"],
                "Caio": ["games", "tecnologia", "cinema"]
            }
            print("Base de Interesses:")
            for nome, itens in interesses.items():
                print(f"  {nome} = {formatar_conjunto(itens)}")
                
            print("\nTabela de Comparação de Pares:")
            print(f"{'Par':<14} | {'Interseção':<22} | {'União':<16} | {'Jaccard'}")
            print("-" * 65)
            
            pares = [("Ana", "Bia"), ("Ana", "Caio"), ("Bia", "Caio")]
            for p1, p2 in pares:
                res = calcular_similaridade_jaccard(interesses[p1], interesses[p2])
                inter_str = f"{formatar_conjunto(res['intersecao'])} ({res['qtd_intersecao']})"
                uniao_str = f"{res['qtd_uniao']} elementos"
                jacc_str = f"{res['jaccard_fracao']} = {res['jaccard_decimal']:.2f}"
                print(f"{p1 + ' e ' + p2:<14} | {inter_str:<22} | {uniao_str:<16} | {jacc_str}")
                
            ranking = recomendar_amigos_para("Ana", interesses)
            print(f"\nResultado esperado: Para a Ana, a recomendação mais forte é o {ranking[0][0]}, o de maior afinidade ({ranking[0][1]}).")
            pausar()
            
        elif opcao == "2":
            cabecalho("OPÇÃO 2: CONTROLE DE ACESSO POR PERFIS (RBAC)")
            rbac = SistemaControleAcesso()
            print("Definição dos Perfis:")
            for p, acoes in rbac.perfis.items():
                print(f"  {p} = {formatar_conjunto(acoes)}")
                
            print("\nCenários de Teste Oficiais:")
            # Cenário 1
            p1 = rbac.obter_permissoes_usuario(["leitor", "editor"])
            print(f"• Usuário com os perfis leitor e editor: permissões = união = {formatar_conjunto(p1)}")
            
            # Cenário 2
            p2 = rbac.obter_permissoes_usuario(["editor", "financeiro"])
            print(f"• Usuário com os perfis editor e financeiro: permissões = {formatar_conjunto(p2)}")
            
            # Cenário 3
            pode = rbac.usuario_pode_executar(["editor", "financeiro"], "excluir")
            print(f"• Esse usuário pode excluir? {'Sim' if pode else 'Não, porque excluir ∉ permissões'}")
            
            # Cenário 4
            ed_sub_admin = "Verdadeiro" if rbac.perfil_esta_contido("editor", "admin") else "Falso"
            fin_sub_admin = "Verdadeiro" if rbac.perfil_esta_contido("financeiro", "admin") else "Falso"
            print(f"• editor ⊆ admin? {ed_sub_admin}. financeiro ⊆ admin? {fin_sub_admin}.")
            pausar()
            
        elif opcao == "3":
            cabecalho("OPÇÃO 3: PRODUTO CARTESIANO E CONJUNTO DAS PARTES (2^n)")
            c1 = ["Tamanho_P", "Tamanho_M"]
            c2 = ["Cor_Azul", "Cor_Preto"]
            prod = produto_cartesiano_manual(c1, c2)
            print(f"A = {c1}")
            print(f"B = {c2}")
            print(f"Produto Cartesiano A × B ({len(prod)} combinações):")
            for par in prod:
                print(f"  {par}")
                
            elem = [1, 2, 3]
            partes = conjunto_das_partes_manual(elem)
            print(f"\nConjunto das Partes P({elem}) - Total: 2^{len(elem)} = {len(partes)} subconjuntos:")
            for sub in partes:
                print(f"  {formatar_conjunto(sub)}")
            pausar()
            
        elif opcao == "4":
            cabecalho("OPÇÃO 4: INTERVALOS REAIS [2, 5)")
            i1 = IntervaloReal(2, 5, fecha_inicio=True, fecha_fim=False)
            print(f"Intervalo 1: {i1}")
            print(f"  2 ∈ [2, 5) ? {'Sim' if i1.contem(2) else 'Não'}")
            print(f"  3.5 ∈ [2, 5) ? {'Sim' if i1.contem(3.5) else 'Não'}")
            print(f"  5 ∈ [2, 5) ? {'Sim' if i1.contem(5) else 'Não'}")
            
            i2 = IntervaloReal(4, 8, fecha_inicio=True, fecha_fim=True)
            print(f"\nIntervalo 2: {i2}")
            inter = i1.intersecao(i2)
            print(f"Interseção [2, 5) ∩ [4, 8] = {inter}")
            pausar()
            
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")


# =============================================================================
# MENU PRINCIPAL
# =============================================================================

def menu_principal():
    while True:
        cabecalho("LABORATÓRIO DE CONJUNTOS - FATEC OSASCO")
        print("Curso: Desenvolvimento de Software Multiplataforma | Matemática Concreta")
        print("Integrantes: Bruno Santos Ichikawa | Geovana Correa dos Santos | Isabela de Sousa Veloso")
        print("-" * 70)
        print("1. Parte 1: Teoria dos Conjuntos (Básico - Operações Manuais vs Nativas)")
        print("2. Parte 2: Conjuntos Numéricos (Intermediário - Classificador & Dízimas)")
        print("3. Parte 3: Mini-projetos (Avançado - Jaccard, RBAC, 2^n, Intervalos)")
        print("4. Executar Bateria de Testes Automatizados (Conferir 100% dos Gabaritos)")
        print("0. Sair do programa")
        print("-" * 70)
        
        opcao = input("Selecione uma opção (0 a 4): ").strip()
        
        if opcao == "1":
            menu_parte1()
        elif opcao == "2":
            menu_parte2()
        elif opcao == "3":
            menu_parte3()
        elif opcao == "4":
            cabecalho("EXECUTANDO TESTES UNITÁRIOS AUTOMATIZADOS")
            os.system(f'"{sys.executable}" -m unittest discover tests')
            pausar()
        elif opcao == "0":
            print("\nEncerrando o Laboratório de Conjuntos. Até mais!\n")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 4.")


if __name__ == "__main__":
    menu_principal()
