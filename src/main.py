# importing module
from tkinter import *
from tkinter.messagebox import showwarning
from pyshorteners import Shortener
import pyperclip

# declaring global variable
url = " "
shorten_final_link = " "
shorten_final_link_var = " "


# function for btn
def short_url():
    global url
    global shorten_final_link
    global shorten_final_link_var
    try:
        url = url_entry_box.get()
        # print(url)
        shorten_url = Shortener().tinyurl.short(url)
        # print(shorten_url)
        short_url_label.config(text=shorten_url, textvariable=shorten_final_link)
        shorten_final_link_var = short_url_label.getvar(shorten_final_link)
        # print(shorten_final_link_var)
    except EXCEPTION as e:
        exception = str(e)
        showwarning("Warning", message=exception+". Please, Enter a right url address")


def copy_func():
    global shorten_final_link_var
    pyperclip.copy(shorten_final_link_var)


# window creating
root = Tk()
root.title("Url Shortner")
root.geometry("535x145")
root.resizable(False, False)            # window can't be maximize
# for getting url
url_entry_label = Label(root, text="Enter your url down bellow")
url_entry_label.pack()
url_entry_box = Entry(root, font=("verdana", 20))
url_entry_box.place(y=25, x=25, width=400)
# for make url short
short_btn = Button(root, text="short", font=("verdana", 13), command=short_url)
short_btn.place(y=24, x=450)
# for show the url here is my new idea applied not copy :)
short_url_label = Label(root, text="Your short url will be shown here after shorten", font=("verdana", 10))
short_url_label.place(y=75, x=25)
# for copying url
copy_btn = Button(root, text="Copy", font=("verdana", 10), command=copy_func)
copy_btn.place(y=75, x=400, width=110)
# for showoff
developed_label = Label(text="Developed By Nafis Iqbal", bg="white")
developed_label.pack(side=BOTTOM, fill=X)
# for showing window and stay longer
root.mainloop()
# end the coe :)
