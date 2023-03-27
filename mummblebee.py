import collections
import json
from functools import reduce

with open("2of4brif.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

Trie = lambda: collections.defaultdict(Trie)
trie = Trie()
END = True
for idx,word in enumerate(english_words):
    reduce(dict.__getitem__, word, trie)[END]=idx

print("\nThis is a solver for NYT Spelling Bee game. \nType in the 7 characters for today:", end =" ")
char_string = input()
print("The 7 characters are: " + char_string)
print("\nType in the central character (in yellow):", end = " ")
central_char = input()
print("The central character is: " + central_char)

my_chars = [char for char in char_string.lower().strip()]
max_length = 15
ans = []

def bfs(prefix, level, trie_node):
    if level >= 4 and prefix in english_words:
        ans.append(prefix)
    for char in my_chars:
        if level < max_length and char in trie_node:
            bfs(prefix + char, level+1, trie_node[char])

bfs("", 0, trie)

new_ans = []
for word in ans:
    if central_char in word:
        new_ans.append(word)

print(f"\nThere are {len(new_ans)} spellable words today. They are: ")
print(*new_ans)
print("\nHave a great day. You are a genius now.\n")