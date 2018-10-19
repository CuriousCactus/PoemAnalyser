import re
from tkinter import *

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
			'snow']

#print(len(oinitconcolours))
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
    
    #text.config(width=text.cget('width'), height=text.cget('height'))
    #text.config(width=maxlinelen, height=lineno)
    #print(text.cget('width'))
    #text.config()
    
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
    #text.config(width=maxlinelen, height=lineno)
    #print(text.cget('width'))
    #text.config(width=text.cget('width'), height=text.cget('height'))
    #print(text.cget('width'))
    #resize()
    #text.config()


        
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
        #selection = str(v.get())
        #label.config(text = selection)
        #v = StringVar()
        #v.set(vc)
        #global vc
        if v.get()=="c":
            constext(cla)
            #vc = "c"
        elif v.get()=="v":
            vowelstext(cla)
            #vc = "v"

    def checkvc():
        global letters
        if v.get() == "v":
            letters = vowels
            #colours = vowelcolours
            
        elif v.get() == "c":
            letters = cons
            #colours = concolours

    def refreshcols():
        #seticol()
        #checkvc()
        #doframe()
        try:
            #print(letters,my_data["p"].get(),ticks)

            cols=[]
            
            for letter in letters:
                
                if my_data[letter].get() == 1:
                    cols.append(fixedcla[letters.index(letter)])
                else:
                    cols.append("#ffffff")
                #print(my_data[letter].get())
            
            #print (cols)
            global cla
            cla = cols
            #print(len(cla))
            #print(cla)
        except:
            pass
            
    def printticks():
        
        
        #print(cla)
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
##            if cla[letters.index(letter)] == "#ffffff":
##                my_data[letter].set(0)
##                ticks.append(0)
##            else:
##                my_data[letter].set(1)
##                ticks.append(1)

    global my_data
    my_data = {}
    

    def doframe():
        global fixedcla 
        #print(cla)
        checkvc()
        seticol()
        refreshcols()
        #print(cla)
        global lframe
        lframe = Frame(win)
        lframe.grid(column=0, row=0, rowspan=3, sticky=N+E+W)
        framecs = dict()
        
        global my_data
        global ticks
        global cla
        ticks = []
        for letter in letters:
            win.rowconfigure(letters.index(letter),weight=1)
            label = Label(lframe, text=letter)
            label.grid(column=0, row=letters.index(letter), sticky=N+S+E+W)
            frame = Frame(lframe, borderwidth=3, relief=SUNKEN)
            frame.grid(column=1, row=letters.index(letter), sticky=N+S+E+W)
            
            framecs[letter] = Frame(frame, bg=fixedcla[letters.index(letter)], width =17)
            framecs[letter].grid(column=0, row=0, sticky=N+S+E+W)
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)
            my_data[letter]=IntVar()
            tick = Checkbutton(lframe, state=NORMAL, variable=my_data[letter], command=printticks)
##            if ticks[letters.index(letter)] == 1:
##                my_data[letter].set(0)
##                ticks.append(0)
##            else:
##                my_data[letter].set(1)
##                ticks.append(1)
            if cla[letters.index(letter)] == "#ffffff":
                my_data[letter].set(0)
                ticks.append(0)
            else:
                my_data[letter].set(1)
                ticks.append(1)
            tick.grid(column=3, row=letters.index(letter))
        #print(cla)
        #print(my_data)
            
    

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
        #refreshcols()
        #print(fixedcla)
        lframe.grid_forget()
        lframe.destroy()
        #print(lframe)
        #print(cla)
        doframe()
        #print(fixedcla)
        
        #printticks()
##        for letter in letters:
##            framecs[letter].config(bg=fixedcla[letters.index(letter)])

    # create child window
    win = Toplevel(root,borderwidth=5)
    #win.grab_set()
    savebutton.config(state='disable')

    win.columnconfigure(0,weight=1)
    win.columnconfigure(1,weight=1)
    


    radioframe = Frame(win, relief=SUNKEN, borderwidth=3)
    radioframe.grid(row=0, column=1, sticky=N+E+W)
    ##radioframe.columnconfigure(2, weight=1)
    

            
    vowelradio = Radiobutton(radioframe, text="Vowels", variable=v, value="v", command=colscheme)
    conradio = Radiobutton(radioframe, text="Consonants", variable=v, value="c", command=colscheme)
    vowelradio.grid(row=0, column=0, sticky=N+S+W)
    conradio.grid(row=1, column=0, sticky=N+S+W)
    
    




    
    
    
    mradioframe = Frame(win, relief=SUNKEN, borderwidth=3)
    mradioframe.grid(row=1, column=1, sticky=N+E+W)
    ##radioframe.columnconfigure(2, weight=1)



    mvowelradio = Radiobutton(mradioframe, text="Oli", variable=namevar, value="Oli", command=colscheme)
    mconradio = Radiobutton(mradioframe, text="Lois", variable=namevar, value="Lois", command=colscheme)
    mvowelradio.grid(row=0, column=0, sticky=N+S+W)
    mconradio.grid(row=1, column=0, sticky=N+S+W)
    
##    if cla == oinitconcolours:
##        namevar.set("Oli")
##    else:
##        namevar.set("Lois")  

    doframe()


    



    bframe = Frame(win)
    bframe.grid(column=1, row=2, sticky=S+E+W)

    def selectall():
        for letter in letters:
            my_data[letter].set(1)
        printticks()

    sallbutton = Button(bframe,text="Select all",command=selectall)
    sallbutton.grid(column=4,row=1,columnspan=1, sticky=S+E+W)
        
    def deselectall():
        for letter in letters:
            my_data[letter].set(0)
        printticks()

    desallbutton = Button(bframe,text="Deselect all",command=deselectall)
    desallbutton.grid(column=4,row=2,columnspan=1, sticky=S+E+W)
            
    #return colchoices

    #printbutton = Button(win,text="Apply",command=printticks)
    #printbutton.grid(column=0,columnspan=4, sticky=N+S+E+W)
    #print(colchoices)
    

    def quit_win():
        win.destroy()
        savebutton.config(state='normal')
        #vowelradio.config(state='normal')
        #conradio.config(state='normal')

    #QuitButton = Button(win,text='Exit',command=quit_win)
    #QuitButton.grid(column=0,columnspan=4, sticky=N+S+E+W)

    win.protocol("WM_DELETE_WINDOW", quit_win)
    
# create scrolled canvas

root = Tk()
# make the canvas expandable

root.config(borderwidth=5)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

vscrollbar = AutoScrollbar(root)
vscrollbar.grid(row=0, column=1,rowspan=2, sticky=N+S)
hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set,highlightthickness=0)
canvas.grid(row=0, column=0,rowspan=2, sticky=N+S+E+W)
canvas.bind("<Configure>", resize)

vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)

padframe = Frame(root, width=5)
padframe.grid(row=0, column=2, sticky=N+S+E+W,rowspan=2)



butframe = Frame(root)
butframe.grid(column=3,row=1,columnspan=1, sticky=N+S+E+W)

def getfile():
    global filepath
    oldfilepath =filepath
    filepath=filedialog.askopenfilename(initialdir ="data")
    if len(filepath) == 0:
        filepath =oldfilepath
    #print(filepath)
    sel()

openbutton = Button(butframe,text="Open file",command=getfile)
openbutton.grid(column=0,row=0,columnspan=1, sticky=N+S+E+W)

savebutton = Button(butframe,text="Change colours",command=messagewindow)
savebutton.grid(column=0,row=1,columnspan=1, sticky=N+S+E+W)

# create canvas contents

textframe = Frame(canvas)
textframe.grid(row=0, column=0, sticky=N+S+E+W)
textframe.rowconfigure(1, weight=1)
textframe.columnconfigure(1, weight=1)

text = Text(textframe,bg="#000000", width=10, height=10, relief=SUNKEN, borderwidth=3)
text.pack(side=LEFT, fill=BOTH, expand = 1)


maxlinelen,lineno=vowelstext(whitecolours)
#maxlinelen=45
#lineno=14
text.config(width=maxlinelen, height=lineno)


canvas.bind("<Configure>", resize)

canvas.create_window(0, 0, anchor=NW, window=textframe)

textframe.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
