from functools import reduce
num = [1,2,3,4,5]
data = reduce(lambda a,b : a * b,num)
print("the product of all elements is :",data)