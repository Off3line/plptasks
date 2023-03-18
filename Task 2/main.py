
## 2.Task:
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
            i = 96 + offset
            rotatedList.append(i)

        if i + offset <= 96:
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


def encode(firstString,offset,secondString):

    ## convert strings into list containing the ascii numbers
    convertedList = stringToNumberConv(firstString)
    convertedListTwo = stringToNumberConv(secondString)
    
    ## merge the list by adding the second list to every other index into the first list
    index = 0
    for i in range(1,(len(convertedList)*2-1),2):
        if(index >= len(convertedListTwo)):
            index = 0
            convertedList.insert(i,convertedListTwo[index])
        else:
            convertedList.insert(i,convertedListTwo[index])
            index +=1
    
    ## execute the inserted rotation by the offset
    convertedList = rotOperation(offset,convertedList)
    print('encoded list: ', convertedList)

    #revert back to alphanumeric numbers
    finalString = numberToStringConv(convertedList)
    print('final list: ' , finalString)

    return finalString


def decode(decodedString,decodedOffset):
    decodedAsciiList = stringToNumberConv(decodedString)
    print('decodedList', decodedAsciiList)
    originalList =  []

    for x in decodedAsciiList[1::2]:
        decodedAsciiList.remove(x)

    print(decodedAsciiList)

    originalList = rotOperation(decodedOffset,decodedAsciiList)

    print(originalList)


offset = -5
encodedMessage = encode('abcde',offset,'jjh')

offset = changeOffset(offset)

decodedMessage = decode(encodedMessage,offset)