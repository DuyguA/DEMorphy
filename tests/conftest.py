# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='session')
def analyzer():
    import demorphy
    return demorphy.Analyzer(char_subs_allowed=True)


@pytest.fixture(scope='session')
def Tag(morph):
    import demorphy
    return demorphy.TagClass
