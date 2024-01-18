
# Desenvolvimento Backend com Kotlin
## Conhecendo o Kotlin e sua DocumentaÇÃO oficial

Percurso:

- 1 Introdução ao Kotlin
- 2 Como instalar o Kotlin
- 3 Por que Kotlin

#### Introdução ao Kotlin

Koltlin é uma linguagem de programação um tanto quanto recente, mas já madura, destinada a tornar os desenvoolvedoras mais felizes.

è concisa, segura, interoperal com Java e outras lingaugens, alem de oferecer muitas maneiras de retulizar codigo entre varias plataformas para uma programação produtiva

##### Instalçaõ do Koltin:

Koltin esta incluso no IntelliJ IDEA e Andorid Studio. entretando podemos usar o Kotlin sem nenhum desses IDEs, atraves do Kotlin PlayGorund

### !ver caderno de estudos para mais links e infomações!

Por que o Koltin?:

é concisa, segura, interoperal com Java e outras lingaugens, alem de oferecer muitas maneiras de retulizar codigo entre varias plataformas para uma programação produtiva

##### Introdução Prática à Linguagem de Programação Kotlin

Dominar a sintaxe do Kotlin atraves de exemplso (hands on) Embora ler sua documentação seja facile agradavel, aprender na pratica e mais eficaz

##### Introdução ao Kotlin na pratica

- Ola mundo
- O baisco sobre funções
- variaveis
- Null Safety
- classes 
- generics

Tdos os exercicios serao retirados pela propria documentação do Kolti, visualizar exerciciosno site

Existe um pacote padrão, quando voce não definir um pacote para o codigo que voce esta escrevendo.

Inix Functions and operator Functions

Declarar função no Kotlin: 


            Fun nome da funcao() {
                  // bloco de codigo
            }

no Koltlin, podemos escolher caso se a função retorna alguma coisa ou não.

No Kotlin, não existe a contenação, fazendo assim a lingaugem de programação ser menos verboso que outras linguagens e mais limpo para que alguem possa ler e entdner o codigo

As funções podem ser declaradas fora do main, sendo depois puxados para dentro do main

* Parametros do tipo VARagr:  é um tipo de parametro uma quantidade indefinida de um determinado objeto, por exemplo: 

      fun printMessage(message: String): Unit 
      {                               
      println(message)
      }

vemos que nessa função do tipo VARagr, ele aceitara todos os objetos do tipo String, que foi defenido na propria sintaxe. è como se fosse uma lista.

* variaveis no Kotlin:

var: uma variavel mutavel, que se pode mudar a qualuer hora no codigo

val: uma constante, não se pode mudar o valor dessa variavel ao percorrer do codigo

VER EXEMPLOS NOS CODIGOS DE KOTLIN.

* Null Safety:

Declara e trata aquela variavel que pode, ou nao, ser nula

   - var neverNull; o valor nesse tipo de variavel nunca pode ser nula.

   - var nullable: a variavel pode sim ser seu valor como nula

   - var inferredNonnNull: o compilador assume que o valor sera não nulo

* classes:

Estruturas de dados que a gente consgeue moldar a apartir de nossas necessidades. e um modelo para a criação de objetos

estrutura de uma classe:

          class 'nome da classe'("variaveis que voce desjea declarar)

----


          class Customer                                  // 1

          class Contact(val id: Int, var email: String)   // 2

           fun main() {

            val customer = Customer()                   // 3 instaciando a classe
    
            val contact = Contact(1, "mary@gmail.com")  // 4 criado um objeto a apartir da classe

            println(contact.id)                         // 5
            contact.email = "jane@gmail.com"            // 6
}

##### Estruturas de Controle de fluxo e Coleçoes em Kotlin

* Objetivo Geral: Explorar as principais estruturas condicnionais e de rpetição (controle de fluxo), além de conhecer allgumas das principais Coleçoes do Koltin.

- Controle de fluxo

    - When
    - Loops
    - Rangens
    - Verificações de Igualdade
    - Expressoes condicnionais

- Coleções:
     
     - Listas (list)
     - Conjuntos
     - Mapas
     - Extension Functions


* When: equivalente ao switch case de outras linguagens de porgramação, o when é basicamnete a mesma estrutura condicional, porem amais maleav2el e facil de trabalhar com ele no seu codigo

Tipo Any: pode recebr qualquel coisa como paramentro, pode ser qualquer tipo de dados

* When Expression: ao inves de executar uma instrução, agora ele esta fazendo uma atribuição, uma função que recebe qualquer coisa e retorna qualquer coisa, aqui etsamos verificando os valores de entrada, para que possamos fazer uma verificação


* Loops: For, While, do-while, iterators

laços de repetição, que intera cada elemento dependenod da necessidade.

Iterator: são implementações de algo ser interado percorrendo elemntos de uma estrutura de daos, no kotlin ele da a possibilidae implementar interator personalizados dentro das nossas classes, instancia interavel

* Ranges:

   - Intervalos dentro da lingaugem de porgramação do Koltin, eles são ferrmanetas que capacitam de fazer nosso codigo mais limpo

   - podemos usar ranges em estrturas de repetiçao, veja alguns operadores de ranges:

           for(i in 0..3)
           for(i in 0 until 3)
           for(i in 2..8 step 2)
           for(i in 3 downTo 0)

##### Equality Checks:

Existem duas formas de decalrar igualdades de um objeto

Comparação Referencial: Sintaxe de tres iguais (===)

Comparação Estrutural: Sintaxe de dois iguais (==)

Sintaxe: 

```

fun main() {


  val authors = setOf("Shakespeare", "Hemingway", "Twain")
  val writers = setOf("Twain", "Shakespeare", "Hemingway")

  println(authors == writers)   // 1 true, por causa que os elemntos Existem em ambas listas
  println(authors === writers)  // 2 false, a ordem da lista não foi respeitada

}


```

##### Estruturas de dados

- List: uma lista e uma estrtura de daos ordenanda, uma lista mutavel ou imutavel conforme nos instacianos no codigo, como por exemplo:

listof(): criação de uma lista imutavel, apenas que podemos acessar-lá e não mudar sua estrutura

mutablelistof(): criação de uma lista mutavel, podemos acessar e mudar sua estrutura, acresentado valores, modificando, etc.


- Set: No Kotlin, a função set não é chamada explicitamente, mas é parte do suporte à sintaxe para operações de atribuição em propriedades. Ela é usada em conjunto com a função get para criar propriedades que podem ser acessadas e modificadas como campos públicos, mas permitem controle personalizado sobre o comportamento de atribuição. A função set é automaticamente acionada quando um valor é atribuído à propriedade

- Map: como a list, tambem existe as mutaveis e as imutaveis
