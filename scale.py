from tkinter import*
window=Tk()
def submit():
    print('temperature is' + str(scale.get())+'degrees')
scale = Scale(window,from_=0,to=100,
              length=600,
              orient=VERTICAL,#orientation of scale
              font=('Consolas',20),
              tickinterval=10,#adds numeric indicators for value
              showvalue=0,#0 hides current value
              resolution=5,#incerement of slider
              troughcolor='pink',
              fg='grey',
              bg='purple'
              
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()
button=Button(window,text='submit',command=submit)
button.pack()
window.mainloop()