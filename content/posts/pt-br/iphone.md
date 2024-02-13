+++
title = "iPhone"
date = "2009-10-29T17:00:00-03:00"
slug = "iphone"
+++

Conteúdo da apresentação do Workshop: Desenvolvimento de Software para iPhone a
mais nova oportunidade do mercado. Apresentado dia 29/10/2009 na FETIN.

Baixe a [apresentação do Workshop](/presentations/workshop.pdf) em pdf.

## Apple Developer Connection

### iPhone Dev Center

O iPhone Dev Center oferece acesso aos recursos técnicos e informações para
auxiliar no desenvolvimento utilizando as últimas tecnologias do iPhone OS.
Para ter acesso a esse conteúdo, basta ter um Apple ID que pode ser obtido
gratuitamente.

Acessando o iPhone Dev Center você encontrará uma riqueza de recursos que
incluem vídeos, códigos de exemplo, documentação técnica, How-To’s, além de
outros conteúdos.

### iPhone SDK 3.1.2

O iPhone SDK 3.1.2 inclui a IDE Xcode, o iPhone Simulator, e uma suite de
ferramentas adicionais para desenvolver aplicações para iPhone e iPod touch.

## Hardware

### iMac ou Macbook

Para desenvolver com o iPhone SDK você precisa ter um Mac com processador Intel
rodando o Mac OS X Leopard (10.5) ou superior.

## Ferramentas para o Desenvolvedor e Tecnologias

### Ferramentas para o Desenvolvedor

#### IDE Xcode

A IDE Xcode oferece tudo que você precisa, desde um editor profissional com
complementação automática de código (code completion) e Cocoa refactoring, até
compiladores de código aberto otimizados pela Apple e que aproveitam
completamente dos processadores de vários núcleos.

#### iPhone Simulator

Rode, teste, e debugue sua aplicação localmente no Mac usando um iPhone
simulado.

#### Interface Builder

O Interface Builder torna simples prototipar uma interface gráfica completa,
sem escrever nenhum código. Criando a disposição das janelas, botões, sliders,
e outro controles que resultará em uma interface com o usuário completamente
funcional. Posteriormente você poderá transformar esse protótipo numa aplicação
real, mantendo todos os objetos da interface e adicionando funcionalidades a
eles. O Xcode trabalha em conjunto com o Interface Builder em tempo real,
portanto, você simplesmente conecta o código que você escreve no Xcode aos
controles gráficos dentro do Interface Builder.

#### Instruments

As Ferramentas do Desenvolvedor incluem uma ferramenta poderosa de otimização e
análise o Instruments que auxilia a encontrar gargalos de performance nas suas
aplicações para iPhone.

O Instruments coleta dados como utilização de disco, memória, ou CPU em tempo
real remotamente de um iPhone conectado. Os dados coletados são mostrados
graficamente como linhas no decorrer do tempo, facilitando o encontro de áreas
com problemas e depois aprofundando para encontrar as linhas de código que
estão ocasionando esse problema.

### Tecnologias

#### Framework Cocoa Touch

O framework Cocoa Touch consiste em bibliotecas, APIs, e tempos de execução
otimizados para a experiência baseada no toque do iPhone.

#### O Objective-C oferece ao Cocoa sua flexibilidade

Grande parte do Cocoa é implementado em Objective-C, uma linguagem de
programação orientada a objetos que usa um tempo de execução completamente
dinâmico para executar eventos da aplicação.

De acordo com o curso da execução da sua aplicação, o tempo de execução do
Objective-C instancia objetos baseado na lógica da execução e não somente na
forma definida durante a compilação. Ou seja os objetos são criados de acordo
com a demanda.

#### Cocoa utiliza o Padrão de Projeto Model-View-Controller

O Cocoa foi projetado completamente utilizando o padrão de projeto
Model-View-Controller (MVC). Os Models (modelos) encapsulam os dados da
aplicação, as Views (visões) exibem e editam esses dados, e os Controllers
(controladores) são responsáveis pela lógica entre os dois. Por separar as
responsabilidades dessa forma, você tem uma aplicação que é simples de
projetar, implementar, e manter.

### Recursos das ferramentas

#### IDE Xcode

**Editor de código fonte** – Escreva código usando um editor profissional com
complementação automática de código (code completion), code folding, destaque
de sintaxe (syntax highlighting), e balões de mensagens mostrando os erros e
breakpoints (pontos de parada) no mesmo local que o seu código.

**Interface Builder** – Projete e teste sua interface gráfica sem escrever uma
linha de código sequer, prototipando em minutos, e depois conectando
graficamente sua interface com o código fonte criado no Xcode.

**iPhone Simulator** – Com o iPhone SDK, a IDE Xcode pode compilar, instalar,
rodar, e debugar aplicações criadas com o Cocoa Touch em um iPhone simulado
criando um fluxo de trabalho extremamente rápido.

**Sistema de compilação integrado** – Responsável por instalar as aplicações em
um dispositivo iPhone conectado.

**Compiladores** – Você tem um conjunto completo de compiladores de código
aberto otimizados pela Apple.

**Debugger Gráfico** – Debugue uma aplicação, utilizando o iPhone Simulator ou
um iPhone conectado na USB, diretamente do editor do Xcode e veja os valores
das variáveis ao passar o mouse por elas.

**Snapshots** – Antes de executar uma operação de risco no seu projeto,
simplesmente clique no botão Snapshot para salvar o estado atual e depois
recuperá-lo facilmente.

**Refactoring** – Reestruture sua aplicação em Objective-C em uma única
operação, mudando as hierarquias dos objetos ou nomes para todas as ocorrências
seja no código ou até mesmo nas interfaces gráficas.

**Documentação Completa** – Procure por qualquer coisa dentro do Xcode e o
visualizador de documentação irá encontrá-la, tanto localmente como no site
Apple Developer Connection.

**Assistente de Pesquisa** – De acordo com o que você digita no seu código,
essa janela ira sugerir definições, uso de API, ou código de exemplo que irão
mantê-lo focado no seu trabalho.

**Controle de Versão** – No Xcode, você encontrará um navegador de repositório
gráfico com suporte aos mais populares softwares de controle de versão.

#### Frameworks Cocoa

**UIKit** – Para o iPhone OS, os frameworks Cocoa Touch foca em interfaces
baseadas em toque e otimização. O UIKit oferece ferramentas básicas e
infraestrutura que você precisa para implementar aplicações gráficas, baseadas
em eventos no iPhone OS.

**Foundation** – Os blocos de construção de qualquer aplicação Cocoa, incluindo
uma coleção de classes e todos os objetos base utilizados em todo Cocoa.

**Graphics** – Os frameworks gráficos abrangem desde animação nativa de alto
nível e imagem nativa até o OpenGL que é padrão da indústria para criação de
aplicações espetaculares.

#### Instruments

**Gravação de dados** – Diga ao Instruments qual aplicação analisar, quais
instrumentos usar e simplesmente clique no grande botão vermelho para iniciar a
coletar os dados e armazenar para análise futura.

**Comparação Visual** – De acordo com que os dados vão sendo gravados e
mostrados ao decorrer do tempo é fácil perceber relacionamentos, ou entre
diferentes tipos de dados coletados ou entre os mesmos dados porém coletados
múltiplas vezes.

**Drill Down** – Inspecione os picos dos dados no gráfico para ver qual o
código está sendo executado naquele momento, depois facilmente vá para o Xcode
para consertar o problema.

**Play Back** – Grave a interação do usuário com sua aplicação, então repita a
gravação para ver como as mudanças no seu código afetaram a performance.

**Biblioteca de Instrumento** – Escolha qualquer um dos instrumentos da
biblioteca desde o baixo nível como CPU, rede, ou atividade de arquivos, até
gráficos avançados e eventos do usuário.

**Instrumentos Personalizados** – Crie seu próprio instrumento usando DTrace e
o criador personalizado do Instruments.

#### Outras ferramentas inclusas com o Mac OS X

**Dashcode** – Um ambiente de desenvolvimento rápido e fácil de usar para
aplicações web, incluindo partes de biblioteca gráfica (GUI), JavaScript
debugger, e mais.

## iPhone Developer Program

### Teste no iPhone

Desenvolva diretamente no iPhone ou iPod touch. Compile, teste, e otimize sua
aplicação para conseguir a melhor performance possível. Exatamente como
usuários irão utilizá-la.

### Teste em tempo real

Conecte seu iPhone para usar o debbuger gráfico do Xcode, ou coletar dados de
performance no Instruments em tempo real. Essas ferramentas de otimização
poderosas permitem identificar rapidamente e corrigir qualquer problema de
performance.

### Suporte Técnico

O iPhone Developer Program inclui duas requisições ao suporte técnico onde os
engenheiros da Apple irão oferecer assistência a nível de código, orientação,
ou irão indicar a documentação técnica apropriada para aumentar o processo de
desenvolvimento.

### Distribua sua Aplicação

O iPhone Developer Program padrão (Standard) oferece acesso ao App Store onde
poderá ser distribuido aplicações grátis ou comerciais para milhões de usuários
do iPhone e iPod Touch. O iPhone Developer Program empresarial (Enterprise) é
para companhias que estão buscando implantar suas próprias aplicações
internamente usando suas Intranets.

#### App Store

Através da App Store é possível alcançar milhões de usuários do iPhone e iPod
touch.

A App Store é acessível pelo Wi-fi e pelas redes do celulares por isso usuários
do iPhone e iPod touch poderão descobrir e baixarem novas aplicações onde eles
estiverem. O usuários poderão procurar aplicações por gênero, destaque, e top
dez. Uma vez baixada, os usuários serão notificados sempre que uma atualização
estiver disponível, diretamente em seus iPhones e iPods touch.

-  Você escolhe o preço da aplicação
-  Você recebe 70% do valor das vendas
-  Sem taxas para aplicações gratuitas
-  Sem taxas para o marketing da aplicação

#### Distribuição na Empresa

Para implantar aplicações próprias internamente para usuários autorizados de
uma companhia, o iPhone Developer Program empresarial está disponível para
companhias com 500 ou mais funcionários.

#### Distribuição direta

Os programas padrão e empresarial permitem compartilhar a aplicação com até 100
outros usuários do iPhone ou iPod touch através da distribuição direta.
Compartilhe a aplicação por email ou postando ela em um website ou servidor.

### Tipos de Programas

#### Programa Padrão $99

Para desenvolvedores que estão criando aplicações gratuitas e comerciais para o
iPhone e iPod touch e desejam distribuir as aplicações na App Store.

#### Programa Empresarial $299

Para companhias com 500 ou mais empregados que estão criando aplicações
internas proprietárias para o iPhone e iPod touch.

#### iPhone Developer Program universitário

O iPhone Developer Program universitário é um programa gratuito designado para
instituições de ensino superior que buscam introduzir o desenvolvimento de
aplicações para iPhone em suas grades curriculares.

#### Comparação entre os programas

|                                          | Programa padrão | Programa empresarial |
| ---------------------------------------- | --------------- | -------------------- |
| iPhone SDK 3.0                           | Incluído        | Incluído             |
| Recursos do iPhone Dev Center            | Incluído        | Incluído             |
| Teste diretamente no iPhone e iPod touch | Incluído        | Incluído             |
| Suporte técnico a nível de código        | Incluído        | Incluído             |
| Fóruns Apple Developer Beta              | Incluído        | Incluído             |
| App Store                                | Incluído        | Não Incluído         |
| Distribuição direta                      | Incluído        | Incluído             |
| Distribuição interna                     | Não Incluído    | Incluído             |

## Como está o mercado atualmente?

Dia 28/09/2009 a Apple anunciou que mais de 2 bilhões de aplicações foram
baixadas da revolucionária App Store, a maior loja de aplicações do mundo.
Atualmente existem mais de 85.000 aplicações disponíveis para mais de 50
milhões de usuários do iPhone e iPod touch mundialmente e mais de 125.000
desenvolvedores que participam do iPhone Developer Program da Apple. “A App
Store reinventou o que você pode fazer com um dispositivo de mão, e nossos
usuários estão claramente amando isso”, disse Steve Jobs, CEO da Apple.

## Links

-  [Conteúdo do Workshop](/presentations/conteudo-workshop.pdf)
-  Become an Xcoder: http://www.cocoalab.com/BecomeAnXcoder.pdf
-  iCodeBlog: http://icodeblog.com/
-  Apps Amuck: http://www.appsamuck.com/
-  iPhone SDK Articles: http://www.iphonesdkarticles.com/

## Referências

-  http://developer.apple.com/iphone/
-  http://developer.apple.com/technology/
-  http://developer.apple.com/iphone/program/
