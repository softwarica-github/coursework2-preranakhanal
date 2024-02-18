#Imported Necessary Modules
from tkinter import *

# Created a function named adminlogin_validation
def adminlogin_validation(username, password):
    '''Checks Whether Username and Password Entry is Entered or not
    and Returns True if Username and Password is entered or Flase if not.'''
    return len(username) != 0 and username != "User Name" and len(password) != 0 and password != "Password"

#Created Function namedadminlogin_error
def adminlogin_data_error():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Error"
    message = "Recheck Your Input\n Values"
    from errors import error as show_error
    show_error(title,message)
    
def dashboard_call(WIN):
    '''Destroys the tkinter window and call open function i.e. login function from a admin page'''


# Create a Function named adminlogin_validate
def adminlogin_validate(WIN,username_value, password_value):
    record = []  # Define the variable record
    if adminlogin_validation(username_value, password_value):
        if str(username_value) == "admin" and str(password_value) == "admin":  
            # Destroys the tkinter window and call open_profile function i.e. profile_view function from a profile page
            WIN.destroy()
            from admin_login import homepage as admin_homepage
            admin_homepage()
    else:
        adminlogin_data_error()

#Created a Function Named adminlogin Which Stores all the Codes of adminlogin Page
# so it can be called later from another program
def adminlogin():
    # Created a Tkinter Window named WIN
    WIN = Tk()
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