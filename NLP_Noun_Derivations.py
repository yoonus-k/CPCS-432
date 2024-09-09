import arabic_reshaper
from bidi.algorithm import get_display

# Function to generate very complex forms for Arabic nouns
def generate_correct_noun_forms(noun):
    # Regular plurals (جمع سالم)
    if noun.endswith('ة'):
        regular_plural = [noun[:-1] + "ات"]  # For feminine nouns ending with "ة"
    else:
        regular_plural = [f"{noun}ون", f"{noun}ين"]
    
    # Broken plurals (جمع التكسير) - specific irregular cases
    broken_plural = {
        "جملة": ["جمل"],
        "مدرس": ["مدارس"],
        "مسلم": ["مسلمون"]
    }.get(noun, [])
    
    # Diminutive forms (اسم التصغير) - properly based on the noun
    diminutive = {
        "جملة": [f"جُمَيْلَة"],
        "مدرس": [f"مُدَيْرِس"],
        "مسلم": [f"مُسَيْلِم"]
    }.get(noun, [])
    
    # Augmentative forms (اسم التكبير) - express larger versions
    augmentative = [f"{noun} ضخم"] if noun == "جملة" else [f"{noun} كبير"]
    
    # Elative forms (اسم التفضيل) - comparatives/superlatives
    elative_forms = [f"أكبر {noun}", f"أفضل {noun}", f"أحسن {noun}"]
    
    # Masdar (verbal noun) - specific to the root of the noun
    masdar = {
        "جملة": [f"تَجْمِيع", f"جَمع"],
        "مدرس": [f"تَدْرِيس", f"دَرْس"],
        "مسلم": [f"إسْلام"]
    }.get(noun, [])
    
    # Verbal forms derived from the noun's root
    verb_forms = {
        "جملة": [f"يَجْمَع"],
        "مدرس": [f"يُدَرِّس"],
        "مسلم": [f"يُسْلِم"]
    }.get(noun, [])
    
    # Active and Passive Participles (اسم الفاعل واسم المفعول)
    active_participle = {
        "جملة": [f"جَامِع"],
        "مدرس": [f"مُدَرِّس"],
        "مسلم": [f"مُسْلِم"]
    }.get(noun, [])
    
    passive_participle = {
        "جملة": [f"مَجْمُوع"],
        "مدرس": [f"مَدْرُوس"],
        "مسلم": [f"مَسْلُوم"]
    }.get(noun, [])
    
    # Imperative forms (فعل الأمر) - commands derived from the root
    imperative_forms = {
        "جملة": [f"اِجْمَع"],
        "مدرس": [f"اِدْرُس"],
        "مسلم": [f"اِسْلِم"]
    }.get(noun, [])
    
    # Vocative forms (النداء) - addressing the noun
    vocative_forms = [f"يا {noun}"]
    
    # Feminine plural forms for nouns ending with "ة"
    feminine_plural = [f"{noun[:-1]}ات"] if noun.endswith('ة') else []
    
    # Possessive attached pronouns (الضمائر المتصلة) for dual and plural
    possessive_forms = [f"{noun}ي", f"{noun}ك", f"{noun}ه", f"{noun}نا", f"{noun}كم", f"{noun}هم"]
    
    # Nouns of place/time (اسم المكان واسم الزمان)
    noun_of_place_time = {
        "جملة": [f"مَجْمَع"],
        "مدرس": [f"مَدْرَس"],
        "مسلم": [f"مَسْلَم"]
    }.get(noun, [])
    
    # Combine all forms into one list
    all_forms = (regular_plural + broken_plural + diminutive + augmentative +
                 elative_forms + masdar + verb_forms + active_participle +
                 passive_participle + imperative_forms + vocative_forms +
                 feminine_plural + possessive_forms + noun_of_place_time)
    
    return all_forms

# Function to display Arabic correctly on the screen
def display_arabic(words):
    reshaped_words = [arabic_reshaper.reshape(word) for word in words]
    bidi_words = [get_display(word) for word in reshaped_words]
    return bidi_words

# Function to write results to a text file (without reshaping)
def write_to_file(words_dict, filename="NLP_Noun_Derivations.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for word, forms in words_dict.items():
            f.write(f"Corrected Complex Derivations for {word}:\n")
            for form in forms:
                f.write(f"{form}\n")
            f.write("\n" + "-"*50 + "\n")

# Generate and store derivations for جملة, مدرس, مسلم
nouns_to_generate = ['جملة', 'مدرس', 'مسلم']
nouns_forms_dict = {}

for noun in nouns_to_generate:
    forms = generate_correct_noun_forms(noun)
    nouns_forms_dict[noun] = forms

# Write the results to a file
write_to_file(nouns_forms_dict)

print("Corrected complex noun derivations have been written to 'NLP_Noun_Derivations.txt'.")
