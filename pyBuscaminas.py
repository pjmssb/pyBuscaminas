from tkinter import *

root = Tk()
#Setting the window
root.configure(bg="black")
root.geometry('1440x720')
root.title('Juego de buscaminas')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="silver", 
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)


root.mainloop()
