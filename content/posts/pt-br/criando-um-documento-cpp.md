+++
title = "Criando um documento C++"
date = "2006-09-25T23:23:00-03:00"
category = "Posts (pt_BR)"
tags = ["c++", "cpp"]
+++

Vamos ver como se cria um documento de código C++, precisamos, inicialmente, de
um compilador. Recomendo o Dev C++ para Windows ou o
[Anjuta](http://anjuta.sourceforge.net/downloads) para
[Linux](http://www.ubuntubrasil.org/), o compilador será necessário para
compilar e para criar o executável do programa.

Basicamente, o compilador é um editor de texto, que converte o arquivo digitado
para um programa. Em outro post explicarei melhor como criar um arquivo no Dev
C++, e no [Anjuta](http://anjuta.sourceforge.net/downloads). Por enquanto
veremos a estrutura basica de um documento C++.

O corpo do aruivo é, basicamente, declaração das bibliotecas e as funções,
devendo, ao menos, conter a função main. Um exemplo simples de documento:

```cpp
#include <iostream> //Biblioteca padrão que iremos utilizar

int main() {
  //comandos
  return 0;
}
```

Existem outras formas de se usar a função main, mas sempre, um documento C++
deve conter ao menos essa função.

O texto depois de `//`, é considerado como comentário e, sendo assim, será
descartado pelo compilador no momento em que o arquivo for compilado. Para
comentários que envolvem mais de uma linha, devem ser delimitados por `/* */`.

Exemplo:

```cpp
// Tudo que vier após as duas barras sera descartado até o final da linha

/* Esse é um comentário que pode abrangir mais de uma linha.
   Sendo assim, tudo que é delimitado será descartado. */
```

Comentários são importantes, para indicar certas partes do programa ou explicar
alguma parte e, ainda, se um mesmo programa for escrito por mais de uma pessoa,
é importante para indicar modificações e/ou necessidades do projeto.

É somente uma noção da linguagem, após de abordar como criar um documento nos
compiladores, começaremos a digitar nossas primeiras linhas de C++.
