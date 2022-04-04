# 0 and 0 = 0
# 1 and 0 = 1  (or vice versa)
def BitwiseOne(strArr):
    new=''
    for i in range(len(strArr[0])):
        if strArr[0][i]=='0' and strArr[1][i]=='0':
            new+='0'
        else:
            new+='1'
    return new       
a=['101','100']
print(BitwiseOne(a))
