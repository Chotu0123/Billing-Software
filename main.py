from tkinter import *
from tkinter import ttk
from typing import Sized
from scrollphathd import scroll
from PIL import Image,ImageTk         #pip intall pillow



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x800")
        self.root.title("Billing Software")

        #Product  Catagories List
        self.Catagory=["Select Option","Clothing","Lifestyle","Mobiles"]
        self.SubCatClothing=["Pant","T-shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_Mufti=6000
        self.price_Spykar=7000
        self.T_shirt=["Polo","Roadstar","Jack&Jones"]
        self.price_polo=500
        self.price_Roadstar=4000
        self.price_JackJones=3000
        self.shirt=["Peter England","Louis Philipe","Park Avenue"]
        self.price_peter=2000
        self.price_louis=1000
        self.price_park=800

        self.SubCatLifestyle=["Bath Soap","Face Cream","Hair Oil"]
        self.Bath_soap=["Lifeboy","Lux","Santoor","Pearl"]
        self.price_life=float(20)
        self.price_lux=20
        self.price_Santoor=40
        self.price_pearl=10
        self.Face_Cream=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.price_fair=45
        self.price_ponds=20
        self.price_olay=40
        self.price_pearl=50
        self.Hair_oil=["Parachute","Jasmin","Bajaj"]
        self.price_parac=25
        self.price_jasmin=78
        self.price_bajaj=46

        self.SubCatMobiles=["Iphone","Sumsang","Xiome","RealMe","OnePlus"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_Iphone_X=140000
        self.price_Iphone_11=160000
        self.price_Iphone_12=200000
        self.Samsang=["Samsamg M30","Samsang M12","Samsang M21"]
        self.price_M16=19000
        self.price_M12=13000
        self.price_M21=22000
        self.Xiome=["Redmi 12","Redme X","Redme Pro"]
        self.price_12=14700
        self.price_X=16000
        self.price_pro=18000
        self.OnePlus=["Oneplus1","Oneplus2","Oneplus3"]
        self.price_one1=19000
        self.price_one2=210000
        self.price_one3=42000

        #Image 1
        img=Image.open("b0.png")
        #img=Image.open("b0.png")
        #img-img.resize((1400,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
       
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=1400,height=150)


         #Images 2
        img_1=Image.open("b0.png")
        #img-img.resize((1400,700),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=1400,y=0,width=1400,height=150)


         #Images 3
        img_2=Image.open("b0.png")
        #img-img.resize((1400,700),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=2800,y=0,width=1400,height=150)

        lbl_title=Label(self.root,text="R S Distributors Billing Software", font=("times new roman",35,"bold"),fg="red")
        lbl_title.place(x=0,y=150,width=1400,height=65)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=215,width=1369,height=690)

        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=340,height=140)

        self.lbL_mob=Label(Cust_Frame,text="Mobile No.",font=("arial",12,"bold"),bg="white",bd=2)
        self.lbL_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",12,"bold"),width=22)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbLCustomer=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=2)
        self.lbLCustomer.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustomer=ttk.Entry(Cust_Frame,font=("arial",12,"bold"),width=20)
        self.txtCustomer.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbLEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="white",text="Email",bd=4)
        self.lbLEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,font=('arial',12,'bold'),width=20)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=360,y=5,width=600,height=140)

        #Categories
        self.lbLCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Categories",bd=4)
        self.lbLCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Catagory, font=("arial",10,"bold"),width=20,state="readonly")
        #self.Combo_Catagory.Current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #SubCategories
        self.lbLSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="SubCategory",bd=4)
        self.lbLSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.Combo_SubCategory=ttk.Combobox(Product_Frame,font=("arial",10,"bold"),width=20,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #Product Name
        self.lbLproduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lbLproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,state="readonly",font=("arial",10,"bold"),width=20)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Price
        self.lbLPrice=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lbLPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",font=("arial",12,"bold"),width=18)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lbLQty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lbLQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,font=("arial",12,"bold"),width=20)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=950,height=200)

        #Image 1
        img12=Image.open("image/b2.jpg")
        #img-img.resize((800,500),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
       
        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=-76,y=-160,width=400,height=500)


         #Images 2
        img_13=Image.open("image/b1.jpg")
        #img-img.resize((1400,700),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=-300,y=-190,width=500,height=700)

        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="White")
        Search_Frame.place(x=970,y=20,width=370,height=45)


        self.lbLBill=Label(Search_Frame,font=("arial",12,"bold"), fg="white", bg="red",text="Bill Number")
        self.lbLBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,font=("arial",12,"bold"),width=18)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)


        self.BtnSearch=Button(Search_Frame,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)



        #Right Frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("arial",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=965,y=60,width=380,height=410)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("arial",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LAbelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("time new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=353,width=950,height=120)

        self.lbLSubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lbLSubTotal.grid(row=0,column=0,sticky=W,padx=4,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=("arial",12,"bold"),width=20)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #tax
        self.lbLtax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Gov Tax",bd=4)
        self.lbLtax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("arial",12,"bold"),width=20)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #Amount
        self.lbLAmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lbLAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("arial",12,"bold"),width=20)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,height=2, text="Add To Cart",font=("arial",10,"bold"),bg="orangered",fg="white",width=14,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_bill=Button(Btn_Frame,height=2, text="Generate Bill",font=("arial",10,"bold"),bg="orangered",fg="white",width=14,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,height=2, text="Save Bill",font=("arial",10,"bold"),bg="orangered",fg="white",width=14,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,height=2, text="Print",font=("arial",10,"bold"),bg="orangered",fg="white",width=14,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,height=2, text="Clear",font=("arial",10,"bold"),bg="orangered",fg="white",width=14,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,height=2, text="Exit",font=("arial",10,"bold"),bg="orangered",fg="white",width=14,cursor="hand2")
        self.BtnExit.grid(row=0,column=5,)


        
if __name__ == '__main__':
    root=Tk()
obj=Bill_App(root)
root.mainloop()
    
    

        