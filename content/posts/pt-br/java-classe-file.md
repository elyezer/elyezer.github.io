+++
title = "Java - Classe File"
date = "2007-08-07T20:45:00-03:00"
category = "Posts (pt_BR)"
slug = "java-classe-file"
+++

Nesse post falarei um pouco sobre a classe
[File](http://java.sun.com/javase/6/docs/api/java/io/File.html) do
[Java](http://java.sun.com). A classe se encontra no pacote
[java.io](http://java.sun.com/javase/6/docs/api/java/io/package-summary.html).
Com dessa classe pode-se fazer algumas operações em um determinado path
(caminho), sendo para um arquivo ou mesmo um diretório.

Mostrarei alguns métodos da classe com alguns exemplos simples. Intuitivamente
pode-se notar que em se tratando de arquivos, conseguiremos descobrir seu
tamanho, ultima modificação... É possível também verificar algumas permissões,
como por exemplo, de leitura e escrita (pode-se notar essas permissões mais
facilmente em sistemas como o [Linux](http://ubuntu-br.org/)).

Começando veremos como passar um caminho para que possamos verificar alguns
atributos. Primeiramente devemos pegar um caminho e logo em seguida instanciar
um objeto do tipo da classe File, passando como argumento do seu construtor o
caminho, portanto, devemos fazer algo assim:

```java
String caminho = new String("/home/usuario/caminho/do/arquivo");
```

Isso em ambiente [Linux](http://ubuntu-br.org/), ou, se preferir em ambiente
Windows:

```java
String caminho = new String("C:/caminho/do/arquivo");
```

Lembrando que o caminho pode ser para um arquivo ou para um diretório (pasta).
Para ilustrar o que foi feito até agora, instanciamos um objeto do tipo String
(sequência de caracteres) , e passamos em seu construtor o caminho para o
arquivo ou diretório. Seria o mesmo que criar uma variável do tipo string e
atribuir o caminho à essa variável.

Agora o que temos que fazer é instanciar um objeto da classe File para analisar
alguns atributos desse caminho:

```java
File path = new File(caminho);
```

Note que passamos como argumento o objeto caminho criado anteriormente, é
possível passar o caminho diretamente no construtor:

```java
File path = new File("/home/usuario/caminho/do/arquivo");
```

Com o objeto path instanciado, podemos agora conhecer alguns métodos para
verificarmos algumas propriedades do caminho passado, lembrando que para se
utilizar um método de um objeto, basta fazer o seguinte:

```java
objeto.nomeDoMetodo();
```

Portando, se queremos verificar se o caminho passado é um arquivo basta usar o
método isFile(). Isso poderia ser verificado assim:

```java
if(path.isFile()) {/*ações*/}
```

Como o método isFile() retorna um boleano, podemos colocá-lo diretamente como
argumento do comando if, ou seja, se retornar um valor true (verdadeiro, ou
seja, é um arquivo) ele executa o bloco {/\*ações\*/}.

Conhecendo como utilizar os métodos dessa classe, agora podemos conhecer alguns
outros métodos bastante interessantes e úteis:

```java
boolean canRead(); //Verifica se tem permissão para leitura
boolean canWrite(); //Verifica se tem permissão para escrita
boolean exists(); //Verifica se o caminho passado existe
boolean isDirectory(); //Verifica se o caminho é um diretório
boolean isAbsolute(); //Verifica se o caminho passado é absoluto
String getAbsolutePath(); //Retorna o caminho absoluto
String getName(); //Retorna o nome do arquivo ou diretório
long length(); //Retorna o tamanho do caminho
long lastModified(); //Retorna a ultima modificação do caminho
```

Se caso você desejar conhecer mais sobre a classe File visite [o manual da
API](http://java.sun.com/javase/6/docs/api/java/io/File.html). Com essas dicas
pode-se criar várias coisas interessantes. Criarei um programa que ao se passar
um caminho (path), ele fala algumas informações sobre o mesmo, e
disponibilizarei o código aqui para estudo.

Até mais.
