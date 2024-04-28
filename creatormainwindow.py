import tkinter as tk
from tkinter import ttk
import time
root = tk.Tk()
wec = ttk.Label(text="Welcome")
wec.pack()
istr = ttk.Label(text="import jstaller jstaller.installer(")
istr.pack()
starttext = ttk.Entry()
starttext.pack()
beforecommand = ttk.Entry()
beforecommand.pack()
ipath = ttk.Entry()
ipath.pack()
endtext = ttk.Entry()
endtext.pack()
istend = ttk.Label(text=")")
istend.pack()
def write():
    file = open(str(time.time()) + ".py","w")
    file.write("import jstaller\n")
    file.write('jstaller.installer(" + str(starttext.get()) + "," + str(beforecommand.get()) + "," + str(ipath.get()) + str(endtext.get()) + ")')
    file.close()

go = ttk.Button(text="Go",command=write())
go.pack()

root.mainloop()
