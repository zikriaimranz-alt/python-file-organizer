
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Admission")
root.geometry("400x350")

fields = ["Student ID", "Name", "Father Name", "Class", "Phone"]
boxes = []

for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i, column=0, pady=5)
    box = tk.Entry(root)
    box.grid(row=i, column=1)
    boxes.append(box)

def submit():
    if boxes[0].get() == "" or boxes[1].get() == "":
        messagebox.showwarning("Warning", "Fill ID and Name")
    else:
        messagebox.showinfo("Success", "Admission Saved")

tk.Button(root, text="Submit", command=submit).grid(
    row=5, column=0, columnspan=2, pady=15
)

root.mainloop()

