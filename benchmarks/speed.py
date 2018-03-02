from __future__ import absolute_import, unicode_literals, division
import codecs
import datetime
import functools
import logging
import os

import time
import timeit
import gc

from demorphy import Analyzer
analyzer = Analyzer(char_subs_allowed=True)

logger = logging.getLogger('demorphy.bench')

def measure_indiv(func, inner_iterations=1, repeats=5):
    gc.disable()
    times = []
    for x in range(repeats):
        start = time.time()
        func()
        times.append(time.time() - start)

    gc.enable()
    return inner_iterations/min(times) 

def load_data(path):
    words = []
    with codecs.open(path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().lower()
            words.append(word)
    return words

def bench_tags(words):
    def _run():
        for word in words:
            analyzer.analyze(word)
    measure = functools.partial(measure_indiv, repeats=repeats)
    logger.info("    analyze(w): %0.0f words/sec", measure(_run, len(words)))
