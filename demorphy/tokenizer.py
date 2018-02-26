# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re

#Split from whitespaces not to ruin named entities, e-mails, urls, abbreviations


def tokenize(single_sentence):
    """
    Split text from whitespaces not to ruin named entities, urls, e-mail adresses and abbreviations.
    Don't split from hypen or @ for above reason
    Split from only unambigious punctuation marks , ; ... ?
    Not disambiguating . is sentence boundary or abbreviation component, not processing "."s
    Feel free to extend with more symbols like $, euro or other currency marks.

    Args:
        single_sentence: unicode string  
    Returns:
        List of tokens of the sentence. Note that punctuation marks that are possibly part of a token is not splitted. Hence, 
        sentence boundary period/abbreviation period disambiguation is developer's responsibility.  
    Raises:
        None
    Examples:
        >>> tokenize(u"Ich ggf. möchte")
        [u'Ich', u'ggf.', u'möchte.']
    """

    return  filter(None, re.split(r"[?!,;\s]+" , single_sentence, flags=re.UNICODE))
