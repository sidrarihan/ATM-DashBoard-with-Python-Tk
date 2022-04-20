
from tkinter import *

root =Tk()
root.title("Welcome to the deposit")
root.geometry("350x250")
root.resizable(width=False, height=False)

def deposiclick():
   
    pass
#defining all cash deposit buttons 

Enter_card_number = Text(root, height = 1, width = 20)
Enter_old_pin = Text(root, height=1, width = 10)
Enter_new_pin = Text(root, height=1, width=10)
ReEnter_the_new_pin = Text(root, height=1, width=10)
Change = Button(root, text="Change", command = deposiclick)

#label for deposit window

cn = Label(root, text="Enter Card Number")
cn.config(font =("Courier", 14))

pn = Label(root, text="Enter old pin")
pn.config(font =("Courier", 14))

amt = Label(root, text="Enter new pin")
amt.config(font =("Courier", 14))

new = Label(root, text="ReEnter the new pin")
amt.config(font =("Courier", 14))

#arranging buttons to grid
cn.grid(row=0, column=0, padx=10,pady=10)
Enter_card_number.grid(row=0, column=1, padx =10,pady=10)

pn.grid(row=1, column=0, padx=10, pady=10)
Enter_old_pin.grid(row=1, column=1, padx=10,pady=10)

amt.grid(row=2, column=0, padx=10, pady=10)
Enter_new_pin.grid(row=2, column=1, padx=10, pady=10)

new.grid(row=3, column=0, padx=10, pady=10)
ReEnter_the_new_pin.grid(row=3, column=1, padx=10, pady=10)

Change.grid(row=4, column=0, padx=10,pady=10)



# mainloop to keep the program running.
root.mainloop()