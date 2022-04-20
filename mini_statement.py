
from tkinter import *

root =Tk()
root.title("Welcome to the mini statement")
root.geometry("350x250")
root.resizable(width=False, height=False)

def statclick():
   
    pass
#defining all cash generate buttons 


card_number = Text(root, height=1, width=20)
show = Button(root, text="show", command = statclick)

#label for generate window

cn = Label(root, text="Enter card number")
cn.config(font =("Courier", 14))

# fd = Label(root, text=" ")
# fd.config(font =("Courier", 14))


#arranging buttons to grid
cn.grid(row=0, column=0, padx=10,pady=10)
# Enter_card_number.grid(row=0, column=1, padx =10,pady=10)

# fd.grid(row=1, column=0, padx=10, pady=10)
card_number.grid(row=1, column=0, padx=10,pady=10)

show.grid(row=3, column=0, padx=10,pady=10)



# mainloop to keep the program running.
root.mainloop()

