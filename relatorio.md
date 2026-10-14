# Relatório Técnico: Teoria dos Conjuntos na Prática Computacional
**Disciplina:** Matemática Concreta | **Curso:** Desenvolvimento de Software Multiplataforma – Fatec Osasco  
**Tema:** Laboratório de Conjuntos e Conjuntos Numéricos

---

### 1. Onde a Teoria dos Conjuntos apareceu no código?

A Teoria dos Conjuntos não atuou como um conceito abstrato distante, mas sim como a **estrutura central de tomada de decisão, validação de regras de negócio e modelagem de dados** ao longo de todo o projeto:

* **Eliminação de Redundâncias e Unicidade:** Na computação básica, listas aceitam duplicatas (`[1, 2, 2, 3]`). A própria definição de conjunto ($\forall x$, a multiplicidade não altera o conjunto) exigiu a criação de um algoritmo de desduplicação (`remover_duplicatas`), garantindo que apenas dados únicos sejam processados, refletindo diretamente o conceito de conjunto bem-definido.
* **Operações Fundamentais como Mecanismo Lógico:**
  * A **União ($A \cup B$)** foi usada para agregação de dados e acúmulo de privilégios.
  * A **Interseção ($A \cap B$)** funcionou como o filtro de similaridade e compatibilidade entre coleções.
  * A **Diferença ($A - B$)** e o **Complemento ($U - A$)** atuaram como cálculo de pendências e detecção de elementos ausentes.
* **Hierarquia e Classificação Numérica (Inclusão):** Na Parte 2, a relação de inclusão de conjuntos $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ e $\mathbb{I} \subset \mathbb{R}$ serviu como o motor de regras de inferência do classificador. Um número provado Natural herda automaticamente a pertinência a $\mathbb{Z}, \mathbb{Q}$ e $\mathbb{R}$.
* **Aplicações de Engenharia de Software (Parte 3):**
  * **Índice de Jaccard:** Utilizou a razão de cardinalidade $\frac{|A \cap B|}{|A \cup B|}$ para transformar conjuntos de interesses em um coeficiente matemático de afinidade (0 a 1).
  * **Controle de Acesso RBAC:** As permissões de um perfil são um conjunto. A concessão de múltiplos perfis a um usuário foi resolvida pela **União de Perfis**; a herança entre papéis foi validada via **Subconjunto ($P_1 \subseteq P_2$)**; e a autorização de execução de comandos foi determinada pela relação de **Pertinência ($ação \in Permissões$)**.

---

### 2. Qual operação foi mais difícil de implementar e por quê?

A operação mais desafiadora do projeto foi a **Identificação de Dízimas Periódicas e a Dedução Algorítmica da Fração Geratriz**, acompanhada da **Diferença Simétrica e Inclusão Estrita sem operadores nativos**:

1. **O Desafio da Fração Geratriz:**
   * Enquanto frações comuns ($a/b$) ou decimais exatos dependem de aritmética simples, a dízima periódica (especialmente a **dízima periódica composta**, como `1,2(5)`) exige desacoplar três componentes heterogêneos: a parte inteira ($I$), a parte decimal não periódica ($N$, com $k$ dígitos) e o período repetente ($P$, com $p$ dígitos).
   * O algoritmo precisou reproduzir digitalmente o método algébrico de cancelamento da cauda infinita: multiplicar a variável por $10^{k+p}$ e por $10^k$, subtrair as equações para eliminar a dízima e, em seguida, aplicar o algoritmo do Máximo Divisor Comum (MDC de Euclides) para reduzir a fração à sua forma irredutível ($113/90$). Tratar o caso singular `0,(9)` — cuja geratriz matemática resulta em $\frac{9}{9} = 1$, promovendo o número de decimal aparente para o conjunto dos Naturais — exigiu rigor matemático e estruturação lógica precisa.

2. **O Desafio de Implementar Operações Manuais "Puristas":**
   * A restrição do enunciado de **não utilizar os operadores prontos do Python** (`|`, `&`, `-`, `^`, `issubset`) impôs que cada relação fosse reconstruída do zero com laços `for` e condicionais `if`.
   * A verificação de **Subconjunto Próprio ($A \subset B$)** exigiu garantir não apenas que todo elemento de $A$ pertence a $B$, mas também a verificação de não-equivalência estrita ($|A| < |B|$ e $A \neq B$), cobrindo com precisão casos de borda como o conjunto vazio ($\emptyset \subseteq B$, mas $\emptyset \not\subset \emptyset$).

---
**Conclusão:** A implementação manual permitiu compreender a complexidade algorítmica por trás das abstrações nativas das linguagens, consolidando a ponte entre o rigor da matemática discreta e as estruturas de dados do desenvolvimento de software moderno.
