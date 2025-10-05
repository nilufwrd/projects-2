from tkinter import*
def done():
    name=entry.get()
    print(name)
    if name:
    
        x=len(name)>1
        
        
        print('Thank you...')
    else:
        print('Please enter something...')
    
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)


    
window = Tk()

entry = Entry(window,font= ('Arial',25),fg='grey',bg='pink',)
entry.insert(0,'Enter...')
entry.pack(side=LEFT)
deletebutton=Button(window,text='delete',command=delete)
deletebutton.pack(side=RIGHT)
donebutton=Button(window,command=done,text='done')
donebutton.pack(side=RIGHT)

backspacebutton=Button(window,text='backspace',command=backspace)
backspacebutton.pack(side=RIGHT)

window.mainloop()