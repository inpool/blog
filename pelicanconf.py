#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Inpool'
SITENAME = "英银坡'S BLOG"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = {
    'zh': '%Y-%m-%d %H:%M'
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('微博', 'http://weibo.com/inpool'),
          ('电子邮件', 'mailto:%69%6e%70%6f%6f%6c%40%31%32%36%2e%63%6f%6d'),)

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
THEME = 'Architect'
SLUG_SUBSTITUTIONS = (
    ('gong ju', 'tools'),
)
