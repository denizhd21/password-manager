from tkinter import *
from tkinter import messagebox
import pyperclip
import random
#Generate Section

def generate():
    # Password Generator Project
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)




    passord_letters = [random.choice(letters) for _ in range(nr_letters)]
    passord_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    passord_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = passord_symbols + passord_numbers + passord_letters

    random.shuffle(password_list)

    password = "".join(password_list)


    input_password.insert(0, password)
    pyperclip.copy(password)

    messagebox.showinfo(title="Password has been created", message="Password has been created and copied to the clipboard.")




# Save Section

def add_info():

    if len(input_password.get()) == 0 or len(input_email.get()) == 0 or len(input_website.get()) == 0:
        messagebox.showerror(title="Uh oh", message="You left some fields empty. Please try again.")
    else:
        is_ok = messagebox.askokcancel(title=input_website.get(), message=f"These are the details entered: "
                                                                          f"\n \nEmail: {input_email.get()} "
                                                                          f"\nPassword: {input_password.get()} "
                                                                          f"\n \nDo you want to continue?")
        if is_ok:
            f = open("file.txt", "a")
            f.write(f"{input_website.get()} | {input_email.get()} | {input_password.get()}\n")
            input_website.delete(0, END)
            input_email.delete(0, END)
            input_password.delete(0, END)
            f.close()











# UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)
canvas = Canvas(height=200, width=200)

img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=img)

canvas.grid(row=1, column=2)

website_text = Label(text="Website: ")
email_text = Label(text="Email/Username: ")
passord_text = Label(text="Password: ")
input_website = Entry(width=39)
input_email = Entry(width=39)
input_password = Entry(width=21)
generate_btn = Button(text="Generate Password", width=14, command=generate)
add_btn = Button(text="Add", width=36, command=add_info)
website_text.grid(row=2, column=1)
email_text.grid(row=3, column=1)
passord_text.grid(row=4, column=1)
input_website.grid(row=2, column=2, columnspan=2)
input_email.grid(row=3, column=2, columnspan=2)

input_password.grid(row=4, column=2)
generate_btn.grid(row=4, column=3)
add_btn.grid(row=5, column=2, columnspan=2)
input_website.focus()

window.mainloop()


