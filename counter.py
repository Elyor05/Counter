from tkinter import *

okno = Tk()
okno.title('Chort')
okno.geometry('200x200')
okno.resizable(False, False)
okno.configure(bg='black')

cnt = 0

def click():
    global cnt
    cnt += 1
    clik.config(text=cnt)


clik = Label(okno, text='0',
             fg='black', bg='yellow',
             font=('Helvetica', 30, 'bold'),
             )

clik.place(x=20, y=20)

button = Button(okno, text='click_here',
                fg='black', bg='yellow',
                font=('Helvetica', 10, 'bold'),
                padx=5, pady=5,
                command=click
                )
button.place(x=100, y=100)

okno.mainloop()
