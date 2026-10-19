"""
1: Addition of Two Numbers
Develop a Tkinter application that accepts two numbers using Entry widgets. Provide an Add
button to calculate and display their addition using a Label widget.
"""


import tkinter as tk

root = tk.Tk()
root.title("Addition Calculator")

# Center the window
width = 350
height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")

# Application title
tk.Label(root, text="🧮 Addition Calculator",
         font=("Arial", 16, "bold")).pack(pady=15)

# Input fields
tk.Label(root, text="Enter First Number:").pack()
num1 = tk.Entry(root)
num1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack()
num2 = tk.Entry(root)
num2.pack(pady=5)

# Addition function
def add():
    no1 = float(num1.get())
    no2 = float(num2.get())
    result.config(text=f"Result: {no1 + no2}")

# Add button
tk.Button(root, text="Add", command=add, font=("Arial", 12)).pack(pady=10)

# Result label
result = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result.pack(pady=5)

# Run the application
root.mainloop()