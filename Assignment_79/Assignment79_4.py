"""
4: Voting Eligibility Checker

Develop a Tkinter application that accepts a person's name and age. Provide a Check Eligibility button to determine whether the person is eligible to vote based ont minimum age of 18 years. 
"""


import tkinter as tk

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("350x300")

# Center the window
width = 380
height = 280
x = (root.winfo_screenwidth() - width) // 2
y = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

# Title
tk.Label(root, text="🗳️ Voting Eligibility Checker",
         font=("Arial", 14, "bold")).pack(pady=15)

# Name input
tk.Label(root, text="Enter Your Name:").pack()
name = tk.Entry(root)
name.pack(pady=5)

# Age input
tk.Label(root, text="Enter Your Age:").pack()
age = tk.Entry(root)
age.pack(pady=5)

# Function to check eligibility
def check():
    person_name = name.get()
    person_age = int(age.get())

    if person_age >= 18:
        result.config(text=f"✅ {person_name} is Eligible to Vote",
                      fg="green")
    else:
        result.config(text=f"❌ {person_name} is Not Eligible to Vote",
                      fg="red")

# Button
tk.Button(root, text="Check Eligibility",
          command=check).pack(pady=12)

# Result label
result = tk.Label(root, text="", font=("Arial", 10, "bold"))
result.pack(pady=5)

root.mainloop()