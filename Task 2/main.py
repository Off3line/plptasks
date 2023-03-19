
## 2.Task: Encode, decode
from encoder import *
from decoder import *



## selected input, based on the assignment sheet
offset = -5
encodedMessage = encode('abcde',offset,'jjh')

offset = changeOffset(offset)
decodedMessage = decode(encodedMessage,offset)