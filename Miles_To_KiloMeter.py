from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=400)
window.config(padx=20,pady=20)

#Conversion function
def get_miles():
    value_mile = input_mile.get()
    calc_km = round(float(value_mile) * 1.609, 2)
    out_km.config(text=calc_km)

#Miles to enter
input_mile = Entry(width=15)
input_mile.insert(END,0)
input_mile.grid(column=1,row=0,padx=30,pady=30)


#Label for free form text
text1 = Label(text="Miles",font=("Arial", 20,"normal"))
text1.grid(column=2,row=0)

text2 = Label(text="is equal to",font=("Arial", 20,"normal"))
text2.grid(column=0,row=1)

text3 = Label(text="Kilometers",font=("Arial", 20,"normal"))
text3.grid(column=2,row=1)

#Kilometers to show
out_km = Label(text="0",font=("Arial", 20,"normal"))
out_km.grid(column=1,row=1,padx=30,pady=30)

#Button
calc_button = Button(text="Calculate",command=get_miles)
calc_button.grid(column=1,row=2)








window.mainloop()