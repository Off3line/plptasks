import random

def encode(firstString,offset):

    ## convert strings into list containing the ascii numbers
    convertedList = stringToNumberConv(firstString)
    randomList = []
    
    index = 1
    for x in range(len(convertedList)-1):
        randomNr = random.randint(97,122)
        convertedList.insert(index,randomNr)
        index += 2
        
    print('encoded , random List',convertedList)




     
    
    ## execute the inserted rotation by the offset
    convertedList = rotOperation(offset,convertedList)
    print('encoded list: ', convertedList)

    #revert back to alphanumeric numbers
    finalString = numberToStringConv(convertedList)
    print('final list: ' , finalString)

    return finalString


def stringToNumberConv(convertedList):
    toasciiList = []
    for x in convertedList: 
        toasciiList.append(ord(x))
    return toasciiList


def numberToStringConv(selectedList):
    toAlphabeticList = ''
    for x in selectedList:
        toAlphabeticList+= chr(x)

    return toAlphabeticList

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

def changeOffset(offset):

    if offset >= 1:
        return -abs(offset)
    else:
        return abs(offset)
