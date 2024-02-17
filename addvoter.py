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

def addnewvoter_validation(name_entry, dob_entry, citizenship_entry, phone_entry, address_entry):
    if len(name_entry.get()) != 0 and isinstance(name_entry.get(), str) and len(dob_entry.get()) != 0 and dob_entry.get().isdigit() and len(dob_entry.get()) == 4 and len(citizenship_entry.get()) != 0 and citizenship_entry.get().isdigit() and len(phone_entry.get()) == 10 and phone_entry.get().isdigit() and len(address_entry.get()) != 0 and isinstance(address_entry.get(), str):
        image_path = "images/profileimg.png"
        decoded_data = lsb.reveal(image_path)
        decoded_data = json.loads(decoded_data)
        
        for i in decoded_data["Voter"]:
            if i[2] == citizenship_entry.get():
                title = "Error"
                message = "Citizenship Number \n Already Exists"
                from errors import error as show_error
                show_error(title,message)
                return False
        
        return True
    else:
        return False

def send(code,phone):
    try:
        to_phone = phone['phoneNumber']
        # Call an api and send parameter to it
        r = requests.get(
            "http://api.sparrowsms.com/v2/sms/",
            params={'token' : 'v2_Rri05e6U3XkCcnmjeOnfxdDzAqz.dY9a',
                  'from'  : 'TheAlert',
                  'to'    : to_phone,
                  'text'  : f'Dear User,Please use {code} as your Voter ID.'})
        status_code = r.status_code
        response = r.text
        response_json = r.json()
    except Exception as e:
        print(f"Error sending OTP: {str(e)}")


def create_new_voter(WIN,name_entry, dob_entry, citizenship_entry, phone_entry, address_entry):
    # Get the data from the user entries
    name = name_entry.get()
    age = dob_entry.get()
    citizenship = citizenship_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    code = random.randint(10000, 99999)
    voted = False

    if addnewvoter_validation(name_entry, dob_entry, citizenship_entry, phone_entry, address_entry):
        # If data is valid, create a new voter dictionary
        image_path = "images/profileimg.png"
        decoded_data = lsb.reveal(image_path)
        decoded_data = json.loads(decoded_data)
        voting_system = decoded_data
    
        new_data = [name, age, citizenship, phone, address, code , voted]
        voting_system["Voter"].append(new_data)
        
        phone = {'phoneNumber': '+977' + phone}
        send(code,phone)
        json_data = json.dumps(voting_system)
        # Encode the JSON data into the image using least significant bit (LSB) method
        encoded_image = lsb.hide(image_path, json_data)
        # Save the output image
        encoded_image.save(image_path)
        confirm_voter(WIN)
    else:
        # If data is not valid, display an error message
        title = "Error"
        message = "Recheck Your Input\n Values"
        from errors import error as show_error
        show_error(title,message)

def confirm_voter(WIN):
    '''Created TopLevel as WIN_top,providing its geometry and title.'''
    
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title('Confirm Voter')
    WIN_top.geometry('300x150')

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)


    def no():
        WIN_top.destroy()
        WIN.destroy()  # Destroy the current page
        from admin_login import homepage as admin_homepage
        admin_homepage()


    #Message to be Displayed at Toplevel
    message = Label(WIN_top, bg='#E0D9EF', text="Name has been successfully \n added in the voter list!", font=tfont_tup, justify="center",
                        foreground="#000000")
    message.pack()


    #No Button which when pressed calls no function
    no_button = Button(WIN_top, bg='#FFFFFF', text=" OK  ", background='Red', foreground="Black", font=("Comic Sans MS", 12), command=no)
    no_button.place(x=108, y=80)

    #Places all GUI of Toplevel into it
    WIN_top.mainloop()

def return_adminhomepage(WIN):
    WIN.destroy()
    from admin_login import homepage as admin_homepage
    admin_homepage()


#Created a Function Named add_new_voter Which Stores all the Codes of add_new_voter Page
# so it can be called later from another program
def add_new_voter():
    '''Similarly,Adding Title to the window and Providing Geaometry to the window.'''
    WIN = Tk()
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