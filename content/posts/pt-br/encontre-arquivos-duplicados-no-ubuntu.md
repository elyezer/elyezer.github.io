+++
title = "Encontre arquivos duplicados no Ubuntu"
date = "2007-07-10T15:20:00-03:00"
category = "Posts (pt_BR)"
slug = "encontre-arquivos-duplicados-no-ubuntu"
+++

Rompendo o grande tempo sem postar algo, escreverei sobre como encontrar
arquivos duplicados em seu HD no Ubuntu.

Primeiramente, um pouco de história, estava tranqüilamente instalando um
programa quando percebi que meu HD estava lotado. Verificando algumas coisas e
organizando um pouco da bagunça percebi que tinha arquivos duplicados, e,
alguns deles, com mais de 1GB. Resolvi perguntar pro
[Google](http://www.google.com.br) se ele sabia de algo e encontrei esse blog:
[files">Find duplicate copies of
files](http://ubuntu.wordpress.com/2005/10/08/find-duplicate-copies-of-files/)
e num comentário encontrei o [FSlint](http://www.pixelbeat.org/fslint/).

Resolvi testá-lo por ser um modo gráfico e não em linha de comando como no post
que encontrei. Rodando para verificar se realmente encontraria. Cumprindo o
trabalho ele mostrou a mensagem: "2518982656 bytes desperdiçados em 7050
arquivos (em 2713 grupos)", ou seja, 2,35GB. Apesar de já ter removido alguns
GB's ainda sobrou 2GB.

Recomendo o programa, achei interessante. Falarei desde a instalação até a
varredura:

## Instalando o FSlint no Ubuntu Feisty (7.04)

Para instalar o FSlint no Ubuntu basta digita o seguinte comando em um
terminal:

```console
sudo apt-get install fslint
```

Para abri-lo basta entrar em Aplicações > Ferramentas do Sistema > FSlint.

## Fazendo a busca no HD

Logo na parte superior da janela do programa você encontra um local para
adicionar os lugares onde deseja que a busca seja feita, no meu caso, escolhi o
meu home e minha partição de arquivos que compartilho entre Windows e Ubuntu.
Feito isso, repare que do lado direito de onde fica listado os arquivos
encontra-se a opção recursivo para que seja procurado nas subpastas dos locais
onde foi especificado. Deve-se clicar em Procurar para iniciar a pesquisa.

Após a busca, mostra-se embaixo do botão Procurar o resumo da busca, falando a
quantidade de bytes desperdiçados. Usando a lista de arquivos que foi gerada a
partir da busca, pode apagar as entradas duplicadas, selecionado o arquivo que
deseja eliminar e clicando em apagar.

Um ótimo programa e eficiente pois encontra arquivo iguais mas que contenham
nomes diferentes pois ele procura pelo hash do arquivo.

Segue um review que encontrei, em inglês, do programa:
http://www.linuxjournal.com/node/1000198. E uma screenshot que tirei do
programa [aqui](http://img362.imageshack.us/my.php?image=fslintny8.png).

Espero que tenha sido de grande utilidade esse post.

Até mais.

**[update]**

Como no comentário, a versão oficial do repositório do Ubuntu é a 2.16. Para
instalar a ultima versão (2.22), basta abrir um terminal e digitar os comandos:

```console
wget http://www.pixelbeat.org/fslint/fslint_2.22-1_all.deb
sudo dpkg -i fslint_2.22-1_all.deb
```

Ou baixar o arquivo
[fslint_2.22-1_all.deb](http://www.pixelbeat.org/fslint/fslint_2.22-1_all.deb)
e dar dois cliques no Gerenciador de Arquivos para instalar o pacote.

**[/update]**
