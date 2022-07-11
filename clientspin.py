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
    imgs = ["./image/wild.jpg", "./image/sunglasses.jpg", "./image/shoe.jpg", 
            "./image/ring.jpg", "./image/phone.jpg", "./image/microphone.jpg", 
            "./image/lipstick.jpg", "./image/icecream.jpg", "./image/drink.jpg", 
            "./image/car.jpg"]
    img=ImageTk.PhotoImage(Image.open(imgs[n]))
    panel=Label(face, image=img)
    panel.grid(row=0, column=nc)
    panel.image = img
    panel.grid(row=0, column = nc)

def win(n1, n2, n3, n4):
    if n1==n2==n3==n4:
        winbox=Label(face, text="WIN!!")
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
