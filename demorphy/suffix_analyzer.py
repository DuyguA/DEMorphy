# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from collections import OrderedDict


class SuffixAnalyzer(object):
    """
    Class for heuristically finding morphological paradigm of a given word, provided it's "verb-looking"
    Includes common endings for verbs and methods for analyzing words by endings.
    """

    VERB_END = OrderedDict([
        ("test", ["V,2per,sing,past,ind", "V,2per,sing,past,subj"]),
        ("est", ["V,2per,sing,pres,subj"]),
        ("tet", ["V,2per,plu,past,subj", "V,2per,plu,past,subj"]),
        ("ten", ["V,1per,plu,past,ind", "V,1per,plu,past,subj", "V,3per,plu,past,ind", "V,3per,plu,past,subj"]),
        ("et",["V,2per,plu,pres,subj"]),
        ("st", ["V,2per,sing,pres,ind"]),
        ("en", ["V,1per,plu,pres,ind", "V,1per,plu,pres,subj", "V,3per,plu,pres,ind", "V,3per,plu,pres,subj", "V,inf"]),
        ("te", ["V,1per,sing,past,ind", "V,1per,sing,past,subj", "V,3per,sing,past,ind", "V,3per,sing,past,subj"]),
        ("e",["V,1per,sing,pres,ind", "V,1per,sing,pres,subj", "V,3per,sing,pres,subj"]),
        ("t", ["V,2per,plu,pres,ind", "V,3per,sing,pres,ind", "V,imp,plu"])
        ])

    VERB_GE = OrderedDict([
            ("tem", ["ADJ,masc,sing,dat,pos,strong", "ADJ,neut,sing,dat,pos,strong"]),
            ("ten", ["ADJ,masc,sing,gen,pos", "ADJ,masc,sing,acc,pos", "ADJ,fem,sing,gen,pos,weak", "ADJ,neut,sing,gen,pos", "ADJ,noGend,plu,nom,pos,weak", "ADJ,noGend,plu,gen,pos,weak", "ADJ,noGend,sing,dat,pos,weak", "ADJ,noGend,plu,dat,pos", "ADJ,noGend,plu,acc,pos,weak"]),
            ("ter", ["ADJ,masc,sing,nom,pos,strong", "ADJ,fem,sing,gen,pos,strong", "ADJ,fem,sing,dat,pos,strong", "ADJ,noGend,plu,gen,pos,strong", "ADJ,comp,<pred>", "ADJ,comp,<adv>"]), 
            ("tes", ["ADJ,neut,sing,nom,pos,strong", "ADJ,neut,sing,acc,pos,strong"]),
            ("te", ["ADJ,masc,sing,nom,pos,weak", "ADJ,fem,sing,nom,pos", "ADJ,fem,sing,acc,pos", "ADJ,neut,sing,nom,pos,weak", "ADJ,neut,sing,acc,pos,weak", "ADJ,noGend,plu,nom,pos,strong", "ADJ,noGend,plu,acc,pos,strong"]),
            ("t", ["V,ppast", "ADJ,pos,<pred>", "ADJ,pos,<adv>"])
            ])

    VERB_ADJ_END = OrderedDict([
        ("endem", ["ADJ,masc,sing,dat,pos,strong", "ADJ,neut,sing,dat,pos,strong"]),
        ("ender", ["ADJ,masc,sing,nom,pos,strong", "ADJ,fem,sing,gen,pos,strong", "ADJ,fem,sing,dat,pos,strong", "ADJ,noGend,plu,gen,pos,strong", "ADJ,comp,<pred>", "ADJ,comp,<adv>"]),
        ("enden", ["ADJ,masc,sing,gen,pos", "ADJ,masc,sing,acc,pos", "ADJ,fem,sing,gen,pos,weak", "ADJ,neut,sing,gen,pos", "ADJ,noGend,plu,nom,pos,weak", "ADJ,noGend,plu,gen,pos,weak", "ADJ,noGend,sing,dat,pos,weak", "ADJ,noGend,plu,dat,pos", "ADJ,noGend,plu,acc,pos,weak"]),
        ("endes", ["ADJ,neut,sing,nom,pos,strong", "ADJ,neut,sing,acc,pos,strong"]),
        ("ende", ["ADJ,masc,sing,nom,pos,weak", "ADJ,fem,sing,nom,pos", "ADJ,fem,sing,acc,pos", "ADJ,neut,sing,nom,pos,weak", "ADJ,neut,sing,acc,pos,weak", "ADJ,noGend,plu,nom,pos,strong", "ADJ,noGend,plus,acc,pos,strong"]),
        ("end", ["ADJ,pos,<pred>", "ADJ,pos,<adv>", "V,ppres"])
        ])

    def __init__(self):
        pass

    @staticmethod
    def guess_word_by_suffix(word):
        """
        Args:
        Returns:
            list of analysis strings.
        Raises:
            None
        Examples:
            >>> SuffixAnalyzer.guess_word_by_suffix(u"grepend")
            ["ADJ,pos,<pred>", "ADJ,pos,<adv>", "V,ppres"]
        """
        if word.startswith(u"ge"):
            for (suff, paradigm_list) in SuffixAnalyzer.VERB_GE.items():
                if word.endswith(suff):
                    lemma = word[:-len(suff)] + u"t" 
                    return lemma, paradigm_list

        for (suff, paradigm_list) in SuffixAnalyzer.VERB_ADJ_END.items():
            if word.endswith(suff):
                lemma = word[:-len(suff)] + u"end" 
                return lemma, paradigm_list

        for (suff, paradigm_list) in SuffixAnalyzer.VERB_END.items():
            if word.endswith(suff):
                lemma = word[:-len(suff)] + u"en"
                return lemma, paradigm_list

        return None, []
