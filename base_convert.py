import string
#int -> int
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
    quotient = int(num/b)

    if num == 0:
        return ""
    
    convertedNum = str(convert(quotient, b)) + str(convertHelper(num % b))

    return convertedNum