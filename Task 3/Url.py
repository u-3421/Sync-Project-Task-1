import pyperclip
import pyshorteners
import tkinter as tk

root = tk.Tk()
root.geometry("450x350")
root.title("URL Shortener")
root.configure(bg="#3D4A55")

url = tk.StringVar()
url_address = tk.StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

title_label = tk.Label(root, text="URL Shortener", font=("Verdana", 28), fg="#121110", bg="#3D4A55")
title_label.pack(pady=10)

url_entry = tk.Entry(root, textvariable=url, width=40, font=("Helvetica", 12), fg="#495057", bg="#C5C5C5", bd=0, highlightthickness=2, highlightbackground="#ced4da", highlightcolor="#ced4da")
url_entry.pack(pady=10)

shorten_button = tk.Button(root, text="Generate Short URL", font=("Helvetica", 12), bg="#525252", fg="#ffffff", bd=0, activebackground="#0062cc", activeforeground="#ffffff", padx=10, pady=5, command=urlshortener)
shorten_button.pack(pady=10)

url_label = tk.Label(root, text="Shortened URL:", font=("Helvetica", 14), fg="#121110", bg="#3D4A55")
url_label.pack(pady=10)

url_output = tk.Entry(root, textvariable=url_address, width=40, font=("Helvetica", 12), fg="#495057", bg="#C5C5C5", bd=0, highlightthickness=2, highlightbackground="#ced4da", highlightcolor="#ced4da")
url_output.pack(pady=10)

copy_button = tk.Button(root, text="Copy", font=("Helvetica", 12), bg="#525252", fg="#ffffff", bd=0, activebackground="#218838", activeforeground="#ffffff", padx=10, pady=5, command=copyurl)
copy_button.pack(pady=10)

root.mainloop()
