def word_length(text):
    l = text.split()
    words_count = len(l)
    letter_length = 0
    for word in l:
        letter_length += len(word)
    return letter_length / words_count

text = input()
print(word_length(text))
