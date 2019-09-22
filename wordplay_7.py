def three_consecutive(s):
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1

