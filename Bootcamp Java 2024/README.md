# Bootcamp Java 2024

### Principios de Desenvolvimento de Sofwtare Colaborativo


Conhecer a estrutura, a historia de criação e evoluça~p da linguagem java, além de suas plataformas, instalação e utilização de IDEs para Desenvolvimento   

- Obejtivos

    - Apresnetar a historia da linguagem Java   
    - Explorar os recursos de cada plataforma 
    - Configurar o ambiente para Desenvolvimento
    - Definir uma IDE e aumentar nossa produtividade


- Jasa basico

A linguagem de java é composta por um conjunto bem defiido de funcionalidades (features).

Java e uma linguagem de programação simples e fácil de entender, pois não contem complexidades que existiam em linguagens de programação anteriores, na verdade, a simplicidade era o objetivo do design dos povos Javasoft, pro que ele tem que funcionar em dispositivos eletronicos

é uma linguagem de programação orientada a objetos. Isso significa que em Java tudo é escrito em termos de classe e objetos

## Dominiando a linguagem de programação Java

IDes, para auemnatr nossa produtividade, nós podemos escolher algumas ferramentas denominadas de IDE - integrated Development Environment ou Ambinete de Desenvolvimento integrado. é um Sofwtare que dispoe de recursos que auxiliar no Desenvolvimento

- Aceleração de nossa escrita com Auto-Complete ou IntelliSense

- Formatação de palavras e blocos de codigos

- Análise de erro de sintaxe

- Compilação de programação

- Depuração (acompnahemnto) de excução o programa

    * classe executavel: uma classe capaz de incializar o conteudo do codigo dentro do projeto

    ```
    public static void main(String[] args) {
         // bloco de codigo   
        }
    ```

- Declarar uma variavel em Java segue sempre a seguinte estrutura:

    ```
    // estrutura

    tipo nomeVariavel = atribuição (opcional em alguns casos)

    // exemplo

    int idade = 23;
    double altura = 1.63

    ```
    - Declarar meteodos em Java segue sempre a seguinte estrutura:

    ```
    // estrutura

    tipoRetorno NomeObjetivoNoInfinitivo Parametros(s)

    // exemplo

   int somar ( int Numero Um, int NumeroDois)
    ```

IDES:

- Eclipse: é uma alternatica muito comum de encontrar ambinetes de Desenvolvimento, pricinciplamente pelo aspecto de uma interface simples, pligins para recursos adicionais, atalhos para operações de meni e de escrita e para quem trabalhar com Java Swing

- IntellliJ: é uma plataforma de codgio aberto para criação de IDes e  ferramnetas para desenvolvedores, mas nem todos os recusros estão disponiveis de forma gratuita

- VSC: Desenvolvido pela Microsoft, é um editor de texto muito simples e interativo que conta com inumeras extensoes, temas variados e integraçãp com tecnologias como NOdeJS e Java

- crtl + shift + p: aparece a opção de criar um novo projeto jaba, ele ja cria todos os coumentos possiveis

#### Sintaxe basica do Java

- Apresentra as regras essenciasi para a ccontrução de códigos com base na linguagem Java

- Anatomia da Classe: basicmanete consolidar tdodo aspectal estrutural da linguagem, seus por ques resumidamente

- Arquivo.java: Todo arquivo .java deve começar com a letra maiuscula. Se a palavra for composta, as segunda palavra deve também ser maiuscla, exemplo: 
        - Calculadora.java
        - CalculadoraCientifica.java

- Nome da classe do arquivo: A Classe deve posssuir o mesmo noeme do arquivo.java

- Objetivo: Explorar os tipos de dados numericos inteiros, numericos decimais, lógicos, cacteres e suas aplicabilidades. Explicar a diferencia entre definição de variaveis e constantes

    - nuemricos inteiros
    - tipos logicos
    - caracteres
    
###### os oito tipos primitivos em Java são

- int
- byte
- short
- long
- float
- double
- char

esses tipos não são considerados obejtos, e portanto representam valores brutos. Eles são armazenamdos diretamente na pilha da memoria

```
<tipo> <nomeVariavel> <=> <atribuiçãoDeValor>
```

* TIPOS DE OPERADORES

    - operadores aritmeticos
    - ||         ternario

            *   ```
            <expressao Condicional> ? (caso condição seja true) : (caso condição seja false)
            ```
    - ||         logicos
    - ||         relacionais
    - ||         unários
  


###### regras para a construção de uma variavel

1. deve conter apenas letras, underline (_), $, ou os numeros de 0 a 9
2. Deve iniciar com uma letra minuscla (boa pratica)
3. Nao pode conter espaços
4. Nao podemos usar palavras chave da linguagem
5. O nome deve ser unico dentro de um escopo

- Identação: BAdicamnete indetar é um termo utilizado para escrever o codigo do programa de forma hieráquica, facilitando assim a vissualização eo entendimento do programa

###### Java Beans

Uma das maiores dificuldades na programação é escrever algoritmos legíveis a n´veis que sejam compreeendidos por todo seu time ou por voce mesmo no futoro. Para isso a lingagem Java sugere, atrasves de conveções, formas de escrita universal para nossas classes, atributos metodos e pacotes

###### assuntos

- Estrutura inical
- Padrão de nomeclatura
- Declarando variáveis e métodos
- Identação
- Organização arquivos
- java Beans

###### metodos

- apresentar ccireteieros para criação de meteodos, parametros e visibilidade

- qual a porposta principal do mteodo

- qual o tipo de retorno esperado apos executar o meteodo

- quais os parametros serao necesarios para ececução do metodo

- o metodo possui o risoc de apresentar alguma exceção

- qual a visibilidade do metodo

Meteodos: 

todas as ações das aplicações são consideradas metodos. Uma classse é definida por atribuitos e metodos. em sua grande maioria, variavies de diferentes tipos e valores. Os mmteodos, por usa vez, correspondem as funções diposivenis dentro de nossas classes

- deve ser noemado como verbo

- seguir o padrao camelCase (todas as letras minusculas com a exceção da primeira letra da segunda palara)

- atenção não exsite em javva o conceito de mteodos globais. Todos os metodos devem sempre ser definidos dentro d eum classe


```
public double somar (int num1, int num2){
    // logica - finalidade do metodo
    return ...
}

public void imprimir(String Texto){
    // logica - finalidade do meteod
    // esse tipo de meteodo noa precisa de retorno
}

public double dividir(int num1, int num2) throws exeception{
    // thors exception: indica que o meteodo utilizado podera gear uma exceção
} 

private void meteodoPrivado{
    // esse metodo nao estara visivel por outra calsse
}
```

###### Escopo

- escopo de classe
- escopo de metodo
- escopo de fluxo

Escopo pode ser entenido comom o ambinete onde uma varivael pode ser acessa. em Java, o escopo de variaveis vai de acordo com vloco onde la foi declarada

###### palavras reservadas

palvras reservadas são identifcadores de uma lingaugem que ja possume uma finalidade espeficia, portanto nao pode serm utilizados para nomear variaveis, classe, meteodos ou atributos

A lingaugem Java possui  52 palavras reservadas

###### java Doc

Apresnetar a ferramneta de documentação da linguagem e explorar como adicionar comengarios em nossso arquivos

###### Terminal e Argumentos

- explorar opções de entrea e saida simples de daods em uma aplicação em Java

- permite que o coidgo java seja executado via terminal

#### Introdução e Estruturas Condiconais com Java
 
- Controle de fluxo

    Controle de fluxo é a habilidade de ajustar a maneira como um programa realiza suas tarefas. Por meio de instruções especiais, chamadas de comandos, essas tarefas pode ser executadas seletivamnete, repetidamente ou ex epcionalmente



Porposta do curso: apresnetar os conceitos e explorar os tipos  de fluxox condicional, excepcional e de repetição em uma aplicação JAva

Assuntos:

    - Estruturas condicionais: if-else, switch-case
    - Estruturas de repetição: for, while, do - while
    - Estruturas de exceções: try-catch- finally, throw


A estrutura switch compara o valor de cada caso com o da variavel sequecialmente, e smepre que encontra um valor correpondente, executa o coidgo asssociaod ao caso. para evitra que as comparações continuem a ser executadas apos um caso correpsondete ter sido encotrado, acresentamos o comnaod break no final de cada bloco de codigo

    - Se optarem por usar switch / case, estudem um pouco sobre os conceitos continue, break e default

Laços ourepetições são representadas pelas seguiintes coisa 

- for (para)
- while ( enquanto)
- do while (faca enquanto)

estruturas excepcionais

 - De froma interpretativa em Java, um erro é algo irreparável, a aplicação trava ou é necerrada drasticamente. Já exceções é um fluxo inesperado da nossa aplicação.


 * java. lang. nullPointerException : quando tentamos obter alguma informaçõa de uma variavel nula

 * java.lang.Arithmeticexception: quando tentamos dividri um valor por zero

 * java.sql.SQLException: quando existe algum erro relacionado a ingteração ao banco de dados

 * java.io.FileNotFoundException: quando tenatmos ler ou escrever em um arquivo que não existe
## POO com Java

## Testes e Gereciamento de dependências em projetos JAVA

## banco d eDados SQL / NoSQL para desenvolvedores backend

## ganhando produtividade no Java com spirng framework
