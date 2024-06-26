from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from colourwork import stackfunctions
from DSTSensor import DSTSensor
 
LeftSensor:stackfunctions  = stackfunctions(True, 'ColorSensor(INPUT_1)')
RightSensor:stackfunctions = stackfunctions(True, 'ColorSensor(INPUT_2)')
DST = DSTSensor('InfraredSensor(INPUT_3)', True)

# LeftWheel:LargeMotor  = LargeMotor(OUTPUT_A)
# RightWheel:LargeMotor = LargeMotor(OUTPUT_B)
LeftSpeed:float  = 1
RightSpeed:float = 1
while True:
    LeftSensor.update()
    RightSensor.update()

    LeftSpeed   *= LeftSensor.sensorChange [0]
    RightSpeed  *= RightSensor.sensorChange[0]

    LeftSpeed   += LeftSensor.sensorModGreen [0]
    RightSpeed  += RightSensor.sensorModGreen[0]

    if DST.objectDetected():
        
    # LeftWheel.on(LeftSpeed)    
    # RightWheel.on(RightSpeed)
