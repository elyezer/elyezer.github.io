#!/usr/bin/env python

AUTHOR = SITENAME = 'Elyézer Rezende'
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

DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = (
    'archives',
    'authors',
    'categories',
    'index',
    'search',
)

EXTRA_PATH_METADATA = {}
STATIC_PATHS = ['images']
PLUGINS = ('tipue_search',)
PLUGIN_PATHS = ('plugins',)

# URL definitions
ARCHIVES_SAVE_AS = 'archives/index.html'
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
SEARCH_SAVE_AS = 'search/index.html'
TAGS_SAVE_AS = 'tags/index.html'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/'

# Theme settings
THEME = 'elyezer-rezende'
THEME_STATIC_DIR = 'static'

AVATAR = 'images/elyezer-rezende.jpg'
ABOUT_ME = (
    'is a Red Hatter, Quality Engineer, Pythonista, Open Source advocate, '
    'Podcaster and Dad.'
)
CC_LICENSE = 'CC-BY-NC-SA'
DISPLAY_CATEGORIES_ON_SIDEBAR = True
LINKS = (
    ('Castálio Podcast', 'http://castalio.info/'),
)
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SOCIAL = (
    ('Facebook', 'https://www.facebook.com/elyezer'),
    ('Github', 'https://github.com/elyezer'),
    ('LinkedIn', 'https://www.linkedin.com/in/elyezer'),
    ('Twitter', 'https://twitter.com/elyezer'),
)
