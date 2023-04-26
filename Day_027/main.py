from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

# Label 

my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

#button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(row=0,column=2)
new_button = Button(text="New Me")
new_button.grid(row=1, column=1)


# Entry

input = Entry(width=10)
input.grid(row=2 ,column=3)
print(input.get())




window.mainloop()
