import customtkinter as ctk
app = ctk.CTk()
app.title("New calculator 6.0 beta test")
app.iconbitmap('$RGWODJ2.ico')
ctk.set_appearance_mode('dark')
v= ctk.CTkEntry(master=app,width=450,height=2)
v1=ctk.CTkLabel(master=app,width=450,text_color="green",text="сдесь будет выводится ровное",font=(app,20))


def b():
    v.insert(ctk.END,0)
def b1():
    v.insert(ctk.END,1)
def b2():
    v.insert(ctk.END,2)
def b3():
    v.insert(ctk.END,3)
def b4():
    v.insert(ctk.END,4)
def b5():
    v.insert(ctk.END,5)
def b6():
    v.insert(ctk.END,6)
def b7():
    v.insert(ctk.END,7)
def b8():
    v.insert(ctk.END,8)
def b9():
    v.insert(ctk.END,9)
def b10():
    v.insert(ctk.END,"/")
def b11():
    v.insert(ctk.END,"*")
def b12():
    v.insert(ctk.END,"+")
def b13():
    v.insert(ctk.END,"-")
def b14():
    p=(v.get())
    pass1=(eval(p))
    v1.configure(text=str(pass1))
def b15():
    v.delete(0,ctk.END)
def r():
    ctk.set_appearance_mode('dark')
def r1():
    ctk.set_appearance_mode('light')

x = ctk.CTkCheckBox(master=app,text="light",hover=True,command=r1,offvalue="dark",onvalue='light')
x1= ctk.CTkCheckBox(master=app,text="dark",hover=True,command=r)

v2=ctk.CTkLabel(master=app,text='math numbers',width=160,font=(app,20))
v3=ctk.CTkLabel(master=app,text='math function',width=160,font=(app,20))
v4=ctk.CTkLabel(master=app,text='math symbols',width=160,font=(app,20))
v14=ctk.CTkButton(master=app,text='0',width=360,hover=True,height=10,font=(app,30),command=(b))
v5=ctk.CTkButton(master=app,text='1',width=360,hover=True,height=10,font=(app,30),command=b1)
v6=ctk.CTkButton(master=app,text='2',width=360,hover=True,height=10,font=(app,30),command=b2)
v7=ctk.CTkButton(master=app,text='3',width=360,hover=True,height=10,font=(app,30),command=b3)
v8=ctk.CTkButton(master=app,text='4',width=360,hover=True,height=10,font=(app,30),command=b4)
v9=ctk.CTkButton(master=app,text='5',width=360,hover=True,height=10,font=(app,30),command=b5)
v10=ctk.CTkButton(master=app,text='6',width=360,hover=True,height=10,font=(app,30),command=b6)
v11=ctk.CTkButton(master=app,text='7',width=360,hover=True,height=10,font=(app,30),command=b7)
v12=ctk.CTkButton(master=app,text='8',width=360,hover=True,height=10,font=(app,30),command=b8)
v13=ctk.CTkButton(master=app,text='9',width=360,hover=True,height=10,font=(app,30),command=b9)
v15=ctk.CTkButton(master=app,text='/',width=360,hover=True,height=10,font=(app,30),command=b10)
v16=ctk.CTkButton(master=app,text='*',width=360,hover=True,height=10,font=(app,30),command=b11)
v17=ctk.CTkButton(master=app,text='+',width=360,hover=True,height=10,font=(app,30),command=b12)
v18=ctk.CTkButton(master=app,text='-',width=360,hover=True,height=10,font=(app,30),command=b13)
v19=ctk.CTkButton(master=app,text='=',width=360,hover=True,height=10,font=(app,30),command=b14)
v21=ctk.CTkButton(master=app,text='delete',width=120,hover=True,command=b15)
v1.grid(row=1,column=6)
v21.grid(row=1,column=7)
x.grid(row=1, column=1)
x1.grid(row=2,column=1)
v2.grid(row=3,column=5)
v14.grid(row=4,column=5,pady=10)
v5.grid(row=5,column=5,pady=10)
v6.grid(row=6,column=5,pady=10)
v7.grid(row=7,column=5,pady=10)
v8.grid(row=8,column=5,pady=10)
v9.grid(row=10,column=5,pady=10)
v10.grid(row=11,column=5,pady=10)
v11.grid(row=12,column=5,pady=10)
v12.grid(row=13,column=5,pady=10)
v13.grid(row=14,column=5,pady=10)
v3.grid(row=3,column=6)
v19.grid(row=4,column=6)
v17.grid(row=5,column=6)
v18.grid(row=6,column=6)
v16.grid(row=8,column=6)
v15.grid(row=7,column=6)
v.grid(row=2,column=6,padx=50)
v4.grid(row=3,column=7)
app.mainloop()
