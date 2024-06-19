from pybricks.ev3devices import Motor, ColorSensor, InfraredSensor

from colourwork import stackfunctions
from DSTSensor import DSTSensor
leftSensor:stackfunctions  = stackfunctions(True, 'ColorSensor(\'in1\')')
rightSensor:stackfunctions = stackfunctions(True, 'ColorSensor(\'in2\')')

leftWheel  = Motor('outA')
rightWheel = Motor('outB')
DST = DSTSensor('InfraredSensor(\'in3\')', True)

# LeftWheel:LargeMotor  = LargeMotor(OUTPUT_A)
# RightWheel:LargeMotor = LargeMotor(OUTPUT_B)
leftSpeed:float  = 1
rightSpeed:float = 1


while True:
    leftSensor.update()
    rightSensor.update()

    leftSpeed   *= leftSensor.sensorChange [0]
    rightSpeed  *= rightSensor.sensorChange[0]

    leftSpeed   += leftSensor.sensorModGreen [0]
    rightSpeed  += rightSensor.sensorModGreen[0]

    if DST.objectDetected: ...
    leftWheel.run(leftSpeed)    
    rightWheel.run(rightSpeed)
