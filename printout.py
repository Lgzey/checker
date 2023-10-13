import requests
import tkinter as tk
from tkinter import font
from tkinter import PhotoImage

root = tk.Tk()
root.title("Email Checker")
root.geometry("681x407")
root.attributes('-alpha', 0.8)
root.resizable(False, False)

root.iconbitmap('icon.ico')


font = font.Font(family="impact", size=45)

bg_image = PhotoImage(file="Hack.png")

backk = tk.Label( root, image = bg_image)
backk.place(x = -2,y = 0)

lay = tk.Label(root, text="HAVE YOU BEEN HACKED?", font=font)
lay.pack(pady=20)

lay2 = tk.Label(root, text="ENTER YOUR E-MAIL", font=font)
lay2.pack(pady=25)

pos = tk.Label(root,text="You are safe",fg="green", font=font)
neg = tk.Label(root, text="Email leaked", fg="red", font=font)
wrong = tk.Label(root, text="are you sure that is email?!", font=font)

def checker():
    pos.pack_forget()
    neg.pack_forget()
    wrong.pack_forget()
    
    url = "https://monitor.firefox.com/api/v1/scan"
    headers = {
        "Host": "monitor.firefox.com",
        "Cookie": "userId=guest-72ef408f-37d7-46b0-b8d6-287ccc692971; _ga_CXG8K4KW4P=GS1.3.1697099237.1.1.1697099384.0.0.0; _ga=GA1.3.481955232.1697099238",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "application/json",
        "Accept-Language": "en-GB,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "X-Csrf-Token": "undefined",
        "Referer": "https://monitor.firefox.com/scan",
        "Origin": "https://monitor.firefox.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "same-origin",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
    }
    tt = "adsd"
    data = {"email": EN.get()}

    response = requests.post(url, json=data, headers=headers)
    res = str(response.json())
    if response.status_code == 200:
        index = res.find("'total': 0")
        if index != -1:
            
            pos.pack()
        else:
            
            neg.pack()
            
    else:
        wrong.pack()

EN = tk.Entry(root, width=50,fg="red")
EN.pack(pady=10)
EN.get()

button = tk.Button(root, text="CHECK", width=6, height=2, command=checker)
button.pack()

root.mainloop()
