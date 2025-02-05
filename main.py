from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime

from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")
        
    # first image
        img=Image.open(r"UI Data\new photo.png")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

      
        
        # bg image
        img3=Image.open(r"UI Data\New.png"
                        )
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,font=("Castellar",35,"bold"),bg="#040f27",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        #=======time=========
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font = ('aptos',14,"bold"),background= '#040f27',foreground= '#55dfe9')
        lbl.place(x=700,y=5,width=130,height=50)
        time()
        
       
         # student button
        img4=Image.open(r"UI Data\Student Details.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button (bg_img,text="Student Details", command=self.student_details,cursor="hand2",font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)  
        
        
        
         # detect Face button
        img5=Image.open(r"UI Data\Face Detection.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button (bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        # attendence Face button
        img6=Image.open(r"UI Data\Attendance.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button (bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        # help Face button
        img7=Image.open(r"UI Data\Helpdesk.png")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button (bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        # train Face button
        img8=Image.open(r"UI Data\Train Data.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button (bg_img,text= "Train Data",cursor="hand2",command=self.train_data,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        # photos Face button
        img9=Image.open(r"UI Data\Photos.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button (bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
         # developer Face button
        img10=Image.open(r"UI Data\Developer.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button (bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
         # exit Face button
        img11=Image.open(r"UI Data\Exit 02.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button (bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("courier",15,"bold"),bg="#00688b",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")
            
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Rcognition","Are you sure to exit this project", parent=self.root)  
        if  self.iExit >0:
            self.root.destroy()
        else: 
            return   
        
        
        # function buttons
        
    def student_details(self): 
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
          
    def attendance_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
          
    def developer_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
          
    def help_data(self): 
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
          
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)    
    root.mainloop()