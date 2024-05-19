def times_table(how_far, num):
    n = 1
    while n<= how_far:
        print(n, "x", num, "=", n*num)
        n = n+1
    
num_in = int(input("enter the number: \n"))
howfar = int(input("how far: \n")) 

times_table(howfar, num_in) 
