#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import random
from collections import defaultdict


def markov(text, chain=None):
    if not chain:
        intdict = lambda: defaultdict(int)
        chain = defaultdict(intdict)

    words = text.split(' ')
    word_count = len(words)

    for i, word in enumerate(words):
        if word_count > i + 1:
            chain[word][words[i+1]] += 1

    return chain


def generate_text(chain, max_size=25):
    word = random.choice(chain.keys())
    result = [word, ]

    while word and len(result) < max_size:
        try:
            possible_words = []
            for possible, count in chain[word].items():
                possible_words = possible_words + [possible] * count
            word = random.choice(possible_words)
        except IndexError:
            word = None
        else:
            result.append(word)

    return result
