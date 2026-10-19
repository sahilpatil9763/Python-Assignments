"""
2: Find the largest Number

Develop a Tkinter application that accepts three numbers from the user. Provide a Find Maximum button to 
determine and display the largest number.
"""


import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Find Maximum")
root.geometry("380x350")

# Center the window
width = 380
height = 350
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

# Title
tk.Label(root, text="🔢 Find Largest Number", font=("Arial", 16, "bold")).pack(pady=15)

# Input fields
tk.Label(root, text="Enter First Number").pack()
n1 = tk.Entry(root)
n1.pack()

tk.Label(root, text="Enter Second Number").pack()
n2 = tk.Entry(root)
n2.pack()

tk.Label(root, text="Enter Third Number").pack()
n3 = tk.Entry(root)
n3.pack()

# Function to find largest number
def find_max():
    a = float(n1.get())
    b = float(n2.get())
    c = float(n3.get())

    result.config(text=f"Largest Number: {max(a, b, c)}")

# Button
tk.Button(root, text="Find Maximum", command=find_max).pack(pady=10)

# Result
result = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
result.pack()

root.mainloop()