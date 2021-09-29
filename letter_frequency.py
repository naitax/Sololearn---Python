def letter_freq(letter, word):
    count = text.count(letter)
    length = len(text)
    freq = int(count/length * 100)
    return freq


text = input()
letter = input()
print(letter_freq(letter, text))
