from tkinter import *

root = Tk()
root.title("Prog")
root.resizable(0,0)
root["bg"] = "#563"
root.geometry("500x500-30-30")

def clickm():
    #lab.config(text = 'Новый текст')#
    #lab['text'] = 'Новый текст'#
    btn2.config(text="jfjfjffjfjf")

btn1 = Button(root, text="click",font="Arial 20 bold",bg="yellow",fg="purple", command=clickm)
btn1.place(x=0,y=0)

btn2 = Button(root, text="tap",font="Arial 20 bold",bg="orange",fg="green")
btn2.place(x=90,y=0)

btn3 = Button(text="    click   ")
btn3.place(x=0,y=90)

btn4 = Button(text="    click   ")
btn4.place(x=90,y=90)

lab = Label(root,text="rfrfrfrf").pack()

root.mainloop()
