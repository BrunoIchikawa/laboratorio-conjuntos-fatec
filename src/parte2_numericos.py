"""
===============================================================================
PARTE 2: CONJUNTOS NUMÉRICOS (NÍVEL INTERMEDIÁRIO)
===============================================================================
Este módulo implementa a classificação de números nos conjuntos fundamentais:
  - N (Naturais): Números de contagem {0, 1, 2, 3, ...}
  - Z (Inteiros): Naturais e seus opostos negativos {..., -2, -1, 0, 1, 2, ...}
  - Q (Racionais): Qualquer número que pode ser escrito como fração a/b (b ≠ 0)
  - I (Irracionais): Números com infinitas casas decimais NÃO periódicas (ex: √2, π)
  - R (Reais): União de todos os Racionais e Irracionais (Q ∪ I)

RECURSOS ADICIONAIS IMPLEMENTADOS:
1. Identificador de dízimas periódicas e cálculo didático da Fração Geratriz.
2. Suporte a frações (a/b), decimais exatos (com vírgula ou ponto) e raízes (√n).
3. Bônus: Crivo de Eratóstenes (números primos) e listagem dos divisores de um número.
===============================================================================
"""

import math
import re
from typing import Dict, Any, List, Tuple


def mdc_manual(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) usando o Algoritmo de Euclides.
    
    Explicação didática:
    Para simplificar uma fração como 25/9 ou 6/3, precisamos achar o maior
    número que divide tanto o numerador quanto o denominador.
    O método de Euclides é simples: vamos dividindo e pegando o resto até
    o resto ser zero.
    """
    a = abs(a)
    b = abs(b)
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a if a != 0 else 1


def simplificar_fracao(numerador: int, denominador: int) -> Tuple[int, int]:
    """
    Simplifica uma fração para a sua forma irredutível.
    Exemplo: 6/3 -> 2/1; 9/9 -> 1/1.
    """
    if denominador == 0:
        raise ValueError("O denominador não pode ser zero!")
    
    # Se o denominador for negativo, passa o sinal para o numerador
    if denominador < 0:
        numerador = -numerador
        denominador = -denominador
        
    divisor_comum = mdc_manual(numerador, denominador)
    return (numerador // divisor_comum, denominador // divisor_comum)


# =============================================================================
# FRAÇÃO GERATRIZ DE DÍZIMAS PERIÓDICAS
# =============================================================================

def eh_dizima_periodica_str(texto: str) -> bool:
    """
    Verifica se a string representa uma dízima periódica com parênteses.
    Exemplos aceitos:
      - '0,(3)' ou '0.(3)' -> período é 3
      - '1,2(5)' ou '1.2(5)' -> parte não periódica é 2, período é 5
      - '2,(7)' -> período é 7
      - '0,(9)' -> período é 9
    """
    texto = texto.strip()
    padrao = r'^[+-]?\d+([,\.]\d*)?\(\d+\)$'
    return bool(re.match(padrao, texto))


def calcular_fracao_geratriz(texto_dizima: str) -> Dict[str, Any]:
    """
    Calcula a fração geratriz de uma dízima periódica passo a passo.
    
    COMO FUNCIONA O MÉTODO ALGÉBRICO (O mesmo ensinado no Ensino Fundamental):
    Exemplo para '1,2(5)':
      Queremos achar x = 1,25555...
      
      1) Identificamos as partes:
         - Sinal: positivo (+)
         - Parte inteira (I): 1
         - Parte decimal não periódica / anti-período (N): '2' (tem k = 1 dígito)
         - Período (P): '5' (tem p = 1 dígito)
         
      2) Multiplicamos x por 10^(k + p) para a vírgula pular o período:
         10^(1+1) * x = 100x = 125,5555...  (Equação 1)
         
      3) Multiplicamos x por 10^k para a vírgula ficar na frente do período:
         10^1 * x = 10x = 12,5555...        (Equação 2)
         
      4) Subtraímos a Equação 2 da Equação 1 (a parte infinita se cancela!):
         100x - 10x = 125 - 12
         90x = 113
         x = 113 / 90
         
      5) Simplificamos a fração calculando o MDC:
         MDC(113, 90) = 1, logo a fração é 113/90.
    """
    s = texto_dizima.strip().replace(',', '.')
    eh_negativo = s.startswith('-')
    if s.startswith('+') or s.startswith('-'):
        s = s[1:]
        
    partes = s.split('(')
    antes_parenteses = partes[0]
    periodo_str = partes[1].replace(')', '')
    
    if '.' in antes_parenteses:
        inteiro_str, antiperiodo_str = antes_parenteses.split('.')
    else:
        inteiro_str = antes_parenteses
        antiperiodo_str = ''
        
    k = len(antiperiodo_str)    # quantidade de dígitos não periódicos
    p = len(periodo_str)        # quantidade de dígitos do período
    
    # Valor com vírgula deslocada após o primeiro período
    val1 = int(inteiro_str + antiperiodo_str + periodo_str)
    # Valor com vírgula deslocada antes do período
    val2 = int(inteiro_str + antiperiodo_str) if (inteiro_str + antiperiodo_str) else 0
    
    numerador = val1 - val2
    denominador = (10 ** (k + p)) - (10 ** k)
    
    if eh_negativo:
        numerador = -numerador
        
    num_simp, den_simp = simplificar_fracao(numerador, denominador)
    
    return {
        "entrada": texto_dizima,
        "parte_inteira": inteiro_str,
        "parte_nao_periodica": antiperiodo_str if antiperiodo_str else "nenhuma",
        "periodo": periodo_str,
        "numerador_bruto": numerador,
        "denominador_bruto": denominador,
        "fracao_geratriz": f"{num_simp}/{den_simp}",
        "numerador": num_simp,
        "denominador": den_simp,
        "valor_decimal": num_simp / den_simp
    }


# =============================================================================
# PARSER GERAL DE NÚMEROS (Inteiros, Frações, Decimais, Raízes, Dízimas)
# =============================================================================

def analisar_expressao_numerica(entrada_str: str) -> Dict[str, Any]:
    """
    Interpreta uma entrada fornecida pelo usuário e determina:
    - O tipo do formato (inteiro, fração, decimal, raiz, dízima)
    - O valor numérico exato ou aproximado
    - Se é um número estritamente racional ou irracional
    """
    s = entrada_str.strip()
    
    # Caso 1: Dízima periódica no formato com parênteses, ex: '1,2(5)' ou '0,(3)'
    if eh_dizima_periodica_str(s):
        info_dizima = calcular_fracao_geratriz(s)
        return {
            "tipo": "dizima_periodica",
            "detalhes": info_dizima,
            "numerador": info_dizima["numerador"],
            "denominador": info_dizima["denominador"],
            "valor": info_dizima["valor_decimal"],
            "eh_racional": True
        }
        
    # Caso 2: Raiz quadrada, ex: '√9', 'v9', 'sqrt(9)', '√2', 'v2'
    padrao_raiz = r'^(√|v|sqrt\()?\s*([+-]?\d+)\)?$'
    m_raiz = re.match(padrao_raiz, s, re.IGNORECASE)
    if ('√' in s or s.lower().startswith('v') or s.lower().startswith('sqrt')):
        # Extrai o radicando
        radicando_str = re.sub(r'[^\d\-+]', '', s)
        radicando = int(radicando_str)
        if radicando < 0:
            raise ValueError(f"Raiz quadrada de número negativo ({radicando}) não é um número Real!")
        
        raiz = math.isqrt(radicando)
        eh_exata = (raiz * raiz == radicando)
        
        return {
            "tipo": "raiz",
            "radicando": radicando,
            "eh_exata": eh_exata,
            "valor": float(raiz) if eh_exata else math.sqrt(radicando),
            "numerador": raiz if eh_exata else None,
            "denominador": 1 if eh_exata else None,
            "eh_racional": eh_exata
        }

    # Caso 3: Fração, ex: '3/4', '-5/2', '6/3'
    if '/' in s:
        partes = s.split('/')
        if len(partes) == 2:
            num = int(partes[0].strip())
            den = int(partes[1].strip())
            num_s, den_s = simplificar_fracao(num, den)
            return {
                "tipo": "fracao",
                "numerador_original": num,
                "denominador_original": den,
                "numerador": num_s,
                "denominador": den_s,
                "valor": num_s / den_s,
                "eh_racional": True
            }

    # Caso 4: Decimal exato, ex: '0,75', '-2.5'
    s_clean = s.replace(',', '.')
    if '.' in s_clean:
        val = float(s_clean)
        # Converte decimal exato para fração: ex 0.75 -> 75/100 -> 3/4
        partes = s_clean.split('.')
        casas = len(partes[1])
        den = 10 ** casas
        num = int(round(val * den))
        num_s, den_s = simplificar_fracao(num, den)
        return {
            "tipo": "decimal_exato",
            "numerador": num_s,
            "denominador": den_s,
            "valor": val,
            "eh_racional": True
        }

    # Caso 5: Número inteiro simples, ex: '7', '-3', '0'
    val_int = int(s)
    return {
        "tipo": "inteiro",
        "numerador": val_int,
        "denominador": 1,
        "valor": float(val_int),
        "eh_racional": True
    }


# =============================================================================
# CLASSIFICADOR DE CONJUNTOS NUMÉRICOS
# =============================================================================

def classificar_numero(entrada: str, n_inclui_zero: bool = True) -> Dict[str, Any]:
    """
    Classifica uma entrada numérica nos conjuntos N, Z, Q, I, R e gera a justificativa.
    
    PARÂMETROS:
    - entrada: String representando o número (ex: '7', '-3', '3/4', '1,2(5)', '√9', '√2').
    - n_inclui_zero: Se True, considera 0 ∈ N. O padrão moderno adotado pelo MEC/Fatec
      é incluir o zero em N. Essa escolha é explicitada na justificativa e no README.
    """
    info = analisar_expressao_numerica(entrada)
    
    pertence = []
    nao_pertence = []
    justificativas = []
    
    eh_racional = info["eh_racional"]
    valor = info["valor"]
    
    # 1. Conjunto dos Reais (R): Todos os números desta atividade são reais
    pertence_R = True
    pertence.append("R")
    
    if not eh_racional:
        # Se NÃO é racional, é IRRACIONAL (I)
        pertence_I = True
        pertence_Q = False
        pertence_Z = False
        pertence_N = False
        
        pertence.append("I")
        nao_pertence.extend(["Q", "Z", "N"])
        justificativas.append(f"É um número irracional (I) com infinitas casas decimais não periódicas (raiz não exata: {entrada} ≈ {valor:.4f}...).")
        justificativas.append("Por ser irracional, não pode pertencer a Q, Z ou N.")
    else:
        # É RACIONAL (Q): Pode ser escrito como a/b com a, b inteiros e b ≠ 0
        pertence_I = False
        pertence_Q = True
        pertence.append("Q")
        nao_pertence.append("I")
        
        num = info["numerador"]
        den = info["denominador"]
        
        # Verifica se simplifica para um número inteiro (denominador == 1)
        eh_inteiro = (den == 1)
        
        if eh_inteiro:
            pertence_Z = True
            pertence.append("Z")
            
            valor_inteiro = num
            
            # Verifica se é Natural (N)
            if valor_inteiro > 0:
                pertence_N = True
                pertence.append("N")
                justificativas.append(f"O número simplificado vale {valor_inteiro}, que é um número inteiro positivo (Natural).")
            elif valor_inteiro == 0:
                if n_inclui_zero:
                    pertence_N = True
                    pertence.append("N")
                    justificativas.append("O número é 0. Pela convenção adotada no projeto, 0 pertence a N (Naturais).")
                else:
                    pertence_N = False
                    nao_pertence.append("N")
                    justificativas.append("O número é 0. Na convenção N*, o zero é excluído dos naturais.")
            else:
                # Inteiro negativo
                pertence_N = False
                nao_pertence.append("N")
                justificativas.append(f"O número vale {valor_inteiro}, que é um inteiro negativo, portanto pertence a Z, mas NÃO é natural (N).")
        else:
            # É uma fração ou decimal que não resulta em inteiro
            pertence_Z = False
            pertence_N = False
            nao_pertence.extend(["Z", "N"])
            justificativas.append(f"Equivale à fração irredutível {num}/{den} (decimal {valor}), portanto pertence a Q, mas não é um número inteiro.")

    # Ordena os conjuntos para exibição clássica
    ordem_conjuntos = ["N", "Z", "Q", "I", "R"]
    conjuntos_pertence = [c for c in ordem_conjuntos if c in pertence]
    conjuntos_nao_pertence = [c for c in ordem_conjuntos if c in nao_pertence]
    
    # Informações extras para dízima periódica
    detalhes_dizima = None
    if info["tipo"] == "dizima_periodica":
        d = info["detalhes"]
        detalhes_dizima = {
            "entrada": entrada,
            "tipo_dizima": "dízima periódica composta" if d["parte_nao_periodica"] != "nenhuma" else "dízima periódica simples",
            "parte_nao_periodica": d["parte_nao_periodica"],
            "periodo": d["periodo"],
            "fracao_geratriz": d["fracao_geratriz"]
        }

    return {
        "entrada": entrada,
        "tipo_detectado": info["tipo"],
        "valor_numerico": valor,
        "pertence_a": conjuntos_pertence,
        "nao_pertence_a": conjuntos_nao_pertence,
        "detalhes_dizima": detalhes_dizima,
        "justificativa": " ".join(justificativas)
    }


# =============================================================================
# BÔNUS: CRIVO DE ERATÓSTENES (PRIMOS) E LISTAGEM DE DIVISORES
# =============================================================================

def crivo_de_eratostenes(limite: int) -> List[int]:
    """
    Gera todos os números primos de 2 até o limite especificado.
    
    Explicação didática do Crivo de Eratóstenes:
    1. Criamos uma lista onde inicialmente todos os números de 2 até o limite
       são marcados como "primos em potencial" (True).
    2. Começamos pelo primeiro primo, o número 2.
    3. Riscaremos todos os seus múltiplos (4, 6, 8, 10...), pois quem é múltiplo
       de 2 não é primo.
    4. Passamos para o próximo número não riscado (o 3) e riscamos seus múltiplos (6, 9, 12...).
    5. Repetimos o processo até a raiz quadrada do limite.
    6. Os números que continuarem não riscados são exatamente os primos!
    """
    if limite < 2:
        return []
        
    eh_primo = [True] * (limite + 1)
    eh_primo[0] = False
    eh_primo[1] = False
    
    limite_busca = int(math.isqrt(limite))
    for p in range(2, limite_busca + 1):
        if eh_primo[p]:
            # Marca todos os múltiplos de p a partir de p*p
            for multiplo in range(p * p, limite + 1, p):
                eh_primo[multiplo] = False
                
    primos = [num for num in range(2, limite + 1) if eh_primo[num]]
    return primos


def listar_divisores(n: int) -> List[int]:
    """
    Lista todos os divisores inteiros positivos de um número natural n.
    
    Explicação didática:
    Um número 'd' é divisor de 'n' se a divisão n / d deixar resto zero (n % d == 0).
    Testamos os números de 1 até n e guardamos todos os que dividem perfeitamente.
    """
    n = abs(n)
    if n == 0:
        return []
        
    divisores = []
    for d in range(1, n + 1):
        if n % d == 0:
            divisores.append(d)
    return divisores
