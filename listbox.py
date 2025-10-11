#listbox = a listing of selectable text items within it's own container
def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    for index in food:
        print(index)
    
def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    
    listbox.config(height=listbox.size())
from tkinter import*

window=Tk()


listbox= Listbox(window,
                 bg='grey',
                 fg='pink',
                 font=('Constantia',25),
                 width=12,#genişlik
                 selectmode=MULTIPLE,#fazladan şey seç
                 )
listbox.pack()
listbox.insert(1,'pizza')#yazılanı ekler
listbox.insert(2,'hamburger')
listbox.insert(3,'hotdog')
listbox.insert(4,'lasagna')
listbox.insert(5,'pasta')
listbox.config(height=listbox.size())#kutunun boyunu inserttekilere göre ayarlar
submitbutton = Button(window,text='submit',command=submit)
submitbutton.pack()
entrybox = Entry(window)
entrybox.pack()
addbutton = Button(window,text='add',command=add)
addbutton.pack()
deletebutton=Button(window,text='delete',command=delete)
deletebutton.pack()
window.mainloop()