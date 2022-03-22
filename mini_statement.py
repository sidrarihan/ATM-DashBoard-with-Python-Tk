
from tkinter import *

root =Tk()
root.title("Welcome to the mini statement")
root.geometry("350x250")
root.resizable(width=False, height=False)

def statclick():
   
    pass
#defining all cash generate buttons 

account_number = Text(root, height = 1, width = 10)
from_date = Text(root, height=1, width=10)
to_date = Text(root, height=1, width=10)
generate = Button(root, text="Generate", command = statclick)

#label for generate window

an = Label(root, text="Account Number")
an.config(font =("Courier", 14))

fd = Label(root, text="From Date")
fd.config(font =("Courier",14))

td = Label(root, text="To Date")
td.config(font =("Courier",14))


#arranging buttons to grid
an.grid(row=0, column=0, padx=10,pady=10)
account_number.grid(row=0, column=1, padx =10,pady=10)

fd.grid(row=1, column=0, padx=10, pady=10)
from_date.grid(row=1, column=1, padx=10,pady=10)

td.grid(row=2, column=0, padx=10, pady=10)
to_date.grid(row=2, column=1, padx=10, pady=10)

generate.grid(row=3, column=0, padx=10,pady=10)



# mainloop to keep the program running.
root.mainloop()