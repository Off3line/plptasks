
## 3.Task: Encode, decode – with random salt
from encoder import *
from decoder import *


## selected input, based on the assignment sheet, no additional string added
offset = -5
encodedMessage = encode('abcde',offset)

offset = changeOffset(offset)
decodedMessage = decode(encodedMessage,offset)