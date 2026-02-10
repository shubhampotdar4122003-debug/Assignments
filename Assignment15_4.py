from functools import reduce 
num = [2,3,4,5,6,7,8,9,10]
data = ((reduce(lambda a,b : a + b,num)))
print("Addition of numbers are",data)