"""
5: Basic Login Form

Develop a Tkinter application that accepts a username and password using Entry widgets. Provide a Login button to validate the entered against predefined values and display an appropriate success or failure message.
"""


import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("350x280")

# Title
tk.Label(root, text="🔐 User Login", font=("Arial", 16, "bold")).pack(pady=15)

# Username
tk.Label(root, text="Username:").pack()
username = tk.Entry(root)
username.pack(pady=5)

# Password
tk.Label(root, text="Password:").pack()
password = tk.Entry(root, show="*")
password.pack(pady=5)

# Login function
def login():
    if username.get() == "admin" and password.get() == "1234":
        result.config(text="✅ Login Successful!", fg="green")
    else:
        result.config(text="❌ Invalid Username or Password", fg="red")

# Login button
tk.Button(root, text="Login", command=login, font=("Arial", 11, "bold")).pack(pady=12)

# Result message
result = tk.Label(root, text="", font=("Arial", 10, "bold"))
result.pack()

root.mainloop()