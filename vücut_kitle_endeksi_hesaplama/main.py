import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(300,300)
window.config(padx=50,pady=50)


def calculate_bmi():
    height = height_entry.get()
    weight = weight_entry.get()

    if weight == "" or height == "":
        Result_Label.config(text="ikisinide giriniz")
    else:
        try:
            bmi = float(weight) / (float(height) / 100 )  ** 2
            result_string = write_result(bmi)
            Result_Label.config(text=result_string)
        except:
            Result_Label.config(text="geçersiz giriş")





weight_input_label = Label(text="Kilonuzu giriniz ")
weight_input_label.pack()

weight_entry = Entry(width=10)
weight_entry.pack()


height_input_label = Label(text="Boyunuzu giriniz(cm şeklinde)")
height_input_label.pack()

height_entry = Entry(width=10)
height_entry.pack()


my_button = Button(text="Sonucunuz için tıklayınız ",command=calculate_bmi)
my_button.pack()
my_button.config()


Result_Label = Label()
Result_Label.pack()




def write_result(bmi):

    result_string = f"Your bmi is: {bmi} You are "

    if bmi <= 18:
        result_string += "zayıf"
    elif bmi > 18 and bmi<=25:
        result_string += "normal"
    elif bmi >=26 and bmi <=30:
        result_string += "şişman"
    else:
        result_string += "obezite"

    return result_string



window.mainloop()