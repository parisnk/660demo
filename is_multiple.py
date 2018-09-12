#Defining the function called is_multiple
def is_multiple(m, n):
    # checking if the remainder of dividing n by m is zeroo
    if n % m == 0:
        # if the remainder is zero, return true
        print("Is multiple")
        # otherwise returns false
    else:
        print("Not multiple")
        
    
#calling function by assining arguments 3, 9  
is_multiple(3, 9)    