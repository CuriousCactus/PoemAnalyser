import colorama
from colorama import Fore, Back, Style

colorama.init()

##Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
##Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
##Style: DIM, NORMAL, BRIGHT, RESET_ALL

####
##
####from subprocess import call
####
####for color in('a','b','d', 'e', 'c'): #cycles through different colours
####    call('cls', shell=True) #clears the screen
####    call('color ' + color, shell=True)
####    print('The quick brown fox jumps over the lazy dog.')
####    time.sleep(1)
####    input("\nPress enter to exit. ")
##
####import time
##
##import ctypes
##
##colours = dict(
##    
##BRIGHT_BLUE    = 0x007b,
##BRIGHT_GREEN    =0x007c,
##BRIGHT_CYAN    = 0x007d,
##BRIGHT_RED    =  0x007e,
##BRIGHT_PURPLE   =0x007f,
##
##DARK_BLACK    =  0x0070,
##DARK_BLUE    =   0x0071,
##DARK_GREEN    =  0x0072,
##DARK_CYAN      = 0x0073,
##DARK_RED    =    0x0074,
##DARK_PURPLE    = 0x0075,
##DARK_YELLOW    = 0x0076,
##
##
##
##BRIGHT_BLUE_BG    = 0x008b,
##BRIGHT_GREEN_BG    = 0x008c,
##BRIGHT_CYAN_BG      = 0x008d,
##BRIGHT_RED_BG    = 0x008e,
##BRIGHT_PURPLE_BG    = 0x008f,
##
##DARK_BLACK_BG    = 0x0080,
##DARK_BLUE_BG    = 0x0081,
##DARK_GREEN_BG    = 0x0082,
##DARK_CYAN_BG      = 0x0083,
##DARK_RED_BG    = 0x0084,
##DARK_PURPLE_BG    = 0x0085,
##DARK_YELLOW_BG    = 0x0086
##
##
###BRIGHT_YELLOW    = 0x000g,
###BRIGHT_WHITE    = 0x000h,
##)
##colours = dict(
##    
##c01    = 0x008b,
##c02    = 0x007b,
##c03    =0x008c,
##c04    = 0x007c,
##c05    = 0x008d,
##c06     = 0x007d,
##c07  =  0x008e,
##c08    = 0x007e,
##c09    = 0x008f,
##c10   =0x007f,
##c11    = 0x0080,
##c12   =  0x0070,
##c13    = 0x0081,
##c14  =   0x0071,
##c15    = 0x0082,
##c16    =  0x0072,
##c17      = 0x0083,
##c18      = 0x0073,
##c19    = 0x0084,
##c20    =    0x0074,
##c21   = 0x0085,
##c22   = 0x0075,
##c23    = 0x0086,
##c24    = 0x0076
##)
##colours = dict(
##    
##c01    = 0x007b,
##c02    =0x007c,
##c03    = 0x007d,
##c04  =  0x007e,
##c05   =0x007f,
##
##c06   =  0x0070,
##c07  =   0x0071,
##c08    =  0x0072,
##c09      = 0x0073,
##c10    =    0x0074,
##c11   = 0x0075,
##c12    = 0x0076,
##
##
##
##c13    = 0x008b,
##c14    = 0x008c,
##c15     = 0x008d,
##c16    = 0x008e,
##c17    = 0x008f,
##
##c18    = 0x0080,
##c19    = 0x0081,
##c20    = 0x0082,
##c21      = 0x0083,
##c22    = 0x0084,
##c23    = 0x0085,
##c24    = 0x0086
##)

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
)
##colours = dict(
##c01    = 0x0084,    
##c02    = 0x0074,
##c03    = 0x008c,
##c04    = 0x007c,
##c05    = 0x0086,
##c06    = 0x0076,
##c07    = 0x008e,
##c08    = 0x007e,
##c09    = 0x0082,
##c10    = 0x0072,
##c11    = 0x008a,
##c12    = 0x007a,
##c13    = 0x0083,
##c14    = 0x0073,
##c15    = 0x008b,
##c16    = 0x007b,
##c17    = 0x0081,
##c18    = 0x0071,
##c19    = 0x0089,
##c20    = 0x0079,
##c21    = 0x0085,
##c22    = 0x0075,
##c23    = 0x008d,
##c24    = 0x007d,
##)
#BRIGHT_YELLOW    = 0x000g,
#BRIGHT_WHITE    = 0x000h,

#colours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,112,113,114,115,116,117,118,119]

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
"j"]

##
#### colorFunc(handle,colours['RED'])
#### print ("Cherry on top")
##

##input("\nPress enter to exit. ")
####for k, v in colours.iteritems():
####    print (k, v)
##
##

##import ctypes
##
### Constants from the Windows API
##STD_OUTPUT_HANDLE = -11
##
##colourFunc = ctypes.windll.kernel32.SetConsoleTextAttribute
##
##
##
##def get_csbi_attributes(handle):
##    # Based on IPython's winconsole.py, written by Alexander Belchenko
##    import struct
##    csbi = ctypes.create_string_buffer(22)
##    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
##    #assert res
##
##    (bufx, bufy, curx, cury, wattr,
##    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
##    return wattr
##
##
##handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
##reset = get_csbi_attributes(handle)
#sorted(d.keys())

#print (sorted(colours.values()))
#print (sorted(colours.values())[2])
#colorFunc(handle,sorted(colours.values())[2])
#colorFunc(handle,0x0002)

#for colour in sorted(colours.values()):

def colourFunc(c,t):
    print(c+t)

for colour in range(0,24):
    colourFunc(colours[sorted(colours.keys())[colour]],cons[colour])

print(Style.RESET_ALL)

for colour in range(0,20):
    colourFunc(colours[sorted(colours.keys())[colour]],vowels[colour])

    
print(Style.RESET_ALL)

#ctypes.windll.kernel32.SetConsoleTextAttribute(handle, RED)
#print ("Cherry on top")
#ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)

input("Press enter to exit. ")


