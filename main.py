import re
from collections import Counter

with open('lovecraft.txt', 'r', encoding="utf8") as lovecraft_file:
    pure_words = re.sub(r'[,.<;:)-=!>_(?"]', '', lovecraft_file.read())
    lovecraft_words = pure_words.lower().split()

with open('austen.txt', 'r', encoding="utf8") as austen_file:
    pure_words = re.sub(r'[,.<;:)-=!>_(?"]', '', austen_file.read())
    austen_words = pure_words.lower().split()

common_words = Counter(lovecraft_words) & Counter(austen_words)
print(common_words)
print("Total: " , len(common_words))