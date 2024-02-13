+++
title = "Diferença entre == e is no Python"
date = "2013-03-21T23:28:00-03:00"
category = "Posts (pt_BR)"
tags = ["python"]
slug = "diferenca-entre-e-is-no-python"
+++

Uma dúvida comum aos que estão iniciando os estudos em Python é a diferença
entre os operadores `==` e `is`, nesse post vamos estudar um pouco mais sobre
eles.

De forma resumida, o operador `==` analisa se os **valores** de dois objetos
são iguais, já o operador `is` verifica se os dois objetos são o **mesmo
objeto**.

Assumindo a definição de cada operador, como explicar a seguinte situação:

```python
>>> n = 5
>>> n == 5
True
>>> n is 5
True
>>> l = [1]
>>> l == [1]
True
>>> l is [1]
False
```

No primeiro teste, estamos utilizando objeto do tipo `int` já no segundo
estamos utilizando objeto do tipo `list`. Observe que ao utilizar `int` os
operadores retornam o mesmo valor, já ao utilizar `list` os resultados
retornados são diferentes. Isso acontece porque o Python realiza o cache de
alguns números inteiros (considerados mais utilizados) para melhoria do
desempenho. Isso pode ser comprovado se utilizarmos um `int` que não esteja
entre os valores de inteiros que vão para o cache, ou mesmo se utilizarmos
outro tipo de objeto como um `float`, observe o exemplo:

```python
>>> n = 1000
>>> n == 1000
True
>>> n is 1000
False
>>> f = 1.0
>>> f == 1.0
True
>>> f is 1.0
False
```

Pode ser verificado o inicio e fim do cache de inteiros no seguinte exemplo:


```python
>>> cache_begin = cache_end = 0
>>> for i in range(-500, 0):
...     if i is int(str(i)):
...             cache_begin = i
...             break
...
>>> for i in range(cache_begin, 500):
...     if i is not int(str(i)):
...             cache_end - i - 1
...             break
...
-258
>>> for i in range(cache_begin, 500):
...     if i is not int(str(i)):
...             cache_end = i - 1
...             break
...
>>> cache_begin
-5
>>> cache_end
256
```

No exemplo acima é possível observar que o cache inicia em -5 e vai até 256.

O Python também realiza o cache de strings literais, como demonstrado no
exemplo:

```python
>>> "a" is "a"
True
>>> "aa" is "a" * 2
True
>>> x = "a"
>>> "aa" is x * 2
False
>>> "aa" is intern(x * 2)
True
```

No último teste do exemplo anterior foi utilizado a função `intern` que retorna
a própria string ou uma string previamente utilizada com o mesmo valor, é por
isso que o último teste retorna `True`.

O operador `is` é bastante utilizado para verificar se algum objeto é `None` ou
nulo. O `None` é um singleton no Python, portanto, todos objetos que são `None`
possuem o mesmo `id` que corresponde ao endereço de memória do objeto na
implementação padrão do Python, o `CPython`:

```python
>>> a = None
>>> b = None
>>> c = None
>>> id(None), id(a), id(b), id(c)
(4557279560, 4557279560, 4557279560, 4557279560)
```

Caso tenha mais alguma dúvida quanto a diferença dos operadores de comparação
`==` e `is` ou gostaria de demonstrar mais algum caso, deixe um comentário.

Referências:

* http://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python
* http://choorucode.com/2012/05/01/integer-caching-in-python/
