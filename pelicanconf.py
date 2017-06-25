#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bryan Travis Smith, Ph.D'
SITENAME = 'Bryan Travis Smith, Ph.D'
SITEURL = 'https://bryantravissmith.github.io'

PATH = 'content'
# Useful for Development
# RELATIVE_URLS = True

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Theme
THEME = 'theme/'

# Formt of urls
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['AffectivaDemo']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://linkedin.com/in/bryantravissmith'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

COLOR_SCHEME_CSS = 'github.css'
HEADER_COLOR = 'DARKTURQUOISE'
# Added for Jupyter Notebook integration
# https://github.com/danielfrg/pelican-ipynb

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['pelican-plugins']       # Ensure your plugin path is in it
PLUGINS = ['ipynb2pelican']             # Name of the plugin
IGNORE_FILES = ['.ipynb_checkpoints']

# PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['ipynb.markup']

IPYNB_USE_META_SUMMARY = True

# Set Defaults

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
