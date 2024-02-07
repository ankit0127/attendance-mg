from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from second import Registration


class Attendence:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Attendence System")

        

        #######BACK GROUND IMAGE########
        imgbg=Image.open(r"C:\Users\28671\OneDrive\Desktop\major project\bg.jpg")
        imgbg=imgbg.resize((1580,800))
        self.photoimgbg=ImageTk.PhotoImage(imgbg)

        self.root.l1=Label(self.root, image=self.photoimgbg)
        self.root.l1.place(x=0,y=170,width=1580,height=800)


        ######LABEL#######
        self.root.l=Label(self.root, text="SIVA SIVANI DEGREE COLLEGE", font=("times new roman",50,"bold"),bg="LIGHT BLUE",fg="BLACK")
        self.root.l.place(x=0,y=10,width=1580,height=150)


        ######IMAGE######
        img1=Image.open(r"C:\Users\28671\OneDrive\Desktop\major project\new registration.jpg")
        img1=img1.resize((300,300))
        self.photoimg1=ImageTk.PhotoImage(img1)

        #####BUTTON#####
        self.root.b1=Button(self.root, image=self.photoimg1,command=self.student)
        self.root.b1.place(x=60,y=300,height=300,width=300)

        self.root.b11=Button(self.root, text="Register Now",command=self.student, font=("Arial",35), bg="light blue")
        self.root.b11.place(x=60,y=600,height=50,width=300)

        
        


        ######IMAGE######
        img2=Image.open(r"C:\Users\28671\OneDrive\Desktop\major project\training.png")
        img2=img2.resize((300,300))
        self.photoimg2=ImageTk.PhotoImage(img2)

        #####BUTTON#####
        self.root.b2=Button(self.root, image=self.photoimg2)
        self.root.b2.place(x=430,y=300,height=300,width=300)

        self.root.b21=Button(self.root, text="Data Training", font=("Arial",35), bg="light pink")
        self.root.b21.place(x=430,y=600,height=50,width=300)


        ######IMAGE#######
        img3=Image.open(r"C:\Users\28671\OneDrive\Desktop\major project\attendence.png")
        img3=img3.resize((300,300))
        self.photoimg3=ImageTk.PhotoImage(img3)


        #####BUTTON#####
        self.root.b3=Button(self.root, image=self.photoimg3, bg="white")
        self.root.b3.place(x=800,y=300,height=300,width=300)

        self.root.b31=Button(self.root, text="Attendance", font=("Arial",35), bg="light green")
        self.root.b31.place(x=800,y=600,height=50,width=300)

        ######IMAGE#######
        img4=Image.open(r"C:\Users\28671\OneDrive\Desktop\major project\update.jpg")
        img4=img4.resize((300,300))
        self.photoimg4=ImageTk.PhotoImage(img4)

        #####BUTTON#####
        self.root.b4=Button(self.root, image=self.photoimg4)
        self.root.b4.place(x=1170,y=300,height=300,width=300)

        self.root.b41=Button(self.root, text="Data Updation", font=("Arial",35), bg="purple")
        self.root.b41.place(x=1170,y=600,height=50,width=300)


    ######### BUTTON FUNCTIONS #######
    def student(self):
        self.new_window=Toplevel(self.root)
        self.app=Registration(self.new_window)
            




if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
