from tkinter import *


window = Tk()
window.title('Miles to Kilometers Converter')
window.minsize(300,100)
window.config(padx=40, pady=10)


def calculate():
    kilometer_num.config(text=int(mile_input.get()) * 1.609)

mile_input = Entry(width=5)
mile_input.grid(column=2,row=1)

mile_label = Label(text='Miles')
mile_label.grid(column=3,row=1)

equal_lable = Label(text='is equal to')
equal_lable.grid(column=1,row=2)

kilometer_num = Label(text = 0)
kilometer_num.grid(column=2,row=2)

kilometer_label = Label(text='Kilometers')
kilometer_label.grid(column=3,row=2)

calculate_button = Button(text='calculate', width=8, command=calculate)
calculate_button.grid(column=2,row=3)


window.mainloop()