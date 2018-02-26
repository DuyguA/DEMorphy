# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest

from demorphy.tokenizer import tokenize

class TestTokenizer:
    def test_split_simple(self):
        assert tokenize(u"Ich bin krank") == [u"Ich", u"bin", u"krank"]

    def test_split_hypen(self):
        assert tokenize(u"Wir können uns auf der U-Bahn treffen") == [u'Wir', u'können', u'uns', u'auf', u'der', u'U-Bahn', u'treffen.']

    def test_split_email(self):
        assert tokenize(u"Bitte schreiben Sie an duygu@iam.uni-bonn.de ") == [u"Bitte", u"schreiben", u"Sie", u"an", u"duygu@iam.uni-bonn.de"]

    def test_split_url(self):
        assert tokenize(u"www.akbank.com.tr ich du Sie bahn.de") == [u'www.akbank.com.tr', u'ich', u'du', u'Sie', u'bahn.de']

    def test_split_punct(self):
        assert tokenize(u"Ich bin krank, sie auch; ich auch") == [u'Ich', u'bin', u'krank', u'sie', u'auch', u'ich', u'auch']

    def test_split_abbrev(self):
        assert tokenize(u"ggf. kommen wir auf Ihr Angebot zurück") == [u'ggf.', u'kommen', u'wir', u'auf', u'Ihr', u'Angebot', u'zurück']
