import sys
import mouse
import keyboard
import time

usage = "  ~ AUTOCLICKER ~\n\n\
    This program automatically triggers mouse clicks\n\
    You can set the delay between each click with the appropriate flag\n\
    /!\ WARNING I do not recommend to set a delay below 10 milliseconds\n\n\
    $> python3 autoclick.py [FLAGS]\n\n\
        --help (-h)         : Display this message\n\
        --delay (-d) DELAY  : Set the DELAY value in millisecond (default value: 1000)\n\n\
    Have fun !\n"

class AutoClick():
    def __init__(self, delay):
        # Amount of seconds between clicks
        self.delay = delay

        # Cooldown clock
        self.clock = time.time()

        # Amount of clicks realised in a sequence
        self.clickCount = 0

    def exitCheck(self):
        if keyboard.is_pressed('escape'):
            exit(0)

    def isRunning(self):
        return not keyboard.is_pressed('ctrl+d')

    def click(self):
        mouse.click()
        self.clickCount += 1


    # Run the autoclick
    def start(self):
        print("Starting auto-click (ctrl+D to stop)")

        # Stop condition check
        while(self.isRunning()):
            self.exitCheck()

            # Cooldown check
            if (time.time() - self.clock > self.delay):
                self.click()
                self.clock = time.time()

    # Run the autoclick without any delay
    def startNoDelay(self):
        print("Starting auto-click (ctrl+D to stop)")

        # Stop condition check
        while(self.isRunning()):
            self.click()

    def run(self):
        print("  ~ Autoclicker ~\nPress Escape to exit\nPress Ctrl+S to start\n")
        while not keyboard.is_pressed('ctrl+s'):
            self.exitCheck()

        while(True):
            # Start the autoclick in the proper mode
            if self.delay == 0:
                self.startNoDelay()
            else:
                self.start()

            print("Clicked", self.clickCount, "times\n")
            self.clickCount = 0

            # Once the auto click was paused
            print("Auto click paused (ctrl+S to resume | Escape to exit)\n")
            while not keyboard.is_pressed('ctrl+s'):
                self.exitCheck()

# TODO Handle the program args with a lib

# Instanciate the auto click with the delay given as parameter
if len(sys.argv) > 2 and (sys.argv[1] == "--delay" or sys.argv[1] == "-d") and sys.argv[2].isnumeric():
    clickBot = AutoClick(int(sys.argv[2]) / 1000)
    clickBot.run()

elif len(sys.argv) > 1 and (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
    print(usage)

# If no delay was set (default = 1 sec)
else:
    # Default
    clickBot = AutoClick(1)
    clickBot.run()

