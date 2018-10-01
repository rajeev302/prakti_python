import re

def text_match(text, endWord):
        patterns = '\w+\S*['+endWord+']$'
        if re.search(patterns,  text):
                return True
        else:
                return False

f = open('my_text_file.txt', "r")
lines = f.read().splitlines()
f.close()

for line in lines:
    if(text_match(line, "START") | text_match(line, "END")):
        print line
        listOfWords = line.split(' ')
        print(listOfWords[0], listOfWords[1])