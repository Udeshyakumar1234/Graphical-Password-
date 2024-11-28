import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def GetPassword(window,photo):
    clicked_tiles = []
    result= None    


    def load_image(file_path=photo):
        # Load the image using Pillow
        img = (file_path)
        
    
        img = img.resize((450, 450), Image.Resampling.LANCZOS)
        
        
        tile_number = 1
        
        for i in range(9):
            for j in range(9):
                # Crop each tile from the image
                left = j * 50
                top = i * 50
                right = left + 50
                bottom = top + 50
                tile = img.crop((left, top, right, bottom))
                
                # Converting the cropped image to a Tkinter-compatible format
                tile_img = ImageTk.PhotoImage(tile)
                
                # Create a button for each tile, pass its number and bind the click event
                button = tk.Button(root, image=tile_img, command=lambda num=tile_number: tile_click(num))
                button.image = tile_img  # avoiding garbage collection 
                button.grid(row=i, column=j, padx=0, pady=0)  
                
                tile_number += 1
        
    # Function to handle tile clicks
    def tile_click(tile_num):
        clicked_tiles.append(tile_num)
        

    # Function to display the result
    def show_result():
        nonlocal result
        if clicked_tiles:
            ans=map(str,clicked_tiles)
            ans=int("".join(ans))
            result=ans
            root.destroy()
           
        else:
            messagebox.showinfo("No Tiles Clicked", "You haven't clicked any tiles yet.")
        
    # Main window
    root = Toplevel(window)
    root.title("Image Segmentation")

    def center_window(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate x and y coordinates for the window to be centered
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        root.geometry(f'{width}x{height}+{x}+{y}')

    window_width =500  # width
    window_height = 600  # height
    center_window(root, window_width, window_height)


    # button for selecting image
    select_button = tk.Button(root, text="Select Image", command=load_image)
    select_button.grid(row=0, column=0, columnspan=9, pady=10, sticky="n")
    root.grid_columnconfigure(0, weight=1)

    # button for showing result

    result_button = tk.Button(root, text="Confirm The Selection", command=show_result)
    result_button.grid(row=10, column=0, columnspan=9, pady=10) 
    root.wait_window()
    return result

    
