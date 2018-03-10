#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ely\xe9zer Rezende'
SITENAME = u'Ely\xe9zer Rezende'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Castálio Podcast', 'http://castalio.info/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/elyezer'),
          ('Github', 'https://github.com/elyezer'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {}


# URL definitions
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
