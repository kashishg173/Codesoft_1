from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("900x550")
root.title("To_Do_List")
root.resizable(False,False)
image_icon=PhotoImage(file="note2.ico")
root.iconphoto(False,image_icon)
def alreadyitems():
     try:
          with open("tasklist.txt",'r') as taskf:
               tasks=taskf.readlines()
               print(tasks)
          for task in tasks:
                         listbox.insert("end",task)
                    
     except:
          fil=open("tasklist.txt","w")
          fil.close()
def add(event):
    global itembox
    text=itembox.get()
    if len(text)>0:
        listbox.insert(ACTIVE,text)
    itembox.set("")
    with open("tasklist.txt",'a') as taskfile:
            taskfile.write(str(text)+"\n")
            taskfile.close()
def addend(event):
    global itembox
    text=itembox.get()
    if len(text)>0:
        listbox.insert(END,text)
    itembox.set("")
    with open("tasklist.txt",'a') as taskfile:
            taskfile.write(str(text)+"\n")
            taskfile.close()
def dell(event):
    global listbox
    a=tmsg.askquestion("Delete","Are you sure you want to delete this task?")
    if a=="yes":

     taskdel = str(listbox.get(listbox.curselection()))
    
     with open("tasklist.txt", 'r') as tasks:
         tasklines = tasks.readlines()
        
     with open("tasklist.txt", 'w') as tas:
        for line in tasklines:
            if line.find(taskdel) == -1:
                tas.write(line)
    
     listbox.delete(listbox.curselection())
    
tit=Label(root,text="TO DO LIST",font="comicsansms 30 bold",bg="#32405b",pady=20,fg="white",relief=RIDGE,borderwidth=10)
tit.pack(fill="x",pady=5)
f1=Frame(root)
f1.pack()
additem=Label(f1,text="Add Tasks",font="comicsans 20 bold")
additem.pack(side=TOP,pady=20,padx=40,anchor="w")
itembox=StringVar()
iboxentry=Entry(f1,textvariable=itembox,font="comicsans 18")
iboxentry.focus()
iboxentry.pack(ipady=7,ipadx=200,side=LEFT,padx=40,anchor="nw")
iboxentry.bind('<Return>',addend)
sub=Button(f1,text="ADD",font="comicsans 16 bold",pady=4,padx=7,bg="#1ECBE1")
sub.pack(anchor="nw",side=LEFT)
sub.bind('<Button-1>',add)


f2=Frame(root)
f2.pack(fill="x")
item=Label(f2,text="Tasks",font="comicsans 20 bold")
item.pack(side=TOP,pady=(30,20),padx=(67,0),anchor="w")

f3=Frame(root)
f3.pack()
listbox=Listbox(f3,font="comicsans 18",bg="#32405b",fg="white",cursor="hand2",selectbackground="#1ECBE1")
listbox.pack(side=LEFT,anchor="nw")
listbox.configure(width=51,height=7)
alreadyitems()
listbox.bind("<Delete>",dell)
scroolbar=Scrollbar(f3,bg="grey")
scroolbar.pack(side=RIGHT,fill="y")
listbox.config(yscrollcommand=scroolbar.set)
scroolbar.config(command=listbox.yview)


imaage=Image.open("delete-48.ico")
#imaage.resize((10,10),Image.LANCZOS)
delicon=ImageTk.PhotoImage(image=imaage)
delbtn=Button(f3,image=delicon)
delbtn.pack(padx=5)
delbtn.bind("<Button-1>",dell)
root.mainloop()