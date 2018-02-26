# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


try:
    from dawg import DAWG, RecordDAWG
except ImportError:
    mssg = ("Install dawg package!")
    raise NotImplementedError(mssg)


class LexiconDawg(RecordDAWG):
    """
    Dag for storing the lexicon
    Keys are words, valuea are pairs of numbers indicating lemma and paradigm
    """

    #We are storing 3 unsigned short ints for paradigms and the lemma ID
    #Byte order is big-endian for a proper sorting, please see DAWG documentation
    FORMAT = str(">QQ")

    def __init__(self, data=None):
        if data is None:
            super(LexiconDawg, self).__init__(self.FORMAT)
        else:
           super(LexiconDawg, self).__init__(self.FORMAT, data)
