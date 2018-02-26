# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from collections import OrderedDict


class ParsedResult(object):
    """
    Class for holding the result of morphologycal analysis.
    """

    __slots__ = ["_lemma", "_guesser", "_paradigm_str", "_paradigm_list", "_gender",
                 "_numerus", "_case", "_person", "_tense", "_mode", "_inflection",
                 "_degree", "_starke", "_category", "_orto","_additional_attributes", "_fields"]

    def __init__(self, paradigm_str, lemma, guesser=False):
        """
        For initializing data fields, intersect possible tagclasses to the paradigm string
        Args:
            paradigm_str: string. Morphological analysis string e.g. : "V,inf", "V,inf,zu", "V,ppast"
            lemma: string. Lemma of the given analysis. Different paradigms might corrspond to different paradigms, since lemma is word category dependent.
            guesser: Boolean. Data field if morphological analysis comes from suffix analyzer unit.
        """
        self._lemma = lemma
        self._guesser = guesser
        self._paradigm_str = paradigm_str
        self._paradigm_list = set(self._paradigm_str.split(","))
        self._gender = self._initialize_field("GENDER")
        self._numerus = self._initialize_field("NUMERUS")
        self._case = self._initialize_field("CASE")
        self._person = self._initialize_field("PERSON")
        self._tense = self._initialize_field("TENSE")
        self._mode = self._initialize_field("MODE")
        self._inflection = self._initialize_field("INFLECTION")
        self._degree = self._initialize_field("DEGREE")
        self._starke = self._initialize_field("STARKE")
        self._category = self._initialize_field("CATEGORY")
        self._orto = self._initialize_field("ORTO")
        self._additional_attributes = self._initialize_field("ATTRS")
        self._fields = self._instance_to_dict()

    def _initialize_field(self, field_identifier):
        field_value = getattr(TagClass, field_identifier).intersection(self._paradigm_list)
        return field_value 

    def _instance_to_dict(self):
        fields = dict((k,v) for k,v in ((prop.upper(), getattr(self, prop)) for prop in dir(self) if not prop.startswith("_")) if v)
        return fields

    def __str__(self):
        return str(self._fields)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self._fields)

    @property
    def lemma(self):
        return self._lemma
        
    @property
    def gender(self):
        return ",".join(self._gender)

    @property
    def numerus(self):
        return ",".join(self._numerus)

    @property
    def case(self):
        return ",".join(self._case)

    @property
    def person(self):
        return ",".join(self._person)

    @property
    def tense(self):
        return ",".join(self._tense)

    @property
    def mode(self):
        return ",".join(self._mode)

    @property
    def inflection(self):
        return ",".join(self._inflection)

    @property
    def degree(self):
        return ",".join(self._degree)

    @property
    def category(self):
        return  ",".join(self._category)

    @property
    def starke(self):
        return  ",".join(self._starke)
        
    @property
    def orto(self):
        return  ",".join(self._orto)

    @property
    def additional_attributes(self):
        return ",".join(self._additional_attributes)

    @property
    def guesser(self):
        return self._guesser

    @property
    def stts_tag(self):
        """
        STTS tag of the word from category and additional attributes
        """
        tag_list = TagClass.STTS_REV[self.category]
        tag = tag_list
        try:
            for attr,t in tag_list.items():
                if attr in self.additional_attributes:
                    tag = t
                    break
        except:
            pass
        return tag

    @property
    def ptb_tag(self):
        """
        PTB tag of the word from category and additional attributes
        """
        tag_list = TagClass.PTB_REV[self.category]
        tag = tag_list
        try:
            for attr,t in tag_list.items():
                if any(attr in cat for cat in  [self.additional_attributes, self.numerus, self.inflection, self.degree]):
                    tag = t
                    break
        except:
            pass
        return tag
    
    def __contains__(self, tags):
        """
        Check if analysis object contains given tags.
        Args:
            tags: string or a set of strings
        Returns:
            Boolean
        Examples:
            >>> o = ParsedResult("ADJ,fem,acc,sing,comp", u"rot")
            >>> "ADV" in o
            False
            >>> "ADJ" in o
            True
            >>> {"ADJ", "fem"} in o
            True
            >>> {"ADJ", "fem", "plu"} in o
            False
            >>> {"ADJ", "plu"} in o
            False
        """

        #{'NN', 'sing'} in tag
        if isinstance(tags, (set, frozenset)):
            if tags <= self._paradigm_list:
                return True
        #'APZR' in tag    
        if tags in self._paradigm_list:
            return True

        return False


class TagClass(object):
    """
    Class for keeping tagset info. Includes gender, numerus, case, person, tense, mode, inflection, degree, category and additional attributes information.
    For STTS tags, please refer to http://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/TagSets/stts-1999.pdf
    For PTB tags, please refer to https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    """

    GENDER = frozenset([
        "masc", #masculine
        "fem",  #feminine
        "neut", #neutral
        "noGender", #no gender after derivation. Not exactly a gender indeed, rather a derivational property. Please see the documentation
        ])

    NUMERUS = frozenset([
        "sing", #singular
        "plu"   #plural
        ])

    CASE = frozenset([
        "nom", #nominative
        "acc", #accusative
        "dat", #dative
        "gen",  #genitive
        ])

    PERSON = frozenset([
        "1per", #first person
        "2per", #second person
        "3per", #third person
        ])
  
    TENSE = frozenset([
        "pres", #simple present, Präsens
        "ppres", #present participle, Partizip I (Partizip Präsens)
        "past", #simple past, preterite,  Präteritum/Imperfekt
        "ppast", #past perfect, Partizip II (Partizip Perfekt)
        ])

    MODE = frozenset([
        "imp", #imperative
        "ind", #indicative
        "subj", #subjunctive
        ])

    INFLECTION = frozenset([
        "inf", #infinitive
        "zu", #infinitive with zu, please see documentation for examples
        ])


    DEGREE = frozenset([
        "pos", #positive, base form of the adjective
        "comp", #comparative
        "sup",  #superlative
        ])
        
    ORTO = frozenset([
        "old", #Older, now unused Dativ
        "short", #shortened forms for  Dativ/Akkusativ e.g. dem Mensch <- dem Menschen
        ])

    STARKE = frozenset([
        "strong", #strong inflection
        "weak", #weak inflection
        ])

    CATEGORY = frozenset([
        "V", #verb
        "ADJ", #adjective
        "ADV", #adverb
        "ART", #artikel
        "CARD", #cardinal number
        "CIRCP", #zirkumposition rechts, please consult tag manual
        "CONJ", #conjunction
        "DEMO", #demonstrative
        "INDEF", #indefinite pronoun
        "INTJ", #interjection
        "ORD", #ordinal number
        "NN", #noun
        "NNP", #proper noun
        "POSS", #possesive
        "POSTP", #postposiiton
        "PRP", #personal pronoun
        "PREP", #preposition
        "PREPART", #preposition with incorporated article
        "PROADV", #pronomial adverb
        "PRTKL", #particle 
        "REL", #relative pronoun
        "TRUNC", #Kompositions-Erstglied , please see the tag manual
        "VPART", #verb particle
        "WPADV", #adverbial interrogative pronoun
        "WPRO", #interrogative pronoun
        "ZU", #zu for infinitive, zu [gehen]
        ])

    ATTRS = frozenset([
        "<mod>", #modal verbs
        "<aux>", #auxiliary verbs
        "<adv>", #adverbial used adjective
        "<pred>", #predicative participle or adjective
        "<ans>", #answers, ja bitte nein 
        "<attr>", #attribute form for adjectives
        "<adj>", #verbal particles of adjectival origin and particles
        "<cmp>", #comparative form for conjunction
        "<coord>", #coordinative form for conjunction
        "<def>", #definite form for articles
        "<indef>", #indefinite form for articles
        "<noinfl>", #no inflection is possible
        "<neg>", #negating form
        "personal", #personal pronoun
        "<prfl>", #pronouns can be used both reflexive or non-reflexive
        "<rec>", #reciprocal pronoun, einander
        "<pro>", #pronominal use
        "<refl>", #reflexive form
        "<subord>", #subordinate form
        "<subst>", #substituierende form
        ])

    STTS_TAGS = OrderedDict({
        "ADJD":["ADJ", ["<pred>", "<adv>"]],
        "ADJA":["ADJ"],
        "ADV":["ADV"],
        "APPR":["PREP"],
        "APPART":["PREPART"],
        "APPO":["POSTP"],
        "APZR": ["CIRCP"],
        "ART":["ART"],
        "CARD":["CARD"],
        "ITJ":["INTJ"],
        "KOUI":[],
        "KOUS":[],
        "KON":[],
        "KOKOM":[],
        "NN" : "NN",
        "NE" : "NNP",
        "PDS":["DEM", ["<subst>"]],
        "PDAT":["DEM", ["<attr>"]],
        "PIS":[],
        "PIAT":[],
        "PIDAT":[],
        "PRF":["PRP", ["<refl>"]],
        "PPER":["PRP"],
        "PPOSS":["POSS", ["<subst>"]],
        "PPOSAT":["POSS", ["<attr>"]],
        "PRELS":["REL", ["<subst>"]],
        "PRELAT":["REL", ["<attr>"]],
        "PWS":["WPRO", ["<subst>"]],
        "PWAT":["WPRO", ["<attr>"]],
        "PWAV":["WPADV"],
        "PAV":["PROADV"],
        "PTKZU":["ZU"],
        "PTKNEG":["PRTKL", ["<neg>"]],
        "PTKVZ":["VPART"],
        "PTKANT":["PRTKL", ["<ans>"]],
        "PTKA":["PREPART"],
        "TRUNC":["TRUNC"],

        "VAFIN":[],
        "VAIMP":[],
        "VAINF":[],
        "VAPP":["V", ["ppast", "<aux>"]],

        "VMFIN":[],
        "VMFINF":[],
        "VMPP":["V", ["ppast", "<mod>"]],

        "VVFIN":[],
        "VVIMP":["V", ["imp"]],
        "VVINF":[],
        "VVIZU":["V", ["zu"]],
        "VVPP":["V", ["ppast"]]
        })

    STTS_REV = {
        "V":OrderedDict([("<mod>","VM"), ("<aux>","VA"), ("","V")]),
        "ADJ":OrderedDict([("<adv>","ADJD"), ("<pred>","ADJD"), ("","ADJA")]),
        "ADV":"ADV",
        "ART":"ART",
        "CARD":"CARD",
        "CIRCP":"APZR",
        "CONJ":["KOUI", "KOUS", "KOKOM", "KON"],
        "DEMO":{"<subst>":"PDS", "<attr>":"PDAT"},
        "INDEF":OrderedDict([("<subst>","PIS"), ("",["PIDAT", "PIAT"])]),
        "INTJ":"ITJ",
        "NN":"NN",
        "NNP":"NE",
        "POSS":{"<subst>":"PPOSS", "<attr>":"PPOSAT"},
        "POSTP":"APPO",
        "PRP":OrderedDict([("<refl>","PRP"), ("","PPER")]),
        "PREP":"APPR",
        "PREPART":"PTKA",
        "ORD":"ADJA",
        "PROADV":"PAV",
        "PRTKL":OrderedDict([("<neg>","PTKNEG"), ("<ans>","PTKANT"), ("","PTK")]),
        "REL":{"<subst>":"PRELS", "<attr>":"PRELAT"},
        "TRUNC":"TRUNC",
        "VPART":"PTKVZ",
        "WPADV":"PWAV",
        "WPRO":{"<subst>":"PWS", "<attr>":"PWAT"},
        "ZU":"PTKZU",
        }


    PTB_TAGS = OrderedDict({
            "CC":["CONJ", ["<coord>"]],
            "CD":["CARD"],
            "DT":["<attr>", ["WPRO", "REL", "POSS", "INDEF", "ART", "DEMO"]],
            "IN":["CONJ", ["<sub>"]], #"PREP"
            "JJR":["ADJ", ["comp"]],
            "JJS":["ADJ", ["sup"]],
            "JJ":["ADJ"],
            "NN":["NN", ["sing"]],
            "NNS":["NN", ["plu"]],
            "NNP":["NNP", ["sing"]],
            "NNPS":["NNP", ["plu"]],
            "PDT":[],
            "POS":[],
            "PRP":["POSS"],
            "PRP$":["PPRO"],
            "RBR":[], #["ADJ", "<Adv>", "comp"]
            "RBS":[], #["ADJ", "<Adv>", "sup"]
            "RB":["ADV", "PROADV", "WPADV"],
            "RP":["PRTKL", "VPART"],
            "UH":["INTJ"],
            "VB":["V", ["inf"]],
            "VBG":[],
            "VBN":[],
            "VBP":[],
            "VBZ":[""],
            "WDT":["WPRO"],
            "WP$":["WPRO", ["gen"]],
            "WP":["WPRO"],
            "WRB":[]
            })

    PTB_REV = {
        "V":OrderedDict([("inf","VB"), ("","V")]),
        "ADJ":OrderedDict([("comp","JJR"), ("sup","JJS"), ("","JJ")]),
        "ADV":"RB",
        "ART":"DET",
        "CARD":"CD",
        "CIRCP":"IN", 
        "CONJ":"CC",
        "DEMO":{"<subst>":"PRON", "<attr>":"DT"},
        "INDEF":{"<subst>":"PRON", "<attr>":"DT"},
        "INTJ":"UH",
        "NN":{"sing":"NN", "plu":"NNS"},
        "NNP":{"sing":"NNP", "plu":"NNPS"},
        "POSS":{"<subst>":"PRON", "<attr>":"DT"},
        "POSTP":"IN",
        "PRP":"PRON",
        "PREP":"IN",
        "PREPART":"IN",
        "ORD":"JJ",
        "PROADV":"RB",
        "PRTKL":"RP",
        "REL":{"<subst>":"PRON", "<attr>":"DT"},
        "TRUNC":"X",
        "VPART":"RP",
        "WPADV":"RB",
        "WPRO":{"<subst>":"PRON", "<attr>":"DT"},
        "ZU":"RP",
        }
