import re
from tkinter import *
from tkinter import filedialog

filepath = "./data/sDPHONsonnet116.txt"



linitvowelcolours = ['#ff0000', '#ff4400', '#ff8800', '#ffbb00', '#ffdd00',
          '#ffff00', '#ddff00', '#bbff00', '#88ff00', '#44ff00',
          '#00ff00', '#00ff44', '#00ff88', '#00ffbb', '#00ffdd',
          '#00ffff', '#00ddff', '#00bbff', '#0088ff', '#0044ff',
          '#0000ff', '#4400ff', '#8800ff', '#bb00ff', '#dd00ff',
          '#ff00ff', '#ff00dd', '#ff00bb', '#ff0088', '#ff0044']

linitconcolours = ['#ff0000', '#ff4400', '#ff8800', '#ffbb00', '#ffdd00',
          '#ffff00', '#ddff00', '#bbff00', '#88ff00', '#44ff00',
          '#00ff00', '#00ff44', '#00ff88', '#00ffbb', '#00ffdd',
          '#00ffff', '#00ddff', '#00bbff', '#0088ff', '#0044ff',
          '#0000ff', '#4400ff', '#8800ff', '#bb00ff', '#dd00ff',
          '#ff00ff', '#ff00dd', '#ff00bb', '#ff0088', '#ff0044']

oinitvowelcolours = [ 'deep pink', 'dark violet', 'purple', 'blue4', 'RoyalBlue3',
			'deep sky blue', 'powder blue', 'cyan', 'spring green', 'forest green', 			'green3','lawn green', 'yellow green', 'goldenrod1','yellow',
			'light salmon', 'orange','tomato', 'red', 'snow4', 'snow']


oinitconcolours = ['magenta2', 'deep pink', 'medium orchid', 'dark violet', 'purple',
			'blue4', 'RoyalBlue3', 'deep sky blue', 'powder blue', 'dark turquoise',
			'cyan', 'spring green', 'forest green', 'green3','lime green',
			'lawn green', 'yellow green', 'goldenrod1','yellow', 'light salmon', 				'orange','tomato', 'red', 'snow4', 'thistle',
			'#0044ff']

whitecolours = ['#ffffff']*30
ticks = [1]*30

name = "Oli"

vc = "c"

cla=oinitconcolours
fixedcla=cla
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

egcons={
"p"  : "Put",
"b"  : "But",
"t"  : "Ten",
"d"  : "Den",
"k"  : "Can",
"m"  : "Man",
"n"  : "Not",
"l"  : "Like",
"r"  : "Run",
"2"  : "heR",
"f"  : "Full",
"v"  : "Very",
"s"  : "Some",
"z"  : "Zeal",
"h"  : "Hat",
"w"  : "Went",
"g"  : "Game",
"tS"  : "CHain",
"dZ"  : "Jane",
"9"  : "loNG",
"T"  : "THin",
"D"  : "THen",
"S"  : "SHip",
"Z"  : "meaSure",
"j"  : "Yes",
"N":"nothiNG"
}


egvowels = {
"i" : "bEAn",
"A" : "bArn",
"O" : "bOrn",
"u" : "bOOn",
"3" : "bUrn",
"I" : "pIt",
"e" : "pEt",
"&" : "pAt",
"V" : "pUtt",
"0" : "pOt",
"U" : "gOOd",
"@" : "actIOn",
"eI" : "bAy",
"aI" : "bUy",
"oI" : "bOy",
"@U" : "nO",
"aU" : "nOw",
"I@" : "pEEr",
"e@" : "pAIr",
"u@" : "pOOr"
}

def phletting(phsyl):
    scons=sorted(cons, key=len)
    scons.reverse()
    svowels=sorted(vowels, key=len)
    svowels.reverse()
    s=scons+svowels
    phlets=[]
    a=0
    while a< len(phsyl):
        out =0
        for phlet in s:
            if phlet == phsyl[a:a+len(phlet)]:
                out = 1
                break
        if out == 1:
            a=a+len(phlet)
            phlets.append(phlet)            
        else:
            a=a+len(phlet)
    return phlets

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

def vowelstext(colours):
    text.delete(1.0, END)
    file = open(filepath,"r")
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

    return maxlinelen,lineno
    
def constext(colours):
    file = open(filepath,"r")
    lineno = 0
    maxlinelen = 0
    text.delete(1.0, END)
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
                cphlets=list(re.sub('[%s]' % ''.join(vowels), '', phsyl))
                vphlet=re.sub('[%s]' % ''.join(cons), '', phsyl)
                phlets=phletting(phsyl)
                for phlet in phlets:
                    for con in cons:
                        if phlet == con:
                            nline=line.replace("/","")
                            if len(nline)>maxlinelen:
                                maxlinelen = len(nline)
                            start=nline.find(phlet,start+1)
                            end=start+len(phlet)
                            tag="tag"+str(con)
                            colourfunc(colours[cons.index(phlet)],cons[cons.index(phlet)],lineno,start,end,tag)
                    if phlet in vowels:
                        nline=line.replace("/","")
                        start=nline.find(phlet,start+1)
                        end=start+len(phlet)
                        tag="tag"+str(phlet)
                        text.insert(INSERT, vphlet)
                        text.tag_add(tag, str(lineno)+"."+str(start), str(lineno)+"."+str(end))
                        text.tag_config(tag, foreground="white")
            text.insert(INSERT, " ")
        text.insert(INSERT, "\n")
    file.close()

def messagewindow():

    namevar = StringVar()
    namevar.set(name)

    v = StringVar()
    v.set(vc)

    def seticol():
        global cla
        global name
        global vc
        if namevar.get() == "Oli":
            name = "Oli"
            if v.get()=="c":
                cla=oinitconcolours
                constext(cla)
                vc = "c"
            elif v.get()=="v":
                cla=oinitvowelcolours
                vowelstext(cla)
                vc = "v"
            
        elif namevar.get() == "Lois":
            name = "Lois"
            if v.get()=="c":
                cla=linitconcolours
                constext(cla)
                vc = "c"
            elif v.get()=="v":
                cla=linitvowelcolours
                vowelstext(cla)
                vc = "v"        
    
    seticol()

    def sel():
        if v.get()=="c":
            constext(cla)
        elif v.get()=="v":
            vowelstext(cla)

    def checkvc():
        global letters
        if v.get() == "v":
            letters = vowels
        elif v.get() == "c":
            letters = cons

    def refreshcols():
        try:
            cols=[]
            
            for letter in letters:
                #print(my_data[letter].get())
                if my_data[letter].get() == 1:
                    cols.append(fixedcla[letters.index(letter)])
                else:
                    cols.append("#ffffff")
            global cla
            cla = cols
        except:
            pass
            
    def printticks():
        global ticks
        global cla
        ticks = []
        for letter in letters:           
            if my_data[letter].get() == 0:
                my_data[letter].set(0)
                ticks.append(0)
            else:
                my_data[letter].set(1)
                ticks.append(1)
        refreshcols()
        sel()

    global my_data
    my_data = {}
    
    def doframe():
        global fixedcla
        checkvc()
        seticol()
        refreshcols()
        global lframe
        pframe = Frame(win, width=50)
        pframe.grid(column=0, row=0, rowspan=3, sticky=N+E+W)
        lframe = Frame(pframe)
        lframe.grid(column=0, row=0, sticky=N+S+E+W)
        framecs = {}
        global my_data
        global cla
        row = 0
        col = 0
        for letter in letters:
            win.rowconfigure(letters.index(letter),weight=1)
            framec = Frame(lframe, bg=fixedcla[letters.index(letter)], width =17)
            framec.grid(row=row, column=col, sticky=N+S+E+W)
            row += 1
            if (row > 8):
                row = 0
                col += 1
            label = Label(framec, text=letter,width=3)
            label.grid(column=0, row=0, sticky=N+S+E+W)
            if vc == "c":
                eg = Label(framec, text=egcons[letter],width=7)
            else:
                eg = Label(framec, text=egvowels[letter],width=7)
            eg.grid(column=1, row=0, sticky=N+S+E+W)
            frame = Frame(framec, borderwidth=3, relief=SUNKEN)
            frame.grid(column=2, row=0, sticky=N+S+E+W)
            framecs[letter] = Frame(frame, bg=fixedcla[letters.index(letter)], width =17)
            framecs[letter].grid(column=0, row=0, sticky=N+S+E+W)
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)
            my_data[letter]=IntVar()
            tick = Checkbutton(framec, state=NORMAL, variable=my_data[letter], command=printticks)
            if cla[letters.index(letter)] == "#ffffff":
                my_data[letter].set(0)
            else:
                my_data[letter].set(1)
            tick.grid(column=3, row=0)
            
    def colscheme():
        global fixedcla
        if namevar.get() == "Oli":
            if v.get()=="c":
                fixedcla=oinitconcolours
            elif v.get()=="v":
                fixedcla=oinitvowelcolours
        elif namevar.get() == "Lois":
            if v.get()=="c":
                fixedcla=linitconcolours
            elif v.get()=="v":
                fixedcla=linitvowelcolours
        lframe.grid_forget()
        lframe.destroy()
        doframe()
        sel()
        
    win = Toplevel(root,borderwidth=5)
    win.resizable(0,0)
    
    savebutton.config(state='disable')
    openbutton.config(state='disable')
    
    win.columnconfigure(0,weight=1)
    win.columnconfigure(1,weight=1)
    
    radioframe = Frame(win, relief=SUNKEN, borderwidth=3)
    radioframe.grid(row=0, column=1, sticky=N+E+W)
               
    vowelradio = Radiobutton(radioframe, text="Vowels", variable=v, value="v", command=colscheme)
    conradio = Radiobutton(radioframe, text="Consonants", variable=v, value="c", command=colscheme)
    vowelradio.grid(row=0, column=0, sticky=N+S+W)
    conradio.grid(row=1, column=0, sticky=N+S+W)
   
    mradioframe = Frame(win, relief=SUNKEN, borderwidth=3)
    mradioframe.grid(row=1, column=1, sticky=N+E+W)

    mvowelradio = Radiobutton(mradioframe, text="Oli", variable=namevar, value="Oli", command=colscheme)
    mconradio = Radiobutton(mradioframe, text="Lois", variable=namevar, value="Lois", command=colscheme)
    mvowelradio.grid(row=0, column=0, sticky=N+S+W)
    mconradio.grid(row=1, column=0, sticky=N+S+W)
    
    doframe()

    bframe = Frame(win)
    bframe.grid(column=1, row=2, sticky=S+E+W)

    def selectall():
        for letter in letters:
            my_data[letter].set(1)
        printticks()

    sallbutton = Button(bframe,text="Select all",command=selectall)
    sallbutton.grid(column=0,row=0, sticky=S+E+W)
        
    def deselectall():
        for letter in letters:
            my_data[letter].set(0)
        printticks()

    desallbutton = Button(bframe,text="Deselect all",command=deselectall)
    desallbutton.grid(column=0,row=1, sticky=S+E+W)

    bframe.columnconfigure(0,weight=1)

    def quit_win():
        win.destroy()
        savebutton.config(state='normal')
        openbutton.config(state='normal')
        
    win.protocol("WM_DELETE_WINDOW", quit_win)
    
root = Tk()

root.config(borderwidth=5)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

vscrollbar = AutoScrollbar(root)
vscrollbar.grid(row=0, column=1,rowspan=2, sticky=N+S)
hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set,highlightthickness=0)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
canvas.bind("<Configure>", resize)

vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)

padframe = Frame(root, width=5)
padframe.grid(row=0, column=2, sticky=N+S+E+W,rowspan=2)

butframe = Frame(root)
butframe.grid(column=3,row=0, sticky=N+S+E+W)

def getfile():
    global filepath
    oldfilepath =filepath
    filepath=filedialog.askopenfilename(initialdir ="data")
    if len(filepath) == 0:
        filepath =oldfilepath
    vowelstext(whitecolours)

openbutton = Button(butframe,text="Open file",command=getfile)
openbutton.grid(column=0,row=0,columnspan=1, sticky=N+S+E+W)

savebutton = Button(butframe,text="Change colours",command=messagewindow)
savebutton.grid(column=0,row=1,columnspan=1, sticky=N+S+E+W)

textframe = Frame(canvas)
textframe.grid(row=0, column=0, sticky=N+S+E+W)
textframe.rowconfigure(1, weight=1)
textframe.columnconfigure(1, weight=1)

text = Text(textframe,bg="#000000", width=10, height=10, relief=SUNKEN, borderwidth=3)
text.pack(side=LEFT, fill=BOTH, expand = 1)

maxlinelen,lineno=vowelstext(whitecolours)
text.config(width=maxlinelen, height=lineno)

canvas.bind("<Configure>", resize)

canvas.create_window(0, 0, anchor=NW, window=textframe)

textframe.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
