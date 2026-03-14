import customtkinter as ctk
import string
import random

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Window
window = ctk.CTk()
window.title("Password Security Analyzer")
window.geometry("560x560")
window.resizable(True, True)
window.grid_columnconfigure(0, weight=1)

# Functions

def copy_password():
    password = password_entry.get()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()

        status_label.configure(text="Password copied to clipboard!")

def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        show_button.configure(text="🙈")
    else:
        password_entry.configure(show="*")
        show_button.configure(text="👁")

def generate_password():

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(12))

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    analyze_password()

def analyze_password():

    password = password_entry.get()

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("• Password should be at least 8 characters")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("• Add uppercase letters")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("• Add numbers")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("• Add special characters")

    # Strength logic
    if score <= 1:
        strength = "Weak"
        color = "red"
        strength_bar.set(0.3)

    elif score <= 3:
        strength = "Medium"
        color = "orange"
        strength_bar.set(0.6)

    else:
        strength = "Strong"
        color = "green"
        strength_bar.set(1)

    result_label.configure(
        text=f"Strength: {strength}",
        text_color=color
    )

    if suggestions:
        suggestions_label.configure(
            text="Suggestions:\n" + "\n".join(suggestions)
        )
    else:
        suggestions_label.configure(
            text="Great password! No suggestions."
        )

# UI

# Title
title = ctk.CTkLabel(
    window,
    text="Password Security Analyzer",
    font=("Segoe UI", 26, "bold")
)
title.grid(row=0, column=0, pady=(40, 10))

# Subtitle (premium touch)
subtitle = ctk.CTkLabel(
    window,
    text="Analyze and generate secure passwords",
    font=("Segoe UI", 13),
    text_color=("gray70", "gray60")
)
subtitle.grid(row=1, column=0, pady=(0,30))

# Password label
password_label = ctk.CTkLabel(
    window,
    text="Enter Password",
    font=("Segoe UI", 14)
)
password_label.grid(row=2, column=0, pady=(0,5))

# Password frame
password_frame = ctk.CTkFrame(window, fg_color="transparent")
password_frame.grid(
    row=3,
    column=0,
    padx=50,
    pady=(0,25),
    sticky="ew"
)
password_frame.grid_columnconfigure(0, weight=1)

# Password entry
password_entry = ctk.CTkEntry(
    password_frame,
    show="*",
    font=("Segoe UI", 14),
    height=36
)
password_entry.grid(row=0, column=0, sticky="ew")

# Show button
show_button = ctk.CTkButton(
    password_frame,
    text="👁",
    width=40,
    command=toggle_password
)
show_button.grid(row=0, column=1, padx=6)

password_entry.bind("<Return>", lambda event: analyze_password())
password_entry.bind(
    "<Key>",
    lambda event: status_label.configure(text="")
)

# Buttons
button_frame = ctk.CTkFrame(window, fg_color="transparent")
button_frame.grid(row=4, column=0, pady=(0,30))

analyze_button = ctk.CTkButton(
    button_frame,
    text="Analyze Password",
    command=analyze_password,
    font=("Segoe UI", 13)
)
analyze_button.grid(row=0, column=0, padx=6)

generate_button = ctk.CTkButton(
    button_frame,
    text="Generate Secure Password",
    command=generate_password,
    font=("Segoe UI", 13)
)
generate_button.grid(row=0, column=1, padx=6)

copy_button = ctk.CTkButton(
    button_frame,
    text="Copy Password",
    command=copy_password,
    font=("Segoe UI", 13)
)
copy_button.grid(row=0, column=2, padx=6)

# Result
result_label = ctk.CTkLabel(
    window,
    text="Strength:",
    font=("Segoe UI", 16, "bold")
)
result_label.grid(row=5, column=0, pady=(0,8))

# Strength bar
strength_bar = ctk.CTkProgressBar(window, width=320)
strength_bar.set(0)
strength_bar.grid(row=6, column=0, pady=(0,25))

# Suggestions
suggestions_label = ctk.CTkLabel(
    window,
    text="",
    font=("Segoe UI", 13),
    justify="center"
)
suggestions_label.grid(row=7, column=0, pady=(0,20))

# Status
status_label = ctk.CTkLabel(
    window,
    text="",
    font=("Segoe UI", 12),
    text_color="green"
)
status_label.grid(row=8, column=0)

# Run
window.mainloop()