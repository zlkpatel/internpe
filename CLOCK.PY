import tkinter as tk
from tkinter import ttk
from time import strftime

# Function to update both time and date
def update_clock():
    time_string = strftime('%I:%M:%S %p')  # 12-hour format
    date_string = strftime('%A, %d %B %Y')  # Full weekday, day, full month, year
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    root.after(1000, update_clock)  # Update every 1 second

# Create main window
root = tk.Tk()
root.title("Modern Digital Clock")
root.geometry("600x250")
root.configure(bg="#1e1e2e")

# Apply ttk style
style = ttk.Style(root)
style.configure('TLabel', background='#1e1e2e', foreground='#f8f8f2', font=('Helvetica', 28, 'bold'))

# Time label
time_label = ttk.Label(root, font=('DS-Digital', 60), anchor='center', style='TLabel')
time_label.pack(pady=20)

# Date label
date_label = ttk.Label(root, font=('Helvetica', 24), anchor='center', style='TLabel')
date_label.pack(pady=10)

# Start updating
update_clock()

# Start the GUI event loop
root.mainloop()
