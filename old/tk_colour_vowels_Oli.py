import re
from tkinter import *



colours = [ 'deep pink', 'dark violet', 'purple', 'blue4', 'RoyalBlue3',
			'deep sky blue', 'powder blue', 'cyan', 'spring green', 'forest green', 			'green3','lawn green', 'yellow green', 'goldenrod1','yellow',
			'light salmon', 'orange','tomato', 'red', 'snow4', 'snow']



vowels=["i", 
"u", 
"I", 
"U", 
"eI", 
"@", 
"@U", 
"e", 
"V", 
"oI", 
"&", 
"0", 
"A", 
"aI", 
"aU", 
"3", 
"O", 
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

class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise (TclError, "cannot use pack with this widget")
    def place(self, **kw):
        raise (TclError, "cannot use place with this widget")

def resize(event):
    text.config(width=event.width, height=event.height)

def colourfunc(col,txt,lineno,start,end,tag):
    text.insert(INSERT, txt)
    text.tag_add(tag, str(lineno)+"."+str(start), str(lineno)+"."+str(end))
    text.tag_config(tag, foreground=col)

# create scrolled canvas

root = Tk()

# make the canvas expandable

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

vscrollbar = AutoScrollbar(root)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set,highlightthickness=0)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
    
canvas.bind("<Configure>", resize)

vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)

# create canvas contents

frame = Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)

text = Text(frame,bg="#000000", width=10, height=10)
text.pack(side=LEFT, fill=BOTH, expand = 1)

file = open("./data/sDPHONsonnet116.txt","r")
lineno = 0
maxlinelen = 0
for line in file: #reading input file into 'line'
    start = - 1
    lineno = lineno + 1
    line = line.replace("'","")
    line = line.replace(",","")
    words = re.split("[ ,.;:!?\s-]|\*|\n|'*|'S",line) #splitting 'line' into words
    words = [x for x in words if x !='']#getting rid of null words
    for word in words: #looping over words in line        
        phsyls = re.split("/",word)
        for phsyl in phsyls:            
            vphlet=phsyl.strip("".join(cons))
            for vowel in vowels:
                if vphlet == vowel:
                    nline=line.replace("/","")
                    if len(nline)>maxlinelen:
                        maxlinelen = len(nline)
                    start=nline.find(phsyl,start+1)
                    end=start+len(phsyl)
                    tag="tag"+str(vowel)
                    colourfunc(colours[vowels.index(vphlet)],phsyl,lineno,start,end,tag)
        text.insert(INSERT, " ")
    text.insert(INSERT, "\n")
file.close()

text.config(width=maxlinelen, height=lineno)
    
canvas.bind("<Configure>", resize)

canvas.create_window(0, 0, anchor=NW, window=frame)

frame.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
