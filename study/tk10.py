from tkinter import *
import random

answer = random.randint(1,100)


def guessing():
    guess = int(guessField.get())
    
    
    if guess > answer:
        msg = "높음"
    
    elif guess < answer:
        msg = "낮음"
        
    else:
        msg = "정답"
        
    resultLabel["text"] = msg
    guessField.delete(0,5)
    
    
def reset():
    global answer
    answer = random.randint(1,100)
    resultLabel["text"] = "다시한번 하세요"
    
    

window = Tk()
window.configure(bg='white')
window.title("숫자를 맞춰보세요") # tk 상단에 제목 바꾸기

window.geometry("500x80")
titleLabel = Label(window, text = "숫자게임에 오신것을 환영합니다.",bg = "white")
titleLabel.pack()


guessField = Entry(window)
guessField.pack(side = "left")
tryButton = Button(window, text ="시도", fg="green",bg="white", command=guessing)

tryButton.pack(side="left")

resetButton = Button(window, text ="초기화", fg="red", bg="white", command=reset)

resetButton.pack(side="left")
resultLabel = Label(window, text ="1부터 100까지 숫자입력",bg ="white")
resultLabel.pack(side="left")

window.mainloop()
    
