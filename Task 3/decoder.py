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