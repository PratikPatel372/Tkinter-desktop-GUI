from tkinter import *
from tkinter import filedialog 
import PIL
from PIL import ImageTk,Image
from tkinter import messagebox
from keras.models import load_model
import numpy as np # MATRIX OPERATIONS
import cv2 # IMAGE PROCESSING - OPENCV
import time
import os
import sys

filePaths= []

def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS
        print(base_path)
    except Exception:
        base_path = os.path.abspath(".")
        print(base_path)
    return os.path.join(base_path, relative_path)

def main():
    def login_crit():
        if name_txt.get()=="" or user_txt.get()=="" or pass_txt.get()=="":
            messagebox.showerror("Error","All fields are required",parent=main)
        elif user_txt.get()!="Pratik372" or pass_txt.get()!="26 05":
            messagebox.showerror("Error","Invalid Username/Password",parent=main)
        else:
            messagebox.showinfo("Welcome",f"Welcome {user_txt.get()}\n Your Password : {pass_txt.get()}",parent=main)
            prediction()

    global main
    main=Tk()
    main.title('Welcome to Login')
    scrW=main.winfo_screenwidth()
    scrH=main.winfo_screenheight()
    main.geometry(str(scrW)+"x"+str(scrH))
    main.resizable(str(scrW),str(scrH))
        
    bg=ImageTk.PhotoImage(file=resource_path("robot.jpg"))
    bg_iamge=Label(main,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
        
    frame_login=Frame(main,bg="black",bd= 5, relief= GROOVE)
    frame_login.place(x=110,y=200, height=340, width=600)
        
    Title=Label(frame_login, text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="black").place(x=50,y=30)
    
    name=Label(frame_login, text="Your Name : ",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=70,y=130)
    name_txt=Entry(frame_login, font=("times new roman",13))
    name_txt.place(x=200,y=130)
        
    user=Label(frame_login, text="User Name : ",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=70,y=180)
    user_txt=Entry(frame_login,font=("times new roman",13))
    user_txt.place(x=200,y=180)
        
    passwd=Label(frame_login, text="Password : ",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=70,y=230)
    pass_txt=Entry(frame_login, show="*", font=("times new roman",13))
    pass_txt.place(x=200,y=230)
            
    Login_btn=Button(main, text="Login",cursor="hand2",command=login_crit, font=("Impact",18),fg="white",bg="#d77337").place(x=250,y=518,width=150,height=40)
    ext_btn=Button(main, text="Exit",cursor="hand2",command=main.destroy, font=("Impact",18),fg="white",bg="#d77337").place(x=420,y=518,width=150,height=40)
    main.mainloop()
    return name_txt,user_txt,pass_txt

def forget():
    global imgframe,thinframe,clear_button
    plus_button.place_forget()
    webcam_button.place_forget()
    Title3.place_forget()
    Title2.place_forget()
            
    imgframe=Frame(prediction_scr,bg="gray",bd=0)
    imgframe.place(x=300,y=27,width=996,height=540)

    thinframe=Frame(prediction_scr,bg="black",bd=0)
    thinframe.place(x=300,y=603,width=996,height=5)
    clear_button=Button(prediction_scr,text="Clear",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white",command=clearpic)
    clear_button.place(x=750,y=620, width=80, height=30)

def clearpic():
    imgframe.place_forget()
    thinframe.place_forget()
    plus_button.place(x=640,y=260, width=150, height=150)
    webcam_button.place(x=800,y=260, width=150, height=150)
    Title3.place(x=635, y=410)  
    Title2.place(x=575,y=30)
    clear_button.place_forget()
    if filePaths:    
        filePaths.clear()
    if video:
        video.release()
        cv2.destroyAllWindows()
    if x:
        del x

def prediction():
    global prediction_scr,Title2,Title3,plus_button,webcam_button
    prediction_scr=Toplevel(main)
    prediction_scr.title("Welcome to Prediction")
    scrW=prediction_scr.winfo_screenwidth()
    scrH=prediction_scr.winfo_screenheight()
    print(scrW,scrH)
    prediction_scr.geometry(str(scrW)+"x"+str(scrH))
    prediction_scr.resizable(str(scrW),str(scrH))
    prediction_scr.config(background = "silver")
        
    frame1=Frame(prediction_scr,bg="black",bd= 5, relief= GROOVE)
    frame1.place(x=0,y=0, height=768, width=250)
    Title1=Label(frame1, text="Species",font=("Calibri",30,"bold"),fg="white",bg="black").place(x=55,y=10)
        
    Blackgrass_button=Button(frame1,text="Black grass",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=100, width=230, height=35)
    Charlock_button=Button(frame1,text="Charlock",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=140, width=230, height=35)
    Cleavers_button=Button(frame1,text="Cleavers",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=180, width=230, height=35)
    CommonChickweed_button=Button(frame1,text="Common Chickweed",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=220, width=230, height=35)
    CommonWheat_button=Button(frame1,text="Common Wheat",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=260, width=230, height=35)
    FatHen_button=Button(frame1,text="Fat Hen",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=300, width=230, height=35)
    LooseSilkybent_button=Button(frame1,text="Loose Silky-bent",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=340, width=230, height=35)
    Maize_button=Button(frame1,text="Maize",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=380, width=230, height=35)
    ScentlessMayweed_button=Button(frame1,text="Scentless Mayweed",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=420, width=230, height=35)
    ShepherdsPurse_button=Button(frame1,text="Shepherds Purse",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=460, width=230, height=35)
    SmallfloweredCranesbill_button=Button(frame1,text="Small Cranesbill",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=500, width=230, height=35)
    Sugarbeet_button=Button(frame1,text="Sugar beet",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white").place(x=5,y=540, width=230, height=35)

    Title2=Label(prediction_scr, text="Select and Predict your plant species",bg="silver",fg="darkblue", font=("times new roman",20,"bold"))
    Title2.place(x=575,y=30)
        
    plus_button=Button(prediction_scr,text="+",font=("calibri",120,"bold"), bd=1, activebackground="silver", bg="silver", fg= "dimgray",command=open_img)
    plus_button.place(x=640,y=260, width=150, height=150)
        
    webcam_button=Button(prediction_scr,text="w", font=("calibri",120,"bold"),bd=1, bg="silver", activebackground="silver", fg= "dimgray",command=open_camera)
    webcam_button.place(x=800,y=260, width=150, height=150)
        
    Title3=Label(prediction_scr, text="Select plant species images",bg="silver",fg="dimgray", font=("times new roman",20,"bold"))
    Title3.place(x=635, y=410)  
        
    back_button=Button(prediction_scr,text="Back",font=("calibri",18,"bold"),bd=2,activebackground="silver", bg="navy", fg= "white",command=prediction_scr.destroy).place(x=300,y=670, width=80, height=30)
    predict_button=Button(prediction_scr,text="Predict",font=("calibri",18,"bold"),bd=2,activebackground="silver", bg="navy", fg= "white",command=predict).place(x=730,y=670, width=120, height=30)
    exit_button=Button(prediction_scr,text="Exit",font=("calibri",18,"bold"),bd=2,activebackground="silver", bg="navy", fg= "white",command=prediction_scr.destroy).place(x=1216,y=670, width=80, height=30)

def predict():
    if filePaths:
        model2=load_model(resource_path("my_model.h5"))       
        givelabel=np.load(resource_path("labels data.npy"),allow_pickle=True)
        testimages = []
        tests = []
        count=1
        num = len(filePaths)
        print(filePaths)
        for i in filePaths:
            print(str(count)+'/'+str(num),end='\r')
            tests.append(i.split('/')[1])
            testimages.append(cv2.resize(cv2.imread(i),(70,70)))
            count = count + 1
        testimages = np.asarray(testimages)    
        newtestimages = []
        for i in testimages:
            blurr = cv2.GaussianBlur(i,(5,5),0)
            hsv = cv2.cvtColor(blurr,cv2.COLOR_BGR2HSV)
            lower = (25,40,50)
            upper = (75,255,255)
            mask = cv2.inRange(hsv,lower,upper)
            struc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
            mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,struc)
            boolean = mask>0
            masking = np.zeros_like(i,np.uint8)
            masking[boolean] = i[boolean]
            newtestimages.append(masking)
            
        newtestimages = np.asarray(newtestimages)            
        newtestimages=newtestimages/255
            
        imgpredict = model2.predict(newtestimages)
            
        pred = np.argmax(imgpredict,axis=1)#CONVERT TO ARRAY
        Species_name = givelabel[pred]#BINARY CLASS TO STRING CLASS CONVERSION
        print(Species_name)
        j=0
        for x_dim in range(200,701,500):
            for y_dim in range(50,441,130):
                myspecies =Label(imgframe,text=Species_name[j],font=("calibri",20,"bold"),bg="gray", fg="black")
                myspecies.place(x=x_dim,y=y_dim)
                print(j,x_dim,y_dim)
                j=j+1
    else:
        msg=Label(prediction_scr,text="First you have to select images",bg="silver",fg="dimgray", font=("times new roman",17))
        msg.place(x=635, y=640)
        msg.after(2000,lambda:msg.destroy())
        
def open_img():
    forget()
    global filePaths
    files = filedialog.askopenfilename(title='Select', filetypes=[("All file", ".*"),("JPEG images", "*.jpeg"),("PNG image", "*.png"),("JPG image", "*.jpg")],multiple=True,parent=prediction_scr)
    var = prediction_scr.tk.splitlist(files)
    filePaths = []
    for f in var:
        filePaths.append(f)
    print(filePaths)
    print(len(filePaths))
    i=0
    for x_dim in range(50,551,500):
        for y_dim in range(13,404,130):
            im= Image.open(filePaths[i])
            img = im.resize((120, 120), Image.ANTIALIAS) 
            tkimg =ImageTk.PhotoImage(img)
            myvar =Label(imgframe,image=tkimg)
            myvar.image=tkimg
            myvar.place(x=x_dim,y=y_dim)
            print(i,x_dim,y_dim)
            i=i+1

def open_camera():
    forget()
    global lmain,video,get_frame,video_stream
    video = cv2.VideoCapture(1)
    if not video.isOpened():
        print("Unable to open external video source")
        print("starting your internal webcam.....")
        video=cv2.VideoCapture(0)


    width=video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video.set(cv2.CAP_PROP_FRAME_WIDTH,660)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
    lmain=Label(imgframe,bg="white")
    lmain.place(x=168,y=10)
    snap_button=Button(imgframe,text="snapshot",font=("calibri",18,"bold"),bd=2, bg="navy", fg= "white",command=snapshot)
    snap_button.place(x=438,y=505,width=100,height=30)
    
    print(width,height)
    
    def video_stream():
        global video_stream
        check, frame = video.read()
        if check:    
            frame=cv2.flip(frame,1)
            cv2frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(cv2frame)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)   
            lmain.after(15, video_stream)
            
    video_stream()

def snapshot():
    global snapshotP
    check, frame = video.read()
    newpath=("C:" + os.environ["HOMEPATH"] + "\Desktop\Snapshot")
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    x= newpath + "\Image" + time.strftime("%H-%M-%S-%d-%m")+ ".png"
    if check:
        cv2.imwrite(x,frame)
        x=x.replace('\\','/')
        filePaths.append(x)
        print(filePaths)
        print(len(filePaths))
    video.release()
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()
    
    