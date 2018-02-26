# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

"""
Token types most probably one want to filters. 
"""

import re



def is_punkt(token):
    """
    Return if token consists of only punctuation and whitespace
    Args:
        token: single token
    Returns:
        Boolean
    Raises:
        None
    Examples:
        >>> is_punkt(" ")
        True
        >>> is_punkt(", ,")
        True
        >>> is_punkt("?!!")
        True
        >>> is_punkt("x")
        False
    """
    #punkt = string.punctuation
    punkt = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return all(letter in punkt or letter.isspace() for letter in token)


def is_email(token):
    """
    Return True for e-mails. Very rough, some other words for instance duygu@SonyCenter return True as well. 
    However, most probably one doesn't want to process that token types anyway.
    Args:
        token: single token
    Returns:
        Booelan
    Raises:
        None
    Examples:
        >>> is_email("duygu@space.de")
        True
        >>> is_email("breakfast@Tiffany's")
        True
        >>> is_email(",")
        False
        >>> is_email("applepie")
        False
    """
    return "@" in token

def is_url(token):
    """
    Return True for url strings. 
    Args:
        token: single token
    Returns:
        Booelan
    Raises:
        None
    Examples:
        >>> is_url("www.google.com")
        True
        >>> is_url("google.com")
        True
        >>> is_url("spacy.org")
        True
        >>> is_url("2.3.1987")
        False
    """
    regex_url = r'((www\d{0,3}[.]|https?://|redir\.aspx\?|[%a-z0-9.\-]+[.][a-z]{2,4}/)([^\s()<>\[\]]+))'
    if any(sw in token for sw in ["www.", "http", ".com", ".org", ".de"]):
      return True
    if re.match(regex_url, token):
      return True
    return False


def contains_num(token):
    """
    Return True for 
    - Dates: 21.01.2011
    - Probably egzotic entities: B2B, sum41 
    - Skype names: duygu621
    Args:
        token: single token
    Returns:
        Booelan
    Raises:
        None
    Examples:
        >>> contains_num("duygu")
        False
        >>> contains_num("2.2017")
        True
    """
    nums = "0123456789"
    return any(num in token for num in nums)


# Regex comes from "Dive into Python" book.
roman_num_regex = re.compile("""
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
""", re.VERBOSE | re.IGNORECASE)


def is_roman_number(token):
    """
    Return True if token is a Roman ordinal number
    Args:
        token: single token
    Returns:
        Boolean
    Raises:
        None
    Examples:
        >>> is_roman_number('IX')
        True
        >>> is_roman_number('XIIIII')
        False
        >>> is_roman_number('II')
        True
        >>> is_roman_number('')
        False
        >>> is_roman_number('duygu')
        False
    """
    if not token:
        return False
    return roman_num_regex.match(token) is not None

def is_egzotic_entity(token):
    """
    Return True if token looks like 
    Skype id duygu.altin
    Twitter hashtag #direnduygu
    Initials:  W., D.A.
    other egzotic tokens such v.2.1.
    Dates such as 2.12.2015 go here as well
    Camel cases are usually not part of language's lexicon and usually an entity e.g. IoT, eGov
    Args:
        token: single token
    Returns:
        Boolean
    Raises:
        None
    """
    if any(t in token for t in [".", "!", "#", "&"]):
        return True
    #Camel case words 
    if not token.isupper() and not token.islower():
        return True
    return False

def is_abbrev(token):
    """
    Return if given token is an abbreviation
    Tokens with . in them returns True
    Tokens that "look like"a an  abbreviation returns True
    Args:
        token: single token
    Returns:
        Boolean
    Raises:
        None
    """
    if "." in token:
        return True
    return looks_like_abbrev(token)


def looks_like_abbrev(token):
    """
    Return if token looks like an abbrev
    Tokens that are longer than 3 characters returns False.
    All upper case and short tokens return True e.g. MIT, AAL, LCD
    All consonant tokens evaluates to an abbreviation such as lcd, ggf
    Args:
        token: single token
    Returns:
        Boolean
    Raises:
        None
    """
    vowels = u"aeiouäöü"
    #too long to be abbrev
    if len(token) > 3:
        return False
    if word.isupper():
        return True
    #all consonant words like lcd, ggf
    if not any(x for x in vowels if x in word):
        return True
    #TODO check word's ending floows German trigrams or not, get perplexity from a char level LM
    return False
