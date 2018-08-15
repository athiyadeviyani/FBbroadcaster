''' www.github.com/athiyadeviyani '''

import fbchat
import random
from tkinter import *
from tkinter import messagebox

#################### LOGIN SCREEN ####################

root = Tk()
root.title("Log In")

root.geometry('400x250')

spc = Label(root, text = "")
spc.pack()

lbl = Label(root, text = "Please enter your FaceBook username and password", font=("Arial",14))
lbl.pack()

spc = Label(root, text = "")
spc.pack()

unamelabel = Label(root, text = "Username")
unamelabel.pack()

uname = Entry(root, width = 20)
uname.pack()

pwdlabel = Label(root, text = "Password")
pwdlabel.pack()

pwd = Entry(root, width = 20, show="*")
pwd.pack()


#################### Actual FaceBook Broadcaster starts here ####################

def login():
    username = uname.get()
    password = pwd.get()
    client = fbchat.Client(username, password)
    root.destroy()

    window = Tk()
    window.title("FaceBook Message Broadcaster")

    window.geometry('600x600')

    #################### FRIENDS handler ####################
    
    friendslist = []

    def clicked():
        friendslist.append(nf.get())
        str = ""
        for friend in friendslist:
            str = str + friend + "\n"
        currentlist.configure(text = str)
        nf.delete(0, END)
        print(friendslist)

    spc = Label(window, text = "", font = ("Arial Bold",30))
    spc.pack()

    lbl = Label(window, text = "FaceBook Message Broadcaster", font = ("Arial Bold",16))
    lbl.pack()

    spc = Label(window, text = "", font = ("Arial Bold",20))
    spc.pack()

    friendslabel = Label(window, text = "FRIENDS", font = ("Arial Bold",14))
    friendslabel.pack()

    currentlabel = Label(window, text = "Current Friends List", font = ("Arial Bold",12))
    currentlabel.pack()

    currentlist = Label(window, text = "", font = ("System", 12))
    currentlist.pack()

    aflabel = Label(window, text = "Add Friend to List", font = ("Arial Bold",12))
    aflabel.pack()

    nf = Entry(window, width = 20)
    nf.pack()

    addbtn = Button(window, text = "Add", bg = "black", fg = "black", command = clicked)
    addbtn.pack()

    def func(event):
        clicked()
    nf.bind('<Return>', func)

    remf = Label(window, text = "Remove Friend from List", font = ("Arial Bold",12))
    remf.pack()

    rf = Entry(window, width = 20)
    rf.pack()

    def rem():
        str = ""
        name = rf.get()
        friendslist.remove(name)
        for friend in friendslist:
            str = str + friend + "\n"
        currentlist.configure(text = str)
        rf.delete(0, END)
        print(name)

    removebtn = Button(window, text = "Remove", bg = "black", fg = "black", command = rem)
    removebtn.pack()

    def rement(event):
        rem()
    rf.bind('<Return>', rement)

    spc = Label(window, text = "", font = ("Arial Bold",20))
    spc.pack()

    #################### MESSAGE handler ####################

    messagelabel = Label(window, text = "MESSAGE", font = ("Arial Bold",14))
    messagelabel.pack()

    messages = []

    def addmsg():
        messages.append(msgbox.get())
        str = ""
        for message in messages:
            str = str + message + "\n"
        messagelines.configure(text = str)
        msgbox.delete(0, END)
        print(messages)

    previewlabel = Label(window, text = "Message Preview", font = ("Arial Bold",12))
    previewlabel.pack()

    messagelines = Label(window, text = "", font = ("System", 12))
    messagelines.pack()

    amlabel = Label(window, text = "Add Message", font = ("Arial Bold",12))
    amlabel.pack()

    msgbox = Entry(window, width = 40)
    msgbox.pack()

    addmbtn = Button(window, text = "Add Message", bg = "black", fg = "black", command = addmsg)
    addmbtn.pack()

    def messadd(event):
        addmsg()
    msgbox.bind('<Return>', messadd)

    def clearmsg():
        messages.clear()
        messagess.configure(text = "")

    clearmsg = Button(window, text = "CLEAR", command = clearmsg)
    clearmsg.pack()

    def send():
        for i in range(len(friendslist)):
            name = friendslist[i]
            friendnames = client.searchForUsers(name)
            for friend in friendnames:
                for message in messages:
                    sent = client.sendMessage(message, thread_id=friend.uid)
        messagebox.showinfo('MESSAGE STATUS', 'SENT!')

    sendmsg = Button(window, text = "SEND MESSAGE", command = send, font = ("Arial Bold", 14))
    sendmsg.pack()

    window.mainloop()

########################################

spc = Label(root, text = "")
spc.pack()

loginbtn = Button(root, text = "Log In", command = login)
loginbtn.pack()

def lgn(event):
    login()
pwd.bind('<Return>', lgn)

root.mainloop()
