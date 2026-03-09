


def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    max_num = arr[0]
    for num in arr:
        
        if num > max_num:
            max_num = num


    print("Output:", max_num)

if __name__ == "__main__":
    main()