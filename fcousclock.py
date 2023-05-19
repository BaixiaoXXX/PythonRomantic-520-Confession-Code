# PythonRomantic-520-Confession-Code
Well, 520 is homophonic to “I love you” in Chinese! In fact, the 20th of May (520) is pronounced （wǔ èr líng）which sound very similar to 我爱你（wǒ ài nǐ）I love you, that is why the 20th (and 21st) have been labeled as the Internet Valentine's Day

import tkinter as tk
import tkinter.messagebox
root = tk.Tk()
root.title('❤')
root.resizable(0, 0)
root.wm_attributes("-toolwindow", 1)
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
widths = 300
heights = 100
x = (screenwidth - widths) / 2
y = (screenheight - heights) / 2
root.geometry('%dx%d+%d+%d' % (widths, heights, x, y))  
tk.Label(root, text='Dear, will you be my girlfriend?', width=37, font=('Verdana', 12)).place(x=0, y=10)
 
 
def OK():  # Agree button
    root.destroy()
    # Show floating love after agreement
 
 
def NO():  # Reject button. Refusing will not exit. You must agree to exit~
    tk.messagebox.showwarning('❤', 'Give you another chance!')
 
 
def closeWindow():
    tk.messagebox.showwarning('❤', 'Escaping is useless')
 
 
tk.Button(root, text='好哦', width=5, height=1, command=OK).place(x=80, y=50)
tk.Button(root, text='不要', width=5, height=1, command=NO).place(x=160, y=50)
root.protocol('WM_DELETE_WINDOW', closeWindow)  # Bind Exit Event
