from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list2 = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list3 = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_list3 + password_list2 + password_list1

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message='Please do not leave any fields empty')

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'This are the details you entered: \nEmail: {email} \n'
                                                              f'Password: {password} \nIs it okay to save?')
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{website} | {email} | {password}\n')
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

my_image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
email_text = Label(text='Email/Username:')
email_text.grid(row=2, column=0)
password_text = Label(text='Password:')
password_text.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky='EW')
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky='EW')
password_input = Entry(width=20)
password_input.grid(row=3, column=1, columnspan=1, sticky='EW')

# Buttons
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, sticky='EW')
add_button = Button(text='Add', width=30, command=write_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
