# DEMorphy

DEMorphy is a morphological analyzer for German language. DEMorphy provides gender, person, singular/plural etc. full inflection information as well as word lemma.  

* source code and usage docs: [Github](https://github.com/DuyguA/DEMorphy)
* companion German morphological dictionaries [Github](https://github.com/DuyguA/german-morph-dictionaries)


## Installation

OS X & Linux, directly from Github:

```sh
$ git clone https://github.com/DuyguA/DEMorphy
$ cd DEMorphy
$ python setup.py install
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

Usage with cache decorators:

```python
>>> from demorphy import Analyzer
>>> from demorphy.cache import memoize, lrudecorator
>>> analyzer = Analyzer(char_subs_allowed=True)
>>> cache_size = 200 #you can arrange the size or unlimited cache. For German lang, we recommed 200 as cache size.
>>> cached = memoize if cache_size=="unlim" else (lrudecorator(cache_size) if cache_size else (lambda x: x))
>>> analyze = cached(analyzer.analyze)
>>> s = analyze(u"gegangen")
>>> for anlyss in s:
        print anlyss
{'CATEGORY': u'ADJ', 'PTB_TAG': u'JJ', 'STTS_TAG': u'ADJD', 'ADDITIONAL_ATTRIBUTES': u'<adv>', 'DEGREE': u'pos', 'LEMMA': u'gegangen'}
{'CATEGORY': u'ADJ', 'PTB_TAG': u'JJ', 'STTS_TAG': u'ADJD', 'ADDITIONAL_ATTRIBUTES': u'<pred>', 'DEGREE': u'pos', 'LEMMA': u'gegangen'}
{'CATEGORY': u'V', 'LEMMA': u'gehen', 'STTS_TAG': u'V', 'TENSE': u'ppast', 'PTB_TAG': u'V'}
```

Iterating over all the lexicon:

```python
>>> from demorphy import Analyzer
>>> analyzer = Analyzer(char_subs_allowed=True)
>>> ix = analyzer.iter_lexicon_formatted()
>>> for i in ix:
        print(i)
```
One can iterate over the lexicon words with a given prefix. Following code will iterate over all the words that begins with "ge":

```python
>>> ix = analyzer.iter_lexicon_formatted(prefix=u"ge")
>>> for i in ix:
        print(i)
```


## Citing


    Altinok, D.: DEMorphy, German Language Analyzer
    Berlin, 2018

Links:

* [PDF](https://arxiv.org/abs/1803.00902)
* [Short Survey on German 2-Level Morphology](https://duygua.github.io/blog/2017/12/10/german-two-level-morphology/)
* [Possible usages of DEMorphy in NLP projects](www.linktocustomer.de)

## Authors

* **Duygu Altinok** 

## License

[MIT](https://github.com/DuyguA/DEMorphy/blob/master/LICENSE.md)
