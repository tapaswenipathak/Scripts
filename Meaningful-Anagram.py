from itertools import permutations
import urllib2
import json

# Take Input sequence of letters
word = raw_input()

# Generate all permutations
anagrams = [''.join(p) for p in permutations(word)]

# Make set to remove duplicates -> Make it a list
anagrams = list(set(anagrams))

# Iterate over all permutations, use anagramica API to find if a genrated
# word is valid english word or not
for i in range(len(anagrams)):
    response = urllib2.urlopen(
        'http://www.anagramica.com/lookup/' + anagrams[i])
    data_retrived = json.load(response)

    # If valid print the word
    if data_retrived['found'] != 0:
        print anagrams[i],
        print ",",
