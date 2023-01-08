from tkinter import *

def shit():
    cwindow = Tk()
    sabelal=Label(cwindow,text="Transactions with Elon musk : 100000000000$",font=("Consolas",25))
    tabelal=Label(cwindow,text="Transactions with Jeff Bezos : 100000000000$",font=("Consolas",25))
    kabelal=Label(cwindow,text="Transactions with Bill Gates :100000000000$",font=("Consolas",25))

    labelshit=Label(cwindow,text="Chibong Bank",font=("Consolas",25))
    labelshit.pack(side="top")

    labelcrap =Label(cwindow,text="View your previous Transactions",font=("Consolas",25))
    labelcrap.pack(side="top")

    sabelal.place(x=10,y=400)
    tabelal.place(x=10,y=450)
    kabelal.place(x=10,y=500)






    cwindow.mainloop()
    


def hello():
    username = entry.get()
    password = passentry.get()
    print("hello "+username,"your password is "+password)
    if username == "Chibong3020" and password =="Chibong3020":
        bwindow = Tk()
    bwindow.config(bg="white")
    brabel=Label(bwindow,text="Successfully logged into account",font=("Consolas",25),fg="blue",bg="White")
    brabel.place(y=300,x=0)

    clabel = Label(bwindow,text="Account balance : 0.00$",font=("Consolas",25),fg="red")
    clabel.place(y=300,x=1100)

    tralabel = Label(bwindow,text="Chibong Bank",font=("Consolas",25))
    tralabel.pack(side="top")

    buttona=Button(bwindow,text="Show transactions",command=shit,font=("consolas",25))
    buttona.pack(side=RIGHT)

    




    bwindow.mainloop()



window=Tk()


button = Button(window,text="Login",
font=("Arial",16,'bold'),
bg= "#f5f536",
fg="#88308a",
padx="10",
pady="10",
relief=RAISED,
command=hello,
state= ACTIVE)

entry=Entry(window,font=("Consolas",25),bg="black",fg="white")

passentry=Entry(window,font=("Consolas",25),bg="black",fg="white",show="*")


label=Label(window,text="username: ",font=("Consolas",25))
label.place(y=260,x=350)

grabel=Label(window,text="password: ",font=("Consolas",25))
grabel.place(y=340,x=350)

tabel=Label(window,text="Chibong Bank",font=("Consolas",25))

nabel=Label(window,text="Enter your username and password to login",font=("Consolas",25))

abel=Label(window,text="To Login, Username = Chibong3020, Password = Chibong3020(Can be changed if u want)",font=("Consolas",25))
abel.pack(side="bottom")




tabel.pack(side="top")
nabel.pack(side="top")
entry.place(x=560,y=260)
button.place(x=670,y=500)
passentry.place(x=560,y=340)
window.mainloop()

