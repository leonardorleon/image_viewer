#!/usr/bin/env python3

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Image viewer")
# Set the icon for the window manager
wm_icon = tk.PhotoImage(file="images/icon.png")
root.call('wm', 'iconphoto', root._w, wm_icon)

# get all the images
my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpeg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/img6.jpg"))

# put the images in a list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

# Make a label for the status bar
status = tk.Label(
    root, text=f"Image 1 of {len(image_list)} ", bd=1, relief=tk.SUNKEN, anchor=tk.E)
# label that will show the current image
my_label = tk.Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back

    # Update image
    my_label.grid_forget()  # Get rid of previous image
    my_label = tk.Label(image=image_list[image_num-1])

    # Update buttons
    button_forward = tk.Button(
        root, text=">>", command=lambda: forward(image_num+1))
    button_back = tk.Button(
        root, text="<<", command=lambda: back(image_num-1))

    # Update status bar
    status = tk.Label(
        root, text=f"Image {image_num} of {len(image_list)} ", bd=1, relief=tk.SUNKEN, anchor=tk.E)

    # Disable forward button if last image is reached
    if image_num == len(image_list):
        button_forward = tk.Button(
            root, text=">>", state=tk.DISABLED)

    # Attach elements to root
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, columnspan=3, sticky=tk.W+tk.E)


def back(image_num):
    global my_label
    global button_forward
    global button_back

    # Update image
    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_num-1])

    # Update buttons
    button_forward = tk.Button(
        root, text=">>", command=lambda: forward(image_num+1))
    button_back = tk.Button(
        root, text="<<", command=lambda: back(image_num-1))

    # Update status bar
    status = tk.Label(
        root, text=f"Image {image_num} of {len(image_list)} ", bd=1, relief=tk.SUNKEN, anchor=tk.E)


    # Disable back button if the first image is reached
    if image_num == 1:
        button_back = tk.Button(root, text="<<", state=tk.DISABLED)

    # Attach elements to root
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status.grid(row=2, columnspan=3, sticky=tk.W+tk.E)


# Create the buttons
button_back = tk.Button(root, text="<<", state=tk.DISABLED)
button_exit = tk.Button(root, text="Exit Program", command=root.quit)
button_forward = tk.Button(root, text=">>", command=lambda: forward(2))

# Place the buttons in the grid
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=5)
# Place the status bar
status.grid(row=2, columnspan=3, sticky=tk.W+tk.E)

root.mainloop()
