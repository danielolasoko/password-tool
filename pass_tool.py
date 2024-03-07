import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # Import simpledialog module separately
import hashlib
import secrets
import pyperclip  # Import pyperclip module for copying to clipboard

class PasswordTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Tool")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Password Tool", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Display options for the user
        tk.Label(self.root, text="Select an option:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.root, text="1. Generate Strong Password", command=self.generate_password, width=30).grid(row=2, column=0, padx=10, pady=5)

        tk.Button(self.root, text="2. Hash and Salt Password", command=self.hash_and_salt_password, width=30).grid(row=3, column=0, padx=10, pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.grid(row=4, column=0, padx=10, pady=5)

        tk.Button(self.root, text="Quit", command=self.root.quit, width=30).grid(row=5, column=0, padx=10, pady=5)

    def generate_password(self):
        length = 12
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=[]{}|;:,.<>?~"
        generated_password = "".join(secrets.choice(characters) for _ in range(length))
        messagebox.showinfo("Generated Password", f"Your generated password: {generated_password}")
        # Add button to copy password
        tk.Button(self.root, text="Copy Password", command=lambda: self.copy_to_clipboard(generated_password)).grid(row=3, column=0, padx=10, pady=5, sticky="w")

    def hash_and_salt_password(self):
        password = self.get_user_input("Enter a password to hash and salt:")
        if password:
            # Generate a random salt
            salt = secrets.token_hex(16)
            # Combine password and salt and hash using SHA-256
            hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
            # Display salt and hashed password
            result_text = f"Salt: {salt}\nHashed Password: {hashed_password}"
            self.result_label.config(text=result_text)
            # Add buttons to copy salt and hash
            tk.Button(self.root, text="Copy Salt", command=lambda: self.copy_to_clipboard(salt)).grid(row=5, column=0, padx=10, pady=5)
            tk.Button(self.root, text="Copy Hash", command=lambda: self.copy_to_clipboard(hashed_password)).grid(row=5, column=0, padx=10, pady=5, sticky="e")
        else:
            messagebox.showerror("Error", "Please enter a password.")

    def get_user_input(self, prompt):
        return simpledialog.askstring("Password Tool", prompt)  # Use simpledialog from tkinter module

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Text copied to clipboard.")

if __name__ == "__main__":
    password_tool = PasswordTool()
    password_tool.root.mainloop()
