from ev3dev2.sensor.lego import ColorSensor, InfraredSensor
import time
class DSTSensor():
    """Functions regarding working with the Infrared Sensor"""
    def __init__(self, sensor:InfraredSensor, IsTest) -> None:

        self.test = IsTest

        self.INFStack:list[InfraredSensor] = []

        self.sensor = sensor

        if self.test:
            for i in range(50): 
                # Populates the calibrator with raw generated hsv data
                self.INFStack.append(self.fakeDST())
        else:
            for i in range(50):
                time.sleep(0.5)
                self.INFStack.append(self.newDST)
    def newDST(self) -> float:
        return self.sensor.proximity * 0.7

    def fakeDST(self) -> float:
        return 100 * 0.7

    def objectDetected(self) -> bool:
        self.detectionthreshold=60
        return self.INFStack[0] < self.detectionthreshold