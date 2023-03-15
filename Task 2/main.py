
## 2.Task: 
def encode(firstString,offset,secondString):
    stringList = list(firstString)
    secondList = list(secondString)
    asciiString = []
    index = 1
    
    for charact in secondList:
        stringList.insert(index,charact)
        index = index + 2

    print(stringList)

def decode():
    print('do that')


encode('abcde',5,'jjh')