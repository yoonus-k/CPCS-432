def inflect_verb(verb_stem):
    prefixes = ['ا', 'ي', 'ت', 'ن', 'ه', 'سا', '']
    suffixes = ['ني', 'ك', 'ها', 'هم', 'كم', 'هن', 'نا', '']
    pre_prefixes = ['و', '', 'ف']
    return sorted(['{}{}{}{}'.format(pp, pre, verb_stem, suf) if not verb.startswith('ا')
            else '{}{}{}{}'.format(pp, pre, verb_stem[1:], suf)
            for pp in pre_prefixes
            for suf in suffixes
            for pre in prefixes])

def inflect_noun(noun):
    prefixes = ['ال', 'بال', 'عال', 'لل', '']
    pre_prefixes = ['و', '', 'ف']
    return ['{}{}{}'.format(pp, p, noun)
            for pp in pre_prefixes
            for p in prefixes]

# verb = "شرب"
# words = inflect_verb(verb)
noun = "جملة"
words = inflect_noun(noun)
with open('sentence.txt', 'w', encoding='utf-8') as file:
    for word in words:
        file.write(word + '\n')

# print(inflect_noun("عربية"))