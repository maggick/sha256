#!/usr/bin/python

from tkinter import *
from tkinter import ttk
import hashlib

def calculate(*args):
    try:
        j=0
        value = str(mdp.get())
        while (j < 20):
            value = hashlib.sha256(value.encode('utf-8')).hexdigest()
            j+=1
        myhash.set(value)
    except ValueError:
        pass
    
root = Tk()
root.title("Encoding")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

mdp = StringVar()
myhash = StringVar()

mdp_entry = ttk.Entry(mainframe, width=7, textvariable=mdp)
mdp_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=myhash).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="hash", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="mot de passe").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="hash: ").grid(column=1, row=2, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

mdp_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()



