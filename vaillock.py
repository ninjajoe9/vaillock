# A program to read a text file and display it to the user through LED's on the keyboard in morse code. 
# Idea originally from Cryptonomicron and Randy Waterhouse's anti Van Eck phreaking script.

#!/usr/bin/env python
import pyautogui as pyag
import time 
import sys

# sets LED to use for display. Default = numlock.  
if len(sys.argv) > 2:
    blinky = sys.argv[2]
    print("vaillock using " + sys.argv[2])
else:
    blinky = "numlock"

wpm = 20 # TODO: do the math and figure out how to actually translate to WPM

morse_alphabet = {
"a" : ".-",
"b" : "-...",
"c" : "-.-.",
"d" : "-..",
"e" : ".",
"f" : "..-.",
"g" : "--.",
"h" : "....",
"i" : "..",
"j" : ".---",
"k" : "-.-",
"l" : ".-..",
"m" : "--",
"n" : "-.",
"o" : "---",
"p" : ".--.",
"q" : "--.-",
"r" : ".-.",
"s" : "...",
"t" : "-",
"u" : "..-",
"v" : "...-",
"w" : ".--",
"x" : "-..-",
"y" : "-.--",
"z" : "--..",
"1" : ".----",
"2" : "..---",
"3" : "...---",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----.",
"0" : "-----",
" " : " ",
"\n" : ""
}


def morse_dit():
    pyag.press(blinky)
    time.sleep(4/wpm)
    pyag.press(blinky)
    time.sleep(4/wpm)


def morse_dah():
    pyag.press(blinky)
    time.sleep(12/wpm)
    pyag.press(blinky)
    time.sleep(4/wpm)


def morse_letter(x):
    encoding = morse_alphabet[x]
    for symbol in encoding:
        if symbol == '-':
            morse_dah()
        elif symbol == '.':
            morse_dit()
        elif symbol == ' ':
            time.sleep(2/wpm)
        else:
            pass
    time.sleep(12/wpm)


def morse_word(word):
    letters = [char for char in word]
    for character in letters:
        morse_letter(character)

def morse_file(file):
    for line in file:
            letters = [char for char in line]
            for character in letters:
                morse_letter(character)

    
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as file:
        morse_file(file)
else:
    filename = input("Please enter the path of a text file: ")
    with open(filename, 'r') as file:
        morse_file(file)

# morse_letter("h")
# morse_letter("e")
# morse_letter("l")
# morse_letter("l")
# morse_letter("o")
# morse_word("world")

# Morse 'R' for testing
# morse_dit()
# morse_dah()
# morse_dit()
