import alyahmor.genelex
generator = alyahmor.genelex.genelex()

all = []
words_verb = [u"شرب",u"لبس",u"ضرب"]
words_noun = [u"جملة",u"مسلم",u"مدرس"]
for word in words_noun:
    noun_forms = generator.generate_forms( word, word_type="noun")
    all += noun_forms

for word in words_verb: 
    verb_forms = generator.generate_forms( word, word_type="verb")
    all += verb_forms

# Store the words in a text file
if noun_forms:
    with open('words_containing_substring.txt', 'w', encoding='utf-8') as file:
        for word in all:
            file.write(word + '\n')