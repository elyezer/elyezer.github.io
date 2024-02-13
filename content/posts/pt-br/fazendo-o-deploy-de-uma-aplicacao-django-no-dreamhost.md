+++
title = "Fazendo o deploy de uma aplicação Django no Dreamhost"
date = "2011-12-22T12:00:00-03:00"
category = "Posts (pt_BR)"
tags = ["deploy", "django", "dreamhost", "python"]
slug = "fazendo-o-deploy-de-uma-aplicacao-django-no-dreamhost"
+++

No [post anterior]({{< ref
"instalacao-do-python-2-7-2-e-django-1-3-1-no-dreamhost" >}}), foi mostrado
como instalar uma versão mais recende do [Python](http://python.org/) e do
Django no [Dreamhost](http://www.dreamhost.com/r.cgi?351246). Nesse post será
demonstrado como fazer o deploy de uma aplicação
[Django](https://www.djangoproject.com/) utilizando o
[virtualenv](http://www.virtualenv.org/).

O [Dreamhost](http://www.dreamhost.com/r.cgi?351246) utiliza o [Passenger
WSGI](http://wiki.dreamhost.com/Passenger_WSGI) para servir aplicações escritas
em Python, por isso, o processo aqui descrito é referente ao deploy utilizando
o [Passenger WSGI](http://wiki.dreamhost.com/Passenger_WSGI).

## Configuração do domínio

O primeiro passo é configurar um domínio para fazer o deploy da aplicação.
Entre no [painel de configuração de
domínios](https://panel.dreamhost.com/index.cgi?tree=domain.manage) e adicione
um novo domínio ou sub-domínio, ou então edite a configuração de um domínio já
existente.

Após inserir o nome do novo domínio ou sub-domínio, na seção "**Web Options**",
marque a opção "**Passenger (Ruby/Python apps only)**".

Um detalhe importante é, que ao utilizar o Passenger, o caminho especificado em
"**Web directory**" deve terminar em *public*. Por exemplo, se o domínio
configurado é **exemplo.com.br**, então o caminho ficará
e`xemplo.com.br/public`.

## Configuração do banco de dados MySQL

Uma vez configurado o domínio, deve ser criado um banco de dados para a
aplicação. A criação do banco pode ser feita na [página de gerência de banco de
dados MySQL](https://panel.dreamhost.com/index.cgi?tree=goodies.mysql). Tenha
pelo menos um *hostname* configurado, pois no
[Dreamhost](http://www.dreamhost.com/r.cgi?351246) não pode ser usado
simplesmente *localhost* ao configurar o *host* do servidor de banco de dados
na aplicação.

## Deploy da apliação Django

Agora que o domínio e o banco de dados da aplicação estão criados, criaremos
uma aplicação [Django](https://www.djangoproject.com/) e faremos o deploy
utilizando o [virtualenv](http://www.virtualenv.org/).

Primeiro é necessário criar o ambiente virtual para nossa apliação, lembrando
que será feito o uso do
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
para nos auxiliar:

```console
mkvirtualenv projeto
```

Ao executar o comando anterior, o ambiente virtual criada já será ativado,
repare o prefixo `(projeto)` no prompt do shell:


```console
(projeto)user@host:path/to/projeto.com.br$
```

Posteriormente, o [virtualenv](http://www.virtualenv.org/) poderá ser ativado
usando o comando:

```
workon projeto
```

Para completar o nome do projeto poderá ser utilizado o tab, assim como é feito
para completar comandos do sistema.

Agora que temos o ambiente virtual criado, podemos instalar o
[Django](https://www.djangoproject.com/):

```console
pip install django
```

Como o [Dreamhost](http://www.dreamhost.com/r.cgi?351246) oferece somente o
MySQL como servidor de banco de dados, teremos que instalar também o driver do
MySQL para Python:

```console
pip install mysql-python
```

Terminado a instalação dos pacotes necessários, poderemos fazer o setup de
nossa aplicação. Primeiramente devemos entrar no diretório que foi configurado
o domínio, estarei utilizando o domínio projeto.com.br como exemplo.

```console
cd projeto.com.br
```

Lembre-se que, como estamos utilizando o Passenger, dentro do diretório
projeto.com.br deverá ter o diretório **public**, como foi definido
anteriormente na configuração do domínio.

Agora poderá ser criado o projeto [Django](https://www.djangoproject.com/):

```console
django-admin.py startproject projeto
```

Também deverá ser criado o arquivo *passenger_wsgi.py*:

```console
touch passenger_wsgi.py
```

Edite esse arquivo e adicione o seguinte conteúdo:

```python
import sys, os

INTERP = os.path.join(os.environ['HOME'], '.virtualenvs', 'projeto', 'bin', 'python')
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + '/projeto')
os.environ['DJANGO_SETTINGS_MODULE'] = "projeto.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
```

Nossa aplicação está quase pronta para ser rodada. Falta fazer a configuração
do banco de dados e do admin. Também será criar um link simbólico para os
arquivos estáticos do admin.

### Configuração da aplicação

Entre no diretório do projeto:

```console
cd projeto
```

E edite o arquivo *settings.py*, primeiro a configuração do banco de dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'hostname.domain.com',
        'PORT': '',
    }
}
```

Primeiro definimos que utilizaremos o MySQL como banco de dados, em seguida
configuramos o nome do banco de dados, nome do usuário e senha. Finalmente, é
configurado o host do servidor do banco de dados, repare que devemos entrar com
o hostname configurado na página de gerência de banco de dados MySQL.

Ainda no arquivo *settings.py*, deverá ser configurado *STATIC_ROOT* para que
os arquivos estáticos do django admin sejam cerregados.

```python
STATIC_ROOT = '/home/user/projeto.com.br/public/static'
```

Para finalizar a configuração da aplicação, devemos adicionar o django admin no
*INSTALLED_APPS*, para isso decomente a linha:

```python
# 'django.contrib.admin',
```

Com isso finalizamos a configuração do projeto. O próximo passo é configurar o
arquivo *urls.py* descomentando as linhas:

```python
# from django.contrib import admin
# admin.autodiscover()
# url(r'^admin/', include(admin.site.urls)),
```

Em seguida criaremos o link simbólico para os arquivos estáticos do django
admin:

```console
mkdir public/static
ln -s ~/.virtualenvs/projeto/lib/python2.7/site-packages/django/contrib/admin/media/ public/static/admin
```

Finalmente, para terminar o deploy, execute o comando *syncdb* para que as
tabelas do banco de dados e um super-usuário seja criado:

```console
cd projeto
python manage.py syncdb
```

Uma vez terminado a execução do *syncdb*, poderemos acessar nosso projeto no
navegador. No exemplo desse post bastaria acessar a URL
`http://projeto.com.br/admin`.

## Referências

-  [Django (Dreamhost Wiki)](http://wiki.dreamhost.com/Django)
-  [Passenger WSGI (Dreamhost Wiki)](http://wiki.dreamhost.com/Passenger_WSGI)
-  [Installing Django With virtualenv on
   Dreamhost](http://andrew.io/weblog/2010/02/installing-django-with-virtualenv-on-dreamhost/)
