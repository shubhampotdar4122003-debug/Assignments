def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num

    print("Output:", min_num)

if __name__ == "__main__":
    main()