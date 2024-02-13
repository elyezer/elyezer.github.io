+++
title = "Instalando o node-sqlite3 na BeagleBone Black"
date = "2013-09-04T09:38:00-03:00"
category = "Posts (pt_BR)"
tags = ["beagleboneblack"]
slug = "instalando-o-node-sqlite3-na-beaglebone-black"
+++

Para instalar o node-sqlite3 na BeagleBone Black é necessário que o npm esteja
atualizado:

```console
npm install -g npm
```

Em seguida basta instalar o pacote node-sqlite3:

```console
npm install -g sqlite3
```

Observe que a flag `-g` foi utilizada para instalar no sistema. Para instalar
localmente é só não utilizar a flag.

O npm precisa ser atualizado pois a versão que vem instalada com a BeagleBone
Black falha ao instalar pacotes que precisam ser compilados devido a um bug ao
comparar a versão do Python. A versão do npm instalada na atualização foi a
1.3.9.
