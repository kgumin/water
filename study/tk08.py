from tkinter import *
window = Tk()


f1 = Frame(window)
f2 = Frame(window)




entry1=Entry(f1)
entry2=Entry(f1)
label1 = Label(f1, text = "너비")
label2 = Label(f1, text = "높이")
b1 =Button(f1, text="이미지 저장")


b2 =Button(f2, text="확대")
b3 =Button(f2, text="축소")
#label3 = Label(f2, text = "이미지")



f1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
b1.grid(row = 2, column = 1)



f2.grid(row = 1, column = 1)
#label3.place(200,300)
b2.grid(row = 1, column = 3)
b3.grid(row = 1, column = 4)




window.mainloop()
