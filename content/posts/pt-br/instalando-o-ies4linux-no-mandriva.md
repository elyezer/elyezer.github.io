+++
title = "Instalando o IEs4Linux no Mandriva"
date = "2008-01-29T09:50:00-03:00"
category = "Posts (pt_BR)"
tags = ["ie", "ie6", "ie7", "ies4linux", "Linux", "Mandriva"]
slug = "instalando-o-ies4linux-no-mandriva"
+++

Quem desenvolve para web sabe muito bem que precisa testar o projeto no IE por
motivos de redenização. Estou escrevendo esse artigo basicamente para explicar
a instalação do [IEs4Linux](http://www.tatanka.com.br/ies4linux) no
[Mandriva](http://mandriva.com). Com esse pacote você terá em seu
[Mandriva](http://mandriva.com) o Internet Explorer 5, 5.5 e 6, além disso você
pode instalar o recurso beta que contém suporte ao IE 7.

O [IEs4Linux](http://www.tatanka.com.br/ies4linux) depende dos seguintes
pacotes: [cabextract](http://www.cabextract.org.uk/) and
[Wine](http://www.winehq.org/). Para instalar esse pacotes, após ter
configurado o urpmi como comentado [aqui]({{< ref
"instalando-o-scribes-no-mandriva-2008" >}}), basta executar os comandos abaixo
num terminal ou então abrir o Gerenciador de Software e procurar pelos pacotes
citados.

```console
su
urpmi wine cabextract
exit
```

Após o termino da instalação, basta executar esses comando num terminal **como
usuário normal** para que seja instalado o
[IEs4Linux](http://www.tatanka.com.br/ies4linux):

```console
wget http://www.tatanka.com.br/ies4linux/downloads/ies4linux-latest.tar.gz
tar zxvf ies4linux-latest.tar.gz
cd ies4linux-*
./ies4linux
```

Ao executar último comando será aberta uma janela onde você poderá escolher
quais IEs você deseja instalar, no canto inferior direito existe um opção para
configurar recursos avançados, clicando nesse botão você terá acesso para
selecionar que deseja instalar o IE7, lembrando que ainda é um recurso beta.

Após configurar a instalação, basta confirmar para que o programa baixe os
pacotes necessários e instale. Após a instalação siga as instruções para
executar os IEs.

Qualquer dúvida, não hesite em comentar. Até a próxima.
