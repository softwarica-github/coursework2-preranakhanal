from tkinter import Button, Label, Toplevel


def error(title,message):
    '''Created TopLevel as WIN_top,providing its geometry and title.'''
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title(title)
    WIN_top.geometry('300x150')

    #Made a list Contaning properties of font so can be called many times in program.
    tfont_tup = ("Comic Sans MS", 15)



