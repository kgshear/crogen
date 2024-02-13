from tkinter import *
from tkinter import ttk

win = Tk()

win.geometry("750x250")


#Define a function to show a message
def myclick():
   message= "Hello "+ entry.get()
   label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
   entry.delete(0, 'end')
   label.pack(pady=30)

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
entry = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Enter Your Name")
entry.pack()
#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()