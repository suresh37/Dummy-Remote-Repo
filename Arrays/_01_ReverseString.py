
def reverse_array(arr):
    n = len(arr)
    new_arr = []
    for i in range(n):
        x = arr.pop()
        new_arr.append(x)
    print(new_arr)


def reverse_string(str):
    arr = list(str)
    arr.reverse()
    print("".join(arr))


"""
   _01_ReverseArray.js
   Reverse a String  
"""
if __name__ == "__main__":
    arr = [4, 5, 1, 2]
    str = "suresh"
    # reverse_array(arr)
    reverse_string(str)
    # print("".join(list(str)[::-1]))
