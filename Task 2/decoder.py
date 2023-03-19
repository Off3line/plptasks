from encoder import *

def decode(decodedString,decodedOffset):
     ## convert strings into list containing the ascii numbers
    decodedAsciiList = stringToNumberConv(decodedString)
    originalString =  []

    ##remove every 2nd element from the list, starting with index 1
    for x in decodedAsciiList[1::2]:
        decodedAsciiList.remove(x)



    originalString = rotOperation(decodedOffset,decodedAsciiList)
    originalString = numberToStringConv(originalString)
   
    return print('decoded string ', originalString)



## Function to reverse the offset when decoding
def changeOffset(offset):

    if offset >= 1:
        return -abs(offset)
    else:
        return abs(offset)