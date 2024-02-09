+++
title = "Installing node-sqlite3 on BeagleBone Black"
date = "2013-09-03 17:13:00"
category = "Embedded Systems"
tags = ["beagleboneblack"]
slug = "installing-node-sqlite3-on-beaglebone-black"
+++

To install node-sqlite3 on BeagleBone Black, first install the latest version
of [npm](https://npmjs.org/):


```console
npm install -g npm
```

Then install the node-sqlite3 module:

```console
npm install -g sqlite3
```

Note the `-g` flag used to install system wide. To install locally don't use
the `-g` flag.

Npm must be updated because the version that comes with BeagleBone Black fails
comparing Python version when installing compiled packages.
