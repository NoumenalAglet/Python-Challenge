#PyParagraph

import os
import re

#defining variables
main_text = ''

#reading paragraph_1 in Resources
file_path = os.path.join("Resources", "paragraph_1.txt")
with open(file_path, 'r', encoding="UTF-8") as f:

    #print(f.readline())
    #print(f.readlines())

    
    main_text = f.readline()
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