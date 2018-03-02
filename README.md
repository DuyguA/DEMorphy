# DEMorphy

DEMorphy is a morphological analyzer for German language. DEMorphy provides gender, person, singular/plural etc. full inflection information as well as word lemma.  

* docs: https://demorphy.readthedocs.io
* source code: [Github](https://github.com/DuyguA/DEMorphy)


## Installation

OS X & Linux, directly from Github:

```sh
git clone https://github.com/DuyguA/DEMorphy.git
cd DEMorphy
python setup.py install
```

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


    Altinok, D.: DEMorphy, German Language Analyzer
    Berlin, 2018

Links:

* [PDF](www.arxiv.org/demorphypage)
* [Short Survey on German 2-Level Morphology](www.linkto2levelpage.de)
* [Possible usages of DEMorphy in NLP projects](www.linktocustomer.de)

## Authors

* **Duygu Altinok** 

## License

[MIT](https://github.com/DuyguA/DEMorphy/blob/master/LICENSE.md)
