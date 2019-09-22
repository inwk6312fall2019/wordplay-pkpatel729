def three_cons(str):
    i = 0
    count = 0
    while i < len(str) - 1:
        if str[i] == str[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1


fin = open('words.txt')
count = 0
for word in fin:
    word = word.strip()
    if three_consecutive(word) == True:
        print(word)
        count += 1
print(count)
