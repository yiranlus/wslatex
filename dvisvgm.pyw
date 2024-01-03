#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from functools import reduce

options = sys.argv[1:-1]
filename = sys.argv[-1]

if ('-v' in sys.argv or
    any(map(lambda x: x.startswith('--version'), sys.argv)) or
    '-h' in sys.argv or
    any(map(lambda x: x.startswith('--help'), sys.argv))):
    os.system(' '.join([r'C:\Windows\system32\wsl.exe', '--', 'dvisvgm'] + sys.argv[1:]))
    exit(0)

if '--stdin' in sys.argv:
    options = sys.argv[1:]
    filename = None

#print(options)
#print(parameters)

# preprocessing the options, including:
# --tmpdir=STRING

def translate_winpath(path):
    return os.popen(f'wsl wslpath -u {path}').read().strip()

options_pp = list(map(
    lambda x:
        f'--tmpdir={translate_winpath(x[8:])}'
        if x.startswith('--tmpdir=')
        else x,
    options))

if filename is None:
    os.system(' '.join([r'C:\Windows\system32\wsl.exe', '--', 'dvisvgm'] + options_pp))
    exit(0)

os.system(' '.join([r'C:\Windows\system32\wsl.exe', '--', 'dvisvgm'] + options_pp + [translate_winpath(filename)]))