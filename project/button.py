from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
tf=Text(frame)


but=Button(frame,text='one',fg='white',bg="red")
but.grid(row=0,column=0)

but1=Button(frame,text='two',fg='yellow')
but1.grid(row=0,column=1)

but2=Button(frame,text='three',fg='yellow')
but2.grid(row=0,column=2)

but3=Button(frame,text='four',fg='yellow')
but3.grid(row=0,column=3)

root.mainloop()



