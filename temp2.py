# from tkinter import *
# WIDTH, HEIGHT = 1130, 650

# root = Tk()
# # frame = Frame(root)
# frame = Canvas(root, width=WIDTH, height=HEIGHT)
# frame.pack()

# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )

# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)

# greenbutton = Button(frame, text="green", fg="green")
# greenbutton.pack( side = LEFT )

# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )

# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)

# root.mainloop()

from tkinter import *
# import tkMessageBox
import tkinter

top = tkinter.Tk()

def helloCallBack():
   tkinter.tkMessageBox.showinfo( "Hello Python", "Hello World")

# B = tkinter.Button(top, text ="Hello", command = helloCallBack, foreground='red', background='blue')

canvas = Canvas(top, width=600, height=600)
canvas.pack()
x0, y0, x1, y1 = 100, 100, 600, 600
canvas.create_rectangle(x0, y0, x1, y1, fill='red')


# B.pack()
# B.place(bordermode=OUTSIDE, height=100, width=100, x=10, y=10)
top.mainloop()