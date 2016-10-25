#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = '//www.inpool.xyz'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

OUTPUT_PATH = '../github/'
OUTPUT_RETENTION = ['.git', '.gitignore', 'CNAME', 'params.json']
DELETE_OUTPUT_DIRECTORY = True

# 多说ID
DUOSHUO_ID = 'inpool'
DUOSHUO_URL = 'http://www.inpool.xyz'

# Plugin Settings
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.3,
        'pages': 0.1
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
