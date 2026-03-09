def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    search = int(input("Enter element to search: "))
    count = 0

    for num in arr:
        if num == search:
            count += 1

    print("Output:", count)

if __name__ == "__main__":
    main()