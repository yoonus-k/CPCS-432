import jpype
import os
from nltk.corpus import wordnet
import nltk

# Download WordNet data (only needed the first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Get the current directory where the Python script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the ArabiTools JAR file
jar_path = os.path.join(current_dir, "ArabiTools-1.2.0.jar")

# Full path to the jvm.dll (adjust this path based on your JDK installation)
jvm_path = r"C:\Program Files\Java\jdk-21\bin\server\jvm.dll"

# Start the JVM with the jvm.dll path and classpath
jpype.startJVM(jvm_path, classpath=[jar_path])

# Use JPackage to access the arabi.tools.words.expan package and Expander class
Expander = jpype.JPackage('arabi').tools.words.expan.Expander

# Create an instance of Expander
expander = Expander()

def get_arabic_lemmas(word, pos):
    """
    This function returns all Arabic lemmas for a given English word and part of speech (POS).
    """
    synsets = wordnet.synsets(word, pos=pos)
    arabic_lemmas = set()

    # Collect all Arabic lemmas from all synsets
    for synset in synsets:
        arabic_lemmas.update(synset.lemma_names('arb'))  # 'arb' for Arabic

    return arabic_lemmas

def get_inflected_and_derived_forms(lemma):
    """
    This function returns all inflected and derived forms of a given Arabic lemma.
    It uses the ArabiTools library for morphological expansion.
    """
    # Use the ArabiTools expander to get inflected and derived forms
    inflections = expander.getExpandByRoot(lemma, 0, True)
    
    # Separating inflected and derived forms (custom logic can be improved)
    inflected_forms = []
    derived_forms = []
    
    # In Arabic, you may add more conditions to distinguish inflected from derived forms
    for form in inflections:
        if len(form) > len(lemma):  # A simple heuristic (length-based) to differentiate
            derived_forms.append(form)
        else:
            inflected_forms.append(form)
    
    return inflected_forms, derived_forms

def main():
    # Input: Take user input for English word and POS
    word = input("Enter the English word: ").strip()
    pos = input("Enter the part of speech (n for noun, v for verb): ").strip()

    # Open a text file to save the results
    output_file = os.path.join(current_dir, "arabic_derivations_output.txt")
    with open(output_file, 'w', encoding='utf-8') as file:

        # Get all possible Arabic lemmas
        arabic_lemmas = get_arabic_lemmas(word, pos)
        file.write(f"Arabic Lemmas for '{word}':\n")
        file.write(", ".join(arabic_lemmas) + "\n\n")

        # For each Arabic lemma, get inflected and derived forms
        for lemma in arabic_lemmas:
            file.write(f"\nLemma: {lemma}\n")

            # Get inflected and derived forms for the lemma
            inflected_forms, derived_forms = get_inflected_and_derived_forms(lemma)

            # Write inflected forms to the file
            file.write(f"Inflected Forms for {lemma}:\n")
            for form in inflected_forms:
                file.write(f"{form}\n")

            # Write derived forms to the file
            file.write(f"Derived Forms for {lemma}:\n")
            for form in derived_forms:
                file.write(f"{form}\n")

    print(f"Results written to {output_file}")

    # Shutdown the JVM after use
    jpype.shutdownJVM()

if __name__ == "__main__":
    main()
