import tkinter as tk

root = tk.Tk()
root.title('Main Window')
root.geometry('400x400')

def get_new_win():

    NewWin = tk.Toplevel(root)
    NewWin.title('New Window')
    NewWin.geometry('300x300')
    NewWinButton.config(state='disable')

    def quit_win():
        NewWin.destroy()
        NewWinButton.config(state='normal')

    QuitButton = tk.Button(NewWin,text='Quit',command=quit_win)
    QuitButton.pack()

    NewWin.protocol("WM_DELETE_WINDOW", quit_win) 

NewWinButton = tk.Button(root,text='New Window', command=get_new_win)
NewWinButton.pack()

root.mainloop()
