# Introdução a linguagem de progrmação C#
## Introdução e dominação ao .NET

- Obejtivo Geral: Apresentar a historia do .NET, como surgiu, aplicações e o que voce pode fazer com ele. A evoulução da plataforma .Net, principais IDEs, Apresentar de maneira prática seus fubdamentos e suas logigas de programação, ccrinado algoritmos para deostra seu desempenho

Percuso:

* Introudção ao.NEt,  historia, versoes, usos
* Diferenças entre .NET Framework (legado) e .Net
* Compilador .NEt e seu funcimaoneto
* Configuraçãp do amibiete e IDEs
* Sintaxe e Indetação
* Tipos de daods
* Operadores de atribuição
* Operadores condicioanis
* operadores lógicos
* operadores aritmeticos e a clasee Math
* Estruturas de repetição
* Estrutura de um programa e meteodo principal
* Array List

#### Introudção ao.NEt,  historia, versoes, usos

O .Net é uma plataforma de desenvolvimento unificado que permite a construção de sistemas e aplicções, ou seja o .NEt é um tipo de IDE. è mantiddo e foi cirado pela microsoft, e uma open source. Pode desevolver os seguintes plataformas, ela trabalha com tres linguagens: C#, F# e Visual Basic

O .NET fornce as seguintes bibliotecas:

- Desktop
- Web
- Mobile
- Gaming
- Iot (intert of things)
- AI

C# é uma linguagem de porgramação usada no .NET

###### historia do .NET

A microsoft começou a trabalhar no C# no finaldo dos anos 90, tendo sua primeira versao do framework lancanda em 2002, tendo como obejtico competir com o JAva.

O conceito de multiplatadofrma era estrondoso na época, e a microsoft trabalhou em melhorias e implementações di sistema em sua plataforma, mas foi impeida pela Sun

Isso o motivou a microsoft a desevolver um ecossietma intregado ao windows, que fosse facil paara deswolvover aplicativos desktop e web, e que fosse amarrado apenas ao windows, aumentando assim a sua revelancia

#### Diferenças entre .NET Framework (legado) e .Net

 O que é framework? é um conjunto de códigos prontos que servem como estrutura para auxiliar no desenvolvimento. Esses códigos trazem funcionalidades já determinadas para agilizar o processo e evitar que as pessoas tenham que reescrever essas funções frequentemente.

 A versao .NEt, que é a versão mais atual, foi reescrita do zero, para funcionar em multiplatarformas, e não somente em uma plataforma, sua ultima versao é a 4.8

 A versão .NET Framerwork foi criado e escrito apenas para funcionar na plataforma windows, onde ja bvem pre-instalado, e impossivel rodar em outras plataformas, como o linux e MAC, sua ultima versao é a 3.1

 #### Compilador .NEt e seu funcionamento

 Smepre quando queremos mudar ou alterar algo do nosso codigo, nos iremos utilizar o compilador .NET para realizar essas mudanças

 - Lingaugem de alto nivel: A linguagem que entedemos e escrevemos nosso codigo fonte

 - linguagem de baixo nivel: A linguagem que a maquina entende, posssui ouca abstração, sendo dificil de entender

O que é um compilador: è um programa que realiza a conversão de linguagem de alto nível para baixo nível. Caminhos para a realização desse compilador

High Level Language => Lexical analyser => Synrax analyser => Intermediate code generator => Code Optimizer => Code generator => Machie Code 

- Compilador: é um programa que realiza a conversao de linguagem de alto nivel para baixo nivel. Exemplo: C#, Java

- Transpilador: é a conversao de uma linguagem ou implemmetação para outra/ A sua Saida permanece em linguagem de alto nivel

Linguagem compilada: São lingaugens o codigo fonte é traduzido para o codgio de maquina. Exemplo; C#, Java

lingaugem interpretada: São linguagens que fazem a leitura e interpretação diretamente do codgio fonte. Exeplo: javaScript Php

 #### Configuraçãp do amibiete e IDEs

 O que é uma IDE?:

 Uma Ide (integrad development Environment), ou amibiente de desevolvimento inttregado, é um software que facilita e integra diversas facilidaaes para a escrita e deupuração do codigo

 Visual Studio é a pricnipal IDE para o .NET com susporte para outras linguagens de programação, e gratuita, o debug rico em detalhes

 Visual Studio Code e um editor de texto usado para facilitar o desevolviemnto de diversas linguagens, totalmente fratuito, possibilidade de instalar extensões, Muito leve em performance

 Rider: tambem é um IDE para o .NEt, rico me funcionalidades, Forte integração com o .NET, facilidade em trabalhar com o Unity, Recomnedações de refatoração de código, atalhos e comando que aumentam a produtividade


- E nessario baixar o .NET SDK no site da microsoft.

Apos nos instalamos o .NET SDK, vamos para o visual studio code e utilizaremos o terminal, sempre que usamos algo relacionado comm o >NEt, temos que digitar primeiro o dotnet

```
dotnet new console
```

ele cria um novo projeto em dotnet

Instalar um extensão que vai facilitar o decorrimento das ualas e aprendizado do coidgo C#

C# extensions for JosKreativ

#### Sintaxe e Indetação

Vamos estudar como é composto um projeto, classes e suas convenções no C#

nessa etapa sera algo mais pratico, logo os programas fetiso estarao no repositorio

     dotnet --info

codigo que mostra as informações sobre o arquivo .NET instalado na maquina



```
dotnet new console
```

quando executamos esse codigo é cirado dois arquivos e duas pastas

arquivos:

- Program.cs
- NomedaPasta.csproj
   - um arquivo de projeto do c#, nele contemos algumas essssecnias que sao descritivas do projeto, ou seja, sao metadados, linguagem xml

Pastas:
- bin
- obj

essas pastas são geradas automaticamentes, que sao um estrutura basica do projeto.

criação de arquivos json para docuemtação do projeto.

criação da primeira classe e entender sua estrtura e organização dentro do visual studio code

Toda nome de classe tem que comecar com letra maiuscula

      prop

- atalho no C# para a criação de uma prorpiedade dentro do C#

nao importa a ordem, de atributos e meteodos dentro de um classe

Toda ação temos que fazer no Program.cs pq ele é o ponto de entrada do sistema 




