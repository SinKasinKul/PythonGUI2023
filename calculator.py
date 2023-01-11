from tkinter import *
from tkinter.ttk import * #theme of Tk

GUI = Tk()
GUI.geometry('500x550')
GUI.title('App Bill calculate.')

style = Style()

style.configure('W.TButton', font = ('calibri', 10, 'bold'),foreground = 'black') #, 'underline'

L01 = Label(GUI,text='Bill Buffet.',font=('Angsana New',30,'bold'))
L01.pack(pady=20)
####################
L02 = Label(GUI,text='Buffet Bill Total(THB).',font=('Angsana New',16,'bold'))
L02.pack(pady=5)

v_total = StringVar() # special value for keep data in GUI
E01 = Entry(GUI,textvariable=v_total,font=('Angsana New',16))
E01.pack(pady=10)
####################
L03 = Label(GUI,text='How many person?',font=('Angsana New',16,'bold'))
L03.pack(pady=5)

v_person = StringVar()
E02 = Entry(GUI,textvariable=v_person,font=('Angsana New',16))
E02.pack(pady=10)

####################
L04 = Label(GUI,text='Service Change 10%',font=('Angsana New',16,'bold'))
L04.pack(pady=5)

####################
L05 = Label(GUI,text='Vat 7%',font=('Angsana New',16,'bold'))
L05.pack(pady=5)

v_result01 = StringVar()
result01 = Label(GUI,textvariable=v_result01,foreground='green')
result01.pack(pady=5)

v_result02 = StringVar()
result02= Label(GUI,textvariable=v_result02,foreground='green')
result02.pack(pady=5)

v_result03 = StringVar()
result03= Label(GUI,textvariable=v_result03,foreground='green')
result03.pack(pady=5)

###################
def Cal() :
    try :
        total = float(v_total.get())
        person = int(v_person.get())

        NTotal = total * person
        ServiceChange = (NTotal * 10) / 100
        vat = (NTotal * 7) / 100
        Gtotal = NTotal + ServiceChange + vat
        
        text01 = f'Net amount:{NTotal:,.2f} THB, Service Change 10%:{ServiceChange:,.2f} THB, Vat7%:{vat:,.2f} THB'
        text03 = f'Total amount:{Gtotal:,.2f} THB'
        text02 = f'with {person} Person ({total:,.2f} per Person.)'
        v_result01.set(text01)
        v_result03.set(text03)
        v_result02.set(text02)
    except:
        v_person.set('')
        v_total.set('')
        text = 'Error!!!, Please input number.'
        v_result01.set(text)
        v_result02.set('')

########
B01 = Button(GUI,text='Click',style='W.TButton',command=Cal)
B01.pack(pady=10,ipadx=20,ipady=20)

def Close() :
    GUI.quit()

B02 = Button(GUI,text='Exit',width=10,style='W.TButton',command=Close)
B02.place(x=400,y=510)


GUI.mainloop()

