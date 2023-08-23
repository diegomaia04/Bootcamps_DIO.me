# 🖥️Python!

🤖[link importante para python](https://wiki.python.org.br/PythonBrasil)🤖
---
### Principais conceitos de python

#### Dados ####


* Existem tipos de dados na linguagem python. Eles servem para definir as caracteriscas e comportanementos de um valor(objeto) para o programa. Os tipos são: 

Texto > ``` srt ``` 

Numerico > ``` int && float && complex ``` 

Sequência > ``` list && tuple && range ``` 

Mapa > ``` dict ``` 

Coleção > ``` set && frozenset ``` 

Boolenao > ``` bool ``` 

Binário > ``` bytes && bytearray && memoryview ```

---------

#### Modo Interativo ####

O interpretador Python pode executar em modo que possibilite o desevolvendor a escrever o codigo e ver o resultado na hora. Existem duas formas de inicar o modo interativo: 

* Escrevendo (python)  no terminal de comando do vscode, para sair do modo interativo do termianl é ```exit()```

* executar o script com a flag -i( sendo que "flag" é o nome do arquivo que vc deseja executar)

-----------

#### Função dir e help ####

* dir: Sem arguemntos, retorna a lista de nomes no escopo local atual. Com um argumrntos, retorna uma lista de atributos validos para o objeto. Exemplo: 

```dir()- Sem Arguemntos ``` 

```dir(100)- Com Arguemntos ```

* help: Invoca o sistema de ajuda integrado.è possível fazer bsucar em modo interativo ou informar por parametro qual o nome do modulo, função, classe, meteodo ou variavel ele fala qual são os argumentoss que o mteodo recebe e o que ele retorrna. Exemplo:

```help()- Sem Arguemntos ``` 

```help(100)- Com Arguemntos ```


-----------
#### Variaveis e Constantes ####


* Variaveis em lingaugens de programça~p podemos definir valores que sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variaveis pois eles nascem com um valor e nao necessariamnete deem pernacem com o mesmo durnate a execucao do programa.

Em Pytohn não precismaos defirnir o tipo de daods da variável, o prorpio python faz isso automaticamente, por isso nao podemos simplmemste ciruar uma variavel sem atribuir um valor. Para alterar o valor d variavel basta fazer uma atribuição de um novo valor


* Constantes: Assim como as variavies,as contantes são utilizadas para armazenar valores. Uma cosntante nasce com um valor e permanece com ele até o final da execução do rpograma, ou seja, o valor é imutável

Python não tem constantes Não exsite uma palavra reservada para informar ao interpretador que o valor é constante, em python usamos a convenção que diz ao progranadir que a variavel é uma constante

-----------

#### Conversão de Tipos de dados ####

* Em alguns momentos é necessario converter o tipod e uma variavel para manipular de forma diferente. Por exemplo:
variaveis do tipo string que aramazenam números e precisamos fazzer alguma operação matmática com esse valor


-----------

#### Funções de entrada e saida

Receber informações e retornar elas ao usuario.

* Função Input: é utilizada quando queremos ler dados da entrada padrão(teclado). Ela recebe uma arguemntos do tipo string, que é exibido para o suaurio na saida padrão(tela). A função lê a entreda, converte para string e ternona o valor

* Função Print: é utilizada quando queremos exibir dados na saída padrão(tela). Ela recebe um argumentos obrigatorio do tipo varargs de objetos e 4 argumentos opcionais(sep,end, file e flush). Todos os obejtos são convertidos para string, separados por sep e termianos por end. A string final é exibida para o usuario



❗Para documentar algo na linguagem python se usa "#" ❗



