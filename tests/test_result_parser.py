# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest

from demorphy.tagset import ParsedResult

class TestParadigmStrings:
    def test_paradigmstr(self):
        parastr = "WPRO,masc,acc,sing,<attr>,strong"
	lemma = u"welche"
	t = ParsedResult(parastr, lemma)
        assert t.lemma == u"welche"
        assert t.gender == "masc"
        assert t.numerus is None
        assert t.case == "acc"
        assert t.person is None
        assert t.tense is None
        assert t.mode is None
        assert t.inflection is None
        assert t.degree is None
        assert t.category == "WPRO"
        assert t.starke == "strong"
        assert t.orto is None
        assert t.additional_attributes == "<attr>"
        assert t.stts_tag == "PWAT"
        assert t.ptb_tag == "DT"


    def test_para2(self):
        parastr = "CONJ,<coord>"
	lemma = u"aber"
	t = ParsedResult(parastr, lemma)
        assert t.lemma == u"aber"
        assert t.gender is None
        assert t.numerus is None
        assert t.case is None
        assert t.person is None
        assert t.tense is None
        assert t.mode is None
        assert t.inflection is None
        assert t.degree is None
        assert t.category == "CONJ"
        assert t.starke is None
        assert t.orto is None
        assert t.additional_attributes == "<coord>"
        assert t.stts_tag == ["KOUI", "KOUS", "KOKOM", "KON"]
        assert t.ptb_tag == "CC"

class TestContains:
    def test_contains_str(self):
        t = ParsedResult("ADJ,masc,acc,sing,sup")

        assert "ADJ" in t
        assert "masc" in t
        assert "acc" in t
        assert "sing" in t
        assert "sup" in t

    def test_contains_set(self):
        t = ParsedResult("ADJ,masc,acc,sing,sup")

        assert {"ADJ", "masc"} in t
        assert {"masc"} in t
        assert {"acc", "ADJ", "acc"} in t

    def test_not_contains_set(self):
        t = ParsedResult("ADJ,masc,acc,sing,sup")

        assert {"ADJ", "masc", "nom"} not in t
        assert {"masc", "nom"} not in t
        assert {"nom"} not in t

    def test_not_contains_str(self):
        t = ParsedResult("ADJ,masc,acc,sing,sup")

        assert "V" not in t
        assert "fem" not in t
        assert "nom" not in t
