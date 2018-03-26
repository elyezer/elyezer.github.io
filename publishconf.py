#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://elyezer.com'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS.extend([
    'extra/CNAME',
    'extra/keybase.txt',
])
EXTRA_PATH_METADATA.update({
    'extra/CNAME': {'path': 'CNAME'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
})

DISQUS_SHORTNAME = 'elyezer'
GA_TRACKING_ID = 'UA-71148736-1'
