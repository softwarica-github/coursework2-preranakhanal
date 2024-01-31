#Imported Necessary Modules
from tkinter import *


def dashboard_call(WIN):
    '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
    WIN.destroy()
    from dashboard import dashboard as dashboard
    dashboard()


#Created a Function Named homepage Which Stores all the Codes of Main Page
# so it can be called later from another program
def homepage():
    #Created a Tkinter Window named WIN
    WIN = Tk()
    #Placed Image as Iconphoto on Window
    # logo_image = PhotoImage(file="images/fish2.png")
    # WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Online Voting System')
    #Set size of Tkinter Window
    WIN.geometry('360x640')
    #Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/background.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)
    
    
    
    button_image = PhotoImage(file="images/arrow.png")
    

    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:dashboard_call(WIN))
    button.place(x=4, y=5)


    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 12)

    # created a function named login_page
    def add_voter_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from addvoter import add_new_voter
        add_new_voter()
        
    def view_voter_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from viewvoter import viewvoter
        viewvoter()
    
    def view_votes_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from viewvotes import viewvotes
        viewvotes()


    #Created a Function named on_enter_add_voter with 'e' as one parameter
    def on_enter_add_voter(e):
        '''Changed Background and Foreground of Login Button named add_voter
        to #edd8ed and red respectively when function is called.'''
        add_voter.config(background='#edd8ed',foreground= "red")

    #Created a Function named on_leave_add_voter with 'e' as one parameter
    def on_leave_add_voter(e):
        '''Changed Background and Foreground of Button named add_voter to
        pink and black respectively when function is called.'''
        add_voter.config(background= '#eb5454', foreground= 'black')

    #created a Login Button which calls login_page function when pressed
    add_voter = Button(WIN,text="Register New Voter",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=lambda:add_voter_page())
    add_voter.place(x = 98,y = 398)
    #Created a Bind i.e. When Entered inside add voter button calls on_enter_add_voter function
    #and when leaves the add voter button calls on_leave_add_voter function
    add_voter.bind('<Enter>',on_enter_add_voter)
    add_voter.bind('<Leave>',on_leave_add_voter)



    # Created a Function named on_enter_view_voter with 'e' as one parameter
    def on_enter_view_voter(e):
        '''Changed Background and Foreground of Button named view_voter
        to #edd8ed and white respectively when function is called.'''
        view_voter.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_view_voter with 'e' as one parameter
    def on_leave_view_voter(e):
        '''Changed Background and Foreground of Button named view_voter to
        pink and black respectively when function is called.'''
        view_voter.config(background= '#eb5454', foreground= 'black')

    # created a view voter list Button which calls view voter function when pressed
    view_voter = Button(WIN,text="View Voter List",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=lambda:view_voter_page())
    view_voter.place(x=113,y=465)
    #Created a Bind i.e. When Entered inside view voter button calls on_enter_view_voter function
    #and when leaved button calls on_leave_view_voter function
    view_voter.bind('<Enter>',on_enter_view_voter)
    view_voter.bind('<Leave>',on_leave_view_voter)


    # Created a Function named on_enter_view_votes with 'e' as one parameter
    def on_enter_view_votes(e):
        '''Changed Background and Foreground of Register Button named view_votes
        to #ABBC41 and white respectively when function is called.'''
        view_votes.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_view_voter with 'e' as one parameter
    def on_leave_view_votes(e):
        '''Changed Background and Foreground of Register Button named view_votes to
        pink and black respectively when function is called.'''
        view_votes.config(background= '#eb5454', foreground= 'black')

    # created a view votes Button which calls view_votes function when pressed
    view_votes = Button(WIN,text="View Votes",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=lambda:view_votes_page())
    view_votes.place(x=127,y=532)
    #Created a Bind i.e. When Entered inside a view votes button calls on_enter_view_votes function
    #and when leaves the view votes button calls on_leave_view_votes function
    view_votes.bind('<Enter>',on_enter_view_votes)
    view_votes.bind('<Leave>',on_leave_view_votes)

    #Updates all Into TKinter Window
    WIN.mainloop()

#calls homepage Function
homepage()