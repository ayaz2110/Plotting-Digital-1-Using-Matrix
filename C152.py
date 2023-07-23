from tkinter import *
root = Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label = Label(root)

array_1d = ["Camrin", "Anees", "Kieran"]
print(array_1d[0])

array_2d = [["Camrin", "A"], ["Anees", "B"], ["Kieran", "C"]]
print(array_2d[0][1])

array_3d = [[["Camrin", "A+", "Excellent"], ["Anees", "A", "Very Good"], ["Kirean", "B+", "Good"]]]
print(array_3d[0][0][2])

def report() :
    label["text"] = array_3d[0][1][0] + "Got Grade" + array_3d[0][1][1] + "And He Is Doing" + array_3d[0][1][2]
    
btn = Button(root, text="Show Report", command = report)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()
