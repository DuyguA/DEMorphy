# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest

from demorphy.token_types import is_punkt, is_email, is_url, contains_num, is_roman_number, is_egzotic_entity, is_abbrev


class TestSmallMethods:
    def test_punkt(self):
        assert is_punkt(u"..,")
        assert is_punkt(u". .,")
        assert is_punkt(u". .> !,")
        assert is_punkt(u" ")
        assert is_punkt(u"  ")
        assert is_punkt(u"duygu") == False
        assert is_punkt(u"ja!") == False
        assert is_punkt(u"12.04.2017") == False

    def test_email(self):
        assert is_email(u"duygu.altinok@4com.de")
        assert is_email(u"duygu@4com.de")
        assert is_email(u"duygu@StarsWithDiamonds")
        assert is_email(u"duyguStarsWithDiamonds") == False
        assert is_email(u"ja!") == False
        assert is_email(u"ja!?  ?") == False

    def test_url(self):
        assert is_url(u"4com.de")
        assert is_url(u"www.4com.de")
        assert is_url(u"wwww.google.com") 
        assert is_url(u"wwww.google.com.tr") 
        assert is_url(u"http://wwww.google.com") 
        assert is_url(u"http://wwww.google.com.tr") 
        assert is_url(u"https://wwww.google.com") 
        assert is_url(u"https://wwww.google.com.tr") 
        assert is_url(u"duygu@StarsWithDiamonds") == False
        assert is_url(u"duyguStarsWithDiamonds") == False
        assert is_url(u"duygu.altinok@4com.de") == False

    def test_contains_num(self):
        assert contains_num(u"12")
        assert contains_num(u"12.21")
        assert contains_num(u"v.1.0")
        assert contains_num(u"duygu383")
        assert contains_num(u"duygu") == False

    def test_roman(self):
        assert is_roman_number(u"XI")
        assert is_roman_number(u"XIIIII") == False
        assert is_roman_number(u"X??") == False
        assert is_roman_number(u"X??II") == False
        assert is_roman_number(u"duygu") == False

    def test_egzotic(self):
        assert is_egzotic_entity(u"#savetheworld")
        assert is_egzotic_entity(u"DEMorphy")
        assert is_egzotic_entity(u"LeMonde")
        assert is_egzotic_entity(u"duygu") == False

    def test_abbrev(self):
        assert is_abbrev(u"1.2.2011")
        assert is_abbrev(u"ggf.")
        assert is_abbrev(u"MIT")
        assert is_abbrev(u"CIA")
        assert is_abbrev(u"LeMonde") == False
        assert is_abbrev(u"duygu") == False
