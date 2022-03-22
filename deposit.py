
from tkinter import *

root =Tk()
root.title("Welcome to the deposit")
root.geometry("350x250")
root.resizable(width=False, height=False)

def deposiclick():
   
    pass
#defining all cash deposit buttons 

card_number = Text(root, height = 1, width = 20)
pin = Text(root, height=1, width = 10)
amount = Text(root, height=1, width=10)
deposit = Button(root, text="Deposit", command = deposiclick)

#label for deposit window

cn = Label(root, text="Card Number")
cn.config(font =("Courier", 14))

pn = Label(root, text="PIN")
pn.config(font =("Courier", 14))

amt = Label(root, text="Amount")
amt.config(font =("Courier", 14))

#arranging buttons to grid
cn.grid(row=0, column=0, padx=10,pady=10)
card_number.grid(row=0, column=1, padx =10,pady=10)

pn.grid(row=1, column=0, padx=10, pady=10)
pin.grid(row=1, column=1, padx=10,pady=10)

amt.grid(row=2, column=0, padx=10, pady=10)
amount.grid(row=2, column=1, padx=10, pady=10)

deposit.grid(row=3, column=0, padx=10,pady=10)



# mainloop to keep the program running.
root.mainloop()