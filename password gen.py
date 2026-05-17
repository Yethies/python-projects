
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(0,10)) ]
    password_symbols = [choice(symbols) for _ in range(randint(2,4)) ]
    password_numbers = [choice(numbers) for _ in range(randint(2,4)) ]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password = "".join(password_list)
    p_entry.insert(0,password)
    pyperclip.copy(password)

def save():
    website=w_entry.get()
    email=e_entry.get()
    password = p_entry.get()

    new_data={
        website:{
        "email":email,
        "password":password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="Every field is important.")
    else:
        try:
            with open("data.json","r") as df:
                data= json.load(df)
        except FileNotFoundError:
            with open("data.json","w") as df:
                json.dump(new_data,df,indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as df:
                json.dump(data, df,indent=4)
        finally:
                w_entry.delete(0,END)
                p_entry.delete(0,END)
def find_password():
    website = w_entry.get()
    try:
        with open("data.json") as df:
            data= json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
            if website in data:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password}")
            else:
                messagebox.showinfo(title="Error",message=f"NO details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200, height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.pack()
canvas.grid(row=0,column=1)

w_label=Label(text="Website:",)
w_label.grid(row=1,column=0)

e_label=Label(text="Email/Username:")
e_label.grid(row=2,column=0)

p_label=Label(text="Password:")
p_label.grid(row=3,column=0)


w_entry=Entry(width=35)
w_entry.grid(row=1,column=1)
w_entry.focus()

e_entry=Entry(width=35)
e_entry.grid(row=2,column=1)
e_entry.insert(0,"yet@gmail.com")

p_entry=Entry(width=33)
p_entry.grid(row=3,column=1)

gp_bt=Button(text="Generate Password",command=generate_password)
gp_bt.grid(row=3,column=2)


ad_bt=Button(text="Add",width=36,command=save)
ad_bt.grid(row=4,column=1,columnspan=2)

s_bt=Button(text="Search",command=find_password)
s_bt.grid(row=1,column=2)
window.mainloop()
