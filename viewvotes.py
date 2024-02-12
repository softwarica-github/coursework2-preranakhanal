#Imported Necessary Modules
from tkinter import *
from tkinter import ttk
import ast
from PIL import Image
from stegano import lsb
import json



#Created a Function Named viewvotes Which Stores all the Codes of viewvotes Page
# so it can be called later from another program
def viewvotes():
    '''Created a Tkinter Window named WIN_viewvotes and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN_viewvotes = Tk()
    logo_image = PhotoImage(file="images/fish2.png")
    WIN_viewvotes.iconphoto(False, logo_image)
    WIN_viewvotes.title('Online Voting System')
    WIN_viewvotes.geometry('360x640')

    # Placed backround_top.png image as Background to a Tkinter Window
    background = PhotoImage(file="images/plainbackground.png")
    label_background = Label(WIN_viewvotes, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 240 and 400 respectively.
    w = Canvas(WIN_viewvotes, width=320, height=600, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 400
    w.create_rectangle(0, 0, 320, 600, fill="#edd09f", outline='#edd09f')
    w.pack(padx=(20,20), pady=(20,20))



    #List contaning properties of font
    tfont_tup = ("Comic Sans MS", 12)

    tv = ttk.Treeview(WIN_viewvotes, show='tree', height=15)
    #Set theme of TreeView as Default
    ttk.Style().theme_use("default")
    #Configured Properties of Tree View
    ttk.Style().configure("Treeview", background="#edd09f",foreground="black",fieldbackground="#edd09f", rowheight=31,font = tfont_tup, highlightthickness=0, bd=0,padding=10,columns=1)
    ttk.Style().map("Treeview",background=[('selected','#edd09f')],foreground=[('selected','black')])
    tv['columns']=('Name', 'Vote')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=W, width=140)
    tv.column('Vote', anchor=E, width=98)
    
    
    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    # Created candidatelist as blank list
    detailedlist = decoded_data['Candidate']

    candidatelist = []
    # for loop to go through every value of detailedlist
    for candidate in reversed(detailedlist):
        name = (candidate[0],candidate[1])
        # append it into candidatelist
        candidatelist.append(name)

    # duplicates candidatelist list into orginal_candidatelist
    orginal_candidatelist = candidatelist.copy()
    # Calculated length of list
    orginal_length = len(candidatelist)
    # Check if Statement is Correct or not
    if orginal_length > 7:
        # stores new length as how much orginal_length is more than 7
        new_length = orginal_length - 7
        # Calls for loop to pop all items after index 7
        for i in range(new_length):
            candidatelist.pop()

    a = 0
    # insert Data from a list of candidatelist
    for data in candidatelist:
        tv.insert(parent='', index=a, iid=a, text='', values=data)
        a = a + 1
    tv.place(x=55, y=100)

    # list containing properties for font
    tfont_tup = ("Comic Sans MS", 12)
    tfont_top = ("Comic Sans MS", 15)

    # Created Rectangle with width of 240 and height of 35
    w.create_rectangle(0, 0, 320, 35, outline="#fb0", fill="#ebac3f")
    # Created a text named viewvotes
    viewvotes_label = Label(WIN_viewvotes, text="candidate List", font=tfont_top, justify="center", background="#ebac3f", foreground="black")
    viewvotes_label.place(x=133, y=20)



    #function named Search
    def search():
        try:
            #for loop which runs till there is a value in orginal_candidatelist list
            for value in orginal_candidatelist:
                #looks if user entered username is there in list
                if username_search.get() == value[0]:
                    #deletes all data shown in viewvotes
                    for item in tv.get_children():
                        tv.delete(item)
                    #show Data of Found User Only
                    tv.insert(parent='', index=1, iid=1, text='', values=value)
                    #breaks the loop
                    break
                #if enterd username is not matched with value and is blank then this executes
                elif username_search.get() == "":
                    #Deletes All Data of candidatelist
                    for item in tv.get_children():
                        tv.delete(item)
                    b = 1
                    for data in candidatelist:
                        tv.insert(parent='', index=b, iid=b, text='', values=data)
                        b = b + 1
                    #breaks loop
                    break
            #if value is not found in orginal_candidatelist list
            else:
                #raises a Errror
                raise ValueError('Value Not found')
        #runs this part of code if error occured
        except:
            #Calls data_not_foound
            data_not_found()



    #Place to Enter Username to search for
    username_search = Entry(WIN_viewvotes, font=tfont_tup, justify="center", width=19, foreground="#AFAFAF")
    username_search.place(x=88, y=425)

    def temp_username(e):
        '''Clears phone_entry to take user input'''
        username_search.delete(0, "end")
    username_search.bind("<FocusIn>",temp_username)
    #Text Displayed in Entry bar so User Know What to look for
    username_search.insert(1,"Enter User Name")
    #Search button which when pressed calls search
    search_button = Button(WIN_viewvotes, text="Search", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command=search)
    search_button.place(x = 135,y = 470)
    #addcandidate button which when pressed calls reback
    addcandidate_button = Button(WIN_viewvotes, text="Add Candidate", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command=lambda:addcandidate(WIN_viewvotes))
    addcandidate_button.place(x = 60,y = 520)
    #return button which when pressed calls reback
    return_button = Button(WIN_viewvotes, text="Return", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command= lambda:return_adminhomepage(WIN_viewvotes))
    return_button.place(x = 225,y = 520)

    #Places all GUI of Tkinter Window into it.
    WIN_viewvotes.mainloop()

#Calls viewvotes Function
viewvotes()