from encoder import *

def decode(decodedString,decodedOffset):
    decodedAsciiList = stringToNumberConv(decodedString)
    print('decodedList', decodedAsciiList)
    originalString =  []

    for x in decodedAsciiList[1::2]:
        decodedAsciiList.remove(x)


    originalString = rotOperation(decodedOffset,decodedAsciiList)
    originalString = numberToStringConv(originalString)
    print('final String', originalString)

def changeOffset(offset):

    if offset >= 1:
        return -abs(offset)
    else:
        return abs(offset)