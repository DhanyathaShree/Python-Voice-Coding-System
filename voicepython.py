import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import os
nx=0
vc=Tk()
t={}
bzz=[]
cap=0
vc.title("Voice Coding")
vc.geometry("600x600")
photo2= PhotoImage(file="/Users/santhosh/Desktop/python.png")
background_label2= Label(vc, image=photo2)
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
background_label2.image = photo2
Label(vc,text="WELCOME TO VOICE CODING",fg="black",bd=2,relief="solid",font=("Apple Chancery",30)).place(x=80,y=5)
Label(vc,text="Ready to code??",fg="black",bd=2,relief="solid",font=("Apple Chancery",25)).place(x=200,y=170)

import mysql.connector as m
con=m.connect(host="localhost",user="root",password="12dhanyatha")
cur=con.cursor()
cur.execute("use voicecoding;") 
def output():
##    if cap==1:
##        voice2=""
##        r2=sr.Recognizer()
##        with sr.Microphone() as source2:
##            r2.adjust_for_ambient_noise(source2)
##            print("say something2:")
##            audio2=r2.listen(source2)
##            try:
##                voice2+=str(r2.recognize_google(audio2))
##                print(voice2)
##            except Exception as e:
##                print("error:"+str(e))
##            if __name__=="__main__":
##                main()
##    df=str(voice2)+".txt"
    global mr
    global f
    global vc5
    exec(f)
    app=open(wet,"r")
    bu=app.read()
    labelx=Label(vc5,text="OUTPUT")
    labelx.place(x=250,y=10)
    hmm=Label(vc5,text=bu,textvariable=bu,bd=1,relief="solid",width=17,height=4,anchor=NW)
    hmm.place(x=270,y=40)
    app.close()

def file():
    global wet 
    global nx
    wet=input("enter ur file name:")+".txt"
##    xta="file"
##    yta=str(len(fill1))
##    print(xta,yta,"xta")
##    ffn={xta+yta:str(wet)}
##    print("ffn",ffn)
##    for xa in fill1:
##        print("xa",xa)
    #import mysql.connector as m
    #con=m.connect(host="localhost",user="root",password="12dhanyatha")
    #cur=con.cursor()
    #cur.execute("use voicecoding;") 
    #ccap="update vc set file="+'"'+str(ffn)+'"'+"where username="+'"'+bbh+'"'+";"
    #cur.execute("update vc set file="+'"'+str(ffn)+'"'+"where username="+'"'+bbh+'"'+";")
    #print("fill",fill1)
    #fill1.update(ffn)
    #print("fill",fill1)
    nx+=1
    #con.commit()
    
def project():
    global vc2
    global vc3
    global vc4
    global vc5
    global bzz
    global cap
    cap+=1
    bzz=[]
    vc5=Tk()
    vc5.title("PYTHON VOICE CODING")
    vc5.geometry("500x250")
    vc5.configure(bg="turquoise")
    import speech_recognition as sr
    while True:
        def main():
            global voice
            voice=""
            r=sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("say something:")
                audio=r.listen(source)
                try:
                    voice+=str(r.recognize_google(audio))
                    print(voice)
                except Exception as e:
                    print("error:"+str(e))
        if __name__=="__main__":
            main()
        label=Label(vc5,text="INPUT")
        label.place(x=10,y=10)
##        code=Entry(vc5,fg="black",bg="gray70",width=21,textvariable=StringVar())
##        code.place(x=30,y=10)
        def z():
            global bzz
            global voice
            bzz+=voice.split()
            n=1
            global f
            if nx==0:
                file()
            f="plant=open('"+wet+"', 'w')\n"
            print(f)
            ff=""
##            lab=bz.count("clean")
##            bzz=[]
##            for jac in range(0,len(bz)):
##                if bz[jac]!="clean":
##                    bzz.append(bz[jac])
##                else:
##                    bzz.pop(jac-1)
##            print(bzz)
            for i in range (0,len(bzz)):
                
##                if len(bzz)<i:
##                    pass
##                elif bzz[i]=="lapse" or bzz[i]=="Labs" or bzz[i]=="labs":
##                    bzz.pop(i-1)
##                    f+=""
##                    ff+=" "
                if bzz[i]=="open":
                    if bzz[i+1]=="string":
                        f+="'"
                        ff+="'"
                    elif bzz[i+1]=="list":
                        f+="["
                        ff+="["
                    elif bzz[i+1]=="tuple" or bzz[i+1]=="pupil":
                        f+="("
                        ff+="("
                    elif bzz[i+1]=="dict":
                        f+="{"
                        ff+="{"
                    elif bzz[i+1]=="off" or bzz[i+1]=="of" or bzz[i+1]=="up":
                        f+="("
                        ff+="("
                elif bzz[i]=="close" or bzz[i]=="closed" or bzz[i]=="closer" or bzz[i]=="clothes" :
                    if bzz[i+1]=="string":
                        f+="'"
                        ff+="'"
                    elif bzz[i+1]=="list":
                        f+="]"
                        ff+="]"
                    elif bzz[i+1]=="tuple" or bzz[i+1]=="pupil":
                        f+=")"
                        ff+=")"
                    elif bzz[i+1]=="dict":
                        f+="}"
                        ff+="}"
                    elif bzz[i+1]=="off" or bzz[i+1]=="of" or bzz[i+1]=="up":
                        f+=")"
                        ff+=")"
                    elif bzz[i+1]!="off" or bzz[i+1]!="of" or bzz[i+1]!="up":
                        f+=" "
                        ff+=" "
                    else:
                        pass
                    
                elif bzz[i]=="bi" or bzz[i]=="be":
                    f+='b'
                    ff+='b'
                elif bzz[i]=="if" or bzz[i]=="If":
                    f+="if"
                    ff+="if"
                elif bzz[i]=="else" or bzz[i]=="els" or bzz[i]=="yells" :
                    f+="else:"
                    f+="\n"
                    f+="    "
                    ff+="else:"
                    ff+="\n"
                    ff+="    "
                elif bzz[i]=="equals" or bzz[i]=="equal":
                    f+="="
                    ff+="="
                elif bzz[i]=="for":
                     f+="for "
                     ff+="for "
                elif bzz[i]=="colon" or bzz[i]==":":
                    f+=":"
                    f+="\n"
                    f+="    "
                    ff+=":"
                    ff+="\n"
                    ff+="    "
                elif bzz[i]=="comma" or bzz[i]=="camma" :
                    f+=","
                    ff+=","
                elif bzz[i]=="end":
                    f+=""
                    ff+=""
                elif bzz[i]=="string" or bzz[i]=="list" or bzz[i]=="tuple" or bzz[i]=="off" or bzz[i]=="dict" or bzz[i]=="of":
                    f+=""
                    ff+=""
                elif bzz[i]=="operation" or bzz[i]=="corporation":
                    if bzz[i+1]=="plus":
                        f+='+'
                        ff+='+'
                    elif bzz[i+1]=="minus":
                        f+='-'
                        ff+='-'
                    elif bzz[i+1]=="multiply":
                        f+='*'
                        ff+='*'
                    elif bzz[i+1]=="divide":
                        f+='/'
                        ff+='/'
                    elif bzz[i+1]=="floor":
                        f+='//'
                        ff+='//'
                    elif bzz[i+1]=="power":
                        f+='**'
                        ff+='**'
                    elif bzz[i+1]=="modulos" or bzz[i+1]=="modulo":
                        f+='%'
                        ff+='%'
                    elif bzz[i+1]=="greater":
                        f+='>'
                        ff+='>'
                    elif bzz[i+1]=="less":
                        f+='<'
                        ff+='<'
                elif bzz[i]=="yah" or bzz[i]=="yeah" or bzz[i]=="Yah":
                    f+='a'
                    ff+='a'
                elif bzz[i].isupper():
                    f+=bzz[i].lower()
                    ff+=bzz[i].lower()
                elif bzz[i]=="plus":
                    f+='+'
                    ff+='+'
                elif bzz[i]=="minus" or bzz[i]=="multiply" or bzz[i]=="divide" or bzz[i]=="floor" or bzz[i]=="power" or bzz[i]=="modulos" or bzz[i]=="greater" or bzz[i]=="less":
                    f+=""
                elif bzz[i]=="next" or bzz[i]=="Next" or bzz[i]=="NEXT":
                    f+="\n"
                    ff+="\n"
                elif bzz[i]=="space":
                    f+=" "
                    ff+=" "
                elif bzz[i]=="tab":
                    if bzz[i]=="tab":
                            n+=1
                    for u in range (0,n):
                        f+="   "
                        ff+="   "
                elif bzz[i]=="dot":
                    ff+="."
                elif bzz[i]=="def" or bzz[i]=="deaf":
                    f+="def"
                    ff+="def"
                elif bzz[i]=="true":
                    f+='True'
                    ff+='True'
                elif bzz[i]=="false":
                    f+='False'
                    ff+='False'
                elif bzz[i]=="sprint" or bzz[i]=="print":
                    f+="plant.write("
                    ff+="print("
                elif bzz[i]=="in":
                    f+=" in "
                    ff+=" in "
                elif bzz[i]=="length":
                    f+="len("
                    ff+="len("
                elif bzz[i]=="input":
                    f+='input("'
                    ff+='input("'
                elif bzz[i]=="integer":
                    f+='int('
                    ff+='int('
                elif bzz[i]=="range" or bzz[i]=="Range":
                    f+="range("
                    ff+="range("
                elif bzz[i]=="str" or bzz[i]=="eval" or bzz[i]=="evil" or bzz[i]=="Evil" or bzz[i]=="star":
                    f+=bzz[i]
                    f+='('
                    ff+=bzz[i]
                    ff+='('
                elif bzz[i]=="stop":
                    break
                    exit()
                elif bzz[i]=="clean":
                    bzz=[]
                    f+=""
                    ff+=""
                elif bzz[i]=="start" and bzz[i+1]=="program":
                    output()
                else:
                    f+=bzz[i]
                    f+=" "
                    ff+=bzz[i]
                    ff+=" "
            f+="\n"
            f+="plant.close()"
            xyz=Label(vc5,text=ff,textvariable=ff,bd=1,relief="solid",width=20,height=4,anchor=NW,justify=LEFT)
            xyz.place(x=40,y=40)
        run=Button(vc5,text="RUN",padx=50,fg="gray",bg="oliveDrab1",command=output)
        run.place(x=350,y=150)
        ex=Button(vc5,text="continue",fg="black",bg="tomato",command=vc5.quit)
        ex.place(x=200,y=200)
        z()
        vc5.mainloop()

def li():
    global vc01
    cur.execute("select username,password,file from vc;")
    cur_=cur.fetchall()
    usn=z_1.get()
    pasn=str(z_2.get())
    oip=0
    yui=0
    global fill1
    global bbh
    for coss in range(0,len(cur_)):
        bbh=cur_[coss][0]
        hbb=str(cur_[coss][1])
        fill1=cur_[coss][2]
        if len(usn)==len(bbh):
            for oss in range(0,len(bbh)):
                if usn[oss]==bbh[oss]:
                    oip+=1
            if oip==len(usn) and oip==len(bbh):
                for iv in range(0,len(pasn)):
                    if pasn[iv]==hbb[iv]:
                        yui+=1
                if yui==len(pasn) and yui==len(hbb):
                    vc01=Tk()
                    vc01.geometry("500x250")
                    vc01.title("choosing file")
                    Label(vc01,text="Choose Your File",fg="black",font=("Apple Chancery",20)).pack()
                    Button(vc01,text="| + | New File",fg="black",bd=2,relief="raised",font=("Georgia",23),padx=35,command=project).place(x=225,y=200)
                else:
                    saw=Label(vc0,text="enter valid username and password",font=("Georgia",15)).place(x=200,y=250)
                    

def p():
    global vc4
    vc4=Tk()
    if (int(q)%int(a_.get())==0):
        import random
        x1=random.randint(10000,99999)
        vc4.title("Password")
        vc4.geometry("500x250")
        vc4.configure(bg="turquoise")
        Label(vc4,text="",bg="turquoise").pack()
        a_password=Label(vc4,text=x1,textvariable=x1,bg="turquoise",justify=LEFT)
        a_password.place(x=200,y=50)
        Label(vc4,text="Your password is",font=("Comic Sans MS",14),bg="turquoise").pack()
        next=Button(vc4,text="next",bg="green",fg="black",font=("Georgia",23),command=project,padx=35)
        next.place(x=200,y=150)
        Button(vc4,text="back",bg="pink",fg="black",font=("Georgia",23),padx=35,command=otp).pack(side=LEFT)
        Button(vc4,text="Exit",bg="red",fg="black",font=("Georgia",23),padx=35,command=vc4.destroy).pack(side=RIGHT)
    import mysql.connector as m
    con=m.connect(host="localhost",user="root",password="12dhanyatha")
    cur=con.cursor()
    name=b.get()
    pas=x1
    cur.execute("use voicecoding;") 
    z='''INSERT INTO vc (email_id,username,password) VALUES(%s,%s,%s)'''
    recordTuple = (re,name,pas)
    cur.execute(z,recordTuple)
    cur.execute("select * from vc;")
    cur.fetchall()
    con.commit()

def otp():
    global vc3
    vc3=Tk()
    #vc3.geometry("600x425")
    global a
    global b
    hub2=str(a.get())
    hub=str(b.get())
    if  (len(hub)<=1):
        global sigus
        sigus=Label(vc3,text="enter valid username",font=("Comic Sans MS",10),fg="tomato",bg="turquoise")
        sigus.pack(expand=1)
    import smtplib
    import random
    se="mrpythonvoicecoder@gmail.com"
    global re
    re=str(hub2)+"@gmail.com"
    password="poojashree"
    m="OTP is "
    global q
    q=str(random.randint(1000,9999))
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(se,password)
    server.sendmail(se,re,m+q)
    global a_
    vc3.title("Password OTP")
    vc3.geometry("600x425")
##    photo= PhotoImage(file="/Users/santhosh/Desktop/kg.png")
##    background_label = Label(vc3, image=photo)
##    background_label.place(x=0, y=0, relwidth=1, relheight=1)
##    background_label.image = photo
    Label(vc3,text="OTP",font=("Comic Sans MS",14),bg="turquoise").pack()
    a_=tkinter.Entry(vc3,bg="white")
    a_.place(x=298,y=80)
    Button(vc3,text="next",bg="green",fg="black",font=("Georgia",23),padx=35,command=p).pack(side=RIGHT)
    Button(vc3,text="back",bg="white",fg="black",font=("Georgia",23),padx=35,command=vc3.destroy).pack(side=LEFT)
    Button(vc3,text="Exit",bg="red",fg="black",font=("Georgia",23),padx=35,command=vc2.destroy).pack(side=RIGHT)

def login():
    global z
    global vc0
    vc0=Tk()
    vc0.title("LOGIN")
    
    vc0.geometry("600x425")
##    photo = PhotoImage(file="/Users/santhosh/Desktop/python.png")
##    background_label = Label(vc, image=photo)
##    background_label.place(x=0, y=0, relwidth=1, relheight=1)
##    background_label.image = photo

    Label(vc0,text="Login",fg="black",font=("Apple Chancery",30)).pack()
    Label(vc0,text="USER NAME:",font=("Apple Chancery",20)).place(x=90,y=100)
    Label(vc0,text="PASSWORD:",font=("Apple Chancery",20)).place(x=90,y=170)
    global z_1
    global z_2
    z_1=Entry(vc0,bg="white")
    z_1.place(x=250,y=110)
    z_2=Entry(vc0,bg="white",show="*")
    z_2.place(x=250,y=170)
    
    Button(vc0,text="Log in",bg="green",fg="black",font=("Georgia",23),padx=35,command=li).place(x=225,y=300)
    Button(vc0,text="back",bg="pink",fg="black",font=("Georgia",23),padx=35,command=lrs).pack(side=LEFT)
def signin():
    global vc2
    vc1.destroy()
    vc2=Tk()
    vc2.title("SIGNIN")
    vc2.geometry("600x425")
    photo = PhotoImage(file="/Users/santhosh/Desktop/kg.png")
    background_label = Label(vc2, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = photo
    Label(vc2,text="Sign in",fg="black",bd=2,relief="raised",font=("Apple Chancery",30)).pack()
    global a
    global b
    Label(vc2,text="EMAIL:",bd=2,relief="raised",font=("Apple Chancery",20)).place(x=90,y=100)
    Label(vc2,text="USER NAME:",bd=2,relief="raised",font=("Apple Chancery",20)).place(x=90,y=170)
    #Label(vc2,text="username must contain character ",font=("Comic Sans MS",15)).place(x=200,y=250)
    a=tkinter.Entry(vc2,bg="white")
    a.place(x=250,y=110)
    b=tkinter.Entry(vc2,bg="white")
    b.place(x=250,y=180)
    Button(vc2,text="Sign in",fg="black",bd=2,relief="raised",font=("Georgia",23),padx=35,command=otp).place(x=225,y=300)
    Button(vc2,text="Exit",fg="black",bd=2,relief="raised",font=("Georgia",23),padx=35,command=vc2.destroy).place(x=480,y=370)

def lrs():
    global vc1
    vc.destroy()
    vc1=Tk()
    vc1.title("LOGIN or SIGNIN")
    vc1.geometry("600x425")
    global photo
    global  background_label
    photo = PhotoImage(file="/Users/santhosh/Desktop/kg.png")
    background_label = Label(vc1, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = photo
    Label(vc1,text="Login or Sign in",fg="black",bd=2,relief="raised",font=("Apple Chancery",30)).pack()
    Button(vc1,text="Log in",fg="black",font=("Georgia",23),bd=2,relief="solid",padx=35,command=login).place(x=220,y=170)
    Button(vc1,text="Sign in",fg="black",font=("Georgia",23),padx=35,bd=2,relief="solid",command=signin).place(x=220,y=250)
    Button(vc1,text="Exit",bg="red",fg="black",font=("calibri",20),bd=2,relief="solid",padx=35,command=vc1.destroy).place(x=500,y=380)
Button(vc,text="start",bg="white",fg="black",bd=2,relief="solid",font=("Georgia",23),padx=35,command=lrs).place(x=225,y=250)
Button(vc,text="Exit",bg="red",bd=2,relief="solid",fg="black",font=("Georgia",23),padx=35,command=vc.destroy).place(x=500,y=550)


vc.mainloop()
