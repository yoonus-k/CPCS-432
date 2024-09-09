import arabic_reshaper
from bidi.algorithm import get_display

# Function to generate advanced verb forms including moods, complex pronouns, and verb patterns
def generate_advanced_forms(root):
    # Basic forms for Past, Present, Imperative
    past_tense = [root, f"{root}وا", f"{root}ت", f"{root}نا", f"{root}تم", f"{root}ن"]
    present_tense = [f"ي{root}", f"ي{root}ون", f"ت{root}", f"ت{root}ين", f"ن{root}", f"ي{root}ن"]
    imperative = [f"ا{root}", f"ا{root}وا", f"ا{root}ي", f"ا{root}ن"]
    
    # Subjunctive mood (المضارع المنصوب)
    subjunctive = [f"ل{root}", f"أ{root}", f"ل{root}وا", f"ل{root}ي"]
    
    # Jussive mood (المضارع المجزوم)
    jussive = [f"ي{root}وا", f"لا{root}", f"ت{root}وا"]
    
    # Passive voice forms
    passive_past = [f"{root[0]}ُ{root[1]}ِ{root[2]}", f"{root[0]}ُ{root[1]}ِ{root[2]}وا", f"{root[0]}ُ{root[1]}ِ{root[2]}ت", f"{root[0]}ُ{root[1]}ِ{root[2]}نا"]
    passive_present = [f"يُ{root}", f"يُ{root}ون", f"تُ{root}", f"تُ{root}ين"]

    # Extended verb patterns (وزن) - Derived forms: II (فعّل), III (فاعل), IV (أفعل)
    form_II = [f"فعّل", f"فعّلوا", f"فعّلت", f"فعّلنا"]
    form_III = [f"فاعل", f"فاعلوا", f"فاعلت", f"فاعلنا"]
    form_IV = [f"أ{root[1:]}"]

    # Active and Passive participle for all forms
    active_participle = [f"{root[0]}ا{root[1]}{root[2]}", f"{root[0]}ا{root[1]}{root[2]}ون", f"{root[0]}ا{root[1]}{root[2]}ة", f"{root[0]}ا{root[1]}{root[2]}ات"]
    passive_participle = [f"م{root[1:]}وب", f"م{root[1:]}وبة", f"م{root[1:]}وبون", f"م{root[1:]}وبات"]
    
    # Derived Nouns: Verbal noun, time/place noun, tool noun, diminutive
    verbal_noun = [f"{root}ان", f"{root}ة", f"{root}ات"]
    noun_of_place = [f"م{root[1:]}ان", f"م{root[1:]}ة"]
    tool_noun = [f"مِ{root[1]}{root[2]}", f"مِ{root[1]}ة"]
    diminutive = [f"فُعَيل", f"فُعَيْلة"]

    # Combine all forms into one list
    all_forms = (past_tense + present_tense + imperative + subjunctive + jussive +
                 passive_past + passive_present + form_II + form_III + form_IV +
                 active_participle + passive_participle + verbal_noun + noun_of_place +
                 tool_noun + diminutive)
    
    return all_forms

# Function to display Arabic correctly on the screen
def display_arabic(words):
    reshaped_words = [arabic_reshaper.reshape(word) for word in words]
    bidi_words = [get_display(word) for word in reshaped_words]
    return bidi_words

# Function to write results to a text file (without reshaping)
def write_to_file(words_dict, filename="arabic_advanced_derivations.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for word, forms in words_dict.items():
            f.write(f"Advanced Derivations for {word}:\n")
            for form in forms:
                f.write(f"{form}\n")
            f.write("\n" + "-"*50 + "\n")

# Generate and store derivations for ضرب, شرب, لبس
words_to_generate = ['ضرب', 'شرب', 'لبس']
words_forms_dict = {}

for word in words_to_generate:
    forms = generate_advanced_forms(word)
    # No reshaping needed for writing to the file
    words_forms_dict[word] = forms

# Write the results to a file
write_to_file(words_forms_dict)

print("Advanced Arabic derivations have been written to 'arabic_advanced_derivations.txt'.")
