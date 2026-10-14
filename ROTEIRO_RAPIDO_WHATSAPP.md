# ROTEIRO RÁPIDO PARA O GRUPO (ESTUDO E APRESENTAÇÃO)
> **Dica:** Este texto foi formatado para ser fácil de ler no celular e pode ser compartilhado diretamente no WhatsApp do grupo.

---

## 1. O QUE É O PROJETO (EM 30 SEGUNDOS)
O professor pediu para programarmos em Python os conceitos de **Teoria dos Conjuntos** e **Conjuntos Numéricos** que vimos nas aulas de Matemática Concreta:
1. **Parte 1:** Fazer as operações de conjuntos (União, Interseção, Diferença, etc.) **na mão** (sem usar funções prontas do Python) e depois comparar com a função pronta para provar que está certo.
2. **Parte 2:** Um programa que recebe qualquer número (fração, raiz, dízima como $1,2(5)$) e diz a quais conjuntos ele pertence ($\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{I}, \mathbb{R}$).
3. **Parte 3:** Mostrar como conjuntos são usados de verdade em sistemas de TI: Recomendador de amigos/músicas (tipo Spotify/Netflix) e Controle de Acesso (quem pode ler, editar ou excluir).

---

## 2. DIVISÃO DA APRESENTAÇÃO (SE FORMOS APRESENTAR)

### 👤 Pessoa 1: Abertura e Parte 1 (Conjuntos Básicos)
- **O que falar:**
  - "Nosso trabalho implementa a Teoria dos Conjuntos em Python."
  - "O professor pediu um desafio: **não usar os atalhos prontos do Python** (como `|` ou `&`)."
  - "Então nós construímos as operações usando apenas laços (`for`) e condições (`if`)."
  - "Por exemplo, na **União**, a gente junta os dois conjuntos, mas sem deixar repetir elementos. Na **Interseção**, a gente só pega o que existe nos dois ao mesmo tempo."
  - "E criamos uma função de teste que compara o nosso código manual com o código nativo do Python, e deu 100% igual nos testes."

### 👤 Pessoa 2: Parte 2 (Conjuntos Numéricos e Dízimas)
- **O que falar:**
  - "Na Parte 2, criamos o classificador de números."
  - "Ele testa se o número é Natural ($\mathbb{N}$), Inteiro ($\mathbb{Z}$), Racional ($\mathbb{Q}$), Irracional ($\mathbb{I}$) ou Real ($\mathbb{R}$)."
  - "Se o número for uma dízima como $1,2(5)$, o programa calcula a **fração geratriz** algebricamente (aquela conta que multiplica por 100 e por 10 para cortar a parte infinita) e simplifica pelo MDC de Euclides, achando $113/90$."
  - "Testamos exatamente os 12 números da tabela do enunciado e todos bateram com o gabarito oficial."

### 👤 Pessoa 3: Parte 3 (Aplicações Reais) e Conclusão
- **O que falar:**
  - "Na Parte 3, aplicamos conjuntos em problemas reais de computação."
  - "O primeiro foi o **Índice de Jaccard**, que mede afinidade entre pessoas dividindo a interseção dos gostos pela união. É a mesma matemática que o Spotify usa para recomendar músicas."
  - "O segundo foi o **RBAC (Controle de Acesso)**: quando um usuário tem dois perfis (tipo Editor e Financeiro), suas permissões são a **União** desses perfis. E para saber se ele pode fazer uma ação, testamos a **Pertinência**."
  - "Concluímos mostrando que a Teoria dos Conjuntos é a base das regras de negócio e da segurança de qualquer software."

---

## 3. AS 7 PERGUNTAS "PEGADINHA" DO PROFESSOR (DECORE ISTO!)

Se o professor decidir fazer perguntas difíceis para testar se vocês realmente sabem ou se só copiaram código, ele vai fazer uma destas perguntas. Aqui está a resposta exata:

### ❓ Pergunta 1: "Vocês usaram as operações prontas do Python (como `setA | setB`)?"
* **Sua Resposta:**
  > "Não para a lógica principal, professor! O enunciado pedia expressamente o desafio de NÃO usar operadores prontos. Então nós criamos funções manuais usando laços `for` e `if`. Usamos o `set` nativo apenas numa função separada para conferir se o nosso algoritmo manual bateu 100% com o resultado esperado."

---

### ❓ Pergunta 2: "Por que $0,(9)$ foi classificado como Natural ($\mathbb{N}$)? Cadê a vírgula?"
* **Sua Resposta:**
  > "Porque algebricamente $0,999...$ é exatamente igual a 1. Na fração geratriz, $10x - x = 9x \implies 9 - 0 = 9 \implies x = 9/9 = 1$. Como 1 é um número inteiro positivo, ele pertence ao conjunto dos Naturais ($\mathbb{N}$)."

---

### ❓ Pergunta 3: "Qual a diferença entre Subconjunto ($A \subseteq B$) e Subconjunto Próprio ($A \subset B$)?"
* **Sua Resposta:**
  > "No subconjunto normal ($A \subseteq B$), todo elemento de A está em B, e os dois conjuntos podem ser até idênticos. Já no subconjunto próprio ($A \subset B$), todo elemento de A está em B, MAS o conjunto B precisa ter pelo menos um elemento a mais que A (eles não podem ser iguais)."

---

### ❓ Pergunta 4: "Como o programa sabe que $\sqrt{2}$ é Irracional e $\sqrt{9}$ é Natural?"
* **Sua Resposta:**
  > "O programa calcula a raiz. Se a raiz der um número inteiro exato (como $\sqrt{9} = 3$), ele classifica como Natural e Inteiro. Se a raiz de um número inteiro não for exata (como $\sqrt{2} \approx 1,4142...$), pela matemática sabemos que ela tem infinitas casas decimais que nunca se repetem em padrão, logo ela pertence aos Irracionais ($\mathbb{I}$) e aos Reais ($\mathbb{R}$)."

---

### ❓ Pergunta 5: "O que o algoritmo de Jaccard tem a ver com Teoria dos Conjuntos?"
* **Sua Resposta:**
  > "Tudo, professor! A fórmula do Índice de Jaccard é o tamanho da Interseção dividido pelo tamanho da União: $|A \cap B| \div |A \cup B|$. No caso da Ana e do Caio, eles têm 2 interesses em comum (interseção) e 5 interesses no total somados (união). A conta dá $2/5 = 0,40$, que é a afinidade entre eles."

---

### ❓ Pergunta 6: "No controle de acesso (RBAC), se o usuário é Editor e Financeiro, como o sistema sabe o que ele pode fazer?"
* **Sua Resposta:**
  > "O sistema faz a **União** das permissões do perfil de Editor com as do Financeiro. Quando o usuário clica em algo, o sistema faz um teste de **Pertinência** ($ação \in Permissões$). Se a ação pertencer ao conjunto, ele autoriza; se não pertencer (como 'excluir'), ele bloqueia."

---

### ❓ Pergunta 7: "Se eu digitar o conjunto $\{1, 2, 2, 3\}$, por que a cardinalidade dá 3 e não 4?"
* **Sua Resposta:**
  > "Porque na Teoria dos Conjuntos a repetição não cria elementos novos. Nós criamos uma função chamada `remover_duplicatas` que limpa as repetições antes de calcular a cardinalidade ($|A| = 3$)."

---

## 4. COMO RODAR NO DIA (SE O PROFESSOR PEDIR PARA MOSTRAR NA HORA)

Abra o terminal na pasta do projeto e digite:

1. **Para mostrar o menu bonitinho na tela:**
   ```bash
   python main.py
   ```
   (Lá tem opção de digitar na hora ou apertar Enter para ver os testes automáticos).

2. **Para rodar todos os testes na frente dele em 1 segundo:**
   ```bash
   python -m unittest discover tests
   ```
   (Vai aparecer `Ran 10 tests in 0.001s - OK`, provando que está 100% testado).
