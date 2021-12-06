from tkinter import *
window = Tk()

label1 = Label(window, text = "label1", bg ="#FF0000")
label2 = Label(window, text = "label2", bg ="#FF0000")
label3 = Label(window, text = "label3", bg ="#FF0000")


# 참고 - 변수는 대,소문자를 구분한다


# 레이블 위치 정하기
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

# label1.pack(side=RIGHT)
# label2.pack(side=RIGHT)
# label3.pack(side=RIGHT)

# label1.pack(side=TOP)
# label2.pack(side=TOP)
# label3.pack(side=TOP)


# label1.pack(side=BOTTOM)
# label2.pack(side=BOTTOM)
# label3.pack(side=BOTTOM)

window.mainloop()


