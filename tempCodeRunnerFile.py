import sqlite3
from io import BytesIO
from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\IS_LAB\IS_Project\New folder\build\asset\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

    

win= Toplevel(window)
win.geometry("522x400")
win.configure(bg = "#FFFFFF")


    canvas = Canvas(
        win,
        bg = "#FFFFFF",
        height = 400,
        width = 522,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file="asset\frame0\image_1.png")
    image_1 = canvas.create_image(
        260.0,
        36.0,
        image=image_image_1
    )

    canvas.create_text(
        13.0,
        106.0,
        anchor="nw",
        text="Enter a Username",
        fill="#1208C4",
        font=("Inter Medium", 15 * -1)
    )

    canvas.create_text(
        13.0,
        186.0,
        anchor="nw",
        text="Pick a Password Picture",
        fill="#1208C4",
        font=("Inter Medium", 15 * -1)
    )

    canvas.create_rectangle(
        9.0,
        127.0,
        213.0,
        164.0,
        fill="#FFFFFF",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        111.0,
        145.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9F3F2",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=28.5,
        y=127.0,
        width=165.0,
        height=35.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=13.0,
        y=213.0,
        width=162.0,
        height=34.0
    )

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        367.0,
        190.0,
        image=image_image_2
    )
win.resizable(False, False)
win.mainloop()
