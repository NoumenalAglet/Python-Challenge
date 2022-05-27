#PyParagraph

import os

#defining variables

#reading paragraph_1 in Resources
file_path = os.path.join("Resources", "paragraph_1.txt")
with open(file_path, 'r', encoding="UTF-8") as f:

    #print(f.readline())
    #print(f.readlines())

    main_text = f.readline()

    words = main_text.split()
    #words = words.count()
    #words are list doe
    
    
    print(words)
#approximate word count
#split()
#count()

#approximate sentence count

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