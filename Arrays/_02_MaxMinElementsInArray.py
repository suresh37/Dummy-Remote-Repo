
def max_min_array(arr):
    min, max = arr[0], arr[0]
    for n in arr[1:]:
        if n < min:
            min = n
        if n > max:
            max = n
    print("Max: ", max, " Min: ", min)


if __name__ == "__main__":
    arr = [7, 9, 5, 4, 3, 2, 10]
    # arr.sort()
    # print("Min: ", arr[0])
    # print("Max: ", arr[len(arr)-1])

    max_min_array(arr)
