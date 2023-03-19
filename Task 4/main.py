
## 3.Task:
from encoder import *
from decoder import *
import sys



enteredQuit = False

while(not enteredQuit):
    inputLine = input('>')

    inputSplit = inputLine.split()

    if 'quit' in inputSplit:
        enteredQuit = True
        break

    elif len(inputSplit) >= 1:

        if len(inputSplit) == 4:

            if inputSplit[0] == 'encode':
                encodeMessage = encode(inputSplit[1],inputSplit[2],inputSplit[3])

            else:
                raise Exception('no encode call found')

        elif len(inputSplit) == 3:

            if inputSplit[0] == 'encode':
                
                encodeMessage = encode(inputSplit[1],inputSplit[2])

            elif inputSplit[0] == 'decode':
                decodeMessage = decode(inputSplit[1],inputSplit[2])

   