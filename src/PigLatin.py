while 1==1:
   inputWord = str(input("Give me a word and I'll translate it into pig latin: "))
   for char in inputWord:
       if char in('a','e','i','o','u'):
           e = inputWord.index(char)
           break
   FirstSyllable = inputWord[0:e]
   RestofWord = inputWord[e:]
   print(RestofWord+FirstSyllable+"ay")