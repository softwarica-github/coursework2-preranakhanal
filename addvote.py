#Imported Necessary Modules
from tkinter import *
from tkinter import ttk
import ast
from PIL import Image
from stegano import lsb
import json
from tkinter import Button


#Created a Function Named viewcandidate Which Stores all the Codes of viewcandidate Page
# so it can be called later from another program
def viewcandidate():
    '''Similarly,Adding Title to the window and Providing Geometry to the window.'''
    WIN_viewcandidate = Tk()
    WIN_viewcandidate.title('Online Voting System')
    WIN_viewcandidate.geometry('360x640')

    # Placed backround_top.png image as Background to a Tkinter Window
    background = PhotoImage(file="images/plainbackground.png")
    label_background = Label(WIN_viewcandidate, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 240 and 400 respectively.
    w = Canvas(WIN_viewcandidate, width=320, height=600, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 240 and 400
    w.create_rectangle(0, 0, 320, 600, fill="#edd09f", outline='#edd09f')
    w.pack(padx=(20,20), pady=(20,20))


    #List contaning properties of font
    tfont_tup = ("Comic Sans MS", 12)

    tv = ttk.Treeview(WIN_viewcandidate, show='tree', height=15)
    #Set theme of TreeView as Default
    ttk.Style().theme_use("default")
    #Configured Properties of Tree View
    ttk.Style().configure("Treeview", background="#edd09f",foreground="black",fieldbackground="#edd09f", rowheight=31,font = tfont_tup, highlightthickness=0, bd=0,padding=10,columns=1)
    ttk.Style().map("Treeview",background=[('selected','#edd09f')],foreground=[('selected','black')])
    tv['columns']=('Name')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=CENTER, width=140)
    
    
    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    # Created candidatelist as blank list
    detailedlist = decoded_data['Candidate']

    candidatelist = []
    # for loop to go through every value of detailedlist
    for candidate in detailedlist:
        name = (candidate[0])
        # append it into candidatelist
        candidatelist.append(name)

    # duplicates candidatelist list into orginal_candidatelist
    orginal_candidatelist = candidatelist.copy()
    # Calculated length of list
    orginal_length = len(candidatelist)
    
    current_count = 7
    # Check if Statement is Correct or not
    if orginal_length > current_count:
        # stores new length as how much orginal_length is more than 7
        new_length = orginal_length - 7
        # Calls for loop to pop all items after index 7
        for i in range(new_length):
            candidatelist.pop()

    # Function to handle button click event
    tfont_tup = ("Comic Sans MS", 15)
    # Loop through the candidate list and create buttons        
    candidates = []
    for i, candidate in enumerate(candidatelist):
        button = Button(WIN_viewcandidate, text=candidate, font=tfont_tup, command=lambda name=candidate: confirm_votes(WIN_viewcandidate,name))
        button.place(x=130, y=100 + i*60)
        candidates.append(button)
        
    def refresh(state,current_count,candidates):
        for candidate in candidates:
            candidate.destroy()
        
        candidatelist = [] 
        if state == True:
            new_current_count = current_count + 7  
            for candidate in detailedlist[current_count:new_current_count]:
                name = candidate[0]
                candidatelist.append(name)
        else:
            new_current_count = current_count - 7
            for candidate in detailedlist[new_current_count:current_count]:
                name = candidate[0]
                candidatelist.append(name)

        current_count = new_current_count
            
        for i, candidate in enumerate(candidatelist):
            button = Button(WIN_viewcandidate, text=candidate, font=tfont_tup, command=lambda name=candidate: confirm_votes(WIN_viewcandidate,name))
            button.place(x=130, y=100 + i*60)
            candidates.append(button)
    # list containing properties for font
    tfont_tup = ("Comic Sans MS", 12)
    tfont_top = ("Comic Sans MS", 15)

    # Created Rectangle with width of 240 and height of 35
    w.create_rectangle(0, 0, 320, 35, outline="#fb0", fill="#ebac3f")
    # Created a text named viewcandidate
    viewcandidate_label = Label(WIN_viewcandidate, text="candidate List", font=tfont_top, justify="center", background="#ebac3f", foreground="black")
    viewcandidate_label.place(x=133, y=20)

    #function named reback which destroys Tkinter window and calls p function .i.e. profile_view from profile page
    def reback():
        WIN_viewcandidate.destroy()
        
    next = True
    back = False
    #return button which when pressed calls reback
    return_button = Button(WIN_viewcandidate, text="Next", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command=lambda: refresh(next,current_count,candidates))
    return_button.place(x = 230,y = 540)
    
    back_button = Button(WIN_viewcandidate, text="Back", padx=10, borderwidth=0, font=tfont_tup, background='#d98d0b', foreground='black', command=lambda: refresh(back,current_count,candidates))
    back_button.place(x = 80,y = 540)

    #Places all GUI of Tkinter Window into it.
    WIN_viewcandidate.mainloop()

#Calls viewcandidate Function
viewcandidate()