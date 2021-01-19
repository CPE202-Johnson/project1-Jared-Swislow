import string
import math
#int -> int or char
#If int is bigger than 9, returns A, B, C, etc.
def convertHelper(num):
    if num > 9:
        num = string.ascii_uppercase[num - 10]
    return num

#int, int -> int
#Recursively converts a number from base 10 to any base from 2 to 16
def convert(num, b):
    if b > 16 or b < 2:
        raise ValueError()
    quotient = math.floor(num/b)

    if num == 0:
        return "0"
    
    convertedNum = str(convert(quotient, b)) + str(convertHelper(num % b))

    #Remove a leading zero, if present
    if convertedNum[0] == "0":
        convertedNum = convertedNum[1:]
    

    return convertedNum