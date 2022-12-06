from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400,height=200)
window.config(padx=20,pady=50)

def button_clicked():
    result_label.config(text=mile_to_km_converter())

def mile_to_km_converter():
    text= input.get()
    return round((int(text) * 1.609),1)

# Label 

Miles_label = Label(text= "Miles",font=("Arial",24,"bold"))
Km_label = Label(text= "Km",font=("Arial",24,"bold"))
equal_label = Label(text= "is equal to",font=("Arial",24,"bold"))
result_label = Label(text= "0",font=("Arial",24,"bold"))

# Label 설정값
Miles_label.grid(column=3,row=1)
Miles_label.config(padx=10,pady=10)
Km_label.grid(column=3,row=2)
Km_label.config(padx=10,pady=10)
equal_label.grid(column=1,row=2)
equal_label.config(padx=10,pady=10)
result_label.grid(column=2,row=2)
result_label.config(padx=10,pady=10)

# Button 

button = Button(text="Calculate",command=button_clicked)
button.grid(column=2,row=3)

#Entry

input = Entry(width=10)
input.grid(column=2,row=1)




window.mainloop()