#Imported Necessary Modules
import ast
from io import BytesIO
import json
import os
from tkinter import *
import tkinter
from PIL import Image
import random
import requests
from stegano import lsb


#Created a Function Named add_new_voter Which Stores all the Codes of add_new_voter Page
# so it can be called later from another program
def add_new_voter():
    '''Created a Tkinter Window named WIN and placed logo_image as icon photo.
    Similarly,Adding Title to the window and Providing Geaometry to the window.'''
    WIN = Tk()
    logo_image = PhotoImage(file="images/logo.png")
    WIN.iconphoto(False, logo_image)
    WIN.title('Online Voting System')
    WIN.geometry('360x640')

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)

    # Placed addvoter.png image as Background to a TKinter Window
    background = PhotoImage(file="images/addvoter.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    #Created a Canvas with width and height of 280 and 425 respectively.
    w = Canvas(WIN, width=280, height=425, borderwidth=0, highlightthickness=0)
    #Created a Rectangle in a Canvas with width and height of 280 and 425
    w.create_rectangle(0, 0, 280, 425, fill="#EF97CC", outline='#6E0042')
    w.pack(padx=30, pady=(155,0))

    #Function named temp_name with one parameter i.e. 'e'
    def temp_name(e):
        '''Clears name_entry to take user input'''
        name_entry.delete(0, "end")

    #Entry Box to take name Input from user
    name_entry = Entry(WIN, font=tfont_tup, justify="center", width=18, foreground="#AFAFAF")
    #Added Text in Entry Box
    name_entry.insert(0, "Full Name")
    #Bind Entry so that when Clicked for Input it calls temp_name
    name_entry.bind("<FocusIn>",temp_name)
    name_entry.place(x=70, y=180)

    #Function named temp_dob with one parameter i.e. 'e'
    def temp_DOB(e):
        '''Clears DOB entry to take user input'''
        DOB_entry.delete(0, "end")

    #Entry Box to take DOB Input from user
    DOB_entry = Entry(WIN, font=tfont_tup, justify="center", width=18, foreground="#AFAFAF")
    #Added Text in Entry Box
    DOB_entry.insert(1, "Date of Birth")
    #Bind Entry so that when Clicked for Input it calls temp_DOB
    DOB_entry.bind("<FocusIn>",temp_DOB)
    DOB_entry.place(x=70, y=240)

    #Function named temp_citizenship with one parameter i.e. 'e'
    def temp_citizenship(e):
        '''Clears citizenship_entry to take user input'''
        citizenship_entry.delete(0, "end")

    #Entry Box to take citizenship Input from user
    citizenship_entry = Entry(WIN, font=tfont_tup, justify="center", width=18, foreground="#AFAFAF")
    #Added Text in Entry Box
    citizenship_entry.insert(2, "Citizenship Number")
    #Bind Entry so that when Clicked for Input it calls temp_citizenship
    citizenship_entry.bind("<FocusIn>",temp_citizenship)
    citizenship_entry.place(x=70, y=300)

    #Function named temp_phone with one parameter i.e. 'e'
    def temp_phone(e):
        '''Clears phone_entry to take user input'''
        phone_entry.delete(0, "end")

    #Entry Box to take phone Input from user
    phone_entry = Entry(WIN, font=tfont_tup, justify="center", width=18, foreground="#AFAFAF")
    #Added Text in Entry Box
    phone_entry.insert(2, "Phone Number")
    phone_entry.bind("<FocusIn>",temp_phone)
    #Bind Entry so that when Clicked for Input it calls temp_phone
    phone_entry.place(x=70, y=360)



    #Function named temp_address with one parameter i.e. 'e'
    def temp_address(e):
        '''Clears citizenship_entry to take user input'''
        address_entry.delete(0, "end")

    #Entry Box to take address Input from user
    address_entry = Entry(WIN, font=tfont_tup, justify="center", width=18, foreground="#AFAFAF")
    #Added Text in Entry Box
    address_entry.insert(2, "Address")
    #Bind Entry so that when Clicked for Input it calls temp_address
    address_entry.bind("<FocusIn>",temp_address)
    address_entry.place(x=70, y=420)
    




    # Created a Function named on_enter_add_new_voter_button with 'e' as one parameter
    def on_enter_add_new_voter_button(e):
        '''Changed Background and Foreground of add_new_voter Button named add_new_voter_button
        to #ABBC41 and white respectively when function is called.'''
        add_new_voter_button.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_add_new_voter_button with 'e' as one parameter
    def on_leave_add_new_voter_button(e):
        '''Changed Background and Foreground of add_new_voter Button named add_new_voter_button to
        pink and black respectively when function is called.'''
        add_new_voter_button.config(background= '#eb5454', foreground= 'black')

     # created a add_new_voter Button which calls add_new_voter_page function when pressed
    add_new_voter_button = Button(WIN,text="Add Voter",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=lambda:create_new_voter(WIN,name_entry,DOB_entry,citizenship_entry,phone_entry,address_entry))
    add_new_voter_button.place(x=114,y=473)
    #Created a Bind i.e. When Entered inside a add_new_voter button calls on_enter_add_new_voter_button function
    #and when leaves the add_new_voter button calls on_leave_add_new_voter_button function
    add_new_voter_button.bind('<Enter>',on_enter_add_new_voter_button)
    add_new_voter_button.bind('<Leave>',on_leave_add_new_voter_button)
    
    
        # Created a Function named on_enter_add_new_voter_button with 'e' as one parameter
    def on_enter_return_button(e):
        '''Changed Background and Foreground of add_new_voter Button named add_new_voter_button
        to #ABBC41 and white respectively when function is called.'''
        return_button.config(background='#edd8ed',foreground= "red")

    # Created a Function named on_leave_add_new_voter_button with 'e' as one parameter
    def on_leave_return_button(e):
        '''Changed Background and Foreground of add_new_voter Button named add_new_voter_button to
        pink and black respectively when function is called.'''
        return_button.config(background= '#eb5454', foreground= 'black')

     # created a add_new_voter Button which calls add_new_voter_page function when pressed
    return_button = Button(WIN,text="Return",padx=13,borderwidth=0,font=tfont_tup,background= '#eb5454', foreground= 'black',command=lambda:return_adminhomepage(WIN))
    return_button.place(x=125,y=525)
    #Created a Bind i.e. When Entered inside a add_new_voter button calls on_enter_add_new_voter_button function
    #and when leaves the add_new_voter button calls on_leave_add_new_voter_button function
    return_button.bind('<Enter>',on_enter_return_button)
    return_button.bind('<Leave>',on_leave_return_button)


    #places all GUI into Tkinter Window
    WIN.mainloop()

#calls add_new_voter function to execute
add_new_voter()