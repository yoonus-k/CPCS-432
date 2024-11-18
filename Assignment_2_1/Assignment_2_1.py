import jpype
import os
from nltk.corpus import wordnet
import nltk
import json

# Download WordNet data (only needed the first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Get the current directory where the Python script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the full path to the ArabiTools JAR file
jar_path = os.path.join(current_dir, "ArabiTools-1.2.0.jar")
jar_path_2 = os.path.join(current_dir, "ArabiToolsLibVerbs-1.0.jar")

# Full path to the jvm.dll (adjust this path based on your JDK installation)
jvm_path = r"C:\Program Files\Java\jdk-21\bin\server\jvm.dll"

# Start the JVM with the jvm.dll path and classpath
#jpype.startJVM(jvm_path, classpath=[jar_path, jar_path_2])
# Start the JVM with the jvm.dll path and classpath (Windows uses semicolons ';' to separate classpaths)
if not jpype.isJVMStarted():  # Ensure JVM isn't started already
    jpype.startJVM(jvm_path, "-Djava.class.path={};{}".format(jar_path, jar_path_2))

# Use JPackage to access the arabi.tools.words.expan package and Expander class
Expander = jpype.JPackage('arabi').tools.words.expan.Expander

#use arabi.tools.verbs.analysis.VerbsConjugation to get the inflections
VerbsConjugation = jpype.JPackage('arabi').tools.verbs.analysis.VerbsConjugation

# Create an instance of Expander
expander = Expander()
vc = VerbsConjugation()


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
     # Separating inflected and derived forms (custom logic can be improved)
    
    
    # use arabi.getVerbsConjugation(word) to get the inflections
    # Assuming `vc` is an instance of a class that has the `getVerbConj` method
    inflected_forms = vc.getVerbConj(lemma)  # Get the inflected forms

    # Assuming `inflected_forms` is a list-like object in Python
    verb = inflected_forms[0]  # Get the first verb
    
    # Call the generate_json_format() method (assuming the method name follows Python's naming conventions)
    structured_result= verb.generateJSONFormat()  # This should return a Python dictionary
    #print(json.dumps(structured_result, indent=4))  # Print the structured result
    # Convert org.json.JSONObject to Python string
    if isinstance(structured_result, str):  # Check if it's already a Python string
        json_string = structured_result
    elif hasattr(structured_result, 'toString'):
        json_string = structured_result.toString()  # Use the toString method to convert
    else:
        print("Unsupported type for structured_result.")
        return None, None

    # Print the JSON string for debugging
    #print("JSON String:", json_string)
    # Load the JSON string
    json_string = str(json_string) 
    data = json.loads(json_string) # Convert the JSON string to a Python dictionary

    # Pretty print the decoded JSON
    #print(json.dumps(data, ensure_ascii=False, indent=2)) # Ensure Arabic characters are displayed correctly
    inflected_forms=json.dumps(data, ensure_ascii=False, indent=2)
    

    

    
    # Use the ArabiTools expander to get derivations 
    derived_forms = expander.getExpandByRoot(lemma, 0, True)
    
   
    return inflected_forms, derived_forms

def main():
    # Input: Take user input for English word and POS
    word = input("Enter the English word: ").strip()
    pos = input("Enter the part of speech (n for noun, v for verb): ").strip()

    # Open a text file to save the results
    output_file = os.path.join(current_dir, "arabic_derivations_"+word+".txt")
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
            
            file.write(f"{inflected_forms}\n")
            file.write("\n")
            # Write derived forms to the file
            file.write(f"Derived Forms for {lemma}:\n")
            for form in derived_forms:
                file.write(f"{form}\n")

    print(f"Results written to {output_file}")

    # Shutdown the JVM after use
    jpype.shutdownJVM()

if __name__ == "__main__":
    main()
