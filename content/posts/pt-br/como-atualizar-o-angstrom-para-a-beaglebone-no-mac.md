+++
title = "Como atualizar o Angstrom para a Beaglebone no Mac"
date = "2012-04-10T20:00:00-03:00"
category = "Posts (pt_BR)"
tags = ["angstrom", "beaglebone", "linux"]
slug = "como-atualizar-o-angstrom-para-a-beaglebone-no-mac"
+++

Recentemente adquiri uma [BeagleBone](http://beagleboard.org/bone) que já vem
com uma imagem da distribuição linux
[Angstrom](http://www.angstrom-distribution.org/). Após brincar um pouco com a
placa, resolvi atualizar para última versão disponível da distribuição.
Contudo, não foi tão trivial pegar a imagem que é gerada no formato img.xz e
gravá-la no cartão SD, já que utilizo o Mac.

Nesse post, veremos como instalar a ferramenta necessária para gravar a imagem
no cartão SD afim de atualizar o
[Angstrom](http://www.angstrom-distribution.org/) para sua última versão.

Para gravarmos a imagem do [Angstrom](http://www.angstrom-distribution.org/) no
cartão SD, primeiro precisamos baixar uma cópia de sua última versão. A última
imagem disponível pode ser encontrada
[aqui](http://www.angstrom-distribution.org/demo/beaglebone/) e sua última
versão, no momento que escrevo o post é
a [Angstrom-Cloud9-IDE-eglibc-ipk-v2012.02-core-beaglebone-2012.02.14.img.xz](http://www.angstrom-distribution.org/demo/beaglebone/Angstrom-Cloud9-IDE-eglibc-ipk-v2012.02-core-beaglebone-2012.02.14.img.xz).

Enquanto é feito o download da imagem que tem 142MB, vamos instalar a
ferramenta xz que será utilizada para gravar a imagem no cartão SD. O site
oficial da ferramenta é [esse](http://tukaani.org/xz/) e a versão para o Mac
pode ser encontrada nesse [link](http://macpkg.sourceforge.net/). Após baixar,
é necessário executar o instalador para que o xz seja instalado.

Agora que temos o xz e a imagem do
[Angstrom](http://www.angstrom-distribution.org/), podemos gravar a imagem no
cartão SD. Coloque o miniSD no adaptador e insira no seu Mac, em seguida, antes
de iniciar a gravação, precisamos assegurar que o cartão está desmontado. Para
isso abra um terminal e execute o comando

```console
mount
```

Para verificar em qual disco o cartão SD está montado, no meu caso o disco foi
montado no caminho "/Volumes/BEAGLE_BONE", em seguida desmonte o cartão com o
comando

```console
diskutil umountDisk /Volumes/BEAGLE_BONE
```
Ao identificar o caminho, execute o comando

```console
diskutil list
```

Para verificar o identificador do sistema para o cartão SD, no meu caso foi
"disk1", repare que no inicio da linha que mostrava o ponto de montagem do
cartão no comando mount deve ser o mesmo identificado no comando diskutil list.

Finalmente, podemos iniciar o procedimento de gravação da imagem no cartão SD,
para isso execute o seguinte comando

```console
xz -dkc Angstrom-Cloud9-IDE-eglibc-ipk-v2012.02-core-beaglebone-2012.02.14.img.xz > /dev/disk1
```

O processo de gravação é um pouco demorado e leva em torno de 30 minutos. Após
completar a gravação é só colocar na
[BeagleBone](http://beagleboard.org/bone) e bootar o sistema.

Esse post inicia um novo assunto aqui no blog. Aguardem por novos posts sobre
Linux Embarcado e [BeagleBone](http://beagleboard.org/bone).

Fonte: http://www.nunoalves.com/open_source/?p=90
