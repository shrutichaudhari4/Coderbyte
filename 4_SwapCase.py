str='HeLLo'
new=''
for i in str:
    if i.isupper():
        new+=i.lower()
    else:
        new+=i.upper()
print(new)

# OR

print(str.swapcase())
