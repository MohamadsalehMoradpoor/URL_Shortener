import pyshorteners
from tkinter import *
from tkinter import messagebox
import webbrowser

# Define window
root = Tk()
root.title('URL Shortener')
root.geometry("450x200")
root.config(bg='#F71FED')
root.resizable(0, 0)

# Functions
def shorter():
    global short_link
    if 'http' in url_entry.get() or 'https' in url_entry.get():
        s = pyshorteners.Shortener()
        short_link = s.tinyurl.short(url_entry.get())
        result_entry = Entry(root, width=len(short_link) + 3)
        result_entry.insert(0, short_link)
        result_entry.place(height=25, relx=0.5, rely=0.7, anchor='c')
        show_in_browser_btn.config(state=NORMAL)
        
    else:
        messagebox.showerror('Error!!', 'Enter a valid URL')
        url_entry.delete(0, END)

def open():
    webbrowser.open(short_link)

# Making the widget
url_entry = Entry(root, width=40)
confirm_btn = Button(root, text='Short URL', bg='#290927',font='sans 10 bold', fg='white', borderwidth=3, command=shorter)
show_in_browser_btn = Button(root, text='Browser',font='sans 10 bold', bg='#2013F1', fg='#F11021', borderwidth=5, command=open, state=DISABLED)
# Griding widget on screen
url_entry.place(height=25, relx=0.5, rely=0.2, anchor='c')
confirm_btn.place(relx=0.5, rely=0.4, anchor='c')
show_in_browser_btn.place(relx=0.87, rely=0.7, anchor='c')
# Calling the main window's mainloop
root.mainloop()