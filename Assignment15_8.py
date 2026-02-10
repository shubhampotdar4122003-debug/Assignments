num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
data = list(filter(lambda a : a % 3 == 0  and a % 5 == 0 ,num))
print("the number are divisible by 3 & 5 are :",data)