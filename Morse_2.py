#-----------------------------------------------------------------
#                    MORSE CODE EXERCISER
#                    ====================
#
# This is a Morse code exercise program. The program generates
# random characters which are converted into Morse code and sent
# to the buzzer
#
# Author: Dogan Ibrahim
# File  : Morse2.py
# Date  : July, 2020
# Modifié par F6EQN 02/2021
#-------------------------------------------------------------------
import RPi.GPIO as GPIO             # Import RPi
import time                 # Import time
import random                   # Import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)              # GPIO mode BCM
Buzzer = 26                 # Buzzer pin

GPIO.setup(Buzzer, GPIO.OUT)            # Buzzer is output
GPIO.output(Buzzer, 1)              # Disable Buzzer

#
# Morse code table as a dictionary
#
MorseCode = {' ': ' ',
   '0': '-----',
   '1': '.----',
   '2': '..---',
   '3': '...--',
   '4': '....-',
   '5': '.....',
   '6': '-....',
   '7': '--...',
   '8': '---..',
   '9': '----.',
   ':': '---...',
   ';': '-.-.-.',
   '?': '..--..',
   '/': '-..-.',
   '.': '.-.-.-',
   ',': '--..--',
   'A': '.-',
   'B': '-...',
   'C': '-.-.',
   'D': '-..',
   'E': '.',
   'F': '..-.',
   'G': '--.',
   'H': '....',
   'I': '..',
   'J': '.---',
   'K': '-.-',
   'L': '.-..',
   'M': '--',
   'N': '-.',
   'O': '---',
   'P': '.--.',
   'Q': '--.-',
   'R': '.-.',
   'S': '...',
   'T': '-',
   'U': '..-',
   'V': '...-',
   'W': '.--',
   'X': '-..-',
   'Y': '-.--',
   'Z': '--..'}

#
# Output a dot
#
def Dot():
    GPIO.output(Buzzer, 0)
    time.sleep(DotTime)
    GPIO.output(Buzzer, 1)
    time.sleep(DotTime)

#
# Output a dash
#
def Dash():
    GPIO.output(Buzzer, 0)
    time.sleep(DashTime)
    GPIO.output(Buzzer, 1)
    time.sleep(DotTime)

try: # fonction qui permet de surveiller une action sur le clavier...

#
# Get the required words per minute, calculate timings
#
    wpm = int(input("Required words per minute: "))
    UnitTime = 1.2/wpm
    DotTime = UnitTime
    InterCharTime = 2 * UnitTime
    DashTime = 3 * UnitTime
    WordTime = 6* UnitTime
   
    cpt = 0 # compteur de caracteres.

    values = MorseCode.values()
    values_list = list(values)
    keys = MorseCode.keys()
    keys_list = list(keys)

    while True:                  # Do forever
        
              
        r = random.randint(1, 42)         # Genere un nb aleatoire pour index
        c = values_list[r]            # Get a value - lit le code pointe par r 
        d = keys_list[r]              # Get its key - lit le caractere pointe par r
        
        if d != ' ': # detecte si le caractere est un espace
      
            cpt = cpt+1 # incremente le compteur de caracteres
        
            if cpt == 6:
                c = ' ' # genere un espace si 5 caracter generes
                d = ' '
                cpt = 0 # remet le compteur a zero
          
            print(d, end="", flush=True)      # Display key
      
            for code in c:                # Do for code
                if code == '-':            # If dash
                    Dash()
                elif code == '.':          # if dot
                    Dot()
            time.sleep(InterCharTime)
      
 
except KeyboardInterrupt:# permet la sortie du pgm si control C
    print("")
    GPIO.output(Buzzer,1)



