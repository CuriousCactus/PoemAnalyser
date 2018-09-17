colours = ['#ff0000', '#ff4400', '#ff8800', '#ffbb00', '#ffdd00',
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

from tkinter import *

root = Tk()
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

my_data = {}

for vowel in vowels:
    root.rowconfigure(vowels.index(vowel),weight=1)
    label = Label(root, text=vowel)
    label.grid(column=0, row=vowels.index(vowel), sticky=N+S+E+W)
    frame = Frame(root, borderwidth=3, relief=SUNKEN)
    frame.grid(column=1, row=vowels.index(vowel), sticky=N+S+E+W)
    framec = Frame(frame, bg=colours[vowels.index(vowel)])
    framec.grid(column=0, row=0, sticky=N+S+E+W)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    my_data[vowel]=IntVar()
    my_data[vowel].set(True)
    tick = Checkbutton(root, state=ACTIVE, variable=my_data[vowel])
    tick.grid(column=3, row=vowels.index(vowel))    

def printticks():    
    for vowel in vowels: 
        print(my_data[vowel].get())

savebutton = Button(root,text="Print",command=printticks)
savebutton.grid(column=0,columnspan=4, sticky=N+S+E+W)

root.mainloop()
