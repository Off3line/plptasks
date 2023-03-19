import random
import string

## encode function which uses random values in case secondString has not been used
def encode(firstString,offset,secondString = None):

    ## convert strings into list containing the ascii numbers
    convertedList = stringToNumberConv(firstString)
    convertedListTwo = []
    if secondString is None:
        secondString = []
        ## generate x amount of chars needed to fill between the firString by: len() -1
        for x in range((len(convertedList)-1)):
            secondString.append(random.choice(string.ascii_lowercase))
        convertedListTwo = stringToNumberConv(secondString)

    else:
        convertedListTwo = stringToNumberConv(secondString)
    
    ## If the second string is given by the argument and also too small, the index will reset to fill the first string
    index = 0
    for i in range(1,(len(convertedList)*2-1),2):
        if(index >= len(convertedListTwo)):
            index = 0
            convertedList.insert(i,convertedListTwo[index])
        else:
            convertedList.insert(i,convertedListTwo[index])
            index +=1
     
    
    ## execute the inserted rotation by the offset
    convertedList = rotOperation(int(offset),convertedList)

    #revert back to alphanumeric numbers
    finalString = numberToStringConv(convertedList)
   

    return  print('final list: ' , finalString)


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

