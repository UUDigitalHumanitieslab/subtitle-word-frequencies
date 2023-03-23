import os
import re

'''Regular expressions that match metatext fragments.'''
metatext_patterns = [
    r'888',
    r'NPO ONDERTITELING TT888, \d+\ninformatie: service.npo.nl',
]

def matches_metatext_re(fragment):
    '''Returns True if a fragment matches any of the regular expressions above.'''
    return any(re.fullmatch(pattern, fragment) for pattern in metatext_patterns)

def is_in_parentheses(fragment):
    return fragment.startswith('(') and fragment.endswith(')')

def is_uppercase(fragment):
    return re.search(r'[A-Z]', fragment) and fragment.upper() == fragment

def qualifies_for_any(fragment, functions):
    '''Returns True if  any of the functions in `functions` return true for `fragment`.'''

    return any(map(lambda func: func(fragment), functions))

def is_metatext(fragment):
    '''Returns True if a fragment should be counted as metatext and thus ignored.'''

    metatext_checks = [matches_metatext_re, is_in_parentheses, is_uppercase]
    return qualifies_for_any(fragment, metatext_checks)

def filter_metatext(text_fragments):
    '''
    Filters an iterable of text fragments (strings)
    to exclude metatext segments like '888
    '''
    
    return filter(
        lambda text: not is_metatext(text),
        text_fragments
    )
