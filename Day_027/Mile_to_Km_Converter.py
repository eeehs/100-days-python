from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=300,height=150)
window.config(padx=100,pady=50)



# Entry box

input_box = Entry(width=10)
input_box.grid(row=0,column=1)

# Label_miles

Label_miles = Label(text="Miles",font=("Arial",13,"bold"))
Label_miles.grid(row=0, column=2)

# Label_isequal

Label_isequal = Label(text="is equal to",font=("Arial",13,"bold"))
Label_isequal.grid(row=1,column=0)

# Label_result

Label_result = Label(text=" 0 ",font=("Arial",13,"bold"))
Label_result.grid(row=1,column=1)

# Label_KM

Label_KM = Label(text="Km",font=("Arial",13,"bold"))
Label_KM.grid(row=1,column=2)

# Button
def button_clicked():
    result = int(input_box.get()) * 1.6
    Label_result.config(text=f"{result}")
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2,column=1)




window.mainloop()