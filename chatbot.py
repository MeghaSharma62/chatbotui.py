from tkinter import *
root = Tk()
def send():
    send="You :"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hello") :
        txt.insert(END,"\n"+"\t"+"computer :hii")
    elif (e.get()=="hii"):
        txt.insert(END,"\n"+"computer :how can I help you today?")
    elif (e.get()=="unable to use data"):
        txt.insert(END,"\n"+"\t"+"computer:are you at the problematic location?")
    elif (e.get()=="yes"):
        txt.insert(END,"\n"+"computer :please make sure that you are in good signal")
    elif (e.get()=="ok"):
        txt.insert(END,"\n"+"computer:any other problem you can solve by calling in customer care thank you")
    elif (e.get()=="thankyou"):
        txt.insert(END,"n\""+"computer:most welcome")
    else:
        txt.insert(END,"\n"+"computer :sorry i didn't get it")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=50)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")