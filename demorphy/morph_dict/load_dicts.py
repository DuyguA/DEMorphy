from __future__ import absolute_import, unicode_literals

import os
import collections

from demorphy import dafsa
from demorphy.data import lemmas, paradigms

WORDS = None
LoadedDict = collections.namedtuple("LoadedDict", [
    'words',
    "lemmas",
    'paradigms',
])


def load_dicts(path):
    """
    Load words dafsa from its dump, lemmas list and paradigms list
    path points to the data folder where words dafsa was dumped
    Args:
        path: directory where dafsa, lemma and paradigm list lies
    Returns:
        A LoadedDict object, basicly tuple of dafsa, lemma list and paradigm list
    """
    global WORDS
    if not WORDS:
        WORDS = dafsa.LexiconDawg().load(os.path.join(path, "words.dg"))

    return LoadedDict(
        words=WORDS,
        lemmas=lemmas,
        paradigms=paradigms,
    )
