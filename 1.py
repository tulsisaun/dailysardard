def find_min_max(arr):
    n = len(arr)

    # Initialize min and max
    if n % 2 == 1:
        mini = maxi = arr[0]
        i = 1
    else:
        if arr[0] < arr[1]:
            mini = arr[0]
            maxi = arr[1]
        else:
            mini = arr[1]
            maxi = arr[0]
        i = 2

    # Process elements in pairs
    while i < n - 1:
        if arr[i] < arr[i + 1]:
            mini = min(mini, arr[i])
            maxi = max(maxi, arr[i + 1])
        else:
            mini = min(mini, arr[i + 1])
            maxi = max(maxi, arr[i])
        i += 2

    return [mini, maxi]

def main():
    arr = [3, 5, 4, 1, 9]
    result = find_min_max(arr)
    print(result[0], result[1])

if __name__ == "__main__":
    main()

    print("hello dailysardard")
