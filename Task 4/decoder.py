from encoder import *

def decode(decodedString,decodedOffset):
    decodedAsciiList = stringToNumberConv(decodedString)
    originalString =  []

    for x in decodedAsciiList[1::2]:
        decodedAsciiList.remove(x)


    originalString = rotOperation(int(decodedOffset),decodedAsciiList)
    originalString = numberToStringConv(originalString)
    
    return print ('decoded to: ', originalString)