+++
title = "Backing up Beaglebone Black SD card image"
date = "2013-10-16 11:00:40"
category = "Embedded Systems"
tags = ["beagleboneblack"]
slug = "backing-up-beaglebone-black-sd-card-image"
+++

Run fdisk to see the SD card partition table (use p command)

```console
sudo fdisk /dev/sdbCommand (m for help): pDisk /dev/sdb: 7948 MB, 7948206080 bytes245 heads, 62 sectors/track, 1021 cylinders, total 15523840 sectorsUnits = sectors of 1 * 512 = 512 bytesSector size (logical/physical): 512 bytes / 512 bytesI/O size (minimum/optimal): 512 bytes / 512 bytesDisk identifier: 0x00000000   Device Boot      Start         End      Blocks   Id  System/dev/sdb1   *        2048      133119       65536    e  W95 FAT16 (LBA)/dev/sdb2          133120     1638399      752640   83  Linux
```

Add one to the end of second partition, this number will be used as count
parameter of dd command, for example:

```console
sudo dd if=/dev/sdb of=./BBB.img bs=512 count=1638400
```

If you'd like to compress the image you could use xz:

```console
xz -zk BBB.img
```

Will be generated the file BBB.img.xz that you could extract and restore to
another MicroSD card.
