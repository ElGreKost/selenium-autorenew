import tkinter as tk
import os


def set_credentials():
    if os.path.exists('credentials'): return # if the credentials are written then go to main code

    root = tk.Tk()

    # create variable to store input
    username_var = tk.StringVar()
    password_var = tk.StringVar()

    # create Entry widget, set variable to store input, and add to the root window
    username = tk.Entry(root, text='username', textvariable=username_var)
    username.pack()
    password = tk.Entry(root, text='password', textvariable=password_var)
    password.pack()

    # create a button to retrieve the input
    def retrieve_credentials():
        name = username_var.get()
        psswd = password_var.get()
        with open('credentials', 'w') as f:
            f.write(f'{name}\n{psswd}')
        root.destroy()  # close the GUI window

    button = tk.Button(root, text="Retrieve Username", command=lambda: retrieve_credentials())
    button.pack()

    root.mainloop()
