# module = a file containing python code
# contain functions and classes and etc.

# used with modular programming
# which helps in separating a program into parts

import messages
import messages as msg 
from messages import hello,hi
# from messages import * (^risky^ import every function)

msg.hello()
messages.hi()

help("modules")