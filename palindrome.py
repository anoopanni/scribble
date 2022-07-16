s = "a"

l, r = 0, len(s)-1

while l != r and l<r:
    if s[l] == s[r]:
        l+=1
        r-=1
    else:
        break
print(l, r)

if l>=r:
    print('it is a palindrome')
else:
    print('it is not a palindrome')