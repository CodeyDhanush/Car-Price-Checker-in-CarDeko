import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load dataset
data = pd.read_csv("car details v4.csv")
data['Make'] = data['Make'].str.strip().str.lower()
data['Model'] = data['Model'].str.strip().str.lower()

# Create GUI window
window = tk.Tk()
window.title("Car Price Checker")
window.geometry("1000x600")
window.configure(bg="black")

# Title
title = tk.Label(window, text="Car Price Checker", font=("Helvetica", 22, "bold"), bg="black", fg="red")
title.pack(pady=15)

# Make Entry
make_label = tk.Label(window, text="Enter Make:", bg="black", fg="white", font=("Helvetica", 13))
make_label.pack()
make_entry = tk.Entry(window, width=50, font=("Helvetica", 12), bg="white", fg="black")
make_entry.pack(pady=5)

# Model Entry
model_label = tk.Label(window, text="Enter Model:", bg="black", fg="white", font=("Helvetica", 13))
model_label.pack()
model_entry = tk.Entry(window, width=50, font=("Helvetica", 12), bg="white", fg="black")
model_entry.pack(pady=5)

# Result Display Frame with Scroll
result_frame = tk.Frame(window, bg="black")
result_frame.pack(pady=20)

x_scroll = tk.Scrollbar(result_frame, orient='horizontal')
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

result_box = tk.Text(result_frame, height=20, width=120, wrap="none", font=("Courier", 10),
                     xscrollcommand=x_scroll.set, bg="black", fg="white")  # Output in white
result_box.pack()

x_scroll.config(command=result_box.xview)

# Search Function
def search_car():
    make = make_entry.get().strip().lower()
    model = model_entry.get().strip().lower()

    if not make or not model:
        messagebox.showwarning("Input Error", "Please enter both Make and Model.")
        return

    filtered = data[(data['Make'] == make) & (data['Model'] == model)]
    result_box.delete("1.0", tk.END)

    if not filtered.empty:
        result_box.insert(tk.END, filtered.to_string(index=False))
    else:
        result_box.insert(tk.END, "❌ No matching car found.")

# Search Button
search_btn = tk.Button(window, text="Search", command=search_car, bg="red", fg="white",
                       font=("Helvetica", 13, "bold"), padx=10, pady=5)
search_btn.pack()

# Run the GUI
window.mainloop()
