#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, time, subprocess, random

money=100

def parser():
    global money
    money=money-1
    data=open('serverdata.txt', 'r')
    line=data.read()
    data.close()
    print(line)
    n1=random.randint(0, 9)
    n2=random.randint(0, 9)
    n3=random.randint(0, 9)
    n4=random.randint(0, 9)
    winfile=" "
    if n1==n2:
        if n2==n3:
            if n3==n4:
                winfile="WIN"
                money=money+100
    output=str(n1)+"#"+str(n2)+"#"+str(n3)+"#"+str(n4)+"#"+str(money)
    dataw=open('serverdata.txt', 'a+')
    dataw.write(output+winfile)
    dataw.write("\n")
    dataw.close()

    return output

host="127.0.0.1"
port=12555
subprocess.Popen("fuser -k "+str(port)+"/tcp", shell=True)
print("Porta di servizio libera")
time.sleep(3)
print("Server avviato")

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

inputmessage="True"

while(True):
    c, addr=s.accept()
    print("Connessione stabilita con "+str(addr))
    dataw=open('serverdata.txt', 'a+')
    dataw.write("Utente: "+str(addr))
    dataw.write("\n")
    dataw.close()
    while(inputmessage!="False"):
        inputmessage=c.recv(1024).decode()
        print("Message from client: "+inputmessage)
        outputmessage=parser()
        c.send(outputmessage.encode())
        print("Message from server: "+outputmessage)
    c.close
    money=100
    print("Connessione interrotta con "+str(addr))
    inputmessage="True"
