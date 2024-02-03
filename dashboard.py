#Imported Necessary Modules
from tkinter import *

#Created a Function Named dashboard Which Stores all the Codes of Main Page
# so it can be called later from another program
def dashboard():
    
    #Created a Tkinter Window named WIN
    WIN = Tk()
    #Named Tkinter Window
    WIN.title('Online Voting System')
    #Set size of Tkinter Window
    WIN.geometry('360x640')
    #Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/background.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 12)

    # created a function named admin_page
  admin_login_button.config(background= '#eb5454', foreground= 'black')

    #created a Login Button which calls admin_page function when pressed
    admin_login_button = Button(WIN,text="Login as Admin",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=admin_page)
    admin_login_button.place(x = 115,y = 398)
    #Created a Bind i.e. When Entered inside a Login button calls on_enter_admin_login function
    #and when leaves the Login button calls on_leave_admin_login function
    admin_login_button.bind('<Enter>',on_enter_admin_login)
    admin_login_button.bind('<Leave>',on_leave_admin_login)

    # Created a Function named on_enter_voter_login with 'e' as one parameter
    def on_enter_voter_login(e):
        '''Changed Background and Foreground of Register Button named voter_login_button
        to #ABBC41 and white respectively when function is called.'''
        voter_login_button.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_voter_login with 'e' as one parameter
    def on_leave_voter_login(e):
        '''Changed Background and Foreground of Register Button named voter_login_button to
        pink and black respectively when function is called.'''
        voter_login_button.config(background= '#eb5454', foreground= 'black')

    # created a Register Button which calls voter_page function when pressed
    voter_login_button = Button(WIN,text="Login as Voter",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=voter_page)
    voter_login_button.place(x=117,y=465)
    #Created a Bind i.e. When Entered inside a Register button calls on_enter_voter_login function
    #and when leaves the Register button calls on_leave_voter_login function
    voter_login_button.bind('<Enter>',on_enter_voter_login)
    voter_login_button.bind('<Leave>',on_leave_voter_login)

    #Updates all Into TKinter Window
    WIN.mainloop()

#calls dashboard Function
dashboard()
