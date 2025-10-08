from tkinter import*
def display():
    if (x.get()==1):
        print('you agree')
    else:
        print('you dont agree')
window=Tk()
x= IntVar()
check_button = Checkbutton(window,
                           text='I agree to something',
                          bg='pink',
                          fg='grey',
                           variable=x,
                            onvalue=1,
                             offvalue=0,
                              command=display,
                              font=('Arial',20),
                              activeforeground='grey',
                              padx=25,
                              pady=10,)
check_button.pack(side=RIGHT)
window.mainloop()