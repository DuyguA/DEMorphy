# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from demorphy.morph_dict.load_dicts import load_dicts


class Dictionary(object):
    """
    Dictionary build on dawg, lemma list and paradigm list
    """
    __slots__ = ["lang", "_dicts", "dafsa", "lemma_list", "path", "paradigm_list"]

    def __init__(self, path):

        self._dicts = load_dicts(path)

        self.lang = "DE_de"
        self.dafsa = self._dicts.words
        self.lemma_list = self._dicts.lemmas
        self.paradigm_list = self._dicts.paradigms

        self.path = path

    def find_paradigm_lemma_id(self, word):
        """
        Given word, find all (lemmaid, paradigmid) pairs
        Args:
            word: unicode string
        Returns:
            list of tuples
        Raises:
            None
        """
        para_lemma_ids_list = self.dafsa[word]
        return para_lemma_ids_list

    def lookup_paradigm(self, para_id):
        """
        Given paradigm id, find the paradigm string
        Args:
            para_id: integer
        Returns:
            paradigm string
        Raises:
            None
        """
        paradigm_str = self.paradigm_list[para_id]
        return paradigm_str

    def lookup_lemma(self, lemma_id):
        """
        Given lemma id, find the paradigm string
        Args:
            lemma_id: integer
        Returns:
            lemma string
        Raises:
            None
        """
        lemma = self.lemma_list[lemma_id]
        return lemma

    def is_known(self, word, char_substitutes={}):
        """
        Check if a word is in lexicon
        """
        if char_substitutes:
            return bool(self.dafsa.similar_keys(word, char_substitutes))
        else:
            return word in self.dafsa

    def find_similar_words(self, word, char_substitutes={}):
        """
        Find similar keys to the given word upto the character changes by char substitution.
        Args:
            word: word from lexicon
            char_substitutes: dictionary for possible characater replacements. default is empty dict
        Returns:
            list of words that are similar to the given word. If word is not in dafsa, empty list.
        Raises:
            None
        """
        words = self.dafsa.similar_keys(word, char_substitutes)
        return words

    def iter_lexicon(self, prefix=u""):
        """
        Iterate over all lexicon, on demand by all words beginning with a given prefix.
        Here we use advantage of data structure.
        Args:
            prefix: unicode string, default empty string
        Yields:
            (word, paradigm, lemma)  tuples
        """
        for word, (lemma_id, para_id) in self.dafsa.iteritems(prefix):
            paradigm, lemma = self.lookup_paradigm(para_id), self.lookup_lemma(lemma_id)
            yield word, paradigm, lemma
