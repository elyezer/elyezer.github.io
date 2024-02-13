+++
title = "Convertendo Imagens via Terminal"
date = "2008-07-18T15:06:00-03:00"
category = "Posts (pt_BR)"
tags = ["converter", "imagem", "terminal"]
slug = "convertendo-imagens-via-terminal"
+++

Recentemente fui nomeado como website mantainer do projeto
[TextFlow](http://textflow.gnulinuxbrasil.org) (projeto do [Yuri
Malheiros](http://ylog.blogspot.com/)). Para que eu consiga fazer as mudanças
no site utilizo ssh pra acessar o servidor, que foi liberado pelo meu amigo [Og
Maciel](http://blog.ogmaciel.com/), responsável pela hospedagem do [site do
projeto](http://textflow.gnulinuxbrasil.org).

E ao me deparar com a seguinte sitação: tinha acabado de enviar uma imagem pro
servidor e seu tamanho não estava adequado ao layout. Me veio a seguinte
questão: é possivel alterar o tamanho de uma imagem utilizando o terminal?

Fazendo essa mesma pergunta pro [Google](http://google.com.br), ele me
responde: Sim!

Foi ai que encontrei um
[artigo](http://estudiolivre.org/tiki-index.php?page=ConverterImagens) no
[Estúdio Livre](http://estudiolivre.org) falando sobre o assunto.

Para redimensionar uma imgem utilizando o terminal, podemos fazer isso
utilizando a ferramenta **convert** que "converte entre diversos formatos de
imagem bem como redimensiona, borra, corta, tira ruído, desenha, roda e mais. O
convert usa o
[ImageMagick](http://estudiolivre.org/tiki-index.php?page=ImageMagick) para
realizar as operações. Digite "man convert" em um terminal para obter mais
ajuda."

Para redimensionarmos uma imagem basta o simples comando:

```console
convert imagem.jpg -scale 50% imagem_pequena.jpg
```

Onde:

-  convert é nossa ferramenta.
-  imagem.jpg é a imagem original.
-  -scale 50% estamos dizendo para a ferramenta redimensionar a imagem
   original para 50% do tamanho original.
-  e finalmente imagem_pequena.jpg é o nome do arquivo que conterá a
   imagem redimensionada.

Com isso pude alterar o tamanho da imagem que não estava de acordo com o layout
sem ter que modificar usando um editor de imagens e depois novamente ter que
enviar o arquivo pro servidor.

Para maiores detalhes sobre as outras funcionalidades você pude consultar o
manual dessa ferramenta utilizando o comando "man convert" ou pode visitar o
[artigo do Estúdio
Livre](http://estudiolivre.org/tiki-index.php?page=ConverterImagens) para
alguns exemplos.

**[update]** Para converter mais de um arquivo basta seguir a dica que o [André
Noel](http://andrenoel.com.br/) indicou. **[/update]**
