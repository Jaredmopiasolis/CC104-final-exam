# Password Generator
import random
from tkinter import *
import json
from tkinter import messagebox
import pyperclip
from PIL import Image, ImageTk
from playsound import playsound
FONT = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    # Initialize a flag to track if field of letters, digits, and symbols is empty
    fields_empty = False

    # Check if the input fields for letters, digits, and symbols are filled
    if not input_letter.get():
        input_letter.config(bg="pink")  # Change background to pink if empty
        fields_empty = True
    else:
        input_letter.config(bg="white")  # Reset to default color if filled

    if not input_digits.get():
        input_digits.config(bg="pink")
        fields_empty = True
    else:
        input_digits.config(bg="white")

    if not input_symbols.get():
        input_symbols.config(bg="pink")
        fields_empty = True
    else:
        input_symbols.config(bg="white")

        # If letters, digits and symbols field is empty, show a warning message
    if fields_empty:
        playsound('warning.mp3', block=False)
        messagebox.showwarning("Warning", "Please fill the letters, digits, and symbols fields.")
        return  # Exit the function if any field is empty

    letters = int(input_letter.get()) if input_letter.get().isdigit() else 0
    digits = int(input_digits.get()) if input_digits.get().isdigit() else 0
    symbols = int(input_symbols.get()) if input_symbols.get().isdigit() else 0

    password_characters = (
        random.choices([chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)], k=letters) +
        random.choices([str(i) for i in range(10)], k=digits) +
        random.choices(['!', '#', '$', '%', '&', '(', ')', '*', '+'], k=symbols)
    )

    random.shuffle(password_characters)

    password = "".join(password_characters)

    input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    username = input_username.get()
    password = input_pass.get()

    # Check if any of the fields are empty
    if not website:
        input_website.config(bg="pink")  # Change background to red
    else:
        input_website.config(bg="white")  # Reset to default color

    if not username:
        input_username.config(bg="pink")
    else:
        input_username.config(bg="white")

    if not password:
        input_pass.config(bg="pink")
        input_letter.config(bg="pink")
        input_digits.config(bg="pink")
        input_symbols.config(bg="pink")
    else:
        input_pass.config(bg="white")
        input_letter.config(bg="white")
        input_digits.config(bg="white")
        input_symbols.config(bg="white")


    if not website or not username or not password:
        playsound('warning.mp3', block=False)
        messagebox.showwarning("Warning", "Please fill blank fields.")
        return

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}
    # Check if the username and website already exist
    if website in data and data[website]["username"] == username:
        playsound('warning.mp3', block=False)
        messagebox.showwarning("Warning", "Username and website already exist. Please use the 'Change Password' button to update the password.")
        return

    data.update(new_data)

    playsound('success.mp3', block=False)
    messagebox.showinfo("Success", f"Password for '{website}' has been saved.")

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    input_website.delete(0, END)
    input_username.delete(0, END)
    input_letter.delete(0, END)
    input_digits.delete(0, END)
    input_symbols.delete(0, END)
    input_pass.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]

                input_username.delete(0, END)  # Clear the username field
                input_username.insert(0, username)  # Insert the found username

                playsound('success.mp3', block=False)
                messagebox.showinfo("Password Found", f"Username: {username}\nPassword: {password}")
                pyperclip.copy(password)
            else:
                playsound('warning.mp3', block=False)
                messagebox.showerror("Error", f"No details for the website '{website}' found.")
    except FileNotFoundError:
        playsound('warning.mp3', block=False)
        messagebox.showerror("Error", "No json file found.")

# ---------------------------- CHANGE PASSWORD ------------------------------- #
def change_password():
    website = input_website.get()
    new_password = input_pass.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:

                data[website]["password"] = new_password  # Update the password

                with open("data.json", "w") as Data_file:
                    json.dump(data, Data_file, indent=4)

                playsound('success.mp3', block=False)
                messagebox.showinfo("Success", f"Password for '{website}' has been updated.")
                input_pass.delete(0, END)  # Clear the password field
                input_website.delete(0, END)
                input_username.delete(0, END)
                input_letter.delete(0, END)
                input_digits.delete(0, END)
                input_symbols.delete(0, END)
    except FileNotFoundError:
        playsound('warning.mp3', block=False)
        messagebox.showerror("Error", "No json file found.")

def manual_button():
    # Create a new window for the manual
    manual_window = Toplevel(window)
    manual_window.title("Manual")
    manual_window.geometry("400x300")  # Set the size of the manual window

    # Create a Text widget for instructions
    instructions = Text(manual_window, wrap='word', padx=10, pady=10)
    instructions.pack(expand=True, fill='both')

    # Add instructions to the Text widget
    instructions.insert('1.0', "---------------PASSWORD MANAGER---------------\n")
    instructions.insert('3.0', "The password manager is the best way to create complex passwords, as it will create a unique password for you every time.Our password manager allows you to create strong, random passwords with one click to boost your online security.\n\n")
    instructions.insert('6.0', "---------Password Manager Instructions--------\n")
    instructions.insert('7.0', "1. Generate Password:\n")
    instructions.insert('8.0', "   - Enter the number of letters, digits, and symbols you want and click 'Generate Password' to create a secure password.\n\n")

    instructions.insert('10.0', "2. Save Password:\n")
    instructions.insert('11.0', "   - Fill in the website, username, and generated password fields and click 'Add' to save your credentials.\n\n")

    instructions.insert('13.0', "3. Find Password:\n")
    instructions.insert('14.0',"   - Enter the website name and click 'Search' to retrieve your saved username and password.\n\n")

    instructions.insert('16.0', "4. Change Password:\n")
    instructions.insert('17.0', "   - If you need to update your password, enter the website and new password and click 'Change Password' to update it.\n\n")

    instructions.insert('19.0', "5. Manual:\n")
    instructions.insert('20.0', "   - Click the manual button to view these instructions.\n\n")

    instructions.insert('22.0', "Note: Ensure you save your passwords securely and do not share them with others.\n\n")

    instructions.insert('24.0', "----------------DEVELOPERS---------------\n")
    instructions.insert('25.0', "Mark Jared M. Solis  - Data structure\n")
    instructions.insert('26.0', "Hershey Jane Almero - GUI\n")
    instructions.insert('27.0', "Lynnell Ainsley A. Rembulat - Find Password and Sound\n")
    instructions.insert('28.0', "Justine D. Adolfo - Find Password and Manual\n")

    # Make the Text widget read-only
    instructions.config(state='disabled')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=10, pady=10)
window.title("Password Manager")

# Create a canvas for the logo
canvas = Canvas(window, width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(rowspan=8, column=0)

#Manual logo
manual_image = Image.open("manual.png")
resized_image = manual_image.resize((30, 30))  # Resize to 30x30
logo_image = ImageTk.PhotoImage(resized_image)  # Corrected line


# Labels
label_website = Label(window, text="Website:")
label_website.grid(row=1, column=1)
label_username = Label(window, text="Email/Username:")
label_username.grid(row=2, column=1)
label_letter = Label(window, text="Letters")
label_letter.grid(row=3, column=1)
label_digits = Label(window, text="Digits:")
label_digits.grid(row=4, column=1)
label_symbols = Label(window, text="Symbols:")
label_symbols.grid(row=5, column=1)
label_pass = Label(window, text="Password:")
label_pass.grid(row=6, column=1)

# Entries
input_website = Entry(window, width=33)
input_website.grid(row=1, column=2)
input_website.focus()
input_username = Entry(window, width=33)
input_username.grid(row=2, column=2)
input_letter = Entry(window, width=10)
input_letter.grid(row=3, column=2, sticky=W)
input_digits = Entry(window, width=10)
input_digits.grid(row=4, column=2, sticky=W)
input_symbols = Entry(window, width=10)
input_symbols.grid(row=5, column=2, sticky=W)
input_pass = Entry(window, width=33)
input_pass.grid(row=6, column=2)

# Buttons
button_search = Button(window, text="Search", highlightthickness=0, command=find_password, width=15)
button_search.grid(row=1, column=3)
button_generate = Button(window, text="Generate Password", highlightthickness=0, command=generate)
button_generate.grid(row=6, column=3)
button_add = Button(window, text="Add", width=43, command=save)
button_add.grid(row=7, column=2, columnspan=2)
button_change = Button(window, text="Change Password", width=43, command=change_password)
button_change.grid(row=8, column=2, columnspan=2)
button_manual = Button(window, image= logo_image, compound=LEFT, command=manual_button)
button_manual.grid(row=0, column=0, sticky=W)

button_manual.image = logo_image
# Start the main loop
window.mainloop()