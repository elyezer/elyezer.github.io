+++
title = "Django no Dreamhost, agora é \"oficial\"!"
date = "2009-11-13T13:50:00-03:00"
category = "Posts (pt_BR)"
tags = ["django", "dreamhost"]
slug = "django-no-dreamhost-agora-e-oficial"
+++

O [Dreamhost](http://www.dreamhost.com/r.cgi?351246) anuncia que "oficialmente"
está suportanto aplicações [Django](http://www.djangoproject.com/). Para ter
sua aplicação rodando basta a simples execução de um script que fará todo o
trabalho pesado para que sua aplicação [Django](http://www.djangoproject.com/)
seja implantada no servidor.

Para execução do script, primeiramente será necessário editar algumas
configurações no dominio hospedado.

## Configuração do dominio

Será necessário ativar o passenger para seu dominio, para isso basta seguir
esses passos:

1. Abra a [página de configuração dos
   domínios](https://panel.dreamhost.com/?tree=domain.manage) do painel de
   controle e edite o domínio desejado.
2. Vá até a seção "Users, Files, and Paths", e assegure que o web direcotry do
   seu dominio termine com `/public`, por exemplo,
   `/home/usuario/elyezer.com/public`.
3. Após a modificação anterior, vá até a seção "Web Options" e marque o
   checkbox para ativar o "Passenger".

Após as modificações anteriores, basta executar o script para poder fazer o
deploy de sua aplicação.

## Utilizando o script para o deploy da aplicação Django

Agora será necessário que você acesse seu servidor via SSH, e após entrar no
diretório da sua aplicação, execute os seguintes comandos:

```console
wget http://wiki.dreamhost.com/django-setup.py
python django-setup.py
```

O script irá orientá-lo durante o restante do processo de configuração de sua
aplicação. Para maiores informações, visite a
[página](http://wiki.dreamhost.com/Django) do wiki do
[Dreamhost](http://www.dreamhost.com/r.cgi?351246) sobre o
[Django](http://www.djangoproject.com/).

## Conclusões

Para quem já havia feito o deploy anteriormente de uma aplicação
[Django](http://www.djangoproject.com/) no
[Dreamhost](http://www.dreamhost.com/r.cgi?351246) perceberá que o processo de
configuração está muito mais simples, quase como um [One Click
Install](http://wiki.dreamhost.com/One_Click_Installs). Com isso o
[Dreamhost](http://www.dreamhost.com/r.cgi?351246) anuncia que está suportando
"oficialmente" aplicações em [Django](http://www.djangoproject.com/) em sua
hospedagem.

## Ainda não tem um servidor de hospedagem?

Aproveite esse novo recurso oferecido pelo
[Dreamhost](http://www.dreamhost.com/r.cgi?351246) e cadastre-se agora mesmo.
Utilize o código promocional DHDJANGO para obter um desconto de até $90 dólares
ao se cadastrar.
