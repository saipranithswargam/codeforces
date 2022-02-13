word=input()
c1=word.upper()
c2=word[1:]
c3=word[0]

if len(word)==1:
    if word==word.lower(): 
        print(word.upper())
    else:
        print(word.lower())
elif c1==word:
    print(word.lower())
elif (c2==c2.upper()) and (c3==c3.lower()):
    print(word.capitalize())
else:
    print(word)
