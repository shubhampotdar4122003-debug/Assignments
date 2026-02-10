num = [1,2,3,4,5,6,7,8,9,10]
data = len(list(filter(lambda x : x % 2 == 0 ,num)))

print("The count of even number :",data)