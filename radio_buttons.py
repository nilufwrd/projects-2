from tkinter import*
#radio button is similar to chechbox but you can only select one from a group
food=['pizza','hamburger','hotdog']
def order():
 if (x.get()==0):
  print('you ordered pizza')
 elif(x.get()==1):
  print('you ordered a hamburger')
 elif(x.get()==2):
  print('you ordered a hotdog')
window=Tk()
x = IntVar()
for index in range(len(food)):
 radiobutton=Radiobutton(window,text=food[index],#adds text to radio buttons
                         variable=x,#groups radio buttons to get if they share the same variable
                         value=index,#assigns each radiobutton with a different value
                         padx=25,#adds padding on x-axis
                         font=('Impact',10),
                         indicator=0,#eliminate circle indicators
                         width=100#sets width of radio buttons
                         )
 
 radiobutton.pack(anchor=W)

window.mainloop()