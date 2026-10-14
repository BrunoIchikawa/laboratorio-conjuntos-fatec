# Guia Completo de Estudo e Apresentação do Código
### Especialmente desenvolvido para membros do grupo com pouca experiência em programação
**Integrantes:** Bruno Santos Ichikawa, Geovana Correa dos Santos, Isabela de Sousa Veloso  
**Curso:** Desenvolvimento de Software Multiplataforma – Fatec Osasco

> **Olá, Geovana e Isabela!**  
> Não se preocupem se vocês não têm muita experiência com programação. Este projeto foi escrito com **código limpo, direto e sem truques complicados**. Vocês não precisam ser experts para tirar nota máxima nesta apresentação: basta entender a **lógica** por trás das coisas.  
> 
> Este guia foi feito para vocês lerem, entenderem em 15 minutos e falarem na frente do professor com total segurança e naturalidade!

---

## 1. O Mapa do Nosso Projeto (Onde está cada coisa?)

Nosso projeto tem uma estrutura muito organizada. Veja como é fácil:

```text
tarefa_codigo/
├── src/
│   ├── parte1_conjuntos.py     --> As contas com conjuntos "na mão" e pelo Python
│   ├── parte2_numericos.py     --> O classificador de números (N, Z, Q, I, R) e a dízima
│   └── parte3_miniprojetos.py  --> O sistema de recomendar amigos (Jaccard) e os perfis de acesso
├── tests/                      --> Nossos 10 testes automatizados que provam que tudo funciona
├── main.py                     --> O menu interativo bonitão que você roda para demonstrar
├── run_demonstracao.py         --> O script que roda tudo de uma vez e gera os logs
├── relatorio.pdf               --> O relatório de 1 página exigido pelo professor
└── README.md                   --> A documentação completa para o GitHub
```

---

## 2. Analogias Simples: Entendendo a Matemática com o Dia a Dia

Antes de olhar o código, entenda o que cada operação significa no "mundo real":

| Conceito Matemático | Símbolo | Analogia do Dia a Dia | No nosso código |
| :--- | :---: | :--- | :--- |
| **Conjunto** | `{...}` | Uma **sacola de compras** onde itens repetidos não contam duas vezes. Se você comprou 2 maçãs iguais, na lista de frutas só conta "maçã". | `remover_duplicatas()` |
| **Pertinência** | $x \in A$ | Olhar dentro da sacola e ver se a "chave do carro" está lá dentro. | `pertence_manual(x, A)` |
| **União** | $A \cup B$ | Juntar tudo que está na sacola A e na sacola B em uma mesa só (sem repetir). | `uniao_manual(A, B)` |
| **Interseção** | $A \cap B$ | O que eu e você compramos **em comum**. Apenas as coisas que estão nas duas sacolas ao mesmo tempo. | `intersecao_manual(A, B)` |
| **Diferença** | $A - B$ | O que tem na **minha** sacola que **não** tem na sua. | `diferenca_manual(A, B)` |
| **Diferença Simétrica** | $A \Delta B$ | O que é exclusivo de cada um: o que só eu tenho + o que só você tem. | `diferenca_simetrica_manual(A, B)` |
| **Subconjunto** | $A \subseteq B$ | A minha sacola é pequena e **todos** os meus itens também estão dentro da sua sacola maior. | `eh_subconjunto_manual(A, B)` |
| **Cardinalidade** | $\|A\|$ | Contar quantos itens diferentes existem dentro da sacola. | `cardinalidade_manual(A)` |

---

## 3. Explicação "Linha por Linha" das Funções Principais

### Parte 1: `src/parte1_conjuntos.py`

#### A) Como verificamos se um número está no conjunto (`pertence_manual`)?
```python
def pertence_manual(elemento, conjunto):
    for item in conjunto:      # Olhamos cada item da lista, um por um
        if item == elemento:   # Se o item for igual ao que procuramos...
            return True        # Achamos! Retorna Verdadeiro!
    return False               # Olhamos a lista inteira e não achamos? Retorna Falso!
```
* **Como você explica para o professor:**  
  *"Professor, essa função funciona como uma busca sequencial bem simples. Ela percorre a lista elemento por elemento usando um laço `for`. Se encontrar o valor, devolve `True`. Se o laço terminar sem encontrar nada, devolve `False`."*

#### B) Como fazemos a União sem usar operadores prontos (`uniao_manual`)?
```python
def uniao_manual(conjunto_a, conjunto_b):
    resultado = []                       # Começamos com uma lista vazia
    for item in conjunto_a:              # Copiamos todos os itens de A
        if not pertence_manual(item, resultado):
            resultado.append(item)
    for item in conjunto_b:              # Depois olhamos os itens de B:
        if not pertence_manual(item, resultado): # Só colocamos se ainda NÃO estiver lá!
            resultado.append(item)
    return ordenar_elementos(resultado)
```
* **Como você explica para o professor:**  
  *"Para unir dois conjuntos sem usar a função pronta do Python, nós criamos uma lista vazia, colocamos todos os elementos de A (sem repetir) e depois percorremos os elementos de B, adicionando apenas aqueles que ainda não estavam no nosso resultado."*

#### C) Como verificamos se A está contido em B (`eh_subconjunto_manual`)?
```python
def eh_subconjunto_manual(conjunto_a, conjunto_b):
    for item in conjunto_a:                      # Para cada item de A:
        if not pertence_manual(item, conjunto_b): # Se esse item NÃO estiver em B...
            return False                         # Já era, A não está contido em B!
    return True                                  # Se todos estavam lá, é Verdadeiro!
```

---

### Parte 2: `src/parte2_numericos.py`

#### A) O que o Classificador faz?
Ele pega qualquer entrada (como `7`, `-3`, `3/4`, `1,2(5)` ou `√2`) e analisa duas coisas:
1. **É Racional ($\mathbb{Q}$) ou Irracional ($\mathbb{I}$)?**
   * Se for raiz não exata (como $\sqrt{2}$), tem infinitas casas que não se repetem. É **Irracional ($\mathbb{I}$)** e Real ($\mathbb{R}$).
   * Se puder ser escrito como fração $a/b$, é **Racional ($\mathbb{Q}$)** e Real ($\mathbb{R}$).
2. **Se for Racional, ele é Inteiro ($\mathbb{Z}$)?**
   * Se a divisão der exata (ex.: $6/3 = 2$ ou $7/1 = 7$), ele é **Inteiro ($\mathbb{Z}$)**.
3. **Se for Inteiro, ele é Natural ($\mathbb{N}$)?**
   * Se for positivo ou zero ($0, 1, 2, ...$), é **Natural ($\mathbb{N}$)**.
   * Se for negativo (ex.: $-3$), **não** é natural!

#### B) O "Truque" da Fração Geratriz da Dízima Periódica (`1,2(5)`):
* **Como você explica para o professor:**  
  *"Professor, para achar a fração geratriz de $1,25555...$, nós usamos o método algébrico tradicional:  
  Chamamos $x = 1,25555...$  
  Multiplicamos por 100 para passar a vírgula depois do primeiro período: $100x = 125,5555...$  
  Multiplicamos por 10 para colocar a vírgula antes do período: $10x = 12,5555...$  
  Subtraindo as duas equações, a parte infinita se cancela: $100x - 10x = 125 - 12 \implies 90x = 113 \implies x = \frac{113}{90}$!  
  Nosso código faz exatamente essa conta de forma automática e usa o MDC de Euclides para simplificar a fração."*

---

### Parte 3: `src/parte3_miniprojetos.py`

#### A) Opção 1: Índice de Jaccard (Sistema de Recomendação de Amigos)
* A fórmula de Jaccard mede o quanto duas pessoas combinam:
  $$\text{Jaccard} = \frac{\text{Interesses em Comum}}{\text{Total de Interesses Diferentes}} = \frac{|A \cap B|}{|A \cup B|}$$
* **No nosso teste oficial:**
  * **Ana e Caio:** têm 2 interesses em comum (`games`, `cinema`) e 5 interesses no total.  
    $\text{Jaccard} = \frac{2}{5} = 0,40$ (40% de afinidade).
  * **Ana e Bia:** têm 2 interesses em comum e 6 no total.  
    $\text{Jaccard} = \frac{2}{6} = 0,33$ (33% de afinidade).
  * **Conclusão:** Para a Ana, o melhor amigo a recomendar é o **Caio**, pois tem a maior afinidade ($0,40$).

#### B) Opção 2: Controle de Acesso por Perfis (RBAC)
* Cada perfil é um conjunto de permissões (ex.: `leitor = {'ler'}`, `editor = {'ler', 'editar'}`).
* Se alguém é `leitor` e `editor`, suas permissões são a **União** dos dois: `{'ler', 'editar'}`.
* Se perguntarmos *"Esse usuário pode excluir?"*, o código faz: `'excluir' in permissoes`. Como não está, responde `Falso`.
* Se perguntarmos *"Editor está contido em Admin?"*, o código faz `editor ⊆ admin`. Como o admin tem todas as permissões do editor, responde `Verdadeiro`.

---

## 4. Roteiro Sugerido para Apresentação em Grupo (5 a 8 minutos)

### Abertura (Geovana):
> *"Boa noite professor! Nosso grupo desenvolveu o Laboratório de Conjuntos dividindo o projeto em três níveis: básico (operações puras de teoria dos conjuntos), intermediário (classificador numérico com dízimas) e avançado (aplicações práticas em sistemas de recomendação e controle de acesso).*  
> *O grande diferencial do nosso trabalho foi cumprir o desafio de não usar nenhuma função pronta do Python na Parte 1, implementando tudo na mão com laços `for` e testes `if`, e depois validando automaticamente contra as funções nativas do Python para garantir 100% de precisão."*

### Demonstração da Parte 1 e 2 (Isabela):
> *(Abre o terminal e digita: `python main.py`)*  
> *"Aqui na Parte 1, nós implementamos união, interseção, diferença, diferença simétrica, pertinência e subconjunto. No Exemplo 1 oficial, quando o usuário digita números repetidos como `1, 2, 2, 3, 4`, nossa função `remover_duplicatas` higieniza a entrada porque na matemática conjuntos não têm repetição.*  
> *Na Parte 2, nosso classificador identifica se o número é Natural, Inteiro, Racional, Irracional ou Real. Ele aceita frações, decimais, raízes e dízimas periódicas. Por exemplo, na dízima `1,2(5)`, o algoritmo deduz algebricamente a fração geratriz `113/90` e simplifica por MDC."*

### Demonstração da Parte 3 e Encerramento (Bruno):
> *"Na Parte 3, nós conectamos a teoria dos conjuntos com a engenharia de software real. Usamos o Índice de Jaccard, que calcula a razão entre a interseção e a união de interesses para recomendar o Caio para a Ana com 40% de afinidade. E no controle de permissões por perfis, mostramos que conceder múltiplos perfis nada mais é do que fazer a União de conjuntos, e checar autorização é verificar se uma ação Pertence ao conjunto de permissões.*  
> *Todos os gabaritos do enunciado foram validados por 10 testes automatizados que rodam em menos de 1 segundo."*

---

## 5. Perguntas que o Professor Pode Fazer (e Como Responder!)

### Pergunta 1: *"Por que vocês não usaram operadores como `|` ou `&` na Parte 1?"*
* **Sua Resposta:** *"Porque o enunciado solicitava explicitamente como desafio não utilizar os operadores prontos da linguagem. O objetivo era demonstrar que compreendemos a lógica fundamental dos algoritmos usando apenas laços `for` e condicionais `if`. Porém, nós usamos as funções nativas como gabarito de conferência para atestar que nossa implementação manual estava 100% correta."*

### Pergunta 2: *"O zero é considerado um número Natural no projeto de vocês?"*
* **Sua Resposta:** *"Sim, professor! Na matemática existem duas escolas: a que começa os naturais em 1 ($N^*$) e a convenção moderna de Peano que inclui o zero ($0 \in \mathbb{N}$). No nosso projeto adotamos $0 \in \mathbb{N}$, mas deixamos isso como um parâmetro configurável e documentamos no README e no código."*

### Pergunta 3: *"Por que o número 0,(9) pertence aos Naturais se ele parece um número decimal?"*
* **Sua Resposta:** *"Porque algebricamente $0,999...$ é exatamente igual a $1$. Quando calculamos a fração geratriz dele: $10x - x = 9,999... - 0,999... \implies 9x = 9 \implies x = 9/9 = 1$. Como 1 é um número inteiro positivo, ele pertence aos Naturais ($\mathbb{N}$), Inteiros ($\mathbb{Z}$), Racionais ($\mathbb{Q}$) e Reais ($\mathbb{R}$)."*

### Pergunta 4: *"O que é a complexidade $2^n$ mencionada no conjunto das partes?"*
* **Sua Resposta:** *"Significa que para cada elemento que adicionamos em um conjunto, o número de subconjuntos dobra. Um conjunto com 3 elementos tem $2^3 = 8$ subconjuntos; com 10 elementos tem $1.024$; e com 30 elementos passa de 1 bilhão! Isso mostra como certos algoritmos combinatórios podem ficar muito lentos se não forem bem planejados."*

---

## 6. Comandos Rápidos para Usar no Dia da Apresentação

Abra o terminal na pasta do projeto e use:

1. **Para rodar o Menu Interativo e navegar na frente do professor:**
   ```bash
   python main.py
   ```
2. **Para rodar a Demonstração Completa que imprime todo o gabarito formatado:**
   ```bash
   python run_demonstracao.py
   ```
3. **Para rodar os Testes Unitários Automatizados e mostrar que tudo está verde (OK):**
   ```bash
   python -m unittest discover tests
   ```

*Pronto! Com este roteiro e o código limpo que preparamos, vocês têm tudo para tirar nota 10 com louvor!*
