#Imported Necessary Modules
from tkinter import *
from tkinter import ttk
import ast
from PIL import Image
from stegano import lsb
import json



def data_not_found():
    '''Store title for toplevel in title and message to be displayed at message and calls show_error function providing title and message'''
    title = "Username Not Found"
    message = "Input Username was\n not Found"
    from errors import error as show_error
    show_error(title, message)
    
def return_adminhomepage(WIN):
    WIN.destroy()
    from admin_login import homepage as admin_homepage
    admin_homepage()

#Created a Function Named viewvoter Which Stores all the Codes of viewvoter Page
# so it can be called later from another program
def viewvoter():
    '''Created a Tkinter Window named WIN_viewvoter and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN_viewvoter = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN_viewvoter.iconphoto(False, logo_image)
    WIN_viewvoter.title('Online Voting System')
    WIN_viewvoter.geometry('360x640')

    # Placed backround_top.png image as Background to a Tkinter Window
    background = PhotoImage(file="images/plainbackground.png")
    label_background = Label(WIN_viewvoter, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 240 and 400 respectively.
    w = Canvas(WIN_viewvoter, width=320, height=600, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 400
    w.create_rectangle(0, 0, 320, 600, fill="#edd09f", outline='#edd09f')
    w.pack(padx=(20,20), pady=(20,20))



    #List contaning properties of font
    tfont_tup = ("Comic Sans MS", 12)

    tv = ttk.Treeview(WIN_viewvoter, show='tree', height=15)
    #Set theme of TreeView as Default
    ttk.Style().theme_use("default")
    #Configured Properties of Tree View
    ttk.Style().configure("Treeview", background="#edd09f",foreground="black",fieldbackground="#edd09f", rowheight=31,font = tfont_tup, highlightthickness=0, bd=0,padding=10,columns=1)
    ttk.Style().map("Treeview",background=[('selected','#edd09f')],foreground=[('selected','black')])
    tv['columns']=('Name', 'Age')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=W, width=140)
    tv.column('Age', anchor=E, width=98)
    
    
    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    # Created voterlist as blank list
    detailedlist = decoded_data['Voter']

    voterlist = []
    # for loop to go through every value of detailedlist
    for voter in reversed(detailedlist):
        name = (voter[0], voter[1])
        # append it into voterlist
        voterlist.append(name)

    # duplicates voterlist list into orginal_voterlist
    orginal_voterlist = voterlist.copy()
    # Calculated length of list
    orginal_length = len(voterlist)
    # Check if Statement is Correct or not
    if orginal_length > 7:
        # stores new length as how much orginal_length is more than 7
        new_length = orginal_length - 7
        # Calls for loop to pop all items after index 7
        for i in range(new_length):
            voterlist.pop()

    a = 0
    # insert Data from a list of voterlist
    for data in voterlist:
        tv.insert(parent='', index=a, iid=a, text='', values=data)
        a = a + 1
    tv.place(x=55, y=100)

    # list containing properties for font
    tfont_tup = ("Comic Sans MS", 12)
    tfont_top = ("Comic Sans MS", 15)

    # Created Rectangle with width of 240 and height of 35
    w.create_rectangle(0, 0, 320, 35, outline="#fb0", fill="#ebac3f")
    # Created a text named viewvoter
    viewvoter_label = Label(WIN_viewvoter, text="Voter List", font=tfont_top, justify="center", background="#ebac3f", foreground="black")
    viewvoter_label.place(x=133, y=20)



    #function named Search
    def search():
        try:
            #for loop which runs till there is a value in orginal_voterlist list
            for value in orginal_voterlist:
                #looks if user entered username is there in list
                if username_search.get() == value[0]:
                    #deletes all data shown in viewvoter
                    for item in tv.get_children():
                        tv.delete(item)
                    #show Data of Found User Only
                    tv.insert(parent='', index=1, iid=1, text='', values=value)
                    #breaks the loop
                    break
                #if enterd username is not matched with value and is blank then this executes
                elif username_search.get() == "":
                    #Deletes All Data of voterlist
                    for item in tv.get_children():
                        tv.delete(item)
                    b = 1
                    for data in voterlist:
                        tv.insert(parent='', index=b, iid=b, text='', values=data)
                        b = b + 1
                    #breaks loop
                    break
            #if value is not found in orginal_voterlist list
            else:
                #raises a Errror
                raise ValueError('Value Not found')
        #runs this part of code if error occured
        except:
            #Calls data_not_foound
            data_not_found()

    #function named reback which destroys Tkinter window and calls p function .i.e. profile_view from profile page
    def reback():
        WIN_viewvoter.destroy()

    #Place to Enter Username to search for
    username_search = Entry(WIN_viewvoter, font=tfont_tup, justify="center", width=19, foreground="#AFAFAF")
    username_search.place(x=88, y=425)

    def temp_username(e):
        '''Clears phone_entry to take user input'''
        username_search.delete(0, "end")
    username_search.bind("<FocusIn>",temp_username)
    #Text Displayed in Entry bar so User Know What to look for
    username_search.insert(1,"Enter User Name")
    #Search button which when pressed calls search
    search_button = Button(WIN_viewvoter, text="Search", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command=search)
    search_button.place(x = 135,y = 470)
    #return button which when pressed calls reback
    return_button = Button(WIN_viewvoter, text="Return", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command=lambda:return_adminhomepage(WIN_viewvoter))
    return_button.place(x = 135,y = 520)

    #Places all GUI of Tkinter Window into it.
    WIN_viewvoter.mainloop()

#Calls viewvoter Function
viewvoter()