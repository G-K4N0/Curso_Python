
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import title

win = Tk()
win.geometry("500x400")

paneText = ttk.Frame(win,padding=10)
paneText.grid()
ttk.Label(paneText, text="", foreground="white" , background="grey",width=20,font=("Arial",30)).grid(column=0,row=0)

paneButtons = ttk.Frame(win,padding="20")
paneButtons.grid()

lista = ['AC','()','%','/','7','8','9','X','4','5','6','-','1','2','3','+','0','.','<-','=']

def botones():
    pos = 0
    for fil in range(0,5):
        for col in range(0,4):
            ttk.Button(paneButtons,text=lista[pos]).grid(column=col,row=fil)
            pos +=1
botones();

win.mainloop()
