from tkinter.font import BOLD
import requests
import json
from tkinter import *
import os

# Change "screen.geometry("XxY")" as you want!!

def delete2():
    screen.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen0)
    screen4.title("Success")
    # screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen0)
    screen5.title("Success")
    # screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()

def dashboard():
    global screen6
    global screen
    screen6 = Toplevel(screen0)
    screen6.title("DASHBOARD")
    screen6.geometry("400x500")
    f1 = Frame(screen6, relief=SUNKEN)
    f1.pack()
    l1 = Label(f1, text="Crypto Dashboard", font=("Times New Roman", 15, BOLD), padx=105, pady=13, fg="black", bg="gold")
    l1.pack()

    def click(event):
      text=event.widget.cget("text")
      print(text)
      if text== "BTC/USD":
        bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin&vs_currencies=usd",headers = {"accept": "application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()
      elif text=="BTC/INR":
        bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin&vs_currencies=Inr",headers = {"accept":"application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()

      elif text=="ADA/USD":
        bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Cardano&vs_currencies=usd",headers = {"accept":"application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()

      elif text=="ADA/INR":
        bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Cardano&vs_currencies=Inr",headers = {"accept":"application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()
      elif text=="ETH/INR":
        bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Ethereum&vs_currencies=Inr",headers = {"accept":"application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()
      elif text=="ETH/USD":
        bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=Ethereum&vs_currencies=usd",headers = {"accept":"application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()

      elif text=="RUN":
        url=f"https://api.coingecko.com/api/v3/simple/price?ids={coin.get()}&vs_currencies={curr.get()}"
        bob=requests.get(url ,headers = {"accept": "application/json"})
        result=(bob.json())
        scvalue.set( result)
        screen.update()

      elif text== "CLEAR":
        scvalue.set(" ")
        screen.update()

    scvalue=StringVar()
    scvalue.set(" ")
    screen=Entry(screen6,textvar=scvalue,font="lucida 20 ")
    screen.pack(fill=X,ipadx=8,padx=10,pady=10)
    
    coin=StringVar()
    coinentry=Entry(screen6,textvariable=coin,font="lucida 20 ")
    coinentry.pack(fill=X,ipadx=8,padx=10,pady=10)
    coinentry.place(y=330)

    curr=StringVar()
    currentry=Entry(screen6,textvariable=curr,font="lucida 20 ")
    currentry.pack(fill=X,ipadx=8,padx=10,pady=10)
    currentry.place(y=380)

    f=Frame(screen6)
    b=Button(f, text="RUN",font="lucida 15 bold",fg="white", bg="green")
    b.pack()
    b.bind("<Button-1>", click)
    f.place(x=0,y=460)

    fexit=Frame(screen6)
    Button(fexit,text=" EXIT ",font="arial 13 bold", command=screen0.destroy, fg="red",bg="black").pack()
    fexit.pack(side=BOTTOM,anchor="e")

    f4=Frame(screen6, borderwidth=6 ,bg="red")
    b0=Button(f4,bg="red",fg="white", text="CLEAR",font="arial 13 bold")
    b0.pack()
    b0.bind("<Button-1>", click)
    f4.pack(side=BOTTOM,anchor="se")

    f=Frame(screen6,bg="grey",borderwidth=4,padx=0,pady=0,relief=SUNKEN)
    b=Button(f, text="BTC/USD",font="lucida 15 bold",fg="yellow", bg="black")
    b.pack(side=RIGHT)
    b.bind("<Button-1>", click)
    f.place(x=75,y=120)

    f=Frame(screen6,bg="grey",borderwidth=4,padx=0,pady=0,relief=SUNKEN)
    b=Button(f, text="BTC/INR",font="lucida 15 bold",fg="yellow", bg="black")
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)
    f.place(x=200,y=120)

    fa=Frame(screen6,bg="grey",borderwidth=4, relief=SUNKEN)
    b=Button(fa, text="ADA/USD",font="lucida 15 bold",fg="blue")
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)
    fa.place(x=75,y=190)

    fa=Frame(screen6,bg="grey",borderwidth=4, relief=SUNKEN)
    b=Button(fa, text="ADA/INR",font="lucida 15 bold",fg="blue")
    b.pack(side=LEFT)
    b.bind("<Button-1>", click)
    fa.place(x=200,y=190)

    f=Frame(screen6,bg="grey",borderwidth=4,padx=0,pady=0,relief=SUNKEN)
    b=Button(f, text="ETH/INR",font="lucida 15 bold",fg="yellow", bg="black")
    b.pack(side=RIGHT)
    b.bind("<Button-1>", click)
    f.place(x=75,y=260)

    f=Frame(screen6,bg="grey",borderwidth=4,padx=0,pady=0,relief=SUNKEN)
    b=Button(f, text="ETH/USD",font="lucida 15 bold",fg="yellow", bg="black")
    b.pack(side=RIGHT)
    b.bind("<Button-1>", click)
    f.place(x=200,y=260)

def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
      file1 = open(username1, "r")
      verify = file1.read().splitlines()
      if password1 in verify:
        dashboard()
        screen2.destroy()
        # screen0.destroy()
      else:
        password_not_recognised()
    else:
      user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen0)
    screen1.title("Register")
    screen1.geometry("300x400")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1).pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "USERNAME",font = ("Calibri",12,BOLD)).pack()
    username_entry = Entry(screen1, textvariable = username,width= 28)
    username_entry.pack()
    Label(screen1, text = "PASSWORD",font = ("Calibri",12,BOLD)).pack()
    password_entry = Entry(screen1, textvariable = password,width= 28)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register",bg="gold",font = ("Calibri",12,BOLD),width= 10, height = 1, command = register_user).pack()
# Login Window
def login():
    global screen2
    screen2 = Toplevel(screen0)
    screen2.title("Login")
    screen2.geometry("300x400")
    Label(screen2).pack()
    Label(screen2, text = "").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1

    Label(screen2, text = "USERNAME",font = ("Calibri",12,BOLD)).pack()
    username_entry1 = Entry(screen2, textvariable = username_verify,width= 28)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "PASSWORD",font = ("Calibri",12,BOLD)).pack()
    password_entry1 = Entry(screen2, textvariable = password_verify,width= 28)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login",bg="gold",font = ("Calibri",12,BOLD), width =10, height = 1, command = login_verify).pack()
    
def main_screen():
    global screen0
    screen0 = Tk()
    screen0.geometry("400x500")
    screen0.title("CYPTO DASHBOARD")
    Label(text = "CRYPTO DASHBOARD", bg = "gold", width = "300", height = "2", font = ("Times New Roman", 18,BOLD)).pack()
    Label(text = "").pack()
    Button(text = "Login",font = ("Times New Roman",13,BOLD), height = "2", width = "30", command = login,bg= "lightseagreen").pack()
    Label(text = "").pack()
    Button(text = "Register",font = ("Times New Roman",13,BOLD),height = "2", width = "30", command = register,bg= "Deepskyblue").pack()
    screen0.mainloop()
main_screen()