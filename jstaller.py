import os
import keyboard
import time
import webbrowser
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

def installer(screen1text,beforecommand,ipath,endtext):
    mb.showinfo('Welcome!','Welcome to a JStaller installer!!!!!!!!')
    w1 = tk.Tk()
    w1.title('Install')
    s1t = tk.Text(w1)
    s1t.insert(1.0,screen1text)
    s1t.config(state='disabled')
    s1t.pack()
    def nstep2():
        w1.destroy()
        w2 = tk.Tk()
        w2.title('Install')
        tk.Label(text='The folowing command is about to run:').pack()
        s2t = tk.Text()
        s2t.config(state='disabled')
        s2t.insert(1.0,beforecommand)
        s2t.pack()
        btn2 = tk.Button(w2,text="Next",command=lambda:n())
        btn2.pack()
        def n():
            os.system(beforecommand)
            nstep3()



        def nstep3():
            w2.destroy()
            w3 = tk.Tk()

            def nstep4():
                w3.destroy()
                edtext = tk.Tk()
                edtext.title('Install')
                et = tk.Text()
                et.insert(endtext)
            l3 = tk.Label(w3,text='The software will now be installed...')
            l3.pack()
            nb = tk.Button(w3,text='Next',command=lambda:nn())
            def nn():
                webbrowser.open(ipath)
                new234 = tk.Tk()
                nt234 = tk.Text(new234)
                nt234.pack()
                nt234.insert(1.0,endtext)

            nb.pack()
            w3.mainloop()
        w2.mainloop()

    ntt222 = tk.Button(w1, text='Next', command=lambda: nstep2())
    ntt222.pack()
    w1.mainloop()
    mb.showinfo('Goodbye','Goodbye from a JStaller installer!')