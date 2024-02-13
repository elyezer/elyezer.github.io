+++
title = "Instalando o Scribes no Mandriva 2008"
date = "2008-01-07T09:55:00-03:00"
category = "Posts (pt_BR)"
tags = ["install", "linux", "mandriva", "scribes"]
slug = "instalando-o-scribes-no-mandriva-2008"
+++

Antes de mais nada, você adicionar os repositórios, caso ainda não tenha feito.
Para isso visite http://easyurpmi.zarb.org e siga os passos.

**[update]** Caso queria mais detalhes sobre a adição de repositórios, dê um
lida no post [Adicionando Repositórios de Programas no
Mandriva](http://sergiorafael.wordpress.com/2008/01/04/adicionando-repositorios-de-programas-no-mandriva/)
feito pelo [Sérgio Rafael Lemke](http://sergiorafael.wordpress.com/).
**[/update]**

Após isso basta digitar em um terminal:

```console
su -
urpmi scribes
```

Até ai nada de novo, o problema está na falta de uma dependência o pacote
gnome-python-gtksourceview que não esta marcada quando se instala o
[Scribes](http://scribes.sourceforge.net/). Você pode verificar se já tem essa
dependência usando o comando:

```console
rpm -q gnome-python-gtksourceview
```

Caso ainda não tenha sido instalada, basta instalá-la:

```console
urpmi gnome-python-gtksourceview
```

Essa é minha primeira contribuição para o [Mandriva
Linux](http://mandriva.com).

Até a próxima.
