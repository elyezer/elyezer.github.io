+++
title = "Modo correto de mostrar tooltip em imagens"
date = "2007-10-03T05:05:00-03:00"
category = "Posts (pt_BR)"
tags = ["image", "imagem", "tooltip", "xhtml"]
slug = "modo-correto-de-mostrar-tooltip-em-imagens"
+++

Encontrei este tutorial que aborda o assunto de tooltip em imagens. Ao
contrário de que muitos acham, inclusive eu achava, é que o atributo alt
incluída dentro da tag `img` já mostrava como tooltip. Porém o atributo `alt`
tem a semântica de mostrar o texto que lhe foi atribuido em caso da imagem não
ser carregada.

Então, o que deve ser feito para mostrar um tooltip em uma imagem? Simples,
mantém o atributo *alt* para que, caso a imagem não seja carregada, mostre o
*alternate text*. E, assim como se faz em links, adicionar o atributo *title* e
atribuir o texto que se deseja como tooltip a esse atributo.

Modo errado de mostrar a tooltip:


Modo correto de mostrar a tooltip:


Lembrando que, isso é somente para [navegadores que
resolveram](http://www.mozilla.org/) [esse
"problema"](http://bugzilla.mozilla.org/show_bug.cgi?id=25537#c31).

Fonte: [ALT and TITLE](http://css.e-lusion.com/tutorials/tooltips.php).
