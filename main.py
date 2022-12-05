import random
import sqlite3
import string
from time import strftime
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

main = Tk()

main.geometry('1100x610')
main.resizable(0,0)
main.title("SMART CAFE SYSTEM")
#images
homeimg= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/home.jpg")
logoimg= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/logo.png")
logoimg2= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/logo2.png")
logoimg3= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/logo3.png")
carticon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/cart.png")
contacticon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/comment.png")
abouticon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/info.png")
startimg= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/start.png")
homeicon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/home.png")
cupicon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/offer.png")
accicon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/account.png")
suppicon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/support.png")
logouticon= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/logout.png")
backimg= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/back.png")
product1= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/Black.png")
product2= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/Rist.png")
product3 = ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/ColdBrew1.png")
product4= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/ColdBrew2.png")
product5= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/capp.png")
product6= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/latte.png")
product7= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/espress.png")
product8= ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/mocha.png")
chimg = ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/ch.png")
cartimg = ImageTk.PhotoImage(file="/home/ak/Downloads/scs/images/cart2.png")
aboutimg=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/about.jpg')
c1img=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/c1.png')
c2img=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/c2.png')
pbgimg=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/pbg.png')
ccimg=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/cc.png')
dpimg=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/images.jpeg')
lgimg=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/padlock.png')
ssimg=ImageTk.PhotoImage(file='/home/ak/Downloads/scs/images/ss.png')
#frames
purchaseframe=Frame(main).place(x=0,y=0)
payframe=Frame(main).place(x=0,y=0)
moneyfrm=Frame(main).place(x=0,y=0)
name=StringVar()
email=StringVar()
sub=StringVar()
msg=StringVar()
cname=StringVar()
cmob=StringVar()
croom=StringVar()
total_price=IntVar()
Rb=IntVar()
Rbn=StringVar()
new_bill=StringVar()
bill_date=StringVar()
lgroom=StringVar()
bill_date.set(strftime('%x %H:%M:%S %p '))

def Guest():
    
    def random_bill(stringLength):
            lettersAndDigits = string.ascii_letters.upper() + string.digits
            strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
            return ('AK'+strr)
 
    new_bill.set(random_bill(8))
    def product():
        global coffee_list,qty_1,qty_2,qty_3,qty_4,qty_5,qty_6,qty_7,qty_8
        global price_1,price_2,price_3,price_4,price_5,price_6,price_7,price_8
        coffee_list=[]
        qty_1=IntVar()
        qty_2=IntVar()
        qty_3=IntVar()
        qty_4=IntVar()
        qty_5=IntVar()
        qty_6=IntVar()
        qty_7=IntVar()
        qty_8=IntVar()
        price_1=IntVar()
        price_2=IntVar()
        price_3=IntVar()
        price_4=IntVar()
        price_5=IntVar()
        price_6=IntVar()
        price_7=IntVar()
        price_8=IntVar()

        label1=Label(main,bg='white',image=pbgimg).place(x=-1,y=-1)
        fm=LabelFrame(purchaseframe,width=220,height=260,bg='white').place(x=10,y=150)
        plbl=Label(purchaseframe,text='COFFEE',image=logoimg2,compound='left',bg='white',font=("",14,'bold')).place(x=50,y=135)
        plbl=Label(purchaseframe,text='Categories',bg='white',font=("",14,'bold')).place(x=30,y=210)
        hotbtn=Button(fm,text='• Hot Coffee',command=hot,bg='white',bd=0,highlightthickness=0,font=("",10,'bold'),cursor='hand2').place(x=45,y=260)
        coldbtn=Button(fm,text='• Cold Coffee',command=cold,bg='white',bd=0,highlightthickness=0,font=("",10,'bold'),cursor='hand2').place(x=45,y=310)
        plbl=Label(purchaseframe,text='Sort By :',bg='white',fg='gray',font=("",11,'bold')).place(x=730,y=202)
        ppbtn=Button(purchaseframe,text='Popular',command=popular,bg='white',bd=0,highlightthickness=0,font=("",10,'bold'),cursor='hand2').place(x=860,y=200)
        newbtn=Button(purchaseframe,text='New  |',command=newest,bg='white',bd=0,highlightthickness=0,font=("",10,'bold'),cursor='hand2').place(x=800,y=200)
        backbtn=Button(purchaseframe,image=backimg,cursor='hand2',activebackground='white',bd=0,command=home,bg='white',highlightthickness=0).place(x=20,y=25)
        buybtn=Button(purchaseframe,text='Cart',image=cartimg,compound='left',font=("",12,'bold'),cursor='hand2',activebackground='white',bd=0,command=pay,bg='white',highlightthickness=0).place(x=950,y=25)
        hot()
    def hot():
        def add1():
                qt=qty_1.get()+1
                qty_1.set(qt)  
                pr1=199*qty_1.get()
                price_1.set(pr1)     
        def add2():
                qt=qty_2.get()+1
                qty_2.set(qt)
                pr1=169*qty_2.get()
                price_2.set(pr1)
        def sub1():
                qt=qty_1.get()-1
                qty_1.set(qt)
                pr1=199*qty_1.get()
                price_1.set(pr1)            
        def sub2():
                qt=qty_2.get()-1
                qty_2.set(qt)
                pr1=169*qty_2.get()
                price_2.set(pr1)
        price_1.set(199)
        price_2.set(169)
        lbl=Label(purchaseframe,text='Hot Coffee ',width=20,bg='white',font=("",14,'bold')).place(x=270,y=210)
        lbl=Label(purchaseframe,text='(2 Items)',bg='white',fg='gray',font=("",12,'bold')).place(x=460,y=213)
        prodfrm1=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=300,y=280)
        prodfrm2=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=600,y=280)
        prodin1=LabelFrame(prodfrm1,bg='white',bd=0,width=216,height=150).place(x=307,y=288)
        prodin2=LabelFrame(prodfrm2,bg='white',bd=0,width=216,height=150).place(x=607,y=288)
        product_1=Label(prodin1,image=product1,bg='white').place(x=330,y=295)
        product_2=Label(prodin2,image=product2,bg='white').place(x=630,y=295)
        prodname1=Label(prodfrm1,text='Black Coffee',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=450)
        prodname2=Label(prodfrm2,text='Ristretto cafe',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=450)
        pr1=Label(prodfrm1,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=495)
        pr2=Label(prodfrm2,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=495)
        price1=Label(prodfrm1,textvariable=price_1,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=350,y=495)
        price2=Label(prodfrm2,textvariable=price_2,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=650,y=495)
        qty1=Label(prodfrm1,textvariable=qty_1,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=430,y=490,width=40,height=30)
        qty2=Label(prodfrm2,textvariable=qty_2,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=730,y=490,width=40,height=30)
        addbtn1=Button(prodfrm1,text='+',command=add1,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=470,y=490)
        subbtn1=Button(prodfrm1,text='-',command=sub1,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=400,y=490)
        addbtn2=Button(prodfrm1,text='+',command=add2,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=770,y=490)
        subbtn2=Button(prodfrm1,text='-',command=sub2,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=700,y=490)
        cart1=Button(prodfrm1,text='Add to Cart',command=AddG1,bg='#3e5348',fg='white',bd=0,highlightthickness=2,font=("",11,'bold'),width=17).place(x=317,y=540)
        cart2=Button(prodfrm1,text='Add to Cart',command=AddG2,bg='#3e5348',fg='white',bd=0,highlightthickness=2,font=("",11,'bold'),width=17).place(x=617,y=540)

    def cold():
        def add3():
                qt=qty_3.get()+1
                qty_3.set(qt)
                pr1=195*qty_3.get()
                price_3.set(pr1)
        def add4():
                qt=qty_4.get()+1
                qty_4.set(qt)
                pr1=185*qty_4.get()
                price_4.set(pr1)
        def sub3():
                qt=qty_3.get()-1
                qty_3.set(qt)
                pr1=195*qty_3.get()
                price_3.set(pr1)
        def sub4():
                qt=qty_4.get()-1
                qty_4.set(qt)
                pr1=185*qty_4.get()
                price_4.set(pr1)
        price_3.set(195)
        price_4.set(185)
        lbl=Label(purchaseframe,text='Cold Coffee ',width=20,bg='white',font=("",14,'bold')).place(x=270,y=210)
        lbl=Label(purchaseframe,text='(2 Items)',bg='white',fg='gray',font=("",12,'bold')).place(x=460,y=213)
        prodfrm1=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=300,y=280)
        prodfrm2=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=600,y=280)
        prodin1=LabelFrame(prodfrm1,bg='white',bd=0,width=216,height=150).place(x=307,y=288)
        prodin2=LabelFrame(prodfrm2,bg='white',bd=0,width=216,height=150).place(x=607,y=288)
        product_1=Label(prodin1,image=product3,bg='white').place(x=350,y=295)
        product_2=Label(prodin2,image=product4,bg='white').place(x=645,y=295)
        prodname1=Label(prodfrm1,text='Cold Brew',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=450)
        prodname2=Label(prodfrm2,text='Cold Brew Cream',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=450)
        pr3=Label(prodfrm1,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=495)
        pr4=Label(prodfrm2,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=495)
        price3=Label(prodfrm1,textvariable=price_3,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=350,y=495)
        price4=Label(prodfrm2,textvariable=price_4,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=650,y=495)
        qty3=Label(prodfrm1,textvariable=qty_3,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=430,y=490,width=40,height=30)
        qty4=Label(prodfrm2,textvariable=qty_4,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=730,y=490,width=40,height=30)
        addbtn3=Button(prodfrm1,text='+',command=add3,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=470,y=490)
        subbtn3=Button(prodfrm1,text='-',command=sub3,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=400,y=490)
        addbtn4=Button(prodfrm1,text='+',command=add4,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=770,y=490)
        subbtn4=Button(prodfrm1,text='-',command=sub4,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=700,y=490)
        
        cart3=Button(prodfrm1,text='Add to Cart',command=AddG3,bg='#3e5348',fg='white',bd=0,highlightthickness=2,font=("",11,'bold'),width=17).place(x=317,y=540)
        cart4=Button(prodfrm1,text='Add to Cart',command=AddG4,bg='#3e5348',fg='white',bd=0,highlightthickness=2,font=("",11,'bold'),width=17).place(x=617,y=540)

    def newest():
        def add5():
                qt=qty_5.get()+1
                qty_5.set(qt)  
                pr1=209*qty_5.get()
                price_5.set(pr1)
        def add6():
                qt=qty_6.get()+1
                qty_6.set(qt)  
                pr1=179*qty_6.get()
                price_6.set(pr1)
        def sub5():
                qt=qty_5.get()-1
                qty_5.set(qt) 
                pr1=209*qty_5.get()
                price_5.set(pr1)           
        def sub6():
                qt=qty_6.get()-1
                qty_6.set(qt)
                pr1=179*qty_6.get()
                price_6.set(pr1)
        price_5.set(209)
        price_6.set(179)
        lbl=Label(purchaseframe,text='New Coffee ',width=20,bg='white',font=("",14,'bold')).place(x=270,y=210)
        lbl=Label(purchaseframe,text='(2 Items)',bg='white',fg='gray',font=("",12,'bold')).place(x=460,y=213)
        prodfrm1=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=300,y=280)
        prodfrm2=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=600,y=280)
        prodin1=LabelFrame(prodfrm1,bg='white',bd=0,width=216,height=150).place(x=307,y=288)
        prodin2=LabelFrame(prodfrm2,bg='white',bd=0,width=216,height=150).place(x=607,y=288)
        product_1=Label(prodin1,image=product5,bg='white').place(x=345,y=295)
        product_2=Label(prodin2,image=product6,bg='white').place(x=635,y=300)
        prodname1=Label(prodfrm1,text='Cappuccino',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=450)
        prodname2=Label(prodfrm2,text='Latte Coffee',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=450)
        pr5=Label(prodfrm1,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=495)
        pr6=Label(prodfrm2,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=495)
        price5=Label(prodfrm1,textvariable=price_5,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=350,y=495)
        price6=Label(prodfrm2,textvariable=price_6,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=650,y=495)
        qty5=Label(prodfrm1,textvariable=qty_5,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=430,y=490,width=40,height=30)
        qty6=Label(prodfrm2,textvariable=qty_6,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=730,y=490,width=40,height=30)
        addbtn5=Button(prodfrm1,text='+',command=add5,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=470,y=490)
        subbtn5=Button(prodfrm1,text='-',command=sub5,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=400,y=490)
        addbtn6=Button(prodfrm1,text='+',command=add6,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=770,y=490)
        subbtn6=Button(prodfrm1,text='-',command=sub6,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=700,y=490)
          
        cart5=Button(prodfrm1,text='Add to Cart',bg='#3e5348',command=AddG5,fg='white',bd=0,highlightthickness=2,font=("",11,'bold'),width=17).place(x=317,y=540)
        cart6=Button(prodfrm1,text='Add to Cart',bg='#3e5348',command=AddG6,fg='white',bd=0,highlightthickness=2,font=("",11,'bold'),width=17).place(x=617,y=540)

    def popular():
        def add7():
                qt=qty_7.get()+1
                qty_7.set(qt)
                pr1=175*qty_7.get()
                price_7.set(pr1)
        def add8():
                qt=qty_8.get()+1
                qty_8.set(qt)
                pr1=195*qty_8.get()
                price_8.set(pr1)
        def sub7():
                qt=qty_7.get()-1
                qty_7.set(qt)
                pr1=175*qty_7.get()
                price_7.set(pr1)
        def sub8():
                qt=qty_8.get()-1
                qty_8.set(qt)
                pr1=195*qty_8.get()
                price_8.set(pr1)
        price_7.set(175)
        price_8.set(195)
        lbl=Label(purchaseframe,text='  Popular',width=20,bg='white',font=("",14,'bold')).place(x=270,y=210)
        lbl=Label(purchaseframe,text='(2 Items)',bg='white',fg='gray',font=("",12,'bold')).place(x=460,y=213)
        prodfrm1=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=300,y=280)
        prodfrm2=LabelFrame(purchaseframe,bg='#3e5348',bd=0,width=230,height=300).place(x=600,y=280)
        prodin1=LabelFrame(prodfrm1,bg='white',bd=0,width=216,height=150).place(x=307,y=288)
        prodin2=LabelFrame(prodfrm2,bg='white',bd=0,width=216,height=150).place(x=607,y=288)
        product_1=Label(prodin1,image=product7,bg='white').place(x=330,y=293)
        product_2=Label(prodin2,image=product8,bg='white').place(x=635,y=295)
        prodname1=Label(prodfrm1,text='Espress Coffee',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=450)
        prodname2=Label(prodfrm2,text='Mocha Coffee',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=450)
        pr7=Label(prodfrm1,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=310,y=495)
        pr8=Label(prodfrm2,text='Rs.',bg='#3e5348',fg='white',font=("",11,'bold')).place(x=610,y=495)
        price7=Label(prodfrm1,textvariable=price_7,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=350,y=495)
        price8=Label(prodfrm2,textvariable=price_8,bg='#3e5348',fg='white',font=("",10,'bold')).place(x=650,y=495)
        qty7=Label(prodfrm1,textvariable=qty_7,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=430,y=490,width=40,height=30)
        qty8=Label(prodfrm2,textvariable=qty_8,bg='#3e5348',fg='white',font=("",12,'bold')).place(x=730,y=490,width=40,height=30)
        addbtn7=Button(prodfrm1,text='+',command=add7,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=470,y=490)
        subbtn7=Button(prodfrm1,text='-',command=sub7,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=400,y=490)
        addbtn8=Button(prodfrm1,text='+',command=add8,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=770,y=490)
        subbtn8=Button(prodfrm1,text='-',command=sub8,bg='#3e5348',fg='white',bd=0,font=("",10,'bold')).place(x=700,y=490)
        
        cart7=Button(prodfrm1,text='Add to Cart',bg='#3e5348',fg='white',bd=0,command=AddG7,highlightthickness=2,font=("",11,'bold'),width=17).place(x=317,y=540)
        cart8=Button(prodfrm1,text='Add to Cart',bg='#3e5348',fg='white',bd=0,command=AddG8,highlightthickness=2,font=("",11,'bold'),width=17).place(x=617,y=540)

    def AddG1():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Black Coffee",str(price_1.get()),qty_1.get()])
            messagebox.showinfo("Product Status","Black Coffee("+str(qty_1.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Black Coffee"+str(qty_1.get())+") is not added to the cart.")
    def AddG2():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Ristretto Cafe",str(price_2.get()),qty_2.get()])
            messagebox.showinfo("Product Status","Ristretto cafe("+str(qty_2.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Ristretto Cafe"+str(qty_2.get())+") is not added to the cart.")
    def AddG3():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Cold Brew",str(price_3.get()),qty_3.get()])
            messagebox.showinfo("Product Status","Cold Brew("+str(qty_3.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cold Brew"+str(qty_3.get())+") is not added to the cart.")
    def AddG4():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Cold Brew Cream",str(price_4.get()),qty_4.get()])
            messagebox.showinfo("Product Status","Cold Brew Cream("+str(qty_4.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cold Brew Cream"+str(qty_4.get())+") is not added to the cart.")
    def AddG5():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Cappuccino",str(price_5.get()),qty_5.get()])
            messagebox.showinfo("Product Status","Cappuccino("+str(qty_5.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cappuccino"+str(qty_5.get())+") is not added to the cart.")
    def AddG6():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Latte Coffee",str(price_6.get()),qty_6.get()])
            messagebox.showinfo("Product Status","Latte Coffee("+str(qty_6.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Latte Coffee"+str(qty_6.get())+") is not added to the cart.")
    def AddG7():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Espress Coffee",str(price_7.get()),qty_7.get()])
            messagebox.showinfo("Product Status","Espress Coffee("+str(qty_7.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Espress Coffee"+str(qty_7.get())+") is not added to the cart.")
    def AddG8():
        global coffee_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            coffee_list.append(["Mocha coffee",str(price_8.get()),qty_8.get()])
            messagebox.showinfo("Product Status","Mocha coffee("+str(qty_8.get())+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Mocha coffee"+str(qty_8.get())+") is not added to the cart.")
    def pay():
        op=messagebox.askyesno("Confirmation !!!","Are you sure that you have finished shopping ?")
        coffee_price=0
        for i in range(len(coffee_list)):
            coffee_price+=int(coffee_list[i][1])
        total_price.set(coffee_price)
        def pay2():
            if cname.get()=="" or cmob.get()=="" or croom.get()=="":
                messagebox.showinfo("Ooops !!!","Please Select fill the Details...!")
            else:
                label1=Label(payframe,bg='white',width=1100,height=610).place(x=0,y=0)
                label2=Label(payframe,bg='white',image=c1img).place(x=-1,y=50)
                backbtn=Button(payframe,image=backimg,cursor='hand2',activebackground='white',bd=0,command=home,bg='white',highlightthickness=0).place(x=20,y=25)
                nmlbl=Label(payframe,text='Billing Info',font=("",24,'bold'),bg='white').place(x=470,y=25)
                nlbl=Label(payframe,text='Payment Method ',bg='white',fg='#b6782e',font=("",20,'bold')).place(x=610,y=115)
                price=Label(moneyfrm,text="Total Price : Rs."+str(total_price.get()),bg='#b6782e',fg='white',font=("",16,'bold')).place(x=600,y=160,width=380,height=100)
                ch1=Radiobutton(moneyfrm,text='  Net Banking',variable=Rb,value=1,highlightbackground='white',highlightcolor='white',cursor='hand2',bg='white',font=("",12,'bold')).place(x=630,y=280)
                ch2=Radiobutton(moneyfrm,text='  UPI ',value=2,variable=Rb,highlightbackground='white',highlightcolor='white',cursor='hand2',bg='white',font=("",12,'bold')).place(x=630,y=330)
                ch3=Radiobutton(moneyfrm,text='  Cash ',value=3,variable=Rb,bg='white',highlightbackground='white',highlightcolor='white',cursor='hand2',font=("",12,'bold')).place(x=630,y=380)
                ch4=Radiobutton(moneyfrm,text=' Credit/Debit Card',variable=Rb,value=4,highlightbackground='white',highlightcolor='white',cursor='hand2',bg='white',font=("",12,'bold')).place(x=630,y=430)
                def billing():
                    if Rb.get()==0 :
                        messagebox.showinfo("Ooops !!!","Please Select fill the Details...!")
                    else :
                        if Rb.get()==1:
                            Rbn.set(" Net Banking")
                            Bill()
                        elif Rb.get()==2:
                            Rbn.set(" UPI")
                            Bill()
                        elif Rb.get()==3:
                            Rbn.set(" Cash")
                            Bill()
                        elif Rb.get()==4:
                            Rbn.set(" Card")
                            Bill()
                paybtn=Button(moneyfrm,text="Pay Now",cursor='hand2',command=billing,font=("",13,'bold'),fg='white',highlightbackground='#b6782e',highlightthickness=2,highlightcolor='#b6782e',bg='#b6782e',bd=0,width=30).place(x=600,y=500,height=35)          
      
        if op :
            label1=Label(payframe,bg='white',width=1100,height=610).place(x=0,y=0)
            label2=Label(payframe,bg='white',image=c2img).place(x=590,y=100)
            backbtn=Button(payframe,image=backimg,cursor='hand2',activebackground='white',bd=0,command=home,bg='white',highlightthickness=0).place(x=20,y=25)
            nmlbl=Label(payframe,text='Billing Info',font=("",24,'bold'),bg='white').place(x=470,y=25)
            nlbl=Label(payframe,text='Personal Detail',bg='white',fg='#b6782e',font=("",20,'bold')).place(x=260,y=115)
            cnamelbl=Label(payframe,text='Name ',bg='white',font=("",13,'bold')).place(x=250,y=180)
            cnametxt=Entry(payframe,textvariable=cname,width=25,highlightthickness=2,bd=0,highlightbackground='#6b6a69',highlightcolor='#b6782e',bg='white',font=("",11,'bold')).place(x=250,y=220,height=30)
            cmobilebl=Label(payframe,text='Mobile No ',bg='white',font=("",13,'bold')).place(x=250,y=270)
            cmobiletxt=Entry(payframe,textvariable=cmob,width=25,highlightthickness=2,bd=0,highlightbackground='#6b6a69',highlightcolor='#b6782e',bg='white',font=("",11,'bold')).place(x=250,y=310,height=30)
            croomlbl=Label(payframe,text='Room No ',bg='white',font=("",13,'bold')).place(x=250,y=360)
            croomtxt=Entry(payframe,textvariable=croom,state='readonly',width=25,highlightthickness=2,bd=0,highlightbackground='#6b6a69',highlightcolor='#b6782e',bg='white',font=("",11,'bold')).place(x=250,y=400,height=30)
            paybtn=Button(payframe,text="Continue",cursor='hand2',command=pay2,font=("",13,'bold'),fg='white',highlightbackground='#b6782e',highlightthickness=2,highlightcolor='#b6782e',bg='#b6782e',bd=0,width=19).place(x=250,y=480,height=35)          
    def Bill():
        label1=Label(main,bg='white',width=1100,height=620).place(x=0,y=0) 
        inv=Label(main,text='Payment summary',font=("",20,'bold'),bg='white',fg='green').place(x=200,y=50)  
        tkv=Label(main,text='Thanks You !!!',font=("",20,'bold'),bg='white',fg='green').place(x=730,y=300)
        tkv=Label(main,text='Your Order Will be Delivered Soon',font=("",10,'bold'),bg='white',fg='green').place(x=700,y=350)
        tkv=Label(main,image=chimg,bg='white').place(x=750,y=100) 
        cnbtn=Button(main,text='Track Your Order',highlightthickness=2,cursor='hand2',bd=0,command=order,bg='blue',fg='white',highlightbackground='blue',highlightcolor='blue',font=("",13,'bold'),width=15).place(x=750,y=480,height=40)
        bill_area=LabelFrame(main,bd=0)
        bill_area.place(x=150,y=120,width=400,height=400)
        bill_txt_area=Text(bill_area)
        bill_txt_area.pack(fill=BOTH,expand=1)
        bill_txt_area.insert(END,"\n\t" +cname.get())
        bill_txt_area.insert(END,"\n\n"+"   "+"Room No :"+croom.get()+" \n")
        bill_txt_area.insert(END,"\n"+"   "+"Payment Summary")
        bill_txt_area.insert(END,"\n"+"   "+"--------------------------------------------\n")
        
        if len(coffee_list)>0:
            for i in coffee_list:
                bill_txt_area.insert(END,"   "+str(i[0])+"(Qty:"+str(i[2])+") \t\t\t\t₹ "+str(i[1])+"\n")
            bill_txt_area.insert(END,"\n"+"   "+"Exra Charges \t\t\t\t₹ 0")
            bill_txt_area.insert(END,"\n"+"   "+"Tax \t\t\t\t₹ 0")
            bill_txt_area.insert(END,"\n\n\n"+"   "+"--------------------------------------------\n")
            bill_txt_area.insert(END,"\n"+"   "+"Total \t\t\t\t₹ "+str(total_price.get()))
            bill_txt_area.insert(END,"\n\n"+"   "+"--------------------------------------------\n")
        save_invoice(bill_txt_area.get("1.0",END))
        bill_txt_area.config(state='disabled',font=("",11),bd=0,highlightthickness=2,highlightbackground='#b6782e',highlightcolor='#b6782e')
    def save_invoice(text):
        conn = sqlite3.connect('/home/ak/Downloads/scs/DB/database.db')
        cursor=conn.cursor()
        cursor.execute('INSERT INTO bill (bill_no,date,bill,name,mob,room,total,status) VALUES(?,?,?,?,?,?,?,?)',(new_bill.get(),bill_date.get(),text,cname.get(),cmob.get(),croom.get(),total_price.get(),"Pending"))
        conn.commit()
        conn.close()
    def order():
        conn = sqlite3.connect("/home/ak/Downloads/scs/DB/database.db")
        cur = conn.cursor()
        cur.execute("select * from bill where bill_no=?",[new_bill.get()])
        row= cur.fetchone()
        label1=Label(main,bg='white',width=1100,height=610).place(x=0,y=0)
        backbtn=Button(main,image=backimg,cursor='hand2',activebackground='white',bd=0,command=account,bg='white',highlightthickness=0).place(x=20,y=25)
        if row!=None:
            label1=Label(main,bg='white',image=logoimg3).place(x=170,y=100)
            label1=Label(main,bg='white',text='Order Details',fg='blue',font=("",11,'bold')).place(x=550,y=120)
            label1=Label(main,bg='white',text='Order Number',fg='gray',font=("",11)).place(x=550,y=160)
            label1=Label(main,bg='white',text='Name',fg='gray',font=("",11)).place(x=550,y=200)
            label1=Label(main,bg='white',text='Date',fg='gray',font=("",11)).place(x=550,y=240)
            label1=Label(main,bg='white',text='Room No',fg='gray',font=("",11)).place(x=550,y=280)
            label1=Label(main,bg='white',text='Total Price(₹)',fg='gray',font=("",11)).place(x=550,y=320)
            
            label1=Label(main,bg='white',text=row[1],font=("",11,'bold')).place(x=800,y=160)
            label1=Label(main,bg='white',text=row[2],font=("",11,'bold')).place(x=800,y=200)
            label1=Label(main,bg='white',text=row[8],font=("",11,'bold')).place(x=800,y=240)
            label1=Label(main,bg='white',text=row[4],font=("",11,'bold')).place(x=800,y=280)
            label1=Label(main,bg='white',text=row[7],font=("",11,'bold')).place(x=800,y=320)
            label1=Label(main,bg='white',text='Order Status',fg='blue',font=("",11,'bold')).place(x=550,y=370)
            label1=Label(main,bg='white',text='Status',fg='gray',font=("",11)).place(x=550,y=410)
            label1=Label(main,bg='white',text=row[6],font=("",11,'bold')).place(x=800,y=410)
            def update():
                conn = sqlite3.connect("/home/ak/Downloads/scs/DB/database.db")
                cur = conn.cursor()
                cur.execute("update bill set status=? where bill_no=?",["Cancelled",new_bill.get()])
                conn.commit()
                conn.close()
                new_bill.set("")
                messagebox.showinfo("Success","Order cancelled !")
                order()
            cancelbtn=Button(main,text='Cancel Order ',command=update,image=carticon,compound='left',bg='#3e5348',fg='white',highlightthickness=2,highlightbackground='#3e5348',font=("",10,'bold'),bd=0).place(x=500,y=500,height=40)
            helpbtn=Button(main,text='Contact Us ',command=contact,image=suppicon,compound='left',bg='#3e5348',fg='white',highlightthickness=2,highlightbackground='#3e5348',font=("",10,'bold'),bd=0).place(x=700,y=500,height=40)

        else:
            label1=Label(main,bg='white',image=logoimg3).place(x=170,y=100)
            label1=Label(main,bg='white',text='No Orders Placed',fg='gray',font=("",20,'bold')).place(x=550,y=300)
    def developer():
        label1=Label(main,bg='white',width=1100,height=610).place(x=0,y=0)
        label1=Label(main,bg='white',image=dpimg).place(x=20,y=20)
        backbtn=Button(main,image=backimg,cursor='hand2',activebackground='white',bd=0,command=account,bg='white',highlightthickness=0).place(x=20,y=25)
        label1=Label(main,text='AK MOORTHI',font=("",28,'bold'),bg='white',fg='#3e5348').place(x=600,y=140)
        label1=Label(main,image=ssimg,bg='white').place(x=850,y=540)
        label1=Label(main,text='REG NO : C21PG188CSC012',font=("",15,'bold'),bg='white').place(x=550,y=330)
        label1=Label(main,text='COURSE : MSC COMPUTER SCIENCE',font=("",15,'bold'),bg='white').place(x=550,y=400)
        label1=Label(main,text='YEAR      : II-YEAR',font=("",15,'bold'),bg='white').place(x=550,y=470)
        label1=Label(main,text='TITLE     : SMART CAFE SYSTEM',font=("",15,'bold'),bg='white').place(x=550,y=260)
    def offer():
        label1=Label(main,bg='white',width=1100,height=610).place(x=0,y=0)
        backbtn=Button(main,image=backimg,cursor='hand2',activebackground='white',bd=0,command=account,bg='white',highlightthickness=0).place(x=20,y=25)
        label1=Label(main,bg='white',image=logoimg3).place(x=170,y=100)
        label1=Label(main,bg='white',text='No Offers Available',fg='gray',font=("",20,'bold')).place(x=550,y=300)
    def home():
        lbl1=Label(main,image=homeimg).place(x=0,y=0) 
        productbtn=Button(main,image=startimg,bg='#ededeb',cursor='hand2',command=product,bd=0,highlightbackground='#ededeb',highlightthickness=0).place(x=50,y=330)
        accbtn=Button(main,text='Account',image=accicon,compound='left',command=account,activebackground='#ededeb',fg='#3e5348',font=("",12,'bold'),bg='#ededeb',cursor='hand2',bd=0,highlightthickness=0).place(x=950,y=30)
    def account():
        label1=Label(main,bg='white',width=1100,height=610).place(x=0,y=0)
        backbtn=Button(main,image=backimg,cursor='hand2',activebackground='white',bd=0,command=home,bg='white',highlightthickness=0).place(x=20,y=25)
        label2=Label(main,bg='white',text='Hey !  '+rows[2],font=("",12,'bold')).place(x=90,y=40)
        fr=LabelFrame(main,bg='white',width=350,height=450).place(x=650,y=100)
        label3=Label(fr,image=logoimg,bg='white',highlightthickness=0).place(x=780,y=120)
        label3=Label(fr,text='Name :',bg='white',justify='right',font=("",12,'bold'),width=10).place(x=680,y=220)
        label3=Label(fr,text=rows[2],bg='white',font=("",12,'bold')).place(x=800,y=220)
        label3=Label(fr,text='Room No:',bg='white',justify='right',width=9,font=("",12,'bold')).place(x=680,y=270)
        label3=Label(fr,text=rows[1],bg='white',font=("",12,'bold')).place(x=800,y=270)
        label3=Label(fr,text='Mobile :',bg='white',justify='right',font=("",12,'bold'),width=10).place(x=680,y=320)
        label3=Label(fr,text=rows[4],bg='white',font=("",12,'bold')).place(x=800,y=320)
        label3=Label(fr,text='E-mail :',bg='white',justify='right',font=("",12,'bold'),width=10).place(x=680,y=370)
        label3=Label(fr,text=rows[3],bg='white',font=("",12,'bold')).place(x=800,y=370)
        label3=Label(fr,text='Address :',bg='white',justify='right',font=("",12,'bold'),width=10).place(x=680,y=420)
        label3=Label(fr,text=rows[5],bg='white',font=("",12,'bold')).place(x=800,y=420)
        savebtn=Button(fr,text="Logout",font=("",12,'bold'),bg='#db5f12',cursor='hand2',fg='white',highlightbackground='#db5f12',highlightthickness=2,bd=0,width=200,image=logouticon,command=login,compound='left').place(x=720,y=480)
        profilebtn=Button(main,text="    Profile",bg='#db5f12',fg='white',cursor='hand2',highlightbackground='#db5f12',highlightthickness=2,bd=0,command=account,image=accicon,compound='left',font=("",12),width=200).place(x=200,y=170,height=40)
        histrybtn=Button(main,text="     Orders",bg='#db5f12',fg='white',cursor='hand2',highlightbackground='#db5f12',highlightthickness=2,bd=0,command=order,image=carticon,font=("",12),compound='left',width=200).place(x=200,y=230,height=40)
        feedbackbtn=Button(main,text="Contact Us",bg='#db5f12',fg='white',cursor='hand2',highlightbackground='#db5f12',highlightthickness=2,bd=0,command=contact,image=suppicon,compound='left',font=("",12),width=200).place(x=200,y=290,height=40)
        aboutbtn=Button(main,text=" About Us",bg='#db5f12',fg='white',cursor='hand2',highlightbackground='#db5f12',highlightthickness=2,bd=0,command=about,image=abouticon,compound='left',font=("",12),width=200).place(x=200,y=350,height=40)
        contactbtn=Button(main,text="Developer",bg='#db5f12',fg='white',cursor='hand2',highlightbackground='#db5f12',highlightthickness=2,bd=0,command=developer,image=contacticon,compound='left',font=("",12),width=200).place(x=200,y=410,height=40)
        offerbtn=Button(main,text="     Offers",bg='#db5f12',fg='white',cursor='hand2',highlightbackground='#db5f12',highlightthickness=2,bd=0,image=cupicon,command=offer,compound='left',font=("",12),width=200).place(x=200,y=470,height=40)   
    def about():
        lbl1=Label(main,image=aboutimg).place(x=0,y=0)
        backbtn=Button(main,image=backimg,bd=0,activebackground='white',cursor='hand2',command=account,bg='white',highlightthickness=0).place(x=20,y=35)
    def contact():
        lbl1=Label(main,bg='white',width=1100,height=610).place(x=0,y=0)
        lbl1=Label(main,bg='white',image=ccimg).place(x=50,y=100)
        backbtn=Button(main,image=backimg,bd=0,activebackground='white',cursor='hand2',command=account,bg='white',highlightthickness=0).place(x=20,y=35)
        lbl11=Label(main,text="Feedback Form ",font=("",20,'bold'),bg='white',fg='#3e5348').place(x=600,y=40)
        lbl11=Label(main,text="_____________________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=580,y=135)
        lbl11=Label(main,text="_____________________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=580,y=210)
        lbl11=Label(main,text="_____________________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=580,y=285)
        lbl11=Label(main,text="_____________________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=580,y=360)
        lbl11=Label(main,text="Name ",font=("",11,'bold'),bg='white').place(x=580,y=130)
        nametxt=Entry(main,textvariable=name,font=("",11,'bold'),bd=0,bg='white',highlightbackground='white',highlightcolor='white',width=25).place(x=670,y=128,height=30)
        lbl12=Label(main,text="E-mail ",font=("",11,'bold'),bg='white').place(x=580,y=205)
        mailtxt=Entry(main,textvariable=email,font=("",11,'bold'),bg='white',bd=0,highlightbackground='white',highlightcolor='white',width=25).place(x=670,y=203,height=30)
        lbl13=Label(main,text="Subject ",font=("",11,'bold'),bg='white').place(x=580,y=280)
        subtxt=Entry(main,textvariable=sub,font=("",11,'bold'),bg='white',bd=0,highlightbackground='white',highlightcolor='white',width=25).place(x=670,y=278,height=30)
        lbl14=Label(main,text="Message ",font=("",11,'bold'),bg='white').place(x=580,y=355)
        msgtxt=Entry(main,textvariable=msg,font=("",11,'bold'),bg='white',bd=0,highlightbackground='white',highlightcolor='white',width=25).place(x=670,y=353,height=30)
        senddbtn=Button(main,command=database,text='Send Message',cursor='hand2',font=("",11,'bold'),bd=0,bg='#1c1c1c',fg='white',highlightbackground='#1c1c1c',highlightthickness=2,width=30).place(x=600,y=450,height=40)   
    def database():
        if name.get() == "" or email.get() == "" or sub.get() == "" or msg.get() == "" :
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        else :
            conn = sqlite3.connect('/home/ak/Downloads/scs/DB/database.db')
            cursor=conn.cursor()
            cursor.execute('INSERT INTO feedback (name,mail,sub,msg) VALUES(?,?,?,?)',(name.get(),email.get(),sub.get(),msg.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", 'Feedback sent Successfully,\n\nClick "OK" to continue.')
            name.set(""),email.set(""),sub.set(""),msg.set("")
    
    conn = sqlite3.connect("/home/ak/Downloads/scs/DB/database.db")
    cur = conn.cursor()
    cur.execute("select * from customer where room=?",[lgroom.get()])
    rows = cur.fetchone()
    cname.set(rows[2])
    cmob.set(rows[4])
    croom.set(rows[1])
    
    home() 

def login():
    lbl1=Label(main,width=1100,height=610,bg='white').place(x=0,y=0)
    lbl2=Label(main,text='SMART  CAFE  SYSTEM',font=("",25,'bold'),bg='white',fg='#3e5348').place(x=400,y=30)
    label2=Label(payframe,bg='white',image=c2img).place(x=590,y=100)
    def login_all():
        conn = sqlite3.connect("/home/ak/Downloads/scs/DB/database.db")
        cur = conn.cursor()
        find_user = 'SELECT * FROM guest WHERE user = ? and password= ?'
        cur.execute(find_user, [(username_entry.get()), (password_entry.get())])
        result= cur.fetchone()
        if result!=None:
            lgroom.set(result[3])
            Guest()
        else:
            messagebox.showerror("Failed", "Wrong Login details, please try again.")
    def click(*args):
        username_entry.delete(0,'end')
    def click2(*args):
        password_entry.delete(0,'end')
    
    lbl11=Label(main,text="______________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=150,y=260)
    lbl11=Label(main,text="______________________________",font=("",15,'bold'),bg='white',fg='gray').place(x=150,y=350)
    lbl11=Label(main,image=accicon,bg='white').place(x=160,y=250)
    lbl11=Label(main,image=lgimg,bg='white').place(x=160,y=340)
        
    username_entry = Entry(main,bd=0, bg="white", fg="gray",font=("", 10,'bold'))
    username_entry.place(x=200, y=255, width=200, height=20)
    username_entry.config(highlightbackground="white", highlightcolor="white")
    username_entry.insert(0,"Username")

    password_entry = Entry(main,bd=0, bg="white", fg="gray", font=("", 10,'bold'), show="•")
    password_entry.place(x=200, y=345, width=200, height=20)
    password_entry.config(highlightbackground="white", highlightcolor="white")
    password_entry.insert(0,"Password")

    username_entry.bind("<Button-1>",click)
    password_entry.bind("<Button-1>",click2)

    loginButton = Button(main, text='Login',fg='white',bg='#6b6a69',bd=0, font=("", 12, "bold"),cursor='hand2', command=login_all)
    loginButton.place(x=180, y=420, width=250, height=35)
    loginButton.config(highlightbackground="#6b6a69", highlightthickness=2)

login()
main.mainloop()
