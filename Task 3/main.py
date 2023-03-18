
## 2.Task:
from encoder import *
from decoder import *




offset = -5
encodedMessage = encode('abcde',offset,'jjh')

offset = changeOffset(offset)
##there is a bug when you put in phisi for example
decodedMessage = decode(encodedMessage,offset)