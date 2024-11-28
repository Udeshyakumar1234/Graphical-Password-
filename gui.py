
#im not even sure how this much
import sqlite3
from pathlib import Path
from io import BytesIO
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import PIL.Image
import image_mod
import Insert

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\IS_LAB\IS_Project\New folder\build\assets\frame0")
 
#signing in fucntion
def sign_in():
    userid = entry_1.get()  
    
    conn = sqlite3.connect('users.db') 
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            userid TEXT PRIMARY KEY,
            password TEXT,
            Images TEXT
        )
    ''')
    # Query the database to check if the userid exists
    c.execute('''SELECT Images,password FROM Users WHERE userid=?''', (userid,))
    result = c.fetchone()
    conn.close()
    

    if result: 
        img = PIL.Image.open(BytesIO(result[0]))
        password=str(image_mod.GetPassword(window,img))
        
        if result[1]==password:
            messagebox.showinfo("DashBoard","Welcome!")
        else:
            messagebox.showerror("Incorrect", "Incorrect segment, Please Try again")
        
        
        
    else:
        messagebox.showerror("Error", "User not found, Please SignUp")  # Show error if user not found

    conn.close()

def sign_up(window):
    from gui2 import create_signup_window
    create_signup_window(window)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("650x620")
window.title("Login Page")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 620,
    width = 650,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    473.0,
    40.0,
    image=image_image_1
)

canvas.create_text(
    293.0,
    153.0,
    anchor="nw",
    text="Username",
    fill="#5F73E7",
    font=("Inter ExtraBoldItalic", 20 * -1)
)

canvas.create_rectangle(
    370.0,
    263.0,
    539.0,
    310.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    462.0,
    209.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#B9BDD7",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=309.0,
    y=187.0,
    width=306.0,
    height=42.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
SignIn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=sign_in,
    relief="flat"
)
SignIn.place(
    x=370.0,
    y=265.0,
    width=169.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
#Sign Up
SignUp = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:sign_up(window),
    relief="flat"
)
SignUp.place(
    x=370.0,
    y=477.0,
    width=169.0,
    height=45.0
)

canvas.create_text(
    376.0,
    459.0,
    anchor="nw",
    text="First time ? Join Now!!",
    fill="#000000",
    font=("Inter ExtraBoldItalic", 15 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    143.0,
    310.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
