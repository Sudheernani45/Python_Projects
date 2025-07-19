
🧠 Code Explanation (Line-by-Line):

import tkinter as tk
from tkinter import messagebox
import winsound
import time
tkinter: Module for GUI creation.

messagebox: Popup dialogs (like errors, info).

winsound: Plays sound on Windows.

time: Used to create delay (for counting effect).

🔒 ATM Class with GUI

class ATM:
    def __init__(self, root):
Class ATM represents the entire simulator logic.

root: The Tkinter main window passed from the main script.


        self.balance = 1000  # Starting balance
        self.pin = "1234"    # Default PIN
User starts with a default ₹1000.

Hardcoded PIN: "1234".


        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("500x400")
        self.root.configure(bg="#2E8B57")  # SeaGreen background
Set window title, size, and background color.


        self.label = tk.Label(root, text="Enter your PIN:", bg="#2E8B57", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)
Label asking user to enter PIN.


        self.pin_entry = tk.Entry(root, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=10)
Password-style input for PIN.


        self.submit_button = tk.Button(root, text="Submit", command=self.check_pin, bg="#FFD700", fg="black", font=("Arial", 12))
        self.submit_button.pack(pady=10)
Submit button triggers check_pin() function on click.

🔐 PIN Check

    def check_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.show_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")
Compares entered PIN with default.

On success, shows main menu; else, shows error popup.

📋 Menu Options

    def show_menu(self):
        self.clear_window()
Clears the screen for the new menu.


        self.label = tk.Label(self.root, text="Select an option:", bg="#2E8B57", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)
New label: Prompt user to choose action.


        self.check_balance_button = tk.Button(...command=self.check_balance...)
        self.withdraw_button = tk.Button(...command=self.withdraw_money...)
        self.deposit_button = tk.Button(...command=self.deposit_money...)
Buttons for balance check, withdraw, and deposit, all styled similarly.

💰 Check Balance

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: {self.balance}")
Shows current balance in a popup.

💸 Withdraw Flow

    def withdraw_money(self):
        self.clear_window()
        ...
        self.withdraw_button = tk.Button(...command=self.process_withdrawal...)
User inputs amount to withdraw.

On clicking withdraw, process_withdrawal() is called.


    def process_withdrawal(self):
        amount = int(self.amount_entry.get())
        if amount > self.balance:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            self.balance -= amount
            messagebox.showinfo("Success", f"Withdrawn: {amount}...")
            self.amount_counting_sound(amount)
Validates if enough balance exists.

If yes, deducts and shows success message.

Triggers sound effect via amount_counting_sound.

💳 Deposit Flow

    def deposit_money(self):
        self.clear_window()
        ...
        self.deposit_button = tk.Button(...command=self.process_deposit...)
Similar layout to withdraw, asks for deposit amount.


    def process_deposit(self):
        amount = int(self.amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Invalid deposit amount")
        else:
            self.balance += amount
            messagebox.showinfo("Success", f"Deposited: {amount}...")
            self.amount_counting_sound(amount)
Validates deposit amount.

Adds to balance and plays sound effect.

🔊 Sound Effect

    def amount_counting_sound(self, amount):
        for _ in range(amount // 100):
            winsound.Beep(1000, 100)
            time.sleep(0.1)
Plays a beep for every ₹100 deposited/withdrawn.

1000 Hz beep, each lasting 0.1 seconds.

🧹 Utility: Clear UI

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
Destroys (clears) all widgets in current window.

🚀 Program Entry Point

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
Starts Tkinter app.

Instantiates ATM class and enters the GUI event loop.

