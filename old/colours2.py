import sys
import re
import colorama
from colorama import Fore, Back, Style

colorama.init()

colours = dict(
c01    = Fore.RED + Back.BLACK + Style.NORMAL,    
c02    = Fore.RED + Back.BLACK + Style.BRIGHT,
c03    = Fore.RED + Back.WHITE + Style.NORMAL,
c04    = Fore.RED + Back.WHITE + Style.BRIGHT,
c05    = Fore.YELLOW + Back.BLACK + Style.NORMAL,
c06    = Fore.YELLOW + Back.BLACK + Style.BRIGHT,
c07    = Fore.YELLOW + Back.WHITE + Style.NORMAL,
c08    = Fore.YELLOW + Back.WHITE + Style.BRIGHT,
c09    = Fore.GREEN + Back.BLACK + Style.NORMAL,
c10    = Fore.GREEN + Back.BLACK + Style.BRIGHT,
c11    = Fore.GREEN + Back.WHITE + Style.NORMAL,
c12    = Fore.GREEN + Back.WHITE + Style.BRIGHT,
c13    = Fore.CYAN + Back.BLACK + Style.NORMAL,
c14    = Fore.CYAN + Back.BLACK + Style.BRIGHT,
c15    = Fore.CYAN + Back.WHITE + Style.NORMAL,
c16    = Fore.CYAN + Back.WHITE + Style.BRIGHT,
c17    = Fore.BLUE + Back.BLACK + Style.NORMAL,
c18    = Fore.BLUE + Back.BLACK + Style.BRIGHT,
c19    = Fore.BLUE + Back.WHITE + Style.NORMAL,
c20    = Fore.BLUE + Back.WHITE + Style.BRIGHT,
c21    = Fore.MAGENTA + Back.BLACK + Style.NORMAL,
c22    = Fore.MAGENTA + Back.BLACK + Style.BRIGHT,
c23    = Fore.MAGENTA + Back.WHITE + Style.NORMAL,
c24    = Fore.MAGENTA + Back.WHITE + Style.BRIGHT,
c25    = Fore.WHITE + Back.BLACK + Style.BRIGHT,
c26    = Fore.BLACK + Back.WHITE + Style.BRIGHT,
)

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



def colourFunc(c,t):
    #print(c+t+Style.RESET_ALL)
    sys.stdout.write(c+t+Style.RESET_ALL)

##for colour in range(0,25):
##    colourFunc(colours[sorted(colours.keys())[colour]],cons[colour])
##
##print(Style.RESET_ALL)
##
##for colour in range(0,20):
##    colourFunc(colours[sorted(colours.keys())[colour]],vowels[colour])
##
##    
##print(Style.RESET_ALL)

import os
os.chdir("C:\\Users\\Lois\\Dropbox\\Personal\\Python\\")


location = "./data/"
#infile = input ("type filename (in ./data/) to convert:\n")
infile = "sDPHONsonnet116.txt"
loc_infile = location + infile
f = open(loc_infile,"r")
#f.replace("2","r")
for line in f: #reading input file into 'line'
    temp=line.replace("'","")
    temp = re.split("[ ,.;:!?\s-]|\*|\n|'*|'S",temp) #splitting 'line' into words
    words = [x for x in temp if x !='']#getting rid of null words
    for word in words: #looping over words in line
        phlets = re.split("/",word)
        #print(phlets)
        for phlet in phlets:
            vphlet=phlet.strip("".join(cons))
            for colour in range(0,20):
                if vphlet == vowels[colour]:
                    colourFunc(colours[sorted(colours.keys())[colour]],phlet)
        sys.stdout.write(" ")
    sys.stdout.write("\n")

f.close()            
sys.stdout.write("\n")


    
 
f = open("sDPHONsonnet116.txt","r")


for line in f: #reading input file into 'line'
    temp=line.replace("'","")
    
    temp = re.split("[ ,.;:!?\s-]|\*|\n|'*|'S",temp) #splitting 'line' into words
    words = [x for x in temp if x !='']#getting rid of null words
    for word in words: #looping over words in line
        phsyls = re.split("/",word)
        for phsyl in phsyls:
            cphlets=list(re.sub('[%s]' % ''.join(vowels), '', phsyl))
            vphlet=list(re.sub('[%s]' % ''.join(cons), '', phsyl))
            phlets=list(phsyl)
            for phlet in phlets:
                for con in cons:
                    if phlet == con:
                        colourFunc(colours[sorted(colours.keys())[cons.index(phlet)]],cons[cons.index(phlet)])
                        sys.stdout.write("")
                        #print(colours[sorted(colours.keys())[cons.index(phlet)]],cons[cons.index(phlet)])
                if phlet in vowels:
                    sys.stdout.write(phlet)
                    #sys.stdout.write("")
                    
        sys.stdout.write(" ")
    sys.stdout.write("\n")
    
f.close()     
input("Press enter to exit. ") 


