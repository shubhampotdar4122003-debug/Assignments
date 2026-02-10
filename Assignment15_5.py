from functools import reduce 
num = [2,3,4,5,6,7,8,9,10]
data = ((reduce(lambda a,b : a if a > b else b,num)))
print("maximum eliments is",data)