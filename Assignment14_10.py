num  = lambda a,b,c : a if a > b  else a > c and b if b > c else c
a = int(input("enter the number :"))
b= int(input("enter the number :"))
c = int(input("enter the number :"))

print("largest number is :",num (a,b,c))