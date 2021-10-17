

if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 2
    arr.sort()
    print(arr)
    print("{}th Max".format(k))
    print(arr[len(arr)-(k)])
    print("{}th Min".format(k))
    print(arr[k-1])
