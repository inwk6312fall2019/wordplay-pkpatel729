def is_abecedarian(word):
    previous_letter = word[0]
    for letter in word:
        if ord(letter) < ord(previous_letter):
            return False
        previous_letter = letter
    return True
