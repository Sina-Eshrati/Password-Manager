from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(website, f"ID: {data[website]['ID']}\nPassword: {data[website]['Password']}")
    except FileNotFoundError:
        messagebox.showwarning("Oops!", "No Data File Founded")
    except KeyError:
        messagebox.showwarning("Oops!", "No details for the website exists")
    finally:
        input_website.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get().title()
    id = input_ID.get()
    password = input_password.get()
    new_data = {
        website: {
            "ID": id,
            "Password": password
        }
    }
    if website and password and id:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        input_website.delete(0, END)
        input_password.delete(0, END)
    else:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", pady=5, font=("Arial", 9, "bold"), fg="#374045")
label_website.grid(row=1, column=0)

label_ID = Label(text="Email/Username:", pady=5, font=("Arial", 9, "bold"), fg="#374045")
label_ID.grid(row=2, column=0)

label_password = Label(text="Password:", pady=10, font=("Arial", 9, "bold"), fg="#374045")
label_password.grid(row=3, column=0)

input_website = Entry(width=32, bd=0)
input_website.focus()
input_website.grid(row=1, column=1)

input_ID = Entry(width=50, bd=0)
input_ID.insert(0, "sina_eshrati@yahoo.com")
input_ID.grid(row=2, column=1, columnspan=2)

input_password = Entry(width=32, bd=0)
input_password.grid(row=3, column=1)

btn_search = Button(text="Search", width=16, bg="#f05945", fg="white", bd=0, font=("Arial", 9, "bold"),
                    command=find_password)
btn_search.grid(row=1, column=2)

btn_gen_pass = Button(text="Generate Password", bg="#f05945", fg="white", bd=0, font=("Arial", 9, "bold"),
                      command=generate_password)
btn_gen_pass.grid(row=3, column=2)

btn_add = Button(text="Add", width=44, bg="#f05945", fg="white", bd=0, font=("Arial", 9, "bold"), command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
