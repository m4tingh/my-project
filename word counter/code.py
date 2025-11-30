import sys
sys.path.append('nltk')



import nltk
from nltk.tokenize import word_tokenize
import os
import nltk.data

def download_punkt():
  nltk.download('punkt_tab', download_dir='punkt')
  nltk.data.path.append('punkt')


if os.path.isdir('punkt') == False:
  download_punkt()

else:
  nltk.data.path.append('punkt')



def counter():
    words = [] 
    sing = ('.', '?', '!', ',', '"', "'", '؛', ':', ')', '(', '[', ']', ';', '`', '’', '“', '”', '``', "''", '»', '«', '/', '\\', 'ـ', '…')
    
    text = input("Please enter your text here: ")
    tokens = word_tokenize(text)
    for token in tokens:
        if token not in sing:
            words.append(token) 
    
    print(len(words))

    answer = input("any other questions? Please answer with yes or no: \n")
    answer = answer.lower().strip()

    while answer != "yes" and answer != "no":
      answer = input("Please answer with yes or no: \n")
   
      answer = answer.lower().strip()

    if answer == "yes":
      counter()

counter()