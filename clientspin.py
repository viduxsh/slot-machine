#!/usr/bin/python3

#-*- coding:UTF-8 -*-

from tkinter import *
from tkinter import messagebox
import socket
from PIL import ImageTk, Image

def sendfunction():
    data="True"
    s.send(data.encode())
    reply=s.recv(1024).decode()
    n1, n2, n3, n4, money=reply.split("#")
    imagefunction(n1, 0)
    imagefunction(n2, 1)
    imagefunction(n3, 2)
    imagefunction(n4, 3)
    winbox=Label(face, text="                    ")
    winbox.grid(row=4, column=1)
    winbox=Label(face, text=money+"€")
    winbox.grid(row=4, column=1)
    win(n1, n2, n3, n4)

def closefunction():
    data="False"
    s.send(data.encode())
    reply=s.recv(1024).decode()
    window.destroy()

def imagefunction(n, nc):
    n=int(n)
    if n==0:
        img=ImageTk.PhotoImage(Image.open("./image/wild.jpg"))
    elif n==1:
        img=ImageTk.PhotoImage(Image.open("./image/sunglasses.jpg"))
    elif n==2:
        img=ImageTk.PhotoImage(Image.open("./image/shoe.jpg"))
    elif n==3:
        img=ImageTk.PhotoImage(Image.open("./image/ring.jpg"))
    elif n==4:
        img=ImageTk.PhotoImage(Image.open("./image/phone.jpg"))
    elif n==5:
        img=ImageTk.PhotoImage(Image.open("./image/microphone.jpg"))
    elif n==6:
        img=ImageTk.PhotoImage(Image.open("./image/lipstick.jpg"))
    elif n==7:
        img=ImageTk.PhotoImage(Image.open("./image/icecream.jpg"))
    elif n==8:
        img=ImageTk.PhotoImage(Image.open("./image/drink.jpg"))
    elif n==9:
        img=ImageTk.PhotoImage(Image.open("./image/car.jpg"))
    panel=Label(face, image=img)
    panel.grid(row=0, column=nc)
    panel.image = img
    panel.grid(row=0, column = nc)

def win(n1, n2, n3, n4):
    int(n1)
    int(n2)
    int(n3)
    int(n4)
    if n1==n2:
        if n2==n3:
            if n3==n4:
                winbox=Label(face, text="WIN!!")
                winbox.grid(row=3, column=1)
            else:
                winbox=Label(face, text="                    ")
                winbox.grid(row=3, column=1)
        else:
            winbox=Label(face, text="                    ")
            winbox.grid(row=3, column=1)
    else:
        winbox=Label(face, text="                    ")
        winbox.grid(row=3, column=1)

window=Tk()
window.protocol("WM_DELETE_WINDOW", closefunction)
window.geometry("1200x400")
window.title("Slot Machine")

s=socket.socket()
host="127.0.0.1"
port=12555
s.connect((host, port))

face=Frame(window)
face.pack()

send=Button(face, bg="gold",  text="Spin", command=sendfunction)
send.grid(row=1, column=1)
close=Button(face, bg="red3", text="Close", command=closefunction)
close.grid(row=2, column=1)

window.mainloop()
