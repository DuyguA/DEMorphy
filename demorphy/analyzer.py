# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import threading
import os

from demorphy.data import CHAR_SUBSTITUTES
from demorphy.suffix_analyzer import SuffixAnalyzer
from demorphy  import morph_dict
from demorphy.tagset import ParsedResult


class Analyzer(object):
    PATH_ENV_VAR = "DEMORPHY_PATH"
    DEFAULT_SUBSTITUTES = CHAR_SUBSTITUTES
    

    _lock = threading.RLock()

    def __init__(self, char_subs_allowed=True):
        """"
        Initialize Analyzer object by dictionary. Dictionary consists of dag, lemma list and paradigms list.
        Examples:
            >>> from demorph import Analyzer
            >>> analyzer = Analyzer(char_subs_allowed=True)
        """

        path = Analyzer.find_dictionary_path()

        with self._lock:
            self.dictionary = morph_dict.Dictionary(path)

        self.char_substitutes = self.dictionary.dafsa.compile_replaces(self.DEFAULT_SUBSTITUTES if char_subs_allowed else {})

        self.extra_char_mappings = {u"ß":u"ss", u"ss":u"ß", u"ue":u"ü", u"oe":u"ö"}

        self.iter_lexicon_raw = self.dictionary.iter_lexicon

    def analyze_by_dafsa(self, surface_form):
        """
        Look up the word from the words dag.
        Args:
            surface_form: Surface form, used as in German lexicon e.g. bist, kurierte...
        Returns:
            list of ParsedResult objects
        Raises:
            None
        Examples:
            >>> analyzer.analyze_by_dafsa(u"gehen")
            [{'PTB_TAG': 'JJ', 'CATEGORY': 'ADJ', 'LEMMA': 'rot', 'ADDITIONAL_ATTRIBUTES': '<adv>', 'DEGREE': 'pos', 'STTS_TAG': 'ADJD'},
             {'PTB_TAG': 'JJ', 'CATEGORY': 'ADJ', 'LEMMA': 'rot', 'ADDITIONAL_ATTRIBUTES': '<pred>', 'DEGREE': 'pos', 'STTS_TAG': 'ADJD'}]
        """

        para_lemma_id_list = self.dictionary.find_paradigm_lemma_id(surface_form)
        para_lemma_list = [(self.dictionary.lookup_lemma(lemma_id), self.dictionary.lookup_paradigm(paradigm_id)) for (lemma_id, paradigm_id) in para_lemma_id_list]
        return [ParsedResult(paradigm_str, lemma) for (lemma, paradigm_str) in para_lemma_list]

    def analyze_by_ending(self, surface_form):
        """
        Analyze word by its ending
        Args:
            surface_form: Surface form, just as in lexicon googliert
        Returns:
            list of ParsedResult objects
        Raises:
            None
        Examples:
            >>> analyzer.analyze_by_ending(u"googlendem")
            [{'PTB_TAG': 'JJ', 'GUESSER': True, 'CATEGORY': 'ADJ', 'CASE': 'dat', 'LEMMA': 'googlend', 'STARKE': 'strong', 'DEGREE': 'pos', 'STTS_TAG': 'ADJA', 'NUMERUS': 'sing', 'GENDER': 'masc'}, 
             {'PTB_TAG': 'JJ', 'GUESSER': True, 'CATEGORY': 'ADJ', 'CASE': 'dat', 'LEMMA': 'googlend', 'STARKE': 'strong', 'DEGREE': 'pos', 'STTS_TAG': 'ADJA', 'NUMERUS': 'sing', 'GENDER': 'neut'}]
        """

        lemma, para_list = SuffixAnalyzer.guess_word_by_suffix(surface_form)
        return [ParsedResult(paradigm_str, lemma, guesser=True) for paradigm_str in para_list]

    def analyze(self, surface_form):
        """
        Look up the word from dafsa, if not fall back onto suffix analyzer
        Char subsitutes already has ü possibly u, ö possibly o i.e. umlauts. However, DAWG package only allows one char-to-one char
        mapping. Hence ss<->ß, ü<->ue and  ö<->oe still remains uncovered and lead rather ugly code here
        Args:
            surface_form: word from lexicon
        Returns:
            list of ParsedResult objects
        Raises:
            None
        Examples:
            >>> analyzer.analyze(u"Flughafen")
            [{'PTB_TAG': 'NN', 'NUMERUS': 'sing', 'CATEGORY': 'NN', 'CASE': 'acc', 'LEMMA': 'Flughafen', 'STTS_TAG': 'NN', 'GENDER': 'masc'},
             {'PTB_TAG': 'NN', 'NUMERUS': 'sing', 'CATEGORY': 'NN', 'CASE': 'dat', 'LEMMA': 'Flughafen', 'STTS_TAG': 'NN', 'GENDER': 'masc'}, {'PTB_TAG': 'NN', 'NUMERUS': 'sing', 'CATEGORY': 'NN', 'CASE':             'nom', 'LEMMA': 'Flughafen', 'STTS_TAG': 'NN', 'GENDER': 'masc'}]
        """

        similar_words = self.dictionary.find_similar_words(surface_form, self.char_substitutes)
        if similar_words:
            return self.analyze_by_dafsa(similar_words[0])
        else:
            nword = surface_form
            for em in self.extra_char_mappings:
                nword = nword.replace(em, self.extra_char_mappings[em])
            if nword != surface_form:
                if self.is_known(nword):
                    return self.analyze_by_dafsa(nword)
            return self.analyze_by_ending(surface_form)

    def is_known(self, word):
        """
        Return if word is in known words. Char substitution is upto the initialization.
        Args:
            word: word as in lexicon, geschreiben, bist, angerufen...
        Returns:
            Boolean
        Raises:
            None
        Examples:
            >>> analyzer.is_known(u"duygu")
            False
            >>> analyzer.is_known(u"roter")
            True
            >>> analyzer.is_known(u"grosse")
            True
            >>> analyzer.is_known(u"große")
            True
        """

        return self.dictionary.is_known(
                word=word,
                char_substitutes=self.char_substitutes
                )
    
    def iter_lexicon_formatted(self, prefix=u""):
        """
        Iterate over all lexicon, by prefix on demand. Default is empty prefix i.e. all words
        Args:
            prefix: unicode string, default empty string
        Yields:
            (word, ParsedResult) pairs
        """

        for (word, paradigm_str, lemma) in self.dictionary.iter_lexicon(prefix):
            yield word, ParsedResult(paradigm_str, lemma)
    
    @classmethod
    def find_dictionary_path(cls):
        """Return absolute path of data directory"""

        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
