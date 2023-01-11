from tkinter import *
from tkinter.ttk import * #theme of Tk
import csv
from datetime import datetime

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file: # W = re-write file // A = Update file 
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.geometry('600x650')
GUI.title('Expense Record Application.')

FONT01 = ('Angsana New',16)

# Image
icon = r'D:\GitHub\PythonGUI2023\expense.png' #'D:\\GitHub\\PythonGUI2023\\expense.png'
iconImage = PhotoImage(file=icon)
L = Label(GUI,image=iconImage)
L.pack()

L01 = Label(GUI,text='Record My Expense.',font=('Angsana New',30,'bold'))
L01.pack(pady=10)

v_expense = StringVar()
E01 = Entry(GUI,textvariable=v_expense,font=FONT01)
E01.pack(pady=5)

L02 = Label(GUI,text='Amount.',font=('Angsana New',30,'bold'))
L02.pack(pady=10)

v_amount = StringVar()
E02 = Entry(GUI,textvariable=v_amount,font=FONT01)
E02.pack(pady=5)

v_result01 = StringVar()
result01 = Label(GUI,textvariable=v_result01,foreground='green')
result01.pack(pady=5)

def dataRecord(event=None):
    try:
        expense = v_expense.get()
        amount = float(v_amount.get())
        dateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        datd = [expense,amount,dateTime]
        writecsv(datd)
        v_result01.set('Record data success!!!')
        v_expense.set('')
        v_amount.set('')
        E01.focus()
    except:
        v_expense.set('')
        v_amount.set('')
        v_result01.set('Record data Failed!!!')

E01.bind('<Return>', lambda x: E02.focus()) 
E02.bind('<Return>',dataRecord) #event=None

def BTS(evet=None):
    v_expense.set('BTS')
    v_amount.set('145')

def BUS(evet=None):
    v_expense.set('Bus')
    v_amount.set('8')

def GAS(evet=None):
    v_expense.set('Gas')
    v_amount.set('1000')

Bbts = Button(GUI,text='BTS',command=BTS)
Bbts.place(x=20,y=180)
Bbus = Button(GUI,text='Bus',command=BUS)
Bbus.place(x=20,y=205)
Bgas = Button(GUI,text='Gas',command=GAS)
Bgas.place(x=20,y=230)

B1 = Button(GUI,text='Save',command=dataRecord)
B1.pack(ipadx=20,ipady=10)

E01.focus()

GUI.mainloop()