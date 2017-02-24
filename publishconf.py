#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
import os
sys.path.append('.')
from pelicanconf import *

DELETE_OUTPUT_DIRECTORY = True
SITEURL = os.getenv('PELICAN_SITE_URL', 'http://beaverbarcamp.org')

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
