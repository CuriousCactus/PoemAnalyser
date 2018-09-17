from tkinter import *

from tkinter import ttk
import sys
import re

FONT_SIZE = 10 # (pixels)

COLORS = ['#ff0000', '#ff4400', '#ff8800', '#ffbb00', '#ffdd00',
          '#ffff00', '#ddff00', '#bbff00', '#88ff00', '#44ff00',
          '#00ff00', '#00ff44', '#00ff88', '#00ffbb', '#00ffdd',
          '#00ffff', '#00ddff', '#00bbff', '#0088ff', '#0044ff',
          '#0000ff', '#4400ff', '#8800ff', '#bb00ff', '#dd00ff',
          '#ff00ff', '#ff00dd', '#ff00bb', '#ff0088', '#ff0044']



vowels=["i", 
"A", 
"O", 
"u", 
"3", 
"I", 
"e", 
"&", 
"V", 
"0", 
"U", 
"@", 
"eI", 
"aI", 
"oI", 
"@U", 
"aU", 
"I@", 
"e@", 
"u@"] 


cons=["p",
"b",
"t",
"d",
"k",
"m",
"n",
"l",
"r",
"f",
"v",
"s",
"z",
"h",
"w",
"g",
"tS", 
"dZ",
"9",
"T",
"D",	 	 	 
"S",	 	 	 
"Z",	 	 	 
"j",
"2",
"N"]



##def colourFunc(c,t):
##    #print(c+t+Style.RESET_ALL)
##    sys.stdout.write(c+t+Style.RESET_ALL)
##
##for colour in range(0,25):
##    colourFunc(colours[sorted(colours.keys())[colour]],cons[colour])
##
##
##for colour in range(0,20):
##    colourFunc(colours[sorted(colours.keys())[colour]],vowels[colour])

    



##root = Tk()
##root.title("Named colour chart")
##row = 0
##col = 0
##for color in COLORS:
##  e = Label(root, text=color, background=color, 
##        font=(None, -FONT_SIZE))
##  e.grid(row=row, column=col, sticky=E+W)
##  row += 1
##  if (row > 36):
##    row = 0
##    col += 1
##
##root.mainloop()

root = Tk()
root.title("Vowels and consonants")
root.resizable(0,0)

f = Frame(root)
f.grid(row=0, column=0, sticky=E+W, padx = 10, pady = 10)

fv = Frame(f)
fc = Frame(f)
fv.grid(row=0, column=0, sticky=E+W, padx = 10, pady = 10)
fc.grid(row=0, column=1, sticky=E+W, padx = 10, pady = 10)

root.columnconfigure(0, weight=1, minsize=300)
f.columnconfigure(0, weight=1)
f.columnconfigure(1, weight=1)
fv.columnconfigure(0, weight=1)
fc.columnconfigure(0, weight=1)


row = 0
col = 0
for vowel in vowels:
  e = Label(fv, text=vowel, background=COLORS[vowels.index(vowel)])
  e.grid(row=row, column=col, sticky=E+W)
  e.columnconfigure(0, weight=1)
  row += 1

row = 0
col = 0
for con in cons:
  e = Label(fc, text=con, background=COLORS[cons.index(con)])
  e.grid(row=row, column=col, sticky=E+W)
  e.columnconfigure(0, weight=1)
  row += 1

root.mainloop()
