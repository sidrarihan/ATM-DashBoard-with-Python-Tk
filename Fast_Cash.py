from tkinter import *

root =Tk()
root.title("Welcome to the Cash Withdrawal")
root.geometry("350x250")
root.resizable(width=False, height=False)

def wdlclick():
   
    pass
#defining all cash deposit buttons 

Enter_card_number = Text(root, height = 1, width = 20)
Enter_pin = Text(root, height=1, width = 20)
number = Button(root, text="200", command = wdlclick)
no_1= Button(root, text="500", command = wdlclick)
no_2 = Button(root, text="1000", command = wdlclick)
no_3= Button(root, text="2000", command = wdlclick)
#label for deposit window

cn = Label(root, text="Enter Card Number")
cn.config(font =("Courier", 14))

pn = Label(root, text="Enter PIN")
pn.config(font =("Courier", 14))

#arranging buttons to grid
cn.grid(row=0, column=0, padx=10,pady=10)
Enter_card_number.grid(row=0, column=1, padx =10,pady=10)

pn.grid(row=1, column=0, padx=10, pady=10)
Enter_pin.grid(row=1, column=1, padx=10,pady=10)

number.grid(row=2, column=0, padx=10,pady=10)
no_1.grid(row=2, column=1, padx=10,pady=10)
no_2.grid(row=3, column=0, padx=10,pady=10)
no_3.grid(row=3, column=1, padx=10,pady=10)
# mainloop to keep the program running.
root.mainloop()