"""
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), 
and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.
"""
def get_words(paragraph):
    for punct in ",.!":
        paragraph = paragraph.replace(punct, " ")

    words = paragraph.lower().split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return [word for word, count in sorted_words[:3]]
