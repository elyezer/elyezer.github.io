+++
title = "Fazendo o deploy de uma aplicação Flask no Dreamhost"
date = "2012-06-28T00:00:00-03:00"
category = "Posts (pt_BR)"
tags = ["deploy", "dreamhost", "flask", "python"]
slug = "fazendo-o-deploy-de-uma-aplicacao-flask-no-dreamhost"
+++

Recentemente realizei um projeto onde utilizei o
[Flask](http://flask.pocoo.org/) como framework web. A decisão de usar o
[Flask](http://flask.pocoo.org/) no lugar do
[Django](https://www.djangoproject.com/) foi devido ao site não precisar de
muitos dos recursos que o Django oferece por ser um framework fullstack. Por
outro lado, o [Flask](http://flask.pocoo.org/) é um microframework que oferece
alguns recursos como:

-  Excelente documentação
-  Utiliza o Jinja2 para os templates
-  Um servidor para desenvolvimento e debug
-  Suporte integrado à unit tests

Nesse post veremos como fazer o deploy de uma aplicação
[Flask](http://flask.pocoo.org/) no
[Dreamhost](http://www.dreamhost.com/r.cgi?351246).

Sem mais delongas vamos ao que interessa. Primeiro é extremamente recomendável
que você instale uma versão mais atualizada do [Python](http://python.org/),
[virtualenv](http://www.virtualenv.org/) e
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) em
sua conta no [Dreamhost](http://www.dreamhost.com/r.cgi?351246). Para instalar
o [Python](http://python.org/) e as demais ferramentas consulte o [post]({{<
ref "instalacao-do-python-2-7-2-e-django-1-3-1-no-dreamhost" >}}) que descreve
a instalação.

A partir de agora será considerado que o [Python](http://python.org/),
[virtualenv](http://www.virtualenv.org/) e
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) estejam
instalados. Em seguida iremos criar um virtualenv para o deploy de uma
aplicação de exemplo, para isso utilize o seguinte comando:

```console
mkvirtualenv projeto
```

O virtualenv será criado e já será ativado. Agora precisamos instalar o
[Flask](http://flask.pocoo.org/), que pode ser feito com o seguinte comando:

```console
pip install flask
```

Com isso está tudo certo para configurar o domínio no painel de controle do
[Dreamhost](http://www.dreamhost.com/r.cgi?351246). Lembre-se que para rodar
aplicações em Python o "*Web directory*" deverá terminar em "*public*", por
exemplo, "exemplo.com.br/public" e o Passenger deve estar ativado para o
domínio.

Uma vez configurado o domínio no painel de controle e assumindo que o domínio
configurado foi "projeto.com.br", acesse o diretório:

```console
cd projeto.com.br
```

Criaremos e entraremos no diretório do projeto

```console
mkdir projeto && cd projeto
```

Em seguida iremos criar o módulo para nossa aplicação, para isso edite o
arquivo projeto.py com o seguinte conteúdo:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
return 'Hello Flask application!'
```

Isso já é o suficiente para verificarmos que nossa aplicação está sendo
executada corretamente. Volte para o diretório do domínio projeto.com.br


```console
cd ..
```

Em seguida o arquivo `passenger_wsgi.py` deverá ser editado com o seguinte
conteúdo:

```python
import os
import sys

INTERP = os.path.join(os.environ['HOME'], '.virtualenvs', 'projeto', 'bin', 'python')
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd() + '/projeto')

from projeto import app as application
```

Concluímos assim o deploy de nossa aplicação em
[Flask](http://flask.pocoo.org/). Para verificar se está tudo certo, basta
acessar no navegador o domínio e verificar se será exibido a mensagem "Hello
Flask application!".

Caso encontre algum problema deixe um comentário. Até a próxima.
