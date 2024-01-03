#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from functools import reduce

options = []
parameters = []

options, parameters = reduce(
    lambda sets, new_item:
        (sets[0] + [new_item], sets[1])
        if new_item.startswith('-')
        else (sets[0], sets[1] + [new_item]),
        sys.argv[1:],
        ([], []))

options = map(lambda x: x[1:] if x.startswith('--') else x, options)

#print(options)
#print(parameters)

# preprocessing the options, including:
# -output-directory=STRING

def translate_winpath(path):
    return os.popen(f'wsl wslpath -u {path}').read().strip()

options_pp = list(map(
    lambda x:
        f'-output-directory={translate_winpath(x[18:])}'
        if x.startswith('-output-directory=')
        else x,
    options))

parameters_pp = parameters
if parameters and not parameters[0].startswith('\\'):
    parameters_pp = list(map(
        lambda x:
            translate_winpath(x)
            if not x.startswith('&')
            else x,
        parameters
    ))

print(['wsl'] + ['latex'] + options_pp + parameters_pp)
os.system(' '.join(['wsl', '--', 'dviluatex'] + options_pp + parameters_pp))