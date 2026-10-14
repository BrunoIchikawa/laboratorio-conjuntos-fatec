# Laboratório de Conjuntos e Conjuntos Numéricos
### Atividade Prática de Matemática Concreta (MC)
**Fatec Osasco – Faculdade de Tecnologia Prefeito Hirant Sanazar**  
**Curso:** Graduação em Desenvolvimento de Software Multiplataforma (DSM)  
**Linguagem Utilizada:** Python 3 (Biblioteca Padrão)

---

## Sobre o Projeto
Este repositório contém a implementação dos requisitos do **Laboratório de Conjuntos**, estruturado nos três níveis de complexidade solicitados:

1. **Parte 1: Teoria dos Conjuntos (Básico)** – Implementação de operações manuais "puras" (apenas laços `for` e condicionais `if`, atendendo ao desafio de não usar operadores prontos) com validação comparativa contra a classe `set` nativa do Python.
2. **Parte 2: Conjuntos Numéricos (Intermediário)** – Classificador de números ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{I}, \mathbb{R}$), identificador de dízimas periódicas simples e compostas com cálculo da fração geratriz via método algébrico e algoritmo de Euclides (MDC), além de gerador de primos (Crivo de Eratóstenes) e divisores.
3. **Parte 3: Integração e Mini-projetos (Avançado)** – Aplicações reais: **Sistema de Recomendação por Interesses (Índice de Jaccard)**, **Controle de Acesso por Perfis (RBAC)**, **Produto Cartesiano / Conjunto das Partes ($2^n$)** e **Intervalos Reais**.

- **Relatório de 1 Página:** Disponível em `relatorio.md` e diagramado para entrega em `relatorio.pdf`.
- **Roteiro de Estudo e Apresentação:** Disponível em `GUIA_APRESENTACAO.md` (com analogias, explicações linha por linha e perguntas do professor).
- **Enunciado Original Reconstituído:** Disponível em `Laboratorio_de_Conjuntos.pdf`.

---

## Estrutura do Repositório

```text
tarefa_codigo/
├── src/
│   ├── __init__.py              # Inicializador do pacote
│   ├── parte1_conjuntos.py      # Operações manuais, nativas e validação
│   ├── parte2_numericos.py      # Classificador numérico, fração geratriz e bônus
│   └── parte3_miniprojetos.py   # Jaccard, RBAC, Conjunto das Partes e Intervalos
├── tests/
│   ├── __init__.py              # Pacote de testes
│   ├── test_parte1.py           # Testes unitários do Exemplo 1 e Exemplo 2
│   ├── test_parte2.py           # Testes dos 12 números da tabela e dízimas
│   └── test_parte3.py           # Testes de Jaccard e RBAC
├── main.py                      # Menu interativo no terminal
├── run_demonstracao.py          # Executa todos os cenários e grava logs
├── logs_execucao.txt            # Saída da execução completa dos testes
├── relatorio.md                 # Relatório técnico de 1 página (Markdown)
├── relatorio.pdf                # Relatório técnico diagramado em PDF
├── GUIA_APRESENTACAO.md         # Roteiro de estudo e apresentação do grupo
├── ROTEIRO_RAPIDO_WHATSAPP.md   # Resumo direto e perguntas frequentes para celular
├── Laboratorio_de_Conjuntos.pdf # Cópia do enunciado da atividade
└── README.md                    # Documentação do projeto
```

---

## Decisões Técnicas e Metodologia

### 1. Desafio Manual vs. Solução Nativa (Parte 1)
O enunciado solicitava explicitamente não utilizar os operadores prontos da linguagem (`|`, `&`, `-`, `^`, `issubset`).
- Todas as operações principais foram programadas com laços `for` e testes lógicos `if`.
- Em paralelo, implementamos funções equivalentes usando a classe nativa `set`.
- A função de validação executa ambas as abordagens e comprova que os resultados são rigorosamente idênticos.

### 2. Tratamento de Elementos Repetidos na Entrada
Na teoria dos conjuntos, a multiplicidade de elementos não altera o conjunto ($A = \{1, 2, 2, 3\} = \{1, 2, 3\}$). A função `remover_duplicatas` processa qualquer entrada bruta preservando apenas a primeira ocorrência antes das operações e do cálculo de cardinalidade ($|A|$).

### 3. Convenção do Zero no Conjunto dos Naturais ($\mathbb{N}$)
Adotamos como padrão a convenção de Peano ($0 \in \mathbb{N}$), comum no contexto de Ciência da Computação. O classificador possui o parâmetro configurável `n_inclui_zero=True`.

### 4. Algoritmo da Fração Geratriz (Método Algébrico)
Para dízimas periódicas compostas (como `1,2(5)`), o programa isola:
- Parte inteira ($I = 1$)
- Anti-período não periódico ($N = 2$, com $k = 1$ dígito)
- Período ($P = 5$, com $p = 1$ dígito)

Aplica o cancelamento da cauda periódica:
$$10^{k+p}x - 10^k x = (100x - 10x) = 125 - 12 \implies 90x = 113 \implies x = \frac{113}{90}$$
E simplifica numerador e denominador utilizando o Algoritmo de Euclides (MDC).

---

## Como Executar o Projeto

Requisitos: Python 3.8 ou superior instalado. Não requer instalação de pacotes externos (`pip`), utilizando apenas a biblioteca padrão.

### 1. Menu Interativo (Terminal)
```bash
python main.py
```
Permite navegar interativamente pelas partes do laboratório, digitar conjuntos e números na hora ou carregar os gabaritos oficiais.

### 2. Demonstração Completa Automatizada
```bash
python run_demonstracao.py
```
Executa todos os exemplos e gabaritos em sequência e atualiza o arquivo `logs_execucao.txt`.

### 3. Execução dos Testes Unitários
```bash
python -m unittest discover tests
```
Roda os 10 testes cobrindo os cenários das Partes 1, 2 e 3.

---

## Resultados e Validação dos Casos de Teste

### Parte 1: Exemplo 1 (Caso Geral)
- **Entrada Bruta:** $A = \{1, 2, 2, 3, 4\}$, $B = \{3, 4, 5, 6\}$, $U = \{1, 2, ..., 10\}$
- **Entrada Tratada:** $A = \{1, 2, 3, 4\}$ ($|A| = 4$), $B = \{3, 4, 5, 6\}$ ($|B| = 4$)

| Operação | Resultado Obtido | Gabarito Oficial | Status |
| :--- | :--- | :--- | :---: |
| $A \cup B$ | `{1, 2, 3, 4, 5, 6}` | `{1, 2, 3, 4, 5, 6}` | Confere |
| $A \cap B$ | `{3, 4}` | `{3, 4}` | Confere |
| $A - B$ | `{1, 2}` | `{1, 2}` | Confere |
| $B - A$ | `{5, 6}` | `{5, 6}` | Confere |
| $A \Delta B$ | `{1, 2, 5, 6}` | `{1, 2, 5, 6}` | Confere |
| Complemento $U - A$ | `{5, 6, 7, 8, 9, 10}` | `{5, 6, 7, 8, 9, 10}` | Confere |
| $3 \in A$ | `Verdadeiro` | `Verdadeiro` | Confere |
| $5 \in A$ | `Falso` | `Falso` | Confere |
| $\{3, 4\} \subseteq A$ | `Verdadeiro` | `Verdadeiro` | Confere |
| $\{3, 4\} \subset A$ | `Verdadeiro` | `Verdadeiro` | Confere |

### Parte 1: Exemplo 2 (Casos de Borda)
- **Conjunto vazio:** $A = \emptyset, B = \{1, 2\} \implies A \cup B = \{1, 2\}; A \cap B = \emptyset; A \subseteq B$ é `Verdadeiro`.
- **Conjuntos iguais:** $A = B = \{1, 2, 3\} \implies A - B = \emptyset; A \Delta B = \emptyset; A \subseteq B$ é `Verdadeiro`; $A \subset B$ é `Falso`.
- **Conjuntos disjuntos:** $A = \{1, 2\}, B = \{3, 4\} \implies A \cap B = \emptyset; A \cup B = \{1, 2, 3, 4\}; A \Delta B = \{1, 2, 3, 4\}$.
- **Um contido no outro:** $A = \{1, 2\}, B = \{1, 2, 3\} \implies A \subset B$ é `Verdadeiro`; $B \subseteq A$ é `Falso`; $B - A = \{3\}$.
- **Repetidos na entrada:** $A = [1, 1, 1, 2] \implies A = \{1, 2\}; |A| = 2$.

---

### Parte 2: Tabela de Classificação de Números

| Entrada | Classificação Obtida | Gabarito Oficial | Justificativa |
| :--- | :--- | :--- | :--- |
| **7** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Inteiro positivo (Natural). |
| **−3** | $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Inteiro negativo, não é natural. |
| **0** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Convenção adotada: $0 \in \mathbb{N}$. |
| **3/4** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{Q}, \mathbb{R}$ | Fração equivalente ao decimal exato 0,75. |
| **−5/2** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{Q}, \mathbb{R}$ | Fração negativa equivalente a −2,5. |
| **6/3** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Fração simplifica exatamente para o inteiro 2. |
| **0,(3)** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{Q}, \mathbb{R}$ | Dízima periódica, geratriz 1/3. |
| **2,(7)** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{Q}, \mathbb{R}$ | Dízima periódica, geratriz 25/9. |
| **1,2(5)** | $\mathbb{Q}, \mathbb{R}$ | $\mathbb{Q}, \mathbb{R}$ | Dízima periódica composta, geratriz 113/90. |
| **0,(9)** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Geratriz resulta em $9/9 = 1$ (Natural). |
| **√9** | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ | Raiz exata igual a 3. |
| **√2** | $\mathbb{I}, \mathbb{R}$ | $\mathbb{I}, \mathbb{R}$ | Raiz não exata (número irracional). |

- **Bônus:**
  - Primos até 30: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`
  - Divisores de 36: `[1, 2, 3, 4, 6, 9, 12, 18, 36]`

---

### Parte 3: Aplicações Práticas

#### Opção 1: Recomendação por Interesses (Índice de Jaccard)
- **Ana:** `{rock, jazz, cinema, games}` (4 interesses)
- **Bia:** `{jazz, cinema, séries, viagens}` (4 interesses)
- **Caio:** `{games, tecnologia, cinema}` (3 interesses)

| Par Comparado | Interseção $|A \cap B|$ | União $|A \cup B|$ | Coeficiente Jaccard | Afinidade |
| :--- | :--- | :--- | :---: | :---: |
| **Ana e Bia** | `{jazz, cinema}` (2) | 6 elementos | $2/6$ | **0,33** (33%) |
| **Ana e Caio** | `{games, cinema}` (2) | 5 elementos | $2/5$ | **0,40** (40%) |
| **Bia e Caio** | `{cinema}` (1) | 6 elementos | $1/6$ | **0,17** (17%) |

Recomendação mais forte para Ana: **Caio** (afinidade de 0,40).

#### Opção 2: Controle de Acesso por Perfis (RBAC)
- Perfis: `leitor = {ler}`, `editor = {ler, editar}`, `admin = {ler, editar, excluir, gerir_usuarios}`, `financeiro = {ver_relatorios}`
- **Usuário leitor + editor:** Permissões = União = `{ler, editar}`.
- **Usuário editor + financeiro:** Permissões = `{ler, editar, ver_relatorios}`.
- **Permissão de exclusão:** `Não`, pois `'excluir'` $\notin$ Permissões do usuário.
- **Hierarquia:** `editor` $\subseteq$ `admin` (`Verdadeiro`); `financeiro` $\subseteq$ `admin` (`Falso`).

---

## Perguntas Obrigatórias do Relatório

1. **Onde a Teoria dos Conjuntos apareceu no código?**  
   Na eliminação de duplicatas (unicidade), na herança hierárquica dos conjuntos numéricos ($\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$), na quantificação de afinidades por sobreposição de preferências (Jaccard) e na segurança por concessão e verificação de privilégios de acesso (RBAC).

2. **Qual operação foi mais difícil de implementar e por quê?**  
   A dedução da fração geratriz de dízimas periódicas compostas (isolamento de $I, N, P$, multiplicação algébrica por potências de 10 e simplificação por MDC de Euclides) e o subconjunto próprio ($A \subset B$) sem operadores prontos, validando que todo elemento de $A$ está em $B$ com restrição estrita de desigualdade.
