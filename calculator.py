from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkthemes import ThemedTk
import math
import random

window = ThemedTk(theme='winxpblue')
window.geometry("310x240")
window.title("calculator ⊞")
window.config(themebg="arc")
var=StringVar()
result=""

def deletelast():
    txt.delete(len(txt.get()) - 1, END)



def clear():
    global result
    result= ""
    var.set("")

def press(num):
    global result
    result= result + str(num)
    var.set(result)

def equalpress():
    try:
        global result
        total= str(eval(result))
        var.set(total)
        result= ""
    except:
        var.set(' error ')
        result = ""

txt=Entry(window,font=('tahoma',15),text=var)
txt.grid(row=0,column=0,columnspan=4,ipady=10, ipadx=10)
btn1 = ttk.Button(window, text="1",width=4,command=lambda: press(1))
btn1.grid(row=1,column=0,ipady=10, ipadx=10)
btn2 = ttk.Button(window, text="2",width=4,command=lambda: press(2))
btn2.grid(row=1,column=1,ipady=10, ipadx=10)
btn3 = ttk.Button(window, text="3",width=4,command=lambda: press(3))
btn3.grid(row=1,column=2,ipady=10, ipadx=10)
btn4 = ttk.Button(window, text="4",width=4,command=lambda: press(4))
btn4.grid(row=2,column=0,ipady=10, ipadx=10)
btn5 = ttk.Button(window, text="5",width=4,command=lambda: press(5))
btn5.grid(row=2,column=1,ipady=10, ipadx=10)
btn6 = ttk.Button(window, text="6",width=4,command=lambda: press(6))
btn6.grid(row=2,column=2,ipady=10, ipadx=10)
btn7 = ttk.Button(window, text="7",width=4,command=lambda: press(7))
btn7.grid(row=3,column=0,ipady=10, ipadx=10)
btn8 = ttk.Button(window, text="8",width=4,command=lambda: press(8))
btn8.grid(row=3,column=1,ipady=10, ipadx=10)
btn9 = ttk.Button(window, text="9",width=4,command=lambda: press(9))
btn9.grid(row=3,column=2,ipady=10, ipadx=10)
btn0 = ttk.Button(window, text="0",width=4,command=lambda: press(0))
btn0.grid(row=4,column=1,ipady=10, ipadx=10)

btnplus = ttk.Button(window, text="+",width=4,command=lambda: press("+"))
btnplus.grid(row=1,column=3,ipady=10, ipadx=10)
btnmin = ttk.Button(window, text="-",width=4,command=lambda: press("-"))
btnmin.grid(row=2,column=3,ipady=10, ipadx=10)
btndotlinedot = ttk.Button(window, text=":",width=4,command=lambda: press(":"))
btndotlinedot.grid(row=3,column=3,ipady=10, ipadx=10)
btnclear = ttk.Button(window, text="CA",width=4,command=clear)
btnclear.grid(row=0,column=4,ipady=10, ipadx=10)
btnmult = ttk.Button(window, text="X",width=4,command=lambda: press("*"))
btnmult.grid(row=1,column=4,ipady=10, ipadx=10)
btnanswer = ttk.Button(window, text="=",width=4,command=equalpress)
btnanswer.grid(row=4,column=4,ipady=10, ipadx=10)
btnroot = ttk.Button(window, text="√",width=4,command=lambda: press('math.sqrt('))
btnroot.grid(row=3,column=4,ipady=10, ipadx=10)
btndot = ttk.Button(window, text=".",width=4,command=lambda: press("."))
btndot.grid(row=2,column=4,ipady=10, ipadx=10)
btn10 = ttk.Button(window, text="(",width=4,command=lambda: press("("))
btn10.grid(row=4,column=2,ipady=10, ipadx=10)
btn11 = ttk.Button(window, text=")",width=4,command=lambda: press(")"))
btn11.grid(row=4,column=3,ipady=10, ipadx=10)
btndltlast = ttk.Button(window, text="u’\u &#9003;’",width=4,command=deletelast)
btndltlast.grid(row=4,column=0,ipady=10, ipadx=10)
mytag= ttk.Label(window, text="old calculator© - made by holynazmoly")
mytag.grid(row=5,column=0,columnspan=4)

window.mainloop()