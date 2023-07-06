import cffi
import tkinter as tk
from tkinter import messagebox, PhotoImage, Text, Entry, Button, Checkbutton
import os
import glob

sleaftheme = "dark"

class Sleaf:
    def __init__(self, master):
        self.master = master
        self.theme = sleaftheme

    def input(self, value, placeholder, event):
        input_field = Entry(self.master)
        input_field.insert(0, placeholder)
        input_field.bind('<Key>', lambda e: event())
        input_field.pack()

    def image(self, src, placeholder, event):
        img = PhotoImage(file=src)
        img_label = tk.Label(self.master, image=img)
        img_label.image = img
        img_label.bind('<Button-1>', lambda e: event())
        img_label.pack()

    def text(self, value):
        text = Text(self.master)
        text.insert('1.0', value)
        text.pack()

    def video(self, src, vol, size, theme, event):
        # Tkinter does not support video playback. This is a placeholder.
        pass

    def createplayer(self, myVideo):
        # Tkinter does not support video playback. This is a placeholder.
        pass

    def msg(self, text):
        messagebox.showinfo("Message", text)

    def button(self, text, event):
        button = Button(self.master, text=text)
        button.bind('<Button-1>', lambda e: event())
        button.pack()

    ffi = cffi.FFI()

# Read the config.sleaf file to get the .dll files
    with open('config.sleaf', 'r') as file:
      dll_files = file.read().split(',')

# Load each .dll file
    for dll_file in dll_files:
      dll_file = dll_file.strip()  # Remove any leading/trailing whitespace
      lib = ffi.dlopen(dll_file)

    # Get the list of all the functions in the .dll file
    functions = [name for name in dir(lib) if callable(getattr(lib, name))]

    # Convert all C (Go) variables to Python variables
    for function in functions:
        globals()[function] = getattr(lib, function)

# Get all .go files in the current directory
    go_files = glob.glob('*.go')

# Define the prefix to look for
    prefix = '//#$SLEAF.'

# Loop through all .go files
    for go_file in go_files:
      with open(go_file, 'r') as file:
          lines = file.readlines()

    # Loop through all lines in the file
    for line in lines:
        # If the line starts with the prefix
        if line.startswith(prefix):
            # Execute the code after the prefix
            exec(line[len(prefix):].strip())



root = tk.Tk()
sleaf = Sleaf(root)
root.mainloop()

