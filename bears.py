#int -> boolean
#Bears problem: Given an amount of bears n, return true if n ever reaches 42 given these conditions:
#   1. If n is even, then you may give back n/2 bears.
#   2. If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears. 
#   3. If n is divisible by 5, then you may give back 42 bears.
def bears(n):
    #Input cleansing
    if type(n) != int or n < 0:
        raise ValueError()

    #Base cases
    if n == 42:
        return True
    elif n < 42:
        return False
    else: #n is an integer above 42
        #If n is divisible by 2
        returnVal1 = bears(int(n/2)) if n % 2 == 0 else False
        if returnVal1 != True: #Only checks for 2nd conditions if first isn't true
            #If n is divisible by 3 or 4
            lastTwoDigits = int(str(n)[len(str(n))-2]) * int(str(n)[len(str(n))-1])
            returnVal2 = bears(n - lastTwoDigits) if (n % 3 == 0 or n % 4 == 0) and (lastTwoDigits != 0) else False #Also checks if lastTwoDigits is 0, which would lead to infinite recursion
            if returnVal2 != True: #Only checks for 3rd condition if second isn't true
                #if n is divisible by 5
                returnVal3 = bears(n - 42) if n % 5 == 0 else False
    
    return (returnVal1 or returnVal2 or returnVal3)
