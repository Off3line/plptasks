import random

def encode(firstString,offset):

    ## convert strings into list containing the ascii numbers
    convertedList = stringToNumberConv(firstString)
    randomList = []
    
    ## iterate x-times the size -1 over the string and add random integers between 97 and 122
    index = 1
    for x in range(len(convertedList)-1):
        randomNr = random.randint(97,122)
        convertedList.insert(index,randomNr)
        index += 2
        
     
    
    ## execute the inserted rotation by the offset
    convertedList = rotOperation(offset,convertedList)

    #revert back to alphanumeric numbers
    finalString = numberToStringConv(convertedList)

    return finalString

## Function to compile the chars into ascii numbers
def stringToNumberConv(convertedList):
    toasciiList = []
    for x in convertedList: 
        toasciiList.append(ord(x))
    return toasciiList

## Function to compile the ascii numbers into chars
def numberToStringConv(selectedList):
    toAlphabeticList = ''
    for x in selectedList:
        toAlphabeticList+= chr(x)

    return toAlphabeticList


## Function which rotates the chars x-times based on the input offset. Range is given by ascii lower character letters 97-122
def rotOperation(offset, rotateString):
    rotatedList = []
    

    for i in rotateString:
        if i + offset >= 123:
            i = (i - 123 + offset) + 97
            rotatedList.append(i)

        elif i + offset <= 96:
            i = (i - 97 + offset) +123
            rotatedList.append(i)

        else:
            rotatedList.append(offset + i)
   

    return rotatedList


