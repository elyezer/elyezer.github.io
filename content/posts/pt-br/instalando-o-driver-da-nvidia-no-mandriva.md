+++
title = "Instalando o Driver da nVidia no Mandriva"
date = "2008-02-14T09:15:00-03:00"
category = "Posts (pt_BR)"
tags = ["howto", "instalar", "install", "mandriva", "nvidia"]
slug = "instalando-o-driver-da-nvidia-no-mandriva"
+++

Antes de mais nada você deve estar se perguntando: mas o [Mandriva
One](http://www.mandriva.com/en/linux/) já não vem com drivers e software
proprietários instalados? E eu respondo: Sim, claro! Porém existe um problema
com o [kernel](http://pt.wikipedia.org/wiki/Kernel) que vem junto com o
[Mandriva One](http://www.mandriva.com/en/linux/). Pelo fato do [Mandriva
One](http://www.mandriva.com/en/linux/) suportar várias configurações o
[kernel](http://pt.wikipedia.org/wiki/Kernel) que o acompanha [detecta no
máximo 880MB de
RAM](http://wiki.mandriva.com/en/Releases/Mandriva/2008.0/Errata#2008_One_detects_only_up_to_880MB_of_RAM),
ou seja, se você tem mais do que 880MB de RAM em seu computador, o
[Mandriva](http://www.mandriva.com.br/) reconhecerá somente parte de sua
memória.

Para resolver isso podemos conferir a [Errata no wiki da
distibuição](http://wiki.mandriva.com/en/Releases/Mandriva/2008.0/Errata) para
que se resolva isso instalando um outro
[kernel](http://pt.wikipedia.org/wiki/Kernel). Como esta bem explicado (em
inglês) deixarei somente o link para o procedimento de atualização de kernel.
Porém se você ficar em duvida quanto ao procedimento, utilize a área de
comentário que terei prazer em ajudar.

Com isso, deve-se instalar também os drivers restritos que você tinha instalado
no [kernel](http://pt.wikipedia.org/wiki/Kernel) antigo no
[kernel](http://pt.wikipedia.org/wiki/Kernel) novo. E é com isso que eu e o
[bedi](http://warever.info/sr/blog/) tivemos alguns problemas, o danado do
driver que pode ser baixado via gerênciador de pacotes do
[Mandriva](http://www.mandriva.com.br/) não queria iniciar nem com "reza
braba".

Decidimos, então, optar pela instalação do driver disponível direto do [site da
nVidia](http://www.nvidia.com.br/page/home.html), esse
[link](http://www.nvidia.com/object/linux_display_ia32_169.07.html) vai para a
pagina de download da última versão do driver disponível no momento desse
artigo, pode ser que tenha uma versão mais nova, portando, vale a pena conferir
se já está disponível uma versão mais recente.

Seguindo as instruções fornecidas pelo site, devemos executar o arquivo:
[NVIDIA-Linux-x86-169.07.pkg1.run](http://us.download.nvidia.com/XFree86/Linux-x86/169.07/NVIDIA-Linux-x86-169.07-pkg1.run),
gostaria de salientar um pré requisito que é bom caso você tenha, o pacote
[kernel](http://pt.wikipedia.org/wiki/Kernel) devel relacionado ao
[kernel](http://pt.wikipedia.org/wiki/Kernel) atual que encontra em sua
maquina. Pois assim o instalador do driver poderá compilar um novo modulo para
o [kernel](http://pt.wikipedia.org/wiki/Kernel). Caso não o possua existe a
possibilidade de baixar um módulo pré compilado no momento da instalação, fica
a seu critério. Descreverei aqui levando em consideração que você tenha o
pacote [kernel](http://pt.wikipedia.org/wiki/Kernel) devel referente ao seu
[kernel](http://pt.wikipedia.org/wiki/Kernel) instalado.

A primeira coisa a ser fazer e também a mais obvia, devemos baixar o arquivo
[NVIDIA-Linux-x86-169.07.pkg1.run](http://us.download.nvidia.com/XFree86/Linux-x86/169.07/NVIDIA-Linux-x86-169.07-pkg1.run).

Depois devemos verificar se existe algo com nvidia instalado no sistema, e se
caso existir devemos remover para instalar o novo driver. Para isso execute o
comando abaixo num terminal, ou, se preferir, remova manualmente todas os
ocorrências de nvidia instaladas no sistema utilizando o **Gerenciador de
Software** em modo gráfico (obs.: os comando devem ser executados como
super-usuário ou root).

```console
urpme `rpm -qa |grep nvidia`
```

Com isso garantimos que não exista nenhum outro pacote relacionado ao driver
instalado. O próximo passo é derrubar o servidor gráfico para poder instalar o
driver. Para isso aperte *Ctrl + Alt + F1*, e depois, estando já em modo texto,
derrube o servidor gráfico com o seguinte comando:

```console
service dm stop
```

Estamos pronto para instalar o driver, mas por garantia devemos fazer um
**backup do *xorg.conf*** caso haja algum imprevisto, para tal, basta executar
o seguinte comando:

```console
cp /etc/X11/xorg.conf /etc/X11/xorg.conf.back
```

Agora realmente estamos prontos para instalar, siga até o diretório no qual
você baixou o driver e execute o comando abaixo para começar a instalação:

```console
sh NVIDIA-Linux-x86-169.07-pkg1.run
```

Como disse anteriormente estou considerando que você tenha instalado em seu
sistema o pacote [kernel](http://pt.wikipedia.org/wiki/Kernel) devel para o
[kernel](http://pt.wikipedia.org/wiki/Kernel) que você está utilizando. A
instalação é simples, basta seguir os passos e no momento em que pergunta se
deseja instalar o módulo do [kernel](http://pt.wikipedia.org/wiki/Kernel) pré
compilado, devemos responder que não, assim começará a compilar o módulo. Logo
em seguida, será perguntado se deseja que o instalador configure o *xorg.conf*,
reponda que sim. Basta agora seguir até o final da instalação.

Com a instalação realizada com sucesso, basta verificar se temos presente o
driver no *xorg.conf*, ao executar o comando abaixo deve retornar algo como o
que segue em seguida:

```console
cat /etc/X11/xorg.conf | grep nvidia
# nvidia-xconfig: X configuration file generated by nvidia-xconfig
# nvidia-xconfig:  version 1.0  (buildmeister@builder3)  Thu Dec 13 19:09:35 PST 2007
Driver "nvidia"
```

Agora que temos o driver instalado em nosso sistema, basta executar o comando
abaixo para levantar o módulo já instalado e depois `Ctrl + Alt Backspace` para
reiniciar o servidor gráfico:

```console
modprobe nvidia
```

Pronto temos a última versão do **driver nVidia** instalado em nosso querido
[Mandriva](http://www.mandriva.com.br/). Qualquer dúvida, comentário ou mesmo
crítica, por favor recorra aos comentários.

**[update]** Ou pode seguir a dica do Manoel Pinho nos comentários e verificar
se resolve o problema, caso contrário o jeito é compilar o driver como descrito
acima. **[/update]**

Até a próxima.
