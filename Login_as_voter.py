#Imported Necessary Modules
from tkinter import *
import json
from PIL import Image
from stegano import lsb

#Created Function namedvoterlogin_error
def voterlogin_data_error():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Error"
    message = "Recheck Your Input\n Values"
    from errors import error as show_error
    show_error(title,message)
    
 

def confirm_voter(WIN,voter_idtemp_voter_id):
    record = []  # Define the variable record

    if voterlogin_validation(voter_idtemp_voter_id):
        # Destroys the tkinter window and call open_profile function i.e. profile_view function from a profile page
        WIN.destroy()
        from addvote import viewcandidate
        viewcandidate()
    else:
        voterlogin_data_error()

#Created a Function Named voterlogin Which Stores all the Codes of voterlogin Page
# so it can be called later from another program
def voterlogin():
    # Created a Tkinter Window named WIN
    WIN = Tk()
    # Placed Image as Iconphoto on Window
    logo_image = PhotoImage(file="images/fish2.png")
    WIN.iconphoto(False, logo_image)
    #Named Tkinter Window
    WIN.title('Online Voting System')
    #Set size of Tkinter Window
    WIN.geometry('360x640')

    # Created register_page function
    def register_page():
        '''Destroys Tkinter Window named WIN and calls page_register
        from register program'''
        WIN.destroy()
        from register import register as page_register
        page_register()

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)
    # Placed backround.png image as BAckground to a TKinter Window
    background = PhotoImage(file="images/loginvoterdown.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 350 and 300 respectively.
    w = Canvas(WIN, width=350, height=230, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 350 and 300
    w.create_rectangle(0, 0, 350, 230, fill="#edd09f", outline='#dca028')
    w.pack(padx=50, pady=(250,0))

    #Function named temp_voter_id with one parameter i.e. 'e'
    def temp_voter_id(e):
        '''Clears voter_idtemp_voter_id_entry to take user input'''
        voter_idtemp_voter_id_entry.delete(0, "end")

    #Entry Box to  take voter_idtemp_voter_id Input from user
    voter_idtemp_voter_id_entry = Entry(WIN, font=tfont_tup, justify="center", width=15, foreground="#AFAFAF")
    #Added Text in Entry Box
    voter_idtemp_voter_id_entry.insert(2, "Voter ID")
    #Bind Entry so that when Clicked for Input it calls temp_voter_id
    voter_idtemp_voter_id_entry.bind("<FocusIn>", temp_voter_id)
    voter_idtemp_voter_id_entry.place(x=85, y=290)


         # Created a Function named on_enter_voterlogin_button with 'e' as one parameter
    def on_enter_voterlogin_button(e):
        '''Changed Background and Foreground of Register Button named voterlogin_button
        to #ABBC41 and white respectively when function is called.'''
        voterlogin_button.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_voterlogin_button with 'e' as one parameter
    def on_leave_voterlogin_button(e):
        '''Changed Background and Foreground of Register Button named voterlogin_button to
        pink and black respectively when function is called.'''
        voterlogin_button.config(background= '#d98d0b', foreground= 'black')

    #Log in Which when pressed calls voterlogin_validate by providing userentry as arguments
    voterlogin_button = Button(WIN, font=tfont_tup, justify="center", width=10, borderwidth=0, text="Next", bg="#d98d0b",command=lambda : confirm_voter(WIN,voter_idtemp_voter_id_entry.get()))
    voterlogin_button.place(x=110, y=370)


    


    #Created a Bind i.e. When Entered inside a Register button calls on_enter_voter_voterlogin function
    #and when leaves the Register button calls on_leave_voter_voterlogin function
    voterlogin_button.bind('<Enter>',on_enter_voterlogin_button)
    voterlogin_button.bind('<Leave>',on_leave_voterlogin_button)


    #Updates GUI Into TKinter Window
    WIN.mainloop()




    



#calls voterlogin function
voterlogin()