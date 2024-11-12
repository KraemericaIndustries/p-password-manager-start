from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list) # Use the JOIN method of the string type, to iterate over the list called password_list, and concatenate each entry in the list to an initially empty string
    password_entry.insert(0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        with open("data.json", mode="r") as data_file:
            # Reading existing data
            data = json.load(data_file)
            # Updating existing data with new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website Entry
website_entry = Entry(width=35)
website_entry.focus() # <- Places the cursor in this widget
#Add some text to begin with
#Gets text in entry
print(website_entry.get())
website_entry.grid(column=1, row=1, columnspan=2)

# Email Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

#Email Entry
email_entry = Entry(width=35)
#Add some text to begin with
email_entry.insert(0, string="bob.kraemer.android@gmail.com")
#Gets text in entry
print(email_entry.get())
email_entry.grid(column=1, row=2, columnspan=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password Entry
password_entry = Entry(width=21)
#Add some text to begin with
#Gets text in entry
print(password_entry.get())
password_entry.grid(column=1, row=3)

# Generate Password Button
def action():
    print("Do something")

#calls action() when pressed
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, columnspan=2)

#Add Button
def action():
    print("Do something")

#calls action() when pressed
add_button = Button(text="Add", command=save, width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()