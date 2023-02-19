import tkinter as tk
from tkinter import *

window=Tk()
window.title("Weight Converter App")
window.geometry("750x500")

Label(window,text="Weight Converter App",font=("Arial", 36 ),fg='#A020F0').pack()

kg=tk.IntVar()

def convert_to_gram():
    kg1=kg.get()
    gram = float(kg1)*1000
    Label(window,text="Weight in grams:",font=("Arial", 18 )).pack()
    Label(window,text=gram, font=("Arial", 18 )).pack()

def convert_to_ounce():
    kg1=kg.get()
    ounce = float(kg1)*35.274
    Label(window,text="Weight in ounce:",font=("Arial", 18 )).pack()
    Label(window,text=ounce,font=("Arial", 18 )).pack()

def convert_to_pound():
    kg1=kg.get()
    pound = float(kg1)*2.20462
    Label(window,text="Weight in pound:",font=("Arial", 18 )).pack()
    Label(window,text=pound, font=("Arial", 18 )).pack()

Label(window,text="Enter the Weight in Kgs",font=("Arial", 18 )).pack()
Entry(window,textvariable=kg, font=('arial', '13')).pack()

Button(window,text="Convert to Gram",bg="#A020F0", fg="#E0FFFF", command=convert_to_gram, font=('arial', '13')).pack(pady=10)
Button(window,text="Convert to Ounce",bg="#A020F0", fg="#E0FFFF",command=convert_to_ounce, font=('arial', '13')).pack(pady=8)
Button(window,text="Convert to Pound",bg="#A020F0", fg="#E0FFFF",command=convert_to_pound, font=('arial', '13')).pack(pady=8)

window.mainloop()
