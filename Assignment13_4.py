num = int(input("Enter a decimal number: "))
binary = ""

for i in range(num):
    if num == 0:
        break
    binary = str(num % 2) + binary
    num = num // 2

print("Binary equivalent is:", binary)
