+++
title = "Arch Linux: Problema com atualização do klibc"
date = "2008-10-11T13:08:00-03:00"
category = "Posts (pt_BR)"
tags = ["archlinux", "atualização", "problema", "update"]
slug = "arch-linux-problema-com-atualizacao-do-klibc"
+++

Para quem está com problema em atualizar o Arch Linux por conta do pacote
klibc, deve fazer uma pequena intervenção para que consiga atualizar o pacote
klibc ou mesmo o sistema:

"Graças a uma limitação na hora de resolver alguns problemas de links
simbólicos, a atualização atual do klibc-1.5.14-1 precisa que um link seja
removido antes de você atualizar o pacote de fato. Por favor, execute o
seguinte comando como root:

```console
# rm /usr/lib/klibc/include/asm
```

Agora você pode atualizar o klibc e/ou seu sistema tranquilamente. Se
você não fizer isto você verá um monte de conflito de arquivos."

Fonte: http://archlinux-br.org/news/38/
