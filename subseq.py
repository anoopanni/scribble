s = "c"

for i in range(len(s)):
    for j in range(len(s)-1):
        print(i)
        word = s[i] + s[i+1: j+2]
        print(word)
