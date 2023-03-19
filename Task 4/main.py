
## 4.Task:  Encode, decode – interactive
from encoder import *
from decoder import *

enteredQuit = False

## While loop to keep command-line interaction possible.
while(not enteredQuit):
    inputLine = input('>')

    inputSplit = inputLine.split()

    if 'quit' in inputSplit:
        enteredQuit = True
        break

    elif len(inputSplit) >= 1:

        if len(inputSplit) == 4:
            
            ## if 2nd string is given, the encode function will take the parameter
            if inputSplit[0] == 'encode':
                encodeMessage = encode(inputSplit[1],inputSplit[2],inputSplit[3])

            else:
                raise Exception('no encode call found')

        elif len(inputSplit) == 3:

            ## if the 2nd string is not stated, the function will choose random ascii characters
            if inputSplit[0] == 'encode':
                
                encodeMessage = encode(inputSplit[1],inputSplit[2])

            elif inputSplit[0] == 'decode':
                decodeMessage = decode(inputSplit[1],inputSplit[2])

   