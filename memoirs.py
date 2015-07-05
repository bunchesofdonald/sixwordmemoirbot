#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

from markov import markov, generate_text


with open('memoirs.json') as infile:
    memoirs = json.load(infile)
    memoirs = [re.sub('[",\.!?-]+', '', m).lower() for m in memoirs]

chain = None
for m in memoirs:
    chain = markov(m, chain)

text = generate_text(chain)
while " ".join(text) in memoirs or len(text) != 6:
    text = generate_text(chain)

print " ".join(text).capitalize()
