import tkinter as tk
from tkinter import messagebox
import secrets
import string


# ================= PASSWORD GENERATOR =================

def generate_password():

    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Invalid Length",
                "Password ki length kam se kam 4 honi chahiye."
            )
            return

        characters = ""

        # Uppercase
        if uppercase_var.get():
            characters += string.ascii_uppercase

        # Lowercase
        if lowercase_var.get():
            characters += string.ascii_lowercase

        # Numbers
        if numbers_var.get():
            characters += string.digits

        # Special Characters
        if symbols_var.get():
            characters += string.punctuation

        # Agar koi option select nahi hai
        if characters == "":
            messagebox.showwarning(
                "Character Selection",
                "Kam se kam ek character type select karo."
            )
            return

        # Generate password
        password = ""

        for i in range(length):
            password += secrets.choice(characters)

        # Password box clear
        password_entry.delete(0, tk.END)

        # Password insert
        password_entry.insert(0, password)

        # Strength check
        check_strength(password)

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Password length me sirf number enter karo."
        )


# ================= PASSWORD STRENGTH =================

def check_strength(password=None):

    if password is None:
        password = password_entry.get()

    if password == "":
        strength_label.config(
            text="Strength: -",
            fg="white"
        )
        return

    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    # Uppercase
    if any(character.isupper() for character in password):
        score += 1

    # Lowercase
    if any(character.islower() for character in password):
        score += 1

    # Number
    if any(character.isdigit() for character in password):
        score += 1

    # Special character
    if any(character in string.punctuation for character in password):
        score += 1

    # Strength result
    if score <= 2:

        strength_label.config(
            text="Strength: Weak",
            fg="red"
        )

    elif score == 3 or score == 4:

        strength_label.config(
            text="Strength: Medium",
            fg="orange"
        )

    else:

        strength_label.config(
            text="Strength: Strong",
            fg="lime"
        )


# ================= COPY PASSWORD =================

def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Pehle password generate karo."
        )
        return

    root.clipboard_clear()

    root.clipboard_append(password)

    root.update()

    messagebox.showinfo(
        "Password Copied",
        "Password clipboard me copy ho gaya."
    )


# ================= CLEAR PASSWORD =================

def clear_password():

    password_entry.delete(0, tk.END)

    strength_label.config(
        text="Strength: -",
        fg="white"
    )


# ================= SHOW PASSWORD =================

def show_password():

    if show_var.get():

        password_entry.config(
            show=""
        )

    else:

        password_entry.config(
            show="*"
        )


# ================= MAIN WINDOW =================

root = tk.Tk()

root.title("Cyber Password Generator")

root.geometry("600x650")

root.resizable(False, False)

root.configure(
    bg="black"
)


# ================= TITLE =================

title_label = tk.Label(
    root,
    text="CYBER PASSWORD GENERATOR",
    font=("Arial", 23, "bold"),
    bg="black",
    fg="lime"
)

title_label.pack(
    pady=(30, 5)
)


# ================= SUBTITLE =================

subtitle_label = tk.Label(
    root,
    text="Generate a Strong & Secure Password",
    font=("Arial", 11),
    bg="black",
    fg="white"
)

subtitle_label.pack(
    pady=(0, 25)
)


# ================= PASSWORD FRAME =================

password_frame = tk.Frame(
    root,
    bg="darkblue",
    padx=20,
    pady=20
)

password_frame.pack(
    padx=40,
    fill="x"
)


# ================= PASSWORD LABEL =================

password_label = tk.Label(
    password_frame,
    text="Generated Password",
    font=("Arial", 11, "bold"),
    bg="darkblue",
    fg="white"
)

password_label.pack(
    anchor="w"
)


# ================= PASSWORD ENTRY =================

password_entry = tk.Entry(
    password_frame,
    font=("Consolas", 16),
    bg="black",
    fg="lime",
    insertbackground="white",
    relief="flat",
    show="*"
)

password_entry.pack(
    pady=10,
    fill="x",
    ipady=8
)


# ================= SHOW PASSWORD =================

show_var = tk.BooleanVar()

show_check = tk.Checkbutton(
    password_frame,
    text="Show Password",
    variable=show_var,
    command=show_password,
    bg="darkblue",
    fg="white",
    selectcolor="black",
    activebackground="darkblue",
    activeforeground="white"
)

show_check.pack(
    anchor="w"
)


# ================= STRENGTH =================

strength_label = tk.Label(
    password_frame,
    text="Strength: -",
    font=("Arial", 11, "bold"),
    bg="darkblue",
    fg="white"
)

strength_label.pack(
    anchor="w",
    pady=(10, 0)
)


# ================= LENGTH FRAME =================

length_frame = tk.Frame(
    root,
    bg="black"
)

length_frame.pack(
    pady=20
)


# ================= LENGTH LABEL =================

length_label = tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 11, "bold"),
    bg="black",
    fg="white"
)

length_label.grid(
    row=0,
    column=0,
    padx=10
)


# ================= LENGTH ENTRY =================

length_entry = tk.Entry(
    length_frame,
    width=8,
    font=("Arial", 12),
    justify="center",
    bg="white",
    fg="black"
)

length_entry.insert(
    0,
    "12"
)

length_entry.grid(
    row=0,
    column=1
)


# ================= OPTIONS FRAME =================

options_frame = tk.Frame(
    root,
    bg="black"
)

options_frame.pack()


# ================= VARIABLES =================

uppercase_var = tk.BooleanVar(
    value=True
)

lowercase_var = tk.BooleanVar(
    value=True
)

numbers_var = tk.BooleanVar(
    value=True
)

symbols_var = tk.BooleanVar(
    value=True
)


# ================= UPPERCASE =================

uppercase_check = tk.Checkbutton(
    options_frame,
    text="Uppercase (A-Z)",
    variable=uppercase_var,
    bg="black",
    fg="white",
    selectcolor="darkblue",
    activebackground="black",
    activeforeground="lime"
)

uppercase_check.grid(
    row=0,
    column=0,
    padx=15,
    pady=5
)


# ================= LOWERCASE =================

lowercase_check = tk.Checkbutton(
    options_frame,
    text="Lowercase (a-z)",
    variable=lowercase_var,
    bg="black",
    fg="white",
    selectcolor="darkblue",
    activebackground="black",
    activeforeground="lime"
)

lowercase_check.grid(
    row=0,
    column=1,
    padx=15,
    pady=5
)


# ================= NUMBERS =================

numbers_check = tk.Checkbutton(
    options_frame,
    text="Numbers (0-9)",
    variable=numbers_var,
    bg="black",
    fg="white",
    selectcolor="darkblue",
    activebackground="black",
    activeforeground="lime"
)

numbers_check.grid(
    row=1,
    column=0,
    padx=15,
    pady=5
)


# ================= SPECIAL CHARACTERS =================

symbols_check = tk.Checkbutton(
    options_frame,
    text="Special (!@#$)",
    variable=symbols_var,
    bg="black",
    fg="white",
    selectcolor="darkblue",
    activebackground="black",
    activeforeground="lime"
)

symbols_check.grid(
    row=1,
    column=1,
    padx=15,
    pady=5
)


# ================= BUTTON FRAME =================

button_frame = tk.Frame(
    root,
    bg="black"
)

button_frame.pack(
    pady=25
)


# ================= GENERATE BUTTON =================

generate_button = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 11, "bold"),
    bg="green",
    fg="white",
    activebackground="lime",
    activeforeground="black",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)

generate_button.grid(
    row=0,
    column=0,
    padx=5
)


# ================= COPY BUTTON =================

copy_button = tk.Button(
    button_frame,
    text="Copy",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="blue",
    fg="white",
    activebackground="cyan",
    activeforeground="black",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)

copy_button.grid(
    row=0,
    column=1,
    padx=5
)


# ================= CLEAR BUTTON =================

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_password,
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    activebackground="orange",
    activeforeground="black",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=2,
    padx=5
)


# ================= FOOTER =================

footer_label = tk.Label(
    root,
    text="Cyber Security Project | Python + Tkinter",
    font=("Arial", 9),
    bg="black",
    fg="gray"
)

footer_label.pack(
    side="bottom",
    pady=15
)


# ================= START PROGRAM =================

root.mainloop()