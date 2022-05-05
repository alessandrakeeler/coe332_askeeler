def even_or_odd(int_list):
    for i in int_list:
        if i%2 == 0:
            print(str(i) + " is even")
            print(" ")
        else:
            print(str(i) + " is odd")
            print(" ")


intlist = [1,2,3,4,5,6,7,8,9,10]
even_or_odd(intlist)
