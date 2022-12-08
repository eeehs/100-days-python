from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    if password_input.get():
        password_input.delete(0,'end')
        password_input.insert(0, password)
    else:
        password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
# def website_contend_get():
#     text1 = Website_input.get()
#     return f"{text} |"

# def email_contend_get():
#     text2 = email_user_input.get()
#     return f"{text} |"

# def password_contend_get():
#     text3 = password_input.get()
#     return f"{text}"

def add():
    
    website = Website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    
    
    if website == "" or email =="" or password== "":
        messagebox.showerror(title="Error",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_029\\data.txt","a") as file:
                content = f"{website} | {email} | {password} \n"
                file.write(content)
            Website_input.delete(0,'end')
            password_input.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_029\\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#Label
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entry
Website_input = Entry(width=35)
Website_input.grid(row=1,column=1,columnspan=2)
Website_input.focus()

email_user_input = Entry(width=35)
email_user_input.grid(row=2,column=1,columnspan=2)
email_user_input.insert(0, "dlrb98&@naver.com")

password_input = Entry(width=35)
password_input.grid(row=3,column=1,columnspan=2)

# Button
generate_button = Button(text="Generate Password",width=35,command=generate_password)
generate_button.grid(row=4,column=1,columnspan=2)

add_button = Button(text="Add",width=35,command=add)
add_button.grid(column=1,row=5,columnspan=2)
root.mainloop()