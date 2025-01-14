s=input("Enter the string:")
s2=""
for i in s:
    if i.isalpha():
        if i.islower():
            s2=s2+i.upper()
        if i.isupper():
            s2=s2+i.lower()
    else:
        s2=s2+i        
print(s2)