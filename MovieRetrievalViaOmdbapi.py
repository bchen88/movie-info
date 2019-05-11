#!/usr/bin/env python
# -*- coding: utf-8 -*-

#required imports
from __future__ import print_function
import argparse
import sys
import json

# This program is assumed to run python 2.x.x
from urllib2 import urlopen
from urllib import urlencode
to_unicode = lambda s: unicode(s)  # noqa
mk_trans = lambda a, b: {ord(ca): ord(cb) for ca, cb in zip(a, b)}

#help description
parser = argparse.ArgumentParser(description='Query OMDb API for a Movie')

#command options
parser.add_argument(
    "-t",
    help="Movie title")

parser.add_argument(
    "--apikey",
    help="Your API key is required!!")

#parse for command options
args = parser.parse_args()

params = {}
keys = ['t']

# get command options
for k in keys:
    if args.__getattribute__(k):
        params[k] = args.__getattribute__(k)

#no three command options are specified
if len(params) == 0:
    parser.print_help()
    sys.exit()

# get API key for OMDb API
if args.__getattribute__('apikey'):
    params['apikey'] = args.__getattribute__('apikey')
else:
    print("Error: API key must be passed via --apikey=YOUR_KEY ",
          file=sys.stderr)
    sys.exit(1)

# call OMDb API
apicall = urlopen('https://www.omdbapi.com/?%s' % urlencode(params), timeout=8)
result = apicall.read()
apicall.close()

# no movie title specified
if not args.t:
    print("NO MOVIE TITLE is specified!!")
    sys.exit()

# print raw output and exit
print(result)
sys.exit()
