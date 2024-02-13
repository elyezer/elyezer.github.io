+++
title = "Adicionando Git Completion no Mac OS X"
date = "2012-08-10T20:00:00-03:00"
category = "Posts (pt_BR)"
tags = ["bash", "completion", "git", "mac os x"]
slug = "adicionando-git-completion-no-mac-os-x"
+++

Se você utiliza o git no Mac OS X e gostaria de adicionar o suporte para
completar os comandos do git assim como os demais comandos do terminal
utilizando tab. Continue a leitura pois é muito simples ter esse recurso em seu
terminal, seja ele **bash** ou **zsh**.

No Mac OS X Mountain Lion (10.8) ao instalar o Xcode pela App Store, você pode
instalar o git facilmente através da instalação do Command Line Tools dentro do
Xcode. Para realizar essa instalação, entre em *Xcode > Preferences...* ou
*Command+,* na aba *Downloads*, selecione *Command Line Tools* em *Components*
e clique em *Install*. Será iniciado o download  e a instalação acontecerá em
seguida. Após a instalação, você terá disponível o comando git em seu terminal.

Agora é possível adicionar o git completion, abra um terminal e execute o
seguinte comando:

```console
curl -Lo ~/.git-completion.bash https://github.com/git/git/raw/master/contrib/completion/git-completion.bash
```

Ele irá fazer o download do
[git-completion.bash](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash)
encontrado no [repositório do git no github](https://github.com/git/git) e irá
salvar o arquivo *.git-completion.bash* no diretório *home*.

Em seguida é necessário realizar o *source* do arquivo baixado, para isso
execute o comando:

```console
source .git-completion.bash
```

No entanto, o recurso somente estará disponível durante essa sessão de
terminal. Para que o git completion esteja disponível em todas as sessões
futuras, basta adicionar o comando executado anteriormente em seu
*.bash_profile*, para isso, execute o seguinte comando:

```console
echo "source .git-completion.bash" >> ~/.bash_profile
```

Feito isso, sempre que iniciar uma nova sessão do terminal, os comandos do git
poderão ser completados utilizando o tab.

Confira o que poderá ser completado:

-  nomes de branch locais ou remotos
-  nomes de tags locais e remotas
-  nomes do arquivo .git/remotes
-  sub comandos do git
-  opções longas comuns (--long-options)

Os exemplos foram realizados no **bash**, para o **zsh** basta fazer o source
no arquivo *.zshrc*.

Caso tenha alguma dúvida deixe um comentário.
