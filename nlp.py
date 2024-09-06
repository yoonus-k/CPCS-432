from farasa.pos import FarasaPOSTagger
from farasa.segmenter import FarasaSegmenter

# Initialize Farasa Segmenter and POS Tagger
segmenter = FarasaSegmenter(interactive=True)
pos_tagger = FarasaPOSTagger(interactive=True)

# Given Arabic words
verbs = ['شرب', 'ضرب', 'لبس']
nouns = ['جملة', 'مدرس', 'مسلم']

# Function to generate all possible inflected or derived forms
def generate_forms(word_list):
    inflected_forms = {}
    for word in word_list:
        # Get POS tags
        pos_tags = pos_tagger.tag(word)
        # Segment the word
        segmented_word = segmenter.segment(word)
        # Store inflected forms
        inflected_forms[word] = {
            'pos_tags': pos_tags,
            'segmented': segmented_word
        }
    return inflected_forms

# Generate forms for verbs and nouns
verb_forms = generate_forms(verbs)
noun_forms = generate_forms(nouns)

# Print or save the results
for word, forms in verb_forms.items():
    print(f"Word: {word}, Forms: {forms}")

for word, forms in noun_forms.items():
    print(f"Word: {word}, Forms: {forms}")
