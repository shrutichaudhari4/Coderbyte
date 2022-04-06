# Addition of all the elements should be greater than or equal to the maximum element of an array:

def ArrayAdditionI(arr):
    a=max(arr)
    sum=0
    for i in arr:
        if i!=a:
            sum+=i
    if sum!=a:
        return False
    else:
        return True

arra=[1,2,3,4,10]
print(ArrayAdditionI(arra))

#OR

arra1=[12,2,3,3,20]
max_element=max(arra1)
element=[i for i in arra1 if i!=max_element]
if max_element<=sum(element):
    print("True")
else:
    print('False')
