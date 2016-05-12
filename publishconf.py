#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://inpool.xyz'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

OUTPUT_PATH = '../blog/'
OUTPUT_RETENTION = ['.git', '.gitignore', 'CNAME', 'params.json']
DELETE_OUTPUT_DIRECTORY = True

# 多说ID
DUOSHUO_ID = 'inpool'

# Plugin Settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.1
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
