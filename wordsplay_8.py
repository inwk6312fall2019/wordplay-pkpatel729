def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i<j:
         if word[i] != word[j]:
            return False
         i = i + 1
         j = j - 1
    return True


 def check(n):
    i = 100000
    while i <= 999999:
        if check(i):
        i = i + 1
 print(i)
