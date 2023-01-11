from tkinter import *

GUI = Tk()

tital = "My First Py GUI"
GUI.title(tital)
GUI.geometry('500x300')

L01 = Label(GUI,text='404. That\'s an error.',font=('Angsana New',40,'bold'))
L02 = Label(GUI,text='Please restart your PC.',font=('Angsana New',32,'bold'))
#L01.pack()
L01.place(x=20,y=20)
L02.place(x=20,y=100)
GUI.mainloop()


