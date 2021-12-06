import tkinter as tk
import random


ans = int(input('정답을 입력해 주세요 : '))
num1 = random.randint(1,10)



if num1 == ans:
    def click():
        btn.config(text = "정답은 " + str(num1) + "  축하합니다 정답 입니다.")
else :
    def click():
        btn.config(text = "정답은 " + str(num1) + "  오답 입니다.")


root =  tk.Tk()
label = tk.Label(root, text = '숫자를 맞춰보세요 (1~10)' )
label.pack()

btn = tk.Button(root, text = '정답공개', command = click) # button, 클릭 명령
btn.pack()

label1 = tk.Label(root, text = '입력한 값은 ' + str(ans) + " 입니다.")
label1.pack()

root.mainloop()
