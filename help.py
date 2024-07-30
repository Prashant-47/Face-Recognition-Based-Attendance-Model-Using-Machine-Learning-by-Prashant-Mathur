from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FaceRecognitionSystem")
   
        title_lbl=Label(self.root,text="HELP - DESK",font=("Cascadia Code",35,"bold"),bg="#011522",fg="#55dfe9")
        title_lbl.place(x=0,y=0,width=1530,height=55)   
        
        img_top=Image.open(r"UI Data\Helpdesk BG.png")
        img_top=img_top.resize((1530,800),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=800)
   
        
    
   
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)    
    root.mainloop()                 