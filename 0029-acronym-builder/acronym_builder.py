"""
Given a string containing one or more words,
return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless 
they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in the order they are given.
The acronym should not contain any spaces.
"""
def build_acronym(s):
    words = s.split(" ")
    unless = ["a", "for", "an","and", "by", "of"]
    result = ""
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in unless:
            result += word[0].upper()
    return result

print(build_acronym("Frequently Asked Questions"))

"""
1. Splitle ayır
2. Bu kelimeleri içeriyorsa çıkar.
3. baş harflerini stringe ekle
,
"""