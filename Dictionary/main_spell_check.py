def spell_check(input_file, dictionary_file):

    #Check spelling of words in the given text against the dictionary file.
    
   
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        dictionary_words = set(line.strip() for line in file)
    
    misspelled_words = []
    lines = input_file.split('\n')
    for line_num, line in enumerate(lines, 1):
        words = line.split()
        position = 1
        for word in words:
            if word.strip() not in dictionary_words:
                misspelled_words.append((word, line_num, position))
            position += len(word) + 1  # +1 for the space after the word
    
    return misspelled_words

# Usage example
dictionary_file = 'cleaned_dictionary.txt'  # Use the path to your cleaned dictionary file

# Read text from dzo.txt file
with open('dzo.txt', 'r', encoding='utf-8') as file:
    text_to_check = file.read()

misspelled = spell_check(text_to_check, dictionary_file)

if misspelled:
    # Print only the first misspelled word
    word, line_num, position = misspelled[0]
    print(f"line {line_num}, {position}th word '{word}' is incorrect.")
else:
    print("No misspelled words found.")

# Define the content of dzo.txt (for demonstration purposes)
dzo_txt_content = """༉ཕུན་ཚོགས་གླིང་གི་ ཁྲིམས་སྲུང་འགག་པ་གིས་ ཚན་རིག་དང་འཕྲུལ་རིག་མཐོ་རིམ་སློབ་གྲྭའི་ ལེགས་སྦྱར་བ་འོགམ་ཅིག་གིས་ འདོད་སྤྱོད་ཀྱི་གནོད་འཚེར་འབད་ཡོད་པའི་ དོགས་པ་ཡོད་མི་གི་གནད་དོན་འདི་ ཞིབ་དཔྱད་འབད་བའི་བསྒང་ར་འདུག

གནད་དོན་འདི་ཡང་ མཐོ་རིམ་སློབ་གྲྭ་གིས་ འབྲུག་རྒྱལ་འཛིན་ཙུག་ལག་སློབ་སྡེ་ལུ་ སྙན་ཞུ་འབད་བའི་ཤུལ་མ་ གཙུག་ལག་སློབ་སྡེ་གིས་ དུས་འཕྲོ་ལས་ ཁྲིམས་སྲུང་འགག་པ་ལུ་ སྙན་ཞུ་འབད་ནུག

འདི་ཡང་ མཐོ་རིམ་སློབ་གྲྭའི་སློབ་ཕྲུག་བུམ་༩གིས་ ལེགས་སྦྱར་བ་འོགམ་འདི་གིས་ ཁོང་ཆ་ཁྱབ་ལུ་ འདོད་སྤྱོད་ཀྱིགནོད་འཚེར་འབད་དེ་ཡོདཔ་སྦེ་ ཁ་ཉེས་བཀལ་ཏེ་འདུག

སློབ་ཕྲུག་བུམོ་འདི་ཚུ་གིས་ གནད་དོན་འདི་གི་སྐོར་ལས་ སློབ་གྲྭའི་བསླབ་སྟོན་དང་རྒྱབ་སྐྱོར་སེ་ཚན་ལུ་ སྙན་ཞུ་འབད་ནུག

མཐོ་རིམ་སློབ་གྲྭའི་གཙོ་འཛིན་གྱིས་སླབ་མི་ནང་ གནད་དོན་འདི་གི་ཐོག་ལུ་ ཉོག་བཤད་ཀྱ་ཡི་གུ་འདི་ འདས་པའི་ཟླཝ་ འགོ་བཙུགས་ཁམས་ཅིག་ནང་ ཐོབ་སྟེ་ཡོདཔ་སྦེ་བཤད་ཅི།

ཁྲིམས་ྲུང་འགག་པ་གིས་བཀོད་མི་ནང་ ལེགས་སྦྱར་བ་འོགམ་འདི་ལུ་ བུམོ་ཚུ་གི་གཟུགས་ཁར་ ཚུལ་མིན་ྱི་སྒོ་ལས་དཀྲོགས་མི་དང་ བཙོག་གཏམ་སླབ་ཡོད་པའི་ ཁ་ཉེས་བཀལ་ཏེ་ཡོདཔ་སྦེ་ཨིན་མས།

མཐོ་རིམ་སློབ་གྲྭའི་གཙོ་འཛིན་གྱིསསླབ་ི་ནང་ ལེགས་སྦྱར་བ་འོགམ་འདི་ མཐོ་རིམ་སློབ་གྲྭའི་ འདོད་སྤྱོ་གནོད་འཚེར་གྱི་སྒྲིག་གཞི་དང་འཁྲིལ་ཏེ་ དགོངས་ཕོག་བཏང་སྟེ་ཡོདཔ་སྦེ་ཨིན་མས།

དོགས་པ་ཅན་ ལེགས་སྦྱར་བ་འདི་ མཐོ་རིམ་སློབ་གྲྭ་འདི་ནང་ལུ་ འདས་པའི་ལོ་༣༠གྱི་རིང་ལུ་ ཕྱག་ཞུ་ཡོདཔ་ཨིན་མས།

འདི་དང་གཅིག་ཁར་ ཁྲིམས་སྲུང་འགག་པ་དང་འཁྲིལ་པ་ཅིན་ ཉོག་བཤད་བཀོད་མི་ལ་ལོ་ཅིག་ ཐིམ་ཕུག་ལུ་ཡོདཔ་ལས་ ཐིམ་ཕུག་གི་ཁྲིམས་སྲུང་འགག་པ་གིས་ ཞིབ་དཔྱད་འབད་ནི་ནང་ལུ་ རྒྱབ་སྐྱོར་འབད་དོ་ཡོདཔ་སྦེ་བཤད་ཅི།

ཀུན་ལེགས་སྒྲོལམ། གན
"""

# Write the content to dzo.txt
with open('dzo.txt', 'w', encoding='utf-8') as file:
    file.write(dzo_txt_content)

