from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Math table generator")
window.geometry("350x900")

def generate_multi_tabel():
    tabels = ""
    for i in range(rangevar.get()+1):
        tabels += str(num.get()) + " x " + str(i) + " = " + str(num.get()*i)+"\n"
    tabel_label.config(text = tabels)


choice_frame = Frame(window)

title = Label(choice_frame, text = "Mathematical Tabel", font = ("times", 43)).place(x = 0, y = 0)
choice_question = Label(choice_frame, text = "Number and Range: ", font = ("helvetica", 15)).grid(row = 1, column = 1, pady = 90, padx = 10)
generate = Button(choice_frame, text = "Generate", command = generate_multi_tabel).grid(row = 1, column = 3, padx = 10)

#creating radio button choices 
rangevar = IntVar()
Radiobutton(choice_frame, text = "10", value = 10, variable = rangevar).grid(row = 2, column = 1)
Radiobutton(choice_frame, text = "20", value = 20, variable = rangevar).grid(row = 2, column = 2)
Radiobutton(choice_frame, text = "30", value = 30, variable = rangevar).grid(row = 2, column = 3)
#setting defualt value if player does not chose
rangevar.set(10)

#creating combobox widjet
num = IntVar()
numbers = Combobox(choice_frame, textvariable = num, width = 5)
numbers["values"] = tuple(range(25))
numbers.grid(row = 1, column = 2)

choice_frame.grid(row = 1, column = 1)


result_frame = Frame(window)

tabel_label = Label(result_frame, anchor = "center", font = ("times", 20))
tabel_label.grid(row = 1, column = 1)

result_frame.grid(row = 2, column = 1, pady = 30)


window.mainloop()