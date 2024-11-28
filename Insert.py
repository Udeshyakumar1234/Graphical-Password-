import sqlite3
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from io import BytesIO
import image_mod
def Insertdata(window):
    # Create a new Toplevel window
    win = Toplevel(window)
    win.geometry("400x300")
    win.title("Insert Data")

    # Variable to hold the username and image path
    username_var = StringVar()
    image_path_var = StringVar()

    # Create and place the entry for username
    username_label = Label(win, text="Enter Username:")
    username_label.pack(pady=10)

    username_entry = Entry(win, textvariable=username_var)
    username_entry.pack(pady=10)

    # Function to select an image file
    def select_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image_path_var.set(file_path)  # Store the image path

    # Create and place the button to select an image
    select_button = Button(win, text="Select Image", command=select_image)
    select_button.pack(pady=10)

    # Function to save the data
    def save_data():
        username = username_var.get()
        image_path = image_path_var.get()

        if username and image_path:
            
            img = Image.open(image_path)
            password=image_mod.GetPassword(window,img)
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format=img.format)
            img_data = img_byte_arr.getvalue()

           
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            userid TEXT PRIMARY KEY,
            password TEXT,
            Images TEXT
                     )
            ''')
            c.execute("INSERT INTO Users (userid,password,Images) VALUES (?, ?, ?)", (username, password, sqlite3.Binary(img_data)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User data saved successfully!")
            win.destroy()  # Close the window
        else:
            messagebox.showerror("Error", "Please enter a username and select an image.")

    
    save_button = Button(win, text="Save", command=save_data)
    save_button.pack(pady=10)