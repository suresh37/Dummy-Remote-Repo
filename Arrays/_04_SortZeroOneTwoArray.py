

if __name__ == "__main__":
    arr = [0, 2, 1, 2, 0]
    z_arr = []
    o_arr = []
    t_arr = []

    for i in arr:
        if(i == 0):
            z_arr.append(i)
        elif(i == 1):
            o_arr.append(i)
        elif(i == 2):
            t_arr.append(i)
    print(z_arr+o_arr+t_arr)
