def spin_word(sentence: str):
    # mine
    words = [x for x in sentence.split()]
    for i in range(0,len(words)):
        if len(words[i]) >=5: words[i] = words[i][::-1]
    return " ".join(words)


print(spin_word("Welcome"))
print(spin_word("to"))
print(spin_word("CodeWars"))
print(spin_word("Hey fellow warriors"))
print(spin_word("This sentence is a sentence"))

def spin_words(sentence):
    # one line
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words(sentence):
    # similar but condenced
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)