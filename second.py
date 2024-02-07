from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Registration:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Student Registration")

        self.root.v1=StringVar()
        self.root.v2=StringVar()
        self.root.v3=StringVar()
        self.root.v4=StringVar()
        self.root.v5=StringVar()
        self.root.v6=StringVar()
        self.root.v7=StringVar()
        self.root.v8=StringVar()
        self.root.v9=StringVar()
        self.root.v10=StringVar()
        self.root.v11=StringVar()
        self.root.v12=StringVar()
        self.root.v13=StringVar()
        


        ###### LABEL #######
        self.root.l=Label(self.root, text="STUDENT REGISTRATION FORM", font=("times new roman",40,"bold"),bg="ORANGE",fg="BLACK")
        self.root.l.place(x=0,y=10,width=1580,height=100)

        ####### BACK GROUND IMAGE ########
        imgbg=Image.open(r"C:\Users\28671\OneDrive\Desktop\major project\bg.jpg")
        imgbg=imgbg.resize((1580,800))
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        self.root.l1=Label(self.root, image=self.photoimgbg)
        self.root.l1.place(x=0,y=120,width=1580,height=800)

        ##### MAIN FRAME #####
        self.root.f=Frame(self.root,bd=3)
        self.root.f.place(x=10,y=130,width=1507,height=645)

        ###### LEFT FRAME ######
        self.root.f1=LabelFrame(self.root,bd=3,bg="light pink", text="STUDENT DETAILS")
        self.root.f1.place(x=23,y=140,width=735,height=625)

        #### CREATING COMBO BOX FOR DIFFERENT GROUP ######
        self.root.f11=LabelFrame(self.root.f1,bd=3,bg="white", text="Course Details")
        self.root.f11.place(x=10,y=5,width=710,height=130)

        self.root.l1=Label(self.root.f11, text="Group *", font=("times new roman",15,"bold"), bg="white")
        self.root.l1.grid(row=0,column=0,padx=15)

        self.root.cb=ttk.Combobox(self.root.f11,textvariable=self.root.v1, font=("times new roman",15,"bold"),width=20,state="readonly")
        self.root.cb["values"]=("Select Group","B.Sc","B.Com","BBA")
        self.root.cb.current(0)
        self.root.cb.grid(row=0,column=1,padx=2,pady=10)

        ### COURSE ####
        self.root.l1=Label(self.root.f11, text="Cousre", font=("times new roman",15,"bold"), bg="white")
        self.root.l1.grid(row=0,column=2,padx=15)

        self.root.cb=ttk.Combobox(self.root.f11,textvariable=self.root.v2, font=("times new roman",15,"bold"),width=20,state="readonly")
        self.root.cb["values"]=("Select Course","MSCS","MECS","BA","CA","Hons","Finance","Marketing","HR")
        self.root.cb.current(0)
        self.root.cb.grid(row=0,column=3,padx=2,pady=10)

        ###### YEAR ######
        self.root.l1=Label(self.root.f11, text="Year", font=("times new roman",15,"bold"), bg="white")
        self.root.l1.grid(row=1,column=0,padx=15)

        self.root.cb=ttk.Combobox(self.root.f11,textvariable=self.root.v3, font=("times new roman",15,"bold"),width=20,state="readonly")
        self.root.cb["values"]=("Choose Year","I","II","III")
        self.root.cb.current(0)
        self.root.cb.grid(row=1,column=1,padx=2,pady=10)

        ### SEMESTER ####
        self.root.l1=Label(self.root.f11, text="Semester", font=("times new roman",15,"bold"), bg="white")
        self.root.l1.grid(row=1,column=2,padx=15)

        self.root.cb=ttk.Combobox(self.root.f11,textvariable=self.root.v4, font=("times new roman",15,"bold"),width=20,state="readonly")
        self.root.cb["values"]=("Choose Semester","I","II","III","IV","V","VI")
        self.root.cb.current(0)
        self.root.cb.grid(row=1,column=3,padx=2,pady=10)

        ##### STUDENT DETAILS #####
        self.root.f12=LabelFrame(self.root.f1,bd=3,bg="white", text="Student Details")
        self.root.f12.place(x=10,y=150,width=710,height=280)

        ##### STUDENT ID #####
        self.root.l12=Label(self.root.f12, text="Student Id *", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=0,column=0,padx=10)

        self.root.e1=ttk.Entry(self.root.f12,textvariable=self.root.v5, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=0,column=1,padx=2, pady=10)

        ####### HALL TICKET NUMBER #######
        self.root.l12=Label(self.root.f12, text="Ht. No.*", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=0,column=2,padx=10)

        self.root.e1=ttk.Entry(self.root.f12,textvariable=self.root.v6, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=0,column=3,padx=2, pady=10)

        ##### NAME ######
        self.root.l12=Label(self.root.f12, text="Student Name *", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=1,column=0,padx=10)

        self.root.e1=ttk.Entry(self.root.f12, textvariable=self.root.v7, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=1,column=1,padx=2, pady=10)

        ##### DOB ######
        self.root.l12=Label(self.root.f12, text="DOB", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=2,column=0,padx=10)

        self.root.e1=ttk.Entry(self.root.f12, textvariable=self.root.v8, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=2,column=1,padx=2, pady=10)

        ##### GENDER ######
        self.root.l12=Label(self.root.f12, text="Gender", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=2,column=2,padx=10)

        self.root.cb12=ttk.Combobox(self.root.f12, textvariable=self.root.v9, font=("times new roman",15,"bold"),width=18,state="readonly")
        self.root.cb12["values"]=("Select","Male","Female","Others")
        self.root.cb12.current(0)
        self.root.cb12.grid(row=2,column=3,padx=2,pady=10)

        ##### BLOOD GROUP ######
        self.root.l12=Label(self.root.f12,  text="Blood Group", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=3,column=0,padx=10)

        self.root.e1=ttk.Entry(self.root.f12,textvariable=self.root.v10, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=3,column=1,padx=2, pady=10)

        ##### PHONE NUMBER ######
        self.root.l12=Label(self.root.f12, text="Phone No.", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=3,column=2,padx=10)

        self.root.e1=ttk.Entry(self.root.f12,textvariable=self.root.v11, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=3,column=3,padx=2, pady=10)

        ##### EMAIL #######
        self.root.l12=Label(self.root.f12, text="Email", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=4,column=0,padx=10)

        self.root.e1=ttk.Entry(self.root.f12,textvariable=self.root.v12, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=4,column=1,padx=2, pady=10)

        ##### ADDRESS #######
        self.root.l12=Label(self.root.f12, text="Address", font=("times new roman",15,"bold"),bg="white")
        self.root.l12.grid(row=4,column=2,padx=10)

        self.root.e1=ttk.Entry(self.root.f12, textvariable=self.root.v13, font=("times new roman",15,"bold"))
        self.root.e1.grid(row=4,column=3,padx=2, pady=10)

        ##### PHOTO INFORMATION #####
        self.root.f13=LabelFrame(self.root.f1,bd=3,bg="white", text="Photo Information")
        self.root.f13.place(x=10,y=445,width=710,height=150)

        self.root.l13=Label(self.root.f13, text="Sample Photo", font=("times new roman",15,"bold"),bg="white")
        self.root.l13.grid(row=0,column=0,padx=10)

        #### RADIO BUTTON ####
        self.root.v14=StringVar()
        self.root.rb1=ttk.Radiobutton(self.root.f13, variable=self.root.v14, text="YES",value="Yes")
        self.root.rb1.grid(row=0,column=1,padx=10)

        ##self.root.v15=StringVar()
        self.root.rb2=ttk.Radiobutton(self.root.f13, variable=self.root.v14, text="NO",value="No")
        self.root.rb2.grid(row=0,column=2,padx=10)

        #### CAMERA BUTTON #####
        self.root.b=Button(self.root.f13, text="camera",command=self.generate_dataset, width=12, font=("times new roman",15,"bold"), bg="light blue", fg="black" )
        self.root.b.grid(row=0,column=3,padx=10)

        #### SAVE BUTTON #####
        self.root.b1=Button(self.root.f13, text="save",command=self.data,width=12, font=("times new roman",15,"bold"), bg="green", fg="black" )
        self.root.b1.grid(row=1,column=0,padx=10, pady=20)

        ######UPDATE BUTTON ######
        self.root.b2=Button(self.root.f13, text="update",command=self.update_data, width=12, font=("times new roman",15,"bold"), bg="tomato", fg="black" )
        self.root.b2.grid(row=1,column=1,padx=10, pady=20)

        ###### DELETE BUTTON ######
        self.root.b3=Button(self.root.f13, text="delete",command=self.delete_data,width=12, font=("times new roman",15,"bold"), bg="orange", fg="black" )
        self.root.b3.grid(row=1,column=2,padx=10, pady=20)

        ###### RESET BUTTON ######
        self.root.b4=Button(self.root.f13, text="reset",command=self.reset,width=12, font=("times new roman",15,"bold"), bg="red", fg="black" )
        self.root.b4.grid(row=1,column=3,padx=10, pady=20)

        ###### RIGHT FRAME ######
        self.root.f2=LabelFrame(self.root,bd=3,bg="light pink", text="STUDENT DETAILS")
        self.root.f2.place(x=770,y=140,width=735,height=625)

        ###### SEARCH AREA ######
        self.root.f21=LabelFrame(self.root.f2,bd=3,bg="white", text="Search")
        self.root.f21.place(x=10,y=10,width=710,height=100)

        ###### OPTION ####
        self.root.cb21=ttk.Combobox(self.root.f21, font=("times new roman",15,"bold"),width=18,state="readonly")
        self.root.cb21["values"]=("Select","Student Id","Ht. Number")
        self.root.cb21.current(0)
        self.root.cb21.grid(row=0,column=0,padx=10,pady=10)

        self.root.e21=ttk.Entry(self.root.f21, font=("times new roman",15,"bold"))
        self.root.e21.grid(row=0,column=1,padx=2, pady=10)

        self.root.b21=Button(self.root.f21, text="get data",width=12, font=("times new roman",15,"bold"), bg="blue", fg="WHITE" )
        self.root.b21.grid(row=0,column=2,padx=10, pady=20)

        ###### DETAILS AREA ######
        self.root.f22=LabelFrame(self.root.f2,bd=3,bg="white", text="Search")
        self.root.f22.place(x=10,y=130,width=710,height=465)

        ### SCROLL BARS #####
        self.root.sb1=ttk.Scrollbar(self.root.f22, orient="horizontal")
        self.root.sb2=ttk.Scrollbar(self.root.f22, orient="vertical")

        self.root.table=ttk.Treeview(self.root.f22,column=("Student Id","Group","Course","Year","Semester","Ht Number","Student Name","DOB","Gender","Blood Group","Phone No.","Email","Address","Photo"),xscrollcommand=self.root.sb1.set,yscrollcommand=self.root.sb2.set)

        self.root.sb1.pack(side=BOTTOM,fill=X)
        self.root.sb2.pack(side=RIGHT,fill=Y)

        self.root.sb1.config(command=self.root.table.xview)
        self.root.sb2.config(command=self.root.table.yview)

        #### TABLE COLUMN DECLARATIOM #######

        self.root.table.heading("Student Id",text="STUDENT ID")
        self.root.table.heading("Group",text="GROUP")
        self.root.table.heading("Course",text="COUSE")
        self.root.table.heading("Year",text="YEAR")
        self.root.table.heading("Semester",text="SEMESTER")
        self.root.table.heading("Ht Number",text="HT NUMBER")
        self.root.table.heading("Student Name",text="STUDENT NAME")
        self.root.table.heading("DOB",text="DOB")
        self.root.table.heading("Gender",text="GENDER")
        self.root.table.heading("Blood Group",text="BLOOD GROUP")
        self.root.table.heading("Phone No.",text="PHONE NO.")
        self.root.table.heading("Email",text="EMAIL")
        self.root.table.heading("Address",text="ADDRESS")
        self.root.table.heading("Photo",text="PHOTO")
        self.root.table["show"]="headings"

        self.root.table.column("Student Id",width=100)
        self.root.table.column("Group",width=100)
        self.root.table.column("Course",width=100)
        self.root.table.column("Year",width=100)
        self.root.table.column("Semester",width=100)
        self.root.table.column("Ht Number",width=100)
        self.root.table.column("Student Name",width=100)
        self.root.table.column("DOB",width=100)
        self.root.table.column("Gender",width=100)
        self.root.table.column("Blood Group",width=100)
        self.root.table.column("Phone No.",width=100)
        self.root.table.column("Email",width=100)
        self.root.table.column("Address",width=100)
        self.root.table.column("Photo",width=100)

        self.root.table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.root.table.bind("<ButtonRelease>",self.get_data) ##### SHOWING DATA#####
        


    def data(self):
        if self.root.v1.get=="Select Group" or self.root.v5.get()=="" or self.root.v6.get()=="" or self.root.v7.get()=="":
            messagebox.showerror("error","* fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anya@0127",database="attendence")
                cur=conn.cursor()
                cur.execute("insert into 3r values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.root.v5.get(),
                                                                                            self.root.v1.get(),
                                                                                            self.root.v2.get(),
                                                                                            self.root.v3.get(),
                                                                                            self.root.v4.get(), 
                                                                                            self.root.v6.get(),
                                                                                            self.root.v7.get(),
                                                                                            self.root.v8.get(),
                                                                                            self.root.v9.get(),
                                                                                            self.root.v10.get(),
                                                                                            self.root.v11.get(), 
                                                                                            self.root.v12.get(),
                                                                                            self.root.v13.get(),
                                                                                            self.root.v14.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Successful","saved",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    #### DATA FETCHING ######
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anya@0127",database="attendence")
        cur=conn.cursor()
        cur.execute("select * from 3r")
        data=cur.fetchall()

        if len(data)!=0:
            self.root.table.delete(*self.root.table.get_children())
            for i in data:
                self.root.table.insert("",END,values=i)
            conn.commit()
        conn.close()

    ##### GETTING DATA ######
    def get_data(self,event=""):
        cursor=self.root.table.focus()  ##inbuilt method
        content=self.root.table.item(cursor)
        data=content["values"]

        self.root.v5.set(data[0]),
        self.root.v1.set(data[1]),
        self.root.v2.set(data[2]),  
        self.root.v3.set(data[3]),
        self.root.v4.set(data[4]), 
        self.root.v6.set(data[5]),
        self.root.v7.set(data[6]),
        self.root.v8.set(data[7]),
        self.root.v9.set(data[8]),
        self.root.v10.set(data[9]),
        self.root.v11.set(data[10]), 
        self.root.v12.set(data[11]),
        self.root.v13.set(data[12]),
        self.root.v14.set(data[13])


    ##### DATA UPDATION #####
    def update_data(self):
        if self.root.v1.get()=="Select Group" or self.root.v5.get()=="" or self.root.v6.get()=="" or self.root.v7.get()=="":
            messagebox.showerror("error","* fields are required",parent=self.root)

        else:
            try:
                update1=messagebox.askyesno("update","confirm",parent=self.root)
                if update1>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anya@0127",database="attendence")
                    cur=conn.cursor()
                    d1="UPDATE 3r SET Course=%s, Year=%s,Semester=%s, Ht_Number=%s, Student_Name=%s,DOB=%s, Gender=%s, Blood_Group=%s, Phone_No=%s, Email=%s, Address=%s, Sample_Photo=%s where Student_Id=%s"
                    value=(self.root.v2.get(),self.root.v3.get(),self.root.v4.get(),self.root.v6.get(),self.root.v7.get(),self.root.v8.get(),self.root.v9.get(),self.root.v10.get(),self.root.v11.get(),self.root.v12.get(),self.root.v13.get(),self.root.v14.get(),self.root.v5.get())  ### STUDENT ID VARIABLE ####
                    cur.execute(d1,value)
                                                                                                                                                                                                                                        
                else:
                    if not update1:
                        return
                messagebox.showinfo("Success", "Data Updated", parent=self.root) 
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"DUE TO:{str(es)}",parent=self.root)

    ######DELETE FUNCTION ######
    def delete_data(self):
        if self.root.v5.get()=="":
            messagebox.showerror("error","Student Id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Detete Data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Anya@0127",database="attendence")
                    cur=conn.cursor()
                    del1="DELETE from 3r where Student_Id=%s"
                    val=(self.root.v5.get(),)
                    cur.execute(del1,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Data Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"DUE TO:{str(es)}",parent=self.root)

    ##### RESET #####
    def reset(self):
        self.root.v5.set(""),
        self.root.v1.set("Select Group"),
        self.root.v2.set("Select Course"),  
        self.root.v3.set("Choose Year"),
        self.root.v4.set("Choose Semester"), 
        self.root.v6.set(""),
        self.root.v7.set(""),
        self.root.v8.set(""),
        self.root.v9.set("Select"),
        self.root.v10.set(""),
        self.root.v11.set(""), 
        self.root.v12.set(""),
        self.root.v13.set(""),
        self.root.v14.set("")

    ####### PHOTO SAMPLE ######
    def generate_dataset(self):
        if self.root.v1.get()=="Select Group" or self.root.v5.get()=="" or self.root.v6.get()=="" or self.root.v7.get()=="":
            messagebox.showerror("error","* fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Anya@0127",database="attendence")
                cur=conn.cursor()
                cur.execute("select * from 3r")
                result=cur.fetchall()
                id=0
                for x in result:
                    id+=1
                d1="UPDATE 3r SET Course=%s, Year=%s,Semester=%s, Ht_Number=%s, Student_Name=%s,DOB=%s, Gender=%s, Blood_Group=%s, Phone_No=%s, Email=%s, Address=%s, Sample_Photo=%s where Student_Id=%s"
                value=(self.root.v2.get(),self.root.v3.get(),self.root.v4.get(),self.root.v6.get(),self.root.v7.get(),self.root.v8.get(),self.root.v9.get(),self.root.v10.get(),self.root.v11.get(),self.root.v12.get(),self.root.v13.get(),self.root.v14.get(),self.root.v5.get()==id+1)  ### STUDENT ID VARIABLE ####
                cur.execute(d1,value)
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                #######   FILE FROM OPEN CV TO DETECT FACE ######
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ###### change pic to gray ####
                    face=face_classifier.detectMultiScale(gray,1.3,5)

                    ### SCALING FACTOR=1.3
                    ### MINIMUM NEIGHBOR=5

                    for (x,y,w,h) in face:
                        crop=img[y:y+h,x:x+w]
                        return crop
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    result,cam_frame=cap.read()
                    if crop(cam_frame) is not None:
                        img_id+=1
                        face=cv2.resize(crop(cam_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="images/user."+str(img_id)+"."+str(img_id)+".jpg" ###### IT WILL PUT NAME FOR OUR IMAGE DATA ######
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,250),2)
                        cv2.imshow("Cropped Face",cam_frame)

                    if cv2.waitKey(0)==13 or int(img_id)==25:  #### AQUIRING NO. OF FRAMES ####
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed")
            
            except Exception as es:
                messagebox.showerror("Error",f"DUE TO:{str(es)}",parent=self.root)


                    








if __name__=="__main__":
    root=Tk()
    obj=Registration(root)
    root.mainloop()
