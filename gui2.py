from tkinter import Toplevel, Canvas, Entry, Button, PhotoImage, filedialog, StringVar, messagebox
from PIL import Image
import sqlite3
from io import BytesIO
import image_mod
from pathlib import Path

ASSETS_PATH = Path(r"E:\IS_LAB\IS_Project\New folder\build\asset\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_signup_window(main_window):
    win = Toplevel(main_window)
    win.geometry("522x400")
    win.configure(bg="#FFFFFF")
    win.title("SignUp")

    canvas = Canvas(
        win,
        bg="#FFFFFF",
        height=400,
        width=522,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Store images as instance variables to prevent garbage collection
    win.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(260.0, 36.0, image=win.image_image_1)

    # Username label and entry field
    canvas.create_text(
        13.0,
        106.0,
        anchor="nw",
        text="Enter a Username",
        fill="#1208C4",
        font=("Inter Medium", 15 * -1)
    )

    win.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(111.0, 145.5, image=win.entry_image_1)
    username_var = StringVar()
    entry_1 = Entry(
        win,
        textvariable=username_var,
        bd=0,
        bg="#D9F3F2",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(x=28.5, y=127.0, width=165.0, height=35.0)
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        367.0,
        190.0,
        image=image_image_2
    )
    win.image_2 = image_image_2
    # Label for selecting a password picture
    canvas.create_text(
        13.0,
        186.0,
        anchor="nw",
        text="Pick a Password Picture",
        fill="#1208C4",
        font=("Inter Medium", 15 * -1)
    )

    # Variable to hold the image path
    image_path_var = StringVar()

    # Function to select an image file
    def select_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image_path_var.set(file_path)  # Store the image path

    # Button for selecting an image
    win.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    select_button = Button(
        win,
        image=win.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=select_image,
        relief="flat"
    )
    select_button.place(x=13.0, y=213.0, width=162.0, height=34.0)

    # Function to save the data
    def save_data():
        username = username_var.get()
        image_path = image_path_var.get()

        if username and image_path:
            try:
                img = Image.open(image_path)
                password = image_mod.GetPassword(main_window, img)
                img_byte_arr = BytesIO()
                img.save(img_byte_arr, format=img.format)
                img_data = img_byte_arr.getvalue()

                conn = sqlite3.connect('users.db')
                c = conn.cursor()
                c.execute('''
                    CREATE TABLE IF NOT EXISTS Users (
                        userid TEXT PRIMARY KEY,
                        password TEXT,
                        Images BLOB
                    )
                ''')
                c.execute("INSERT INTO Users (userid, password, Images) VALUES (?, ?, ?)", (username, password, sqlite3.Binary(img_data)))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User data saved successfully!")
                win.destroy()  # Close the window
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Please enter a username and select an image.")

    # Save button
    save_button = Button(
        win,
        text="Save",
        command=save_data
    )
    save_button.place(x=200, y=270, width=100, height=30)

    win.resizable(False, False)
    return win
