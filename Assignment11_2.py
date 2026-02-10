
num = int(input("enter the number :"))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("toal digits",count)