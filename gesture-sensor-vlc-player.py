import serial # Serial library for serial communication
import time # Required for delay functions
import pyautogui

# Create Serial port object
arduinoSerialData = serial.Serial('COM6', 9600)

# Wait for 2 seconds for the communication to establish
time.sleep(2)

while True:
    incoming = arduinoSerialData.readline().decode('ascii').strip() # Read the serial data and decode it from bytes to string
    print(incoming)
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], interval=0.2)
        
    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')
        
    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right')

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'up')

    incoming = ""
