import pprint

from demorphy import Analyzer
from demorphy.cache import memoize, lrudecorator



def main(cache_size):
    """
    Sample usage
    We use cache for recurring words such as pronouns, conjunctions, common verbs, modular and auxiliary verbs.
    """
    analyzer = Analyzer(char_subs_allowed=True)
    cached = memoize if cache_size=="unlim" else (lrudecorator(cache_size) if cache_size else (lambda x: x))
    analyze = cached(analyzer.analyze)
    x = analyzer.iter_lexicon_formatted(u"ge")
    for i in x:
        print(i)





if __name__=="__main__":
    main(200)
