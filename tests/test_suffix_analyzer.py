# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest

from demorphy.suffix_analyzer import SuffixAnalyzer


class TestAnalogyLookup:
    def test_suff_ana(self):
        word = u"googlendem"
        result = (u"googlend", ["ADJ,masc,sing,dat,pos,strong", "ADJ,neut,sing,dat,pos,strong"])
        res = SuffixAnalyzer.guess_word_by_suffix(word)
        assert res == result

    def test_empty(self):
        word = u"lalala"
        result = None, []
        res = SuffixAnalyzer.guess_word_by_suffix(word)
        assert res == result


