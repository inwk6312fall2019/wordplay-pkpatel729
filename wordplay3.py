def avoids(word,str):
        for i in str:
                if i in word:
                        return 0
        return 1


str= input('enter string')
fin=open('words.txt')
for j in fin:
        word=j.strip()
        k=avoids(word,str)
        if k==1:
                print(word)


