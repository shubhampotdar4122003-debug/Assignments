import MarvellousNum

def ListPrime(lst):
    sum_prime = 0
    for num in lst:
        if MarvellousNum.ChkPrime(num):
            sum_prime += num
    return sum_prime


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

print("Addition of prime numbers is:", ListPrime(arr))