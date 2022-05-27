#PyParagraph

import os
import re

#defining variables
main_text = ''
no_of_words = 0
no_of_sentences = 0
ave_letter_count = 0.0
ave_sentence_len = 0.0

#reading paragraph_1 in Resources
file_path = os.path.join("Resources", "paragraph_3.txt")
with open(file_path, 'r', encoding="UTF-8") as f:

    #print(f.readline())
    #print(f.readlines())


    main_text = f.read()
    #print(main_text)
    
    #approximate word count
    no_of_words = len(main_text.split())   
    print(no_of_words)

    #approximate sentence count
    no_of_sentences = len(re.split("(?<=[.!?]) +", main_text))
    
    print(no_of_sentences)

    #average letter count

    #average sentence length


#output to terminal
'''
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
'''

'''
reTest = '118-899-0703 859.030.9320 490*943*2039'
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(reTest)
for match in matches:
    print(match)
print(reTest[178:179])
'''