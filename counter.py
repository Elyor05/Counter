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

clik.place(relx=20, y=20, anchor="n")

button = Button(okno, text='click_here',
                fg='black', bg='yellow',
                font=('Helvetica', 10, 'bold'),
                padx=5, pady=5,
                command=click
                )
button.place(relx=0.3, rely=0.6)

okno.mainloop()
