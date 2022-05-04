#!/usr/bin/env python3

import string
import random
import tkinter as tk

version="1.2"
title="Password Generator " + "v." + version + " ~ GweiGod"
w=500
h=300
center=(w/2)
max_entry=50
font_sm_config=("Arial",12,"bold")
font_lg_config=("Arial",14,"bold")

char=list(string.ascii_letters + string.digits + "!@#$%^&*()_+")

def Generate(root,cvs,entry,btn,output):
    if (btn["text"]) == "Generate" and entry != "" and entry.isnumeric() and int(entry) <= int(max_entry):
        password=[]
        for i in range(int(entry)):
            password.append(random.choice(char))

        random.shuffle(password)
        password=str("").join(password)

        output=tk.Button(root,text=password,font=font_sm_config,command=lambda: Copy(root,cvs,password))
        output.config(border=0,cursor="hand1",bg="#000",fg="#fff")
        cvs.create_window((w/2),200,window=output)
        print(password)

        btn["text"]="Exit (Esc)"

    elif (btn["text"]) == "Exit (Esc)":
        Exit(root)
        print("Exited")

def Copy(root,cvs,password):
    root.clipboard_clear()
    root.clipboard_append(password)

    label=tk.Label(root, text="Copied to clipboard!")
    label.config(bg="#000",fg="#fff",font=font_sm_config)
    cvs.create_window(center,230,window=label)
    print("Copied")



def Exit(root):
    root.destroy()


def Init():
    root=tk.Tk()
    root.title(title)
    root.resizable(False, False)
    root.iconphoto(False, tk.PhotoImage(file="icon.png"))
    cvs=tk.Canvas(root,width=w,height=h,bg="#000")
    cvs.pack()

    output=tk.Button()
    btn=tk.Button()

    label=tk.Label(root,text="Password length: (Max 50)")
    label.config(bg="#000",fg="#fff",font=font_sm_config)
    cvs.create_window(center,70,window=label)

    entry=tk.Entry(root, width=5, border=2, justify="center", font=font_sm_config)
    cvs.create_window(center,100,window=entry)
    
    
    btn=tk.Button(root,text="Generate", border=3, cursor="hand1", font=font_lg_config, command=lambda:Generate(root,cvs,entry.get(),btn,output))
    root.bind("<Return>",lambda event:Generate(root,cvs,entry.get(),btn,output))
    cvs.create_window(center,150,window=btn)

    root.bind("<Escape>",lambda event:Exit(root))
    root.mainloop()


Init()