+++
title = "Instalação do Python 2.7.2 e Django 1.3.1 no Dreamhost"
date = "2011-12-12T20:00:00-03:00"
category = "Posts (pt_BR)"
tags = ["django", "dreamhost", "pip", "python", "virtualenv", "virtualenvwrapper"]
slug = "instalacao-do-python-2-7-2-e-django-1-3-1-no-dreamhost"
+++

Em servidores compartilhados normalmente não é possível ter a versão do
[Python](http://python.org) ou mesmo do [Django](http://www.djangoproject.com/)
de acordo com as necessidades do projeto. Porém, tendo um acesso SSH, é
possível instalar, no diretório *home*, a versão requerida para rodar o
projeto.

Como exemplo, será demonstrado como instalar uma versão do
[Python](http://python.org) e do [Django](http://www.djangoproject.com/)
diferente da oferecida pelo serviço de hospedagem compartilhada do
[Dreamhost](http://www.dreamhost.com/r.cgi?351246). No momento da escrita do
post as versões do [Python](http://python.org) e do
[Django](http://www.djangoproject.com/) oferecidas são, respectivamente, 2.5.2
e 1.2.1. Serão instaladas as versões atuais que são 2.7.2 para o
[Python](http://python.org) e 1.3.1 para o
[Django](http://www.djangoproject.com/).

Além disso, será configurado o [pip](http://pypi.python.org/pypi/pip), \
[virtualenv](http://www.virtualenv.org/) e
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
para facilitar manter diversos projetos e criar ambientes virtuais para atender
as necessidades de cada projeto.

Antes de iniciar tenha certeza que seu usuário tenha acesso SSH. É desejável
ter algum conhecimento sobre Linux para facilitar o entendimento das  etapas
descritas.

## Configuração inicial do ambiente

Sua conta deve estar configurada como descrito:

Primeiro, crie os diretórios necessários:

```console
cd ~
# Criação dos diretórios raiz (e log/setup)
mkdir -pv soft run www log log/setup backup data
# Criação dos subdiretórios dentro de run (nosso FHS)
for subdir in bin etc include lib man share
do
    mkdir -pv run/${subdir}
done
# link simbólicos para manter os manuais em um local comum
ln -sv ../man run/share/man
# link simbólico dentro de log para os logs do apache
ln -sv ../logs log/vhosts
```

Em seguida, edite o arquivo `~/.bashrc` para configurar o ambiente, adicione as
seguintes linhas:

```console
# Variável para facilitar as instalações
export RUN=$HOME/run

# Adiciona o run/bin ao PATH do sistema
PATH=$RUN/bin:$PATH

# Define os caminhos para bibliotecas
export LD_LIBRARY_PATH=$RUN/lib:$LD_LIBRARY_PATH
export LD_RUN_PATH=$RUN/lib:$LD_RUN_PATH
```

Após editar o `.bashrc` execute o comando abaixo para assegurar ele seja
carregado na sessão atual.

```console
. ~/.bashrc
```

Para maiores informações e outras configurações visite [Unix account
setup](http://wiki.dreamhost.com/Unix_account_setup). Para instalar o
[Python](http://python.org), somente as configurações descritas são
suficientes.

## Instalação do Python 2.7.2

O [Python](http://python.org) precisa ser baixado e compilado, para isso basta
executar os comandos:

```console
# Diretório para baixar e compilar o Python
cd ~/soft
# Download do Python 2.7.2
wget http://python.org/ftp/python/2.7.2/Python-2.7.2.tgz
# Extrai o conteúdo do pacote
tar -zxvf Python-2.7.2.tgz
# Acessa o diretório com o conteúdo extraido
cd Python-2.7.2
# Configura a instalação, repare no prefixo informado
./configure --prefix=$RUN
# Compilação do Python
make
# Instalação do Python
make install
# Se tudo ocorreu bem, teremos o python 2.7.2 instalado
python --version
```

## Instalação do setuptools e do pip

Para gerenciar os pacotes, será utilizado o
[pip](http://pypi.python.org/pypi/pip). Porém para facilitar a instalação do
[pip](http://pypi.python.org/pypi/pip) será intalado o setuptools que oferece o
comando easy\_install. Para instalar o setuptools execute os comandos:

```console
# Diretório para baixar e compilar o Python
cd ~/soft
# Download do setuptools para o Python 2.7.x
wget http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
# Instalação do setuptools, repare no prefixo informado
sh setuptools-0.6c11-py2.7.egg --prefix=$RUN
```

Uma vez instalado o setuptools, pode-se instalar o pip executando o seguinte
comando:

```console
easy_install pip
```

Agora que tem o pip instalado, será mais fácil de instalar os outros pacotes.

## Instalação do virtualenv e virtualenvwrapper

Para instalar o [virtualenv](http://www.virtualenv.org/) e
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/),
basta executar o seguinte comando:

```console
pip install virtualenvwrapper
```

Como o [virtualenv](http://www.virtualenv.org/) é uma dependência do
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/),
ele será automaticamente instalado, pois o pip se encarrega de resolver as
dependencias dos pacotes que serão instalados.

Para configurar o
[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/),
adicione as seguintes linhas no *~/.bashrc*:

```console
export WORKON_HOME=~/.virtualenvs
source virtualenvwrapper.sh
```

Essa configuração informa que os ambientes virtuais serão instalados no
diretório `~/.virtualenvs`.

Para que esse configuração tenha efeito imediado execute o comando:

```console
. ~/.bashrc
```

Caso o comando anterior não seja executado, somente na próxima vez que iniciar
uma sessão SSH, as configurações entrarão em vigor.

## Instalação do Django

Finalmente, para instalação do [Django](http://www.djangoproject.com/), já que
temos o [pip](http://pypi.python.org/pypi/pip) instalado, basta executar o
comando:

```console
pip install django
```

Com isso teremos o Django disponível no sistema. Eu tenho a preferência de
instalar o Django sempre que criar um [virtualenv](http://www.virtualenv.org/),
pois dessa forma cada projeto pode permanescer com sua versão requerida do
[Django](http://www.djangoproject.com/).

## Maiores informações

Para maiores informações consulte as referências:

-  [Unix account setup](http://wiki.dreamhost.com/Unix_account_setup)
-  [Django (Dreamhost Wiki)](http://wiki.dreamhost.com/Django)
-  [Python (Dreamhost Wiki)](http://wiki.dreamhost.com/Python)
