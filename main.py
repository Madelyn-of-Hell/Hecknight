from colourwork import stackfunctions
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_B
 
LeftSensor:stackfunctions  = stackfunctions(True, 'ColorSensor(INPUT_1)')
RightSensor:stackfunctions = stackfunctions(True, 'ColorSensor(INPUT_2)')
LeftWheel:LargeMotor  = LargeMotor(OUTPUT_A)
RightWheel:LargeMotor = LargeMotor(OUTPUT_B)
LeftSpeed:float  = 1
RightSpeed:float = 1
while True:
    LeftSensor.update()
    RightSensor.update()

    LeftSpeed   *= LeftSensor.sensorChange[0]
    RightSensor *= RightSensor.sensorChange[0]

    LeftWheel.on(LeftSpeed)    
    RightWheel.on(RightSpeed)
