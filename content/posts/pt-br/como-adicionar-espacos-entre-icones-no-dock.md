+++
title = "Como adicionar espaços entre ícones no Dock"
date = "2012-04-21T12:00:00-03:00"
category = "Mac"
tags = ["dock", "mac os x"]
slug = "como-adicionar-espacos-entre-icones-no-dock"
+++

Essa dica rápida é para quem deseja deixar os ícones das aplicações que ficam
no *Dock* do *Mac OS X* mais organizados. Com a adição de "espaços em branco"
como separadores ao seu *Dock*, por exemplo, é possível organizar os ícones das
aplicações por categorias.Para adicionar os espaços é muito simples, abra um
terminal e entre com o seguinte comando:

```
defaults write com.apple.dock persistent-apps -array-add ‘{“tile-type”=”spacer-tile”;}’
```

Repita o comando acima quantas vezes desejar, cada execução corresponde a um
espaço adicionado.

Apesar de ainda não serem exibidos, os espaços foram adicionados. Para que eles
sejam exibidos é necessário terminar e iniciar o *Dock*, para isso basta
executar o seguinte comando:

```
killall Dock
```

Em alguns instantes o *Dock* será iniciado novamente e terá os espaços que você
adicionou à direita dos ícones. Para organizar os ícones e os espaços é só
arrastar.

A adição de mais espaços poderá ser feita no futuro executando os mesmos
comandos. Os espaços que já foram adicionados serão mantidos.

Essa dica rápida foi testada no OS X **Snow Leopard** e no **Lion**.

Fonte: http://css-tricks.com/snippets/html/add-spaces-to-dock-in-os-x/
