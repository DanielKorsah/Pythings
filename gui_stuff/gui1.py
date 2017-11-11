import tkinter

# initialise
window = tkinter.Tk()
window.title("Fannybaws")
window.geometry("600x400")
window.wm_iconbitmap("favicon.ico")


# create label
lbl = tkinter.Label(window, text="Username")
lbl.pack()

entry = tkinter.Entry(window)
entry.pack()
lbl = tkinter.Label(window, text="Password")
lbl.pack()
entrywwww = tkinter.Entry(window)
entry.pack()
# button widget called btn
btn = tkinter.Button(window, text="Enter")

# pack the widget on the window
lbl.pack()

btn.pack()

# start application
window.mainloop()