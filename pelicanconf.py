#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'OSU Open Source Lab'
SITENAME = u'Beaver Barcamp 14'
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Specify name of a theme installed via the pelican-themes tool
THEME = "barcamp-theme"

FEED_RSS = 'rss20.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
