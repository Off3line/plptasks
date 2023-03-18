
## 2.Task:
def stringToNumberConv(convertedList):
    toasciiList = []
    for x in convertedList: 
        toasciiList.append(ord(x))

    print(toasciiList)
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
    print(' encoded list: ', convertedList)

    #revert back to alphanumeric numbers
    finalList = numberToStringConv(convertedList)
    print('final list: ' , finalList)





def decode():
    print('do that')


encode('abcde',-5,'jjh')