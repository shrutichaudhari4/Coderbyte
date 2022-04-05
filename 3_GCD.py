# Using for and if
def GCF(arr):
  factors_num=[]
  factors_num2=[]
  for i in range(1,arr[0]+1):
    if arr[0]%i==0:
      factors_num.append(i)
  for j in range(1,arr[1]+1):
    if arr[1]%j==0:
      factors_num2.append(j)
  common=[com for com in factors_num if com in factors_num2]
  return max(common)
a=[45,12]
print (GCF(a))

# OR

def GCD2(arr):
    factors1=set([i for i in range(1,arr[0]+1) if arr[0]%i==0])
    factors2=set([i for i in range(1,arr[1]+1) if arr[1]%i==0])
    return max(factors1.intersection(factors2))
print(GCD2([15,60]))
