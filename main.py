import time
import random
# Colour Sensors - range between [TBD]
leftXYZ:list = ['0','0','0']
rightXYZ:list = ['0','0','0']

# A temporary measure - creates random values to be 
# perceived as white for testing purposes.
class newwhite():
    def new() -> list:
        return [random.randint(6901,9642)/10000,random.randint(7157,10000)/10000, random.randint(5906,8252)/10000]

# Declares necessary variables - the calibration values, 
# the stacks, and the initialiser (another debug option)
calibrate:list = []
stack:dict = []
parsedStacks = {}
init:bool = True

# Initialisation protocols - calibrates the sensors
# and populates the stacks 
if init:
    init = False

    for i in range(10): 
        time.sleep(0.5)
        calibrate.append(newwhite.new())
    
    stack = calibrate*5 
    print(stack)
    print(calibrate)

while True: 
    break