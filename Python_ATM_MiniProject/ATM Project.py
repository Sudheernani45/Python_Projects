import tkinter as tk
from tkinter import messagebox
import winsound
import time

# ATM class with Tkinter interface
class ATM:
    def __init__(self, root):
        self.balance = 1000  # Starting balance
        self.pin = "1234"    # Default PIN for this simulation

        # Creating the Tkinter window
        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("500x400")  # Enlarged ATM window size
        self.root.configure(bg="#2E8B57")  # Set ATM background color to SeaGreen

        # Creating Entry fields and buttons
        self.label = tk.Label(root, text="Enter your PIN:", bg="#2E8B57", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)

        self.pin_entry = tk.Entry(root, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_pin, bg="#FFD700", fg="black", font=("Arial", 12))
        self.submit_button.pack(pady=10)

    def check_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.show_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def show_menu(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Select an option:", bg="#2E8B57", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)

        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance, bg="#FFD700", fg="black", font=("Arial", 12))
        self.check_balance_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", command=self.withdraw_money, bg="#FFD700", fg="black", font=("Arial", 12))
        self.withdraw_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit Money", command=self.deposit_money, bg="#FFD700", fg="black", font=("Arial", 12))
        self.deposit_button.pack(pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: {self.balance}")

    def withdraw_money(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Enter amount to withdraw:", bg="#2E8B57", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)

        self.amount_entry = tk.Entry(self.root, font=("Arial", 14))
        self.amount_entry.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.process_withdrawal, bg="#FFD700", fg="black", font=("Arial", 12))
        self.withdraw_button.pack(pady=10)

    def process_withdrawal(self):
        amount = int(self.amount_entry.get())
        if amount > self.balance:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            self.balance -= amount
            messagebox.showinfo("Success", f"Withdrawn: {amount}\nNew Balance: {self.balance}")
            self.amount_counting_sound(amount)

    def deposit_money(self):
        self.clear_window()

        self.label = tk.Label(self.root, text="Enter amount to deposit:", bg="#2E8B57", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)

        self.amount_entry = tk.Entry(self.root, font=("Arial", 14))
        self.amount_entry.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.process_deposit, bg="#FFD700", fg="black", font=("Arial", 12))
        self.deposit_button.pack(pady=10)

    def process_deposit(self):
        amount = int(self.amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Invalid deposit amount")
        else:
            self.balance += amount
            messagebox.showinfo("Success", f"Deposited: {amount}\nNew Balance: {self.balance}")
            self.amount_counting_sound(amount)

    def amount_counting_sound(self, amount):
        # Simulate a counting sound for each 100 units withdrawn or deposited
        for _ in range(amount // 100):
            winsound.Beep(1000, 100)  # Frequency of 1000Hz and duration of 100ms
            time.sleep(0.1)  # Delay to simulate counting effect

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main Function to run the ATM Simulator
if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
