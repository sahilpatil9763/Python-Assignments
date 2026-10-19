"""
3: Area of Circle

Develop a Tkinter application that accepts the radius of a circle. Provide a Calculate Area button to calculate and display the area of circle.
"""


import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Area of Circle")
root.geometry("350x250")

# Center the window
width = 350
height = 250
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

# Title
tk.Label(root, text="⭕ Area of Circle",
         font=("Arial", 16, "bold")).pack(pady=15)

# Radius input
tk.Label(root, text="Enter Radius:").pack()
radius = tk.Entry(root)
radius.pack(pady=5)

# Function to calculate area
def calculate():
    r = float(radius.get())
    area = math.pi * r * r
    result.config(text=f"Area: {area:.2f}")

# Calculate button
tk.Button(root, text="Calculate Area", command=calculate).pack(pady=10)

# Result label
result = tk.Label(root, text="Result will appear here", font=("Arial", 12, "bold"), fg="green")
result.pack(pady=5)

root.mainloop()