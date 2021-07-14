#import library
from tkinter import *
import tkinter as tk
from tkinter import ttk
#initialize window
root = Tk()
root.geometry('800x600')
root.config(bg = 'SlateGray3')
root.title('Cadastro')
root.resizable(0,0)

#Cadastro Alunos
contactlist = [
    ['Nilton',  '001', 'Informatica','12345678'],
    ['Leonardo',  '002', 'Informatica','12345678'],
    ['Gabriel',   '003', 'Informatica','12345678'],
    ]
Name = StringVar()
Id = StringVar()
Curso = StringVar()
Telefone = StringVar()
#create frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=10)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


########### function to get select value

def Selected():
    return int(select.curselection()[0])

##fun to add new contact
def AddContact():
    contactlist.append([Name.get(), Id.get(),Curso.get(),Telefone.get()])
    Select_set()

# fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Id.get(),Curso.get(),Telefone.get()]
    Select_set()
    
#to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
# to view selected contact(first select then click on view button)
def VIEW():
    NAME, ID, CURSO, TELEFONE = contactlist[Selected()]
    Name.set(NAME)
    Id.set(ID)
    Curso.set(CURSO)
    Telefone.set(TELEFONE)


###exit game window   
def EXIT():
    root.destroy()

#empty name and Id field

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,Curso,Telefone in contactlist :
        select.insert (END, name)
Select_set()



######define buttons #####labels and entry widget
Label(root, text = 'CADASTRO ALUNO', font='arial 18 bold', bg = 'SlateGray3').place(x= 300, y=15)

Label(root, text = 'NOME', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=70)
Entry(root, textvariable = Name).place(x= 100, y=70)
Label(root, text = 'ID', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=100)
Entry(root, textvariable = Id).place(x= 60, y=100)
Label(root, text = 'Curso', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=130)
Entry(root, textvariable = Curso).place(x= 90, y=130)
Label(root, text = 'Telefone', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=160)
Entry(root, textvariable = Telefone).place(x= 110, y=160)



Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddContact).place(x= 250, y=70)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT).place(x= 330, y=70)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE).place(x= 410, y=70)
Button(root,text="VER", font='arial 12 bold',bg='SlateGray4', command = VIEW).place(x= 510, y=70)


Button(root,text="SAIR", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 350, y=560)


#CAdastro PRofessores
Professores = [
    ['Professor1',  'Formação1'],
    ['Professor2',  'Formação2'],
    ]
Nomeprof = StringVar()
Form = StringVar()

frame2 = Frame(root)
frame2.pack(side = LEFT)

scroll2 = Scrollbar(frame2, orient=VERTICAL)
select2 = Listbox(frame2, yscrollcommand=scroll2.set, height=10)
scroll2.pack(side=LEFT, fill=Y)
select2.pack(side=LEFT,  fill=BOTH, expand=2)



def Selected2():
    return int(select2.curselection()[0])

def AddProf():
    Professores.append([Nomeprof.get(), Form.get()])
    Select_set2()

def EDIT2():
    Professores[Selected()] = ([Nomeprof.get(), Form.get()])
    Select_set2()
    
def DELETE2():
    del Professores[Selected2()]
    Select_set2()
   
def VIEW2():
    NOMEPROF, FORM = Professores[Selected2()]
    Nomeprof.set(NOMEPROF)
    Form.set(FORM)

def Select_set2() :
    Professores.sort()
    select2.delete(0,END)
    for Nomeprof,Form in Professores :
        select2.insert (END, Nomeprof)

Select_set2()

######define buttons #####labels and entry widget
Label(root, text = 'CADASTRO PROFESSOR', font='arial 18 bold', bg = 'SlateGray3').place(x= 250, y=360)

Label(root, text = 'NOME', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=400)
Entry(root, textvariable = Nomeprof).place(x= 90, y=400)
Label(root, text = 'FORMAÇÃO', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=430)
Entry(root, textvariable = Form).place(x= 130, y=430)

Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddProf).place(x= 300, y=400)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT2).place(x= 380, y=400)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE2).place(x= 460, y=400)
Button(root,text="VER", font='arial 12 bold',bg='SlateGray4', command = VIEW2).place(x= 570, y=400)


root.mainloop()
  
