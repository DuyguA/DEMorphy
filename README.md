# DEMorphy

DEMorphy is a morphological analyzer for German language. DEMorphy provides gender, person, singular/plural etc. full inflection information as well as word lemma.  

* docs: https://demorphy.readthedocs.io
* source code: [github](https://github.com/DuyguA/DEMorphy)


## Installation

OS X & Linux, directly from Github:

```sh
pip install git+git://github.com/DuyguA/DEMorphy.git
```

or

```sh
pip install git+https://github.com/DuyguA/DEMorphy.git
```

OS X & Linux, download package and data separately. Make a 

```sh
pip install demorphy
```

then, download [the dictionary](https://github.com/DuyguA/DEMorphy/blob/master/DEMorphy/data/words.dg) and place it under **demorphy/demorphy/data/**.

## Usage 

Basic usage:

```sh
$ python
```
```python
>>> from demorphy import Analyzer
>>> analyzer = Analyzer(char_subs_allowed=True)
>>> s = analyzer.analyze(u"gegangen")
>>> for anlyss in s:
        print anlyss
{'CATEGORY': u'ADJ', 'PTB_TAG': u'JJ', 'STTS_TAG': u'ADJD', 'ADDITIONAL_ATTRIBUTES': u'<adv>', 'DEGREE': u'pos', 'LEMMA': u'gegangen'}
{'CATEGORY': u'ADJ', 'PTB_TAG': u'JJ', 'STTS_TAG': u'ADJD', 'ADDITIONAL_ATTRIBUTES': u'<pred>', 'DEGREE': u'pos', 'LEMMA': u'gegangen'}
{'CATEGORY': u'V', 'LEMMA': u'gehen', 'STTS_TAG': u'V', 'TENSE': u'ppast', 'PTB_TAG': u'V'}
```

## Citing


    Altinok, D.: DEMorphy, German Language Analyzer, 
    Berlin, 2018

Links:

* [PDF](www.arxiv.org/demorphypage)
* [Short Survey on German 2-Level Morphology](www.linkto2levelpage.de)
* [Possible usages of DEMorphy in NLP projects](www.linktocustomer.de)

## Authors

* **Duygu Altinok** 

## License

[MIT](https://github.com/DuyguA/DEMorphy/blob/master/LICENSE)
