from tkinter import *


root =Tk()
root.title("Welcome to the main page")
root.geometry("350x250")
root.resizable(width=False, height=False)
#defining calls for the button pages.
def myClick():
    pass
def deposit():
    import deposit

def mini_statement():
    import mini_statement
# def balance_inquiry():
#     import balance_inquiry
def cash_withdrawal():
    import cash_withdrawal

def transfer_funds():
    import Transfer_funds
def fast_cash():
    import Fast_Cash
def update_contact():
    import Update_contacts
# def change_pin():
#     import change_pin
# defining all buttons
cash_deposit = Button(root, text="Deposit Cash", command=deposit)
mini_statement = Button(root, text="Mini Statement", command=mini_statement)
balance_inquiry = Button(root, text="Balance Inquiry", command=myClick)
cash_withdrawal = Button(root, text="Cash Withdrawal", command=cash_withdrawal)
transfer_funds = Button(root, text="Transfer Funds", command=transfer_funds)
change_pin = Button(root, text="Change PIN", command=myClick)
fast_cash = Button(root, text="Fast Cash", command=fast_cash)
update_contact = Button(root, text="Update Contact", command=update_contact)

#Arranging all buttons in a grid.
cash_deposit.grid(row=0, column=0, padx=10,pady=10)
mini_statement.grid(row=0, column=1, padx=10,pady=10)

cash_withdrawal.grid(row=1, column=0, padx=10,pady=10)
fast_cash.grid(row=1, column=1, padx=10,pady=10)

balance_inquiry.grid(row=2, column=0, padx=10,pady=10)
change_pin.grid(row=2, column=1, padx=10,pady=10)


transfer_funds.grid(row=3, column=0, padx=10,pady=10)
update_contact.grid(row=3, column=1, padx=10,pady=10)

#Resizing all buttons equally
cash_deposit.config(height=2, width=20)
mini_statement.config(height=2, width=20)
cash_withdrawal.config(height=2, width=20)
fast_cash.config(height=2, width=20)
balance_inquiry.config(height=2, width=20)
change_pin.config(height=2, width=20)
transfer_funds.config(height=2, width=20)
update_contact.config(height=2, width=20)

# mainloop to keep the program running.
root.mainloop()