import time, random
from colormath.color_objects import HSVColor, AdobeRGBColor
from colormath.color_conversions import convert_color# Colour Sensors - range between [TBD]
from pybricks.ev3devices import ColorSensor

# A temporary measure - creates random values to be 
# perceived as white for testing purposes.
class stackfunctions():
    "All functions relating to working with the sensor stack. Includes debug values."
    
    def __init__(self, IsTestMode:bool, ColourSensor:ColorSensor) -> None:
        "Declares necessary variables and populates the stack. Currently uses debug values, needs to be switched to sensors when building robot."
        
        # The parsed initial input from the sensor, used to determine the difference between true white and the tile's colour.
        self.calibrateStack:list = []
        # The stack containing the parsed black value
        self.blackStack:list = []
        # The stack containing the parsed green values (hue and value)
        self.greenStack:list = []
        # The lists into which all data is initially dumped.
        self.inputStackRaw:list[HSVColor] = []
        self.inputStackParsed:list = []
        # The measurements of change in the stack
        self.sensorChange:list[int] = [0,0,0,0,0]
        self.sensorModGreen:list[int] = [0,0,0,0,0]
        self.Sensor = ColourSensor

        self.test:bool = IsTestMode
        # Initialisation protocols - calibrates the sensors
        # and populates the stacks 
        if self.test:
            for i in range(50): 
                # Populates the calibrator with raw generated hsv data
                self.inputStackRaw.append(self.newwhite())
        else:
            for i in range(50):
                time.sleep(0.5)
                self.inputStackRaw.append(convert_color(AdobeRGBColor(self.Sensor.rgb()), HSVColor))

        
    def newwhite(self) -> list:
        "Debug function: Generates XYZ colour values, then returns HSV values."
        # Creates XYZ (Raw input from sensors)
        xyz = AdobeRGBColor(random.randint(200,255),random.randint(200,255), random.randint(200,255))
        # Converts to HSV (Useful colour format)
        return convert_color(xyz, HSVColor).get_value_tuple()
    
    def update(self):
        "Cycles the stack by one. Should be called every loop, ideally as the first instruction"
        # Cycles the stack down
        for i in range(1,len(self.inputStackRaw)):
            self.inputStackRaw[-i] = self.inputStackRaw[-(i+1)]
        
        # Generates false data in testing mode. REPLACE IN RELEASE VERSION
        if self.test: self.inputStackRaw[0] = self.newwhite()
        else: self.inputStackRaw[0] = self.Sensor.rgb()

        # Converts the raw calibrated data into a more useful format
        self.inputStackParsed:list = []
        for i in range(len(self.inputStackRaw)): self.inputStackParsed.append(HSVColor(round(self.inputStackRaw[i][0]), round(self.inputStackRaw[i][1]*100), round(self.inputStackRaw[i][2])))
        
        # Populates the stacks with the relevant data.
        for i in self.inputStackParsed: 
            self.blackStack.append(i.hsv_v)
            self.greenStack.append([i.hsv_h,i.hsv_s] if i.hsv_h < 135 and i.hsv_h > 80 and i.hsv_s > 20 and i.hsv_v > 30 else [0,0])
        
        # Create detection values. Tweak in testing so the furthest spread is a few seconds behind.
        try:self.sensorChange[0] = (self.inputStackParsed[0].hsv_s/self.inputStackParsed[1].hsv_s) *100
        except:self.sensorChange[0] = 0
        try:self.sensorChange[1] = (self.inputStackParsed[0].hsv_s/self.inputStackParsed[4].hsv_s) *100
        except:self.sensorChange[1] = 0
        try:self.sensorChange[2] = (self.inputStackParsed[0].hsv_s/self.inputStackParsed[9].hsv_s) *100
        except:self.sensorChange[2] = 0
        try:self.sensorChange[3] = (self.inputStackParsed[0].hsv_s/self.inputStackParsed[19].hsv_s) *100
        except:self.sensorChange[3] = 0
        try:self.sensorChange[4] = (self.inputStackParsed[0].hsv_s/self.inputStackParsed[49].hsv_s) *100
        except:self.sensorChange[4] = 0
        
        try:self.sensorModGreen[0] = (self.greenStack[0].hsv_s/self.greenStack[1].hsv_s) *100
        except:self.sensorModGreen[0] = 0
        try:self.sensorModGreen[1] = (self.greenStack[0].hsv_s/self.greenStack[4].hsv_s) *100
        except:self.sensorModGreen[1] = 0
        try:self.sensorModGreen[2] = (self.greenStack[0].hsv_s/self.greenStack[9].hsv_s) *100
        except:self.sensorModGreen[2] = 0
        try:self.sensorModGreen[3] = (self.greenStack[0].hsv_s/self.greenStack[19].hsv_s) *100
        except:self.sensorModGreen[3] = 0
        try:self.sensorModGreen[4] = (self.greenStack[0].hsv_s/self.greenStack[49].hsv_s) *100
        except:self.sensorModGreen[4] = 0

        for value in self.sensorChange: print(value, '%')
       
    def compareblack(top, reference):
        "returns the difference between the most recent list element and a given element."
        return [top[2]-reference[2]]
    
    def showcolours(self, colour): return f"https://www.convertingcolors.com/hsv-color-{round(colour[0])}_{round(colour[1])}_{round(colour[2])}.html?"
    
# Declares stack
# Enables testing features such as artificial list population


# Cycles the stack by one clearing the lowest value and moving every
# value down one to allow for a new value to enter the stack
if __name__ == '__main__':
    stack = stackfunctions(True, 'e')

    while True: 
        time.sleep(0.1)
        # x = stack.update(True)
        
        # for y in range(len(x)):
        #     x[y] = str(x[y])
        stack.update(True, '')
        # print(stack.blackStack)
        # print(stack.greenStack)
        # print(stack.inputStackParsed)

        # break
    