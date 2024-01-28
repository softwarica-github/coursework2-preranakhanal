#Imported Necessary Modules
from tkinter import *



#Created a Function Named adminlogin Which Stores all the Codes of adminlogin Page
# so it can be called later from another program
def adminlogin():
    # Created a Tkinter Window named WIN
    WIN = Tk()
    # Placed Image as Iconphoto on Window
    # logo_image = PhotoImage(file="images/fish2.png")
    # WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Online Voting System')
    #Set size of Tkinter Window
    WIN.geometry('360x640')
    


    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)
    # Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/loginvoterdown.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 350 and 300 respectively.
    w = Canvas(WIN, width=350, height=280, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 350 and 300
    w.create_rectangle(0, 0, 350, 300, fill="#edd09f", outline='#dca028')
    w.pack(padx=50, pady=(230,0))
    
    button_image = PhotoImage(file="images/arrow.png")
    

    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:dashboard_call(WIN))
    button.place(x=4, y=5)

    #Function named temp_username with one parameter i.e. 'e'
    def temp_username(e):
        '''Clears username_entry to take user input'''
        username_entry.delete(0, "end")

    #Entry Box to  take Username Input from user
    username_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    username_entry.insert(2, "User Name")
    #Bind Entry so that when Clicked for Input it calls temp_username
    username_entry.bind("<FocusIn>", temp_username)
    username_entry.place(x=85, y=260)

    #Function named temp_password with one parameter i.e. 'e'
    def temp_password(e):
        '''Clears password_entry to take user input and configured password entry to show * when password is entered.'''
        password_entry.config(show="*")
        password_entry.delete(0, "end")
    #Entry Box to take Password Input from user
    password_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    password_entry.insert(0, "Password")
    #Bind Entry so that when Clicked for Input it calls temp_password
    password_entry.bind("<FocusIn>", temp_password)
    password_entry.place(x=85, y=330)
    #Log in Which when pressed calls adminlogin_validate by providing userentry as arguments
    adminlogin_button = Button(WIN, font=tfont_tup, justify="center", width=10, borderwidth=0, text="Log In", bg="#d98d0b",command=lambda : adminlogin_validate(WIN,username_entry.get(),password_entry.get()))
    adminlogin_button.place(x=110, y=410)


     # Created a Function named on_enter_register_button with 'e' as one parameter
    def on_enter_adminlogin_button(e):
        '''Changed Background and Foreground of Register Button named register_button
        to #ABBC41 and white respectively when function is called.'''
        adminlogin_button.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_register_button with 'e' as one parameter
    def on_leave_adminlogin_button(e):
        '''Changed Background and Foreground of Register Button named register_button to
        pink and black respectively when function is called.'''
        adminlogin_button.config(background= '#d98d0b', foreground= 'black')

    adminlogin_button.bind('<Enter>',on_enter_adminlogin_button)
    adminlogin_button.bind('<Leave>',on_leave_adminlogin_button)

  

  

    #Updates GUI Into TKinter Window
    WIN.mainloop()

#calls adminlogin function
adminlogin()