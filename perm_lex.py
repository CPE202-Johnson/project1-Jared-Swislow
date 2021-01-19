#str -> list[strings]
#Recursively generates all permutations of a string in lexographic order,
# taking a string of length greater than 1 that is in alphabetical order
def perm_gen_lex(original):
    permList = []
    if len(original) == 1:
        return [original]

    #Loops through each letter in the original string
    for i in range(len(original)):
        simplifiedStr = original[:i] + original[i+1:]
        smallerList = perm_gen_lex(simplifiedStr)
        #Loops through all permutations given by the recursive call and adds
        # the removed character to the front of them
        for j in range(len(smallerList)):
            permList.append(original[i] + smallerList[j])
    
    return permList