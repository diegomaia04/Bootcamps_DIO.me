# 🖥️Python!

🤖[link importante para python](https://wiki.python.org.br/PythonBrasil)🤖
---
### Principais conceitos de python

❗Para documentar algo na linguagem python se usa "#" ❗

#### 🎲 Dados 🎲####


* Existem tipos de dados na linguagem python. Eles servem para definir as caracteriscas e comportanementos de um valor(objeto) para o programa. Os tipos são: 

Texto > ``` srt ``` 

Numerico > ``` int && float && complex ``` 

Sequência > ``` list && tuple && range ``` 

Mapa > ``` dict ``` 

Coleção > ``` set && frozenset ``` 

Boolenao > ``` bool ``` 

Binário > ``` bytes && bytearray && memoryview ```

---------

#### 🤬 Modo Interativo 🤬####

O interpretador Python pode executar em modo que possibilite o desevolvendor a escrever o codigo e ver o resultado na hora. Existem duas formas de inicar o modo interativo: 

* Escrevendo (python)  no terminal de comando do vscode, para sair do modo interativo do termianl é ```exit()```

* executar o script com a flag -i( sendo que "flag" é o nome do arquivo que vc deseja executar)

-----------

#### 🧩Função dir e help 🧩####

* dir: Sem arguemntos, retorna a lista de nomes no escopo local atual. Com um argumrntos, retorna uma lista de atributos validos para o objeto. Exemplo: 

```dir()- Sem Arguemntos ``` 

```dir(100)- Com Arguemntos ```

* help: Invoca o sistema de ajuda integrado.è possível fazer bsucar em modo interativo ou informar por parametro qual o nome do modulo, função, classe, meteodo ou variavel ele fala qual são os argumentoss que o mteodo recebe e o que ele retorrna. Exemplo:

```help()- Sem Arguemntos ``` 

```help(100)- Com Arguemntos ```


-----------
#### 🔷 Variaveis e Constantes 🔷 ####


* Variaveis em lingaugens de programça~p podemos definir valores que sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variaveis pois eles nascem com um valor e nao necessariamnete deem pernacem com o mesmo durnate a execucao do programa.

Em Pytohn não precismaos defirnir o tipo de daods da variável, o prorpio python faz isso automaticamente, por isso nao podemos simplmemste ciruar uma variavel sem atribuir um valor. Para alterar o valor d variavel basta fazer uma atribuição de um novo valor


* Constantes: Assim como as variavies,as contantes são utilizadas para armazenar valores. Uma cosntante nasce com um valor e permanece com ele até o final da execução do rpograma, ou seja, o valor é imutável

Python não tem constantes Não exsite uma palavra reservada para informar ao interpretador que o valor é constante, em python usamos a convenção que diz ao progranadir que a variavel é uma constante

-----------

#### Conversão de Tipos de dados ####

* Em alguns momentos é necessario converter o tipod e uma variavel para manipular de forma diferente. Por exemplo:
variaveis do tipo string que aramazenam números e precisamos fazzer alguma operação matmática com esse valor


-----------

#### 🔜 Funções de entrada e saida 🔙

Receber informações e retornar elas ao usuario.

* Função Input: é utilizada quando queremos ler dados da entrada padrão(teclado). Ela recebe uma arguemntos do tipo string, que é exibido para o suaurio na saida padrão(tela). A função lê a entreda, converte para string e ternona o valor

* Função Print: é utilizada quando queremos exibir dados na saída padrão(tela). Ela recebe um argumentos obrigatorio do tipo varargs de objetos e 4 argumentos opcionais(sep,end, file e flush). Todos os obejtos são convertidos para string, separados por sep e termianos por end. A string final é exibida para o usuario

-----------

### Operadores *️⃣

#### Operedores Aritiméticos

São operadores que executam contas matemáticas, como adição, subtração, multiplicação e divisão, ver no exemplo de codigos!

#### Operedores de Comparação

São operadores que comparam dois valores. comparam duas variavies ou constantes conforme o que você desjear

#### Opeadores de atribuição

A atribuição de valores é a passagem de informação a determinada variável. Na linguagem Python tem definido que o sinal de igual (=) é o operador de atribuição.É possivel sobrescrever ou adicionar uma variavel já criada atribuindo a mais um  valor

#### Operadores logicos

São operadores utilizados em conjutno com os operaodes de comparação, para montar um expressão logica. Quando um operador de comparação é utilizado, o rsultado é um booleano, dessa forma pdoemos combinar opeardores de comparação com os opeadores logicos

#### Operadores de identidade

Os operadores de identidade servem para a comparação de objetos. Nessa comparação é verificado se eles ocupam a mesma posição na memória, o que significará que se trata do mesmo objeto


#### operadores de associação
São operadores que utilizados para saber se um objeto está presente em uma sequência, PODE SER QUALUQER OBJETO!


--------------------------

#### Estruturas Condicionais e de repetição 

Aprender como o interpretador Python utiliza a indentação do código para delimitar os blocos dde comandos

Identar códgio é uma forma de manter o código fonte mais legível e manitennível. MAs em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina


------------------

#### Estruturas Condicionais  

 Estrutura condicional  permite o desvio de fluxo de controle, quandod etermianas exepressões lógicas são atendidas

* if: para cirar um estrutura condiconal simples, composta por um unico desvio, podemos  utilizar a palavra reservada if. O Ocmnaod irá testar a expressão lógica, e em caso de retorno verdadeiro ações presentes no bloco de código do if serão executadas

* if/else: para criar um estrtura condcional com dois desvios, podemos utilizar as palavras reservadas if e sle. COmo sabemos se a expressão lógica testada no fi for verdadeira, então o bloco de código do fi será executado. caso contrário o bloco de codigo do else se´ra executado

* if/elif/else; Em alguns cenários queremos mais de dois desvios, para jssl podemos utilizar a palavra reservada elfi. O elif é composto por uma nova expressão lógica, que será testada e caso retrone verdaderio o bloco de codigo do elif será executado, Não existe um numeor maixmo de elifs que podemos utilizar, porem evite ciriar grandes estrturas condicionais, pois elas aumentam a compexidade do codigo

* If aninhado, podemos criaar estruturas condiconais aninhadas, para isso absta adiconar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else

* If ternário: permite escrever uma condição em uma única linha. ele é composto por três partes, a primeira parte é o retorno casp a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caos a expressão não seja atendida


-------------

#### Estruturas de Repetição

* O que são estruturas de repetição?: São estruturas para repetir um trecho de código um determiando número de vezes. Esse número pode ser conehcido previamente ou determiando atrés de uma expressão lógica

* Comando for é usado para percorrer um objeto iteravel. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código de ve ser executado, ou quando queremos percorrer um objeto iterável

* Função Range é uma função built-in do python, ela é usada para produzir uma sequencia de nuemros interios a partit de um inicio(inclusivo) para um fim(excluviso). Se usarmos range(i, j) será produzindo:
i, i+1,i+2,i+3
ELA recebe 3 arguemntos: stop(obrigatorio), satrt(opciona)l e step opcional))

* O comando while é usado para repetir um blocod e codigo varias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de codigo deve ser executado

------

#### Manipulando String com Python

   
  A Classe String do Python é famosa por ser rica em méteodos e possuir uma interfcae muito fácil de trabalhar.
  Em algumas linguagens manipular sequência de caracteres não é um trabalho trivial, em Python esse travalho é muito simples


  ```
  curso = "Python" 
  ```


``` 
print(curso.upper())
-> o valor retorna interamnete em maiusculo
```

``` 
print(curso.lower())
-> o valor retorna interamnete em minisuculo
```

``` 
print(curso.title())
-> o valor retorna com a pirmeira letra em maisucla
```
``` 
print(curso.strip())
-> o valor retorna sem espaço no terminal 
```

``` 
print(curso.lstrip())
-> o valor retorna com espaço a direita no terminal
```

``` 
print(curso.rstrip())
-> o valor retorna com espaço na esquerda
```
```
print(curso.center(10, "#"))
-> o valor retorna atqe que a astring tenha 10 caracteres, ele adicona o que esta em "x" para completar 
```

```
print(".".join(curso))
-> o que esta entre "x" retorna entre os caracteres dovalor da String 
```

* Interpolação de variavel  em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o metodo format e a última é utilizando f strings.A primeira forma não é atualmente recomenda e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 ultumas

* Fatiamneto de String: fatiamneto de strings e uma tecnica utilizada para retornar substrings( partes da string original), informando inicio(start), fim (stop) e passo(step): [start: stop[step]]

* Strings de multiplas linhas: Strings de múltiplas linhas são definidas informandos 3 aspas simples ou duplas duranre a atribuição. Elas podem ocupar várias linhas de codigo, e todos os espaços em branco são incluídos na string final

---------------

### Estrutura de dados

#### Trabalhando com listas ede dados

* Criando listas: Listas em python podem armazenar de maneira sequencial qualuqer tipo de objet. podemos criar listas utilizando o construtor lits, a função rangeou colocando valores separados por virgula detro de colchentes. Listas são obejtos mutáveis, portanto podemos alterar seus valores após a crialção

* Acesso direto: a lista é uma sequencia portanto podemos acessar utilizando indices. Contamos o indice de determinada sequenncia a aprtir de zero

* listas aninhadas

Listas podem armazenar todos os tipo de obejtos Python, portanto podemos ter lsiras que armazenam outras listas. COm isso ppodemos criar estruturas bidimensionais(tabelas), e acessar irnfomando os  indices de linha e clouna

* Fatiamento: alem de acessar elemntos diretamnete, podemos extrair um conjuto de valores de uma sequencia. Para isso basta passar o indice inicial e/ou final para acessar o conjuto. Podemos ainda informar quantas posições o curuso deve pular no acesso

*Iterar lsitas; a forma mais comum para percorrer os daos de uma lista é utilizando o comando for

* Função enumerate: ás vezes é necessario saber qual o indice do obejto dentro do laço for, para isso podemos usar a função enumate

* Compreensão de listas: A compreensão de lista oferece uma sintaxe mais curta quando voc~e deseja: criar uma novalista com base nos valores de uma lsita existente (filtro) ou gerar uma nova lista aplicando alguma modificacao nos elmentos de uma lista existente


