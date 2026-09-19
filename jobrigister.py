# STEP 1: Import libraries
import tkinter as tk

# STEP 2: Create main window
root = tk.Tk()

# STEP 3: Set window title
root.title("Job Registration Form")

# STEP 4: Set window size
root.geometry("800x900")


# STEP 5: Create Canvas
canvas = tk.Canvas(root)

# STEP 6: Create Scrollbar
scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview
)

# STEP 7: Create Frame inside Canvas
form_frame = tk.Frame(canvas)

# STEP 8: Configure Canvas scrolling
form_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=form_frame,
    anchor="nw"
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

# Put Canvas and Scrollbar in window
canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# STEP 9: Add heading
tk.Label(
    form_frame,
    text="JOB REGISTRATION FORM",
    font=("Arial", 20, "bold")
).pack(pady=20)


# STEP 10: Name
tk.Label(form_frame, text="Full Name").pack()
name = tk.Entry(form_frame, width=40)
name.pack(pady=5)


# STEP 11: Email
tk.Label(form_frame, text="Email").pack()
email = tk.Entry(form_frame, width=40)
email.pack(pady=5)


# STEP 12: Phone
tk.Label(form_frame, text="Phone Number").pack()
phone = tk.Entry(form_frame, width=40)
phone.pack(pady=5)


# STEP 13: Address
tk.Label(form_frame, text="Address").pack()
address = tk.Entry(form_frame, width=40)
address.pack(pady=5)


# STEP 14: Gender
tk.Label(form_frame, text="Gender").pack()

gender = tk.StringVar(value="Male")

tk.Radiobutton(
    form_frame,
    text="Male",
    variable=gender,
    value="Male"
).pack()

tk.Radiobutton(
    form_frame,
    text="Female",
    variable=gender,
    value="Female"
).pack()


# STEP 15: Job Position
tk.Label(
    form_frame,
    text="Job Position"
).pack(pady=5)

job_position = tk.StringVar(
    value="Software Developer"
)

jobs = [
    "Software Developer",
    "Web Developer",
    "Graphic Designer",
    "Accountant"
]

tk.OptionMenu(
    form_frame,
    job_position,
    *jobs
).pack()


# STEP 16: Education
tk.Label(
    form_frame,
    text="Education"
).pack(pady=5)

education = tk.Entry(
    form_frame,
    width=40
)
education.pack(pady=5)


# STEP 17: Company Name
tk.Label(
    form_frame,
    text="Company Name"
).pack()

company = tk.Entry(
    form_frame,
    width=45
)
company.pack(pady=4)


# STEP 18: Job Name
tk.Label(
    form_frame,
    text="Job Name"
).pack()

job = tk.Entry(
    form_frame,
    width=45
)
job.pack(pady=4)


# STEP 19: Applicant Name
tk.Label(
    form_frame,
    text="Applicant Name"
).pack()

applicant_name = tk.Entry(
    form_frame,
    width=45
)
applicant_name.pack(pady=4)


# STEP 20: Email
tk.Label(
    form_frame,
    text="Email"
).pack()

applicant_email = tk.Entry(
    form_frame,
    width=45
)
applicant_email.pack(pady=4)


# STEP 21: Phone Number
tk.Label(
    form_frame,
    text="Phone Number"
).pack()

applicant_phone = tk.Entry(
    form_frame,
    width=45
)
applicant_phone.pack(pady=4)


# STEP 22: Qualification
tk.Label(
    form_frame,
    text="Qualification"
).pack()

qualification = tk.Entry(
    form_frame,
    width=45
)
qualification.pack(pady=4)


# STEP 23: Experience
tk.Label(
    form_frame,
    text="Work Experience"
).pack()

experience = tk.Entry(
    form_frame,
    width=45
)
experience.pack(pady=4)


# STEP 24: Communication Skills
tk.Label(
    form_frame,
    text="Communication Skills"
).pack()

communication = tk.StringVar(
    value="Good"
)

tk.Radiobutton(
    form_frame,
    text="Excellent",
    variable=communication,
    value="Excellent"
).pack()

tk.Radiobutton(
    form_frame,
    text="Good",
    variable=communication,
    value="Good"
).pack()

tk.Radiobutton(
    form_frame,
    text="Average",
    variable=communication,
    value="Average"
).pack()


# STEP 25: Other Job Requirements
tk.Label(
    form_frame,
    text="Other Skills / Requirements"
).pack()

other = tk.Entry(
    form_frame,
    width=45
)
other.pack(pady=4)


# STEP 26: Register Function
def register():

    if (
        company.get() == "" or
        job.get() == "" or
        applicant_name.get() == "" or
        applicant_email.get() == "" or
        applicant_phone.get() == ""
    ):

        messagebox.showwarning(
            "Warning",
            "Please fill all required fields!"
        )

    else:

        messagebox.showinfo(
            "Registration",
            "Job Registration Successful!"
        )


# STEP 27: Register Button
tk.Button(
    form_frame,
    text="REGISTER",
    command=register,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=15)


# STEP 28: Run program
root.mainloop()



