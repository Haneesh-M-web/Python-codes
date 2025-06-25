print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
import re
def madlibs():
    text = '''Today I went to the zoo. I saw a(n) ADJECTIVE NOUN jumping up and down in its tree.  
He VERB ADVERB through the large tunnel that led to its NOUN.  
I got some peanuts and passed them through the cage to a gigantic ADJECTIVE NOUN towering above my head.  
Feeding that animal made me hungry. I went to get a ADJECTIVE scoop of ice cream.  
It VERB ADVERB down my arm and onto my NOUN.'''
    print("Original Text:\n", text)
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', text)
    for placeholder in placeholders:
        word = input(f"Enter a {placeholder.lower()}: ")
        text = text.replace(placeholder, word, 1)
    print("\nModified Text:\n", text)
    with open('madlibs_output.txt', 'w') as file:
        file.write(text)
    print("\nModified text saved to 'madlibs_output.txt'")
madlibs()
