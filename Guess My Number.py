import tkinter as tk
import random

numper = random.randint(1, 100)
attempts = 0

def check():
    global attempts

    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=attempts)

        if guess > numper:
            result.config(text="less")
        elif guess < numper:
            result.config(text="more")
        else:
            result.config(text="congratulations")

    except:
        result.config(text="enter number")

def new_game():
    global numper
    numper = random.randint(1, 100)
    entry.delete(0, tk.END)
    result.config(text="")
    
window = tk.Tk()
window.title("guess my number")
window.geometry("300x300")
window.config(bg="green")

# عدد المحاولات فوق على اليمين
attempts_frame = tk.Frame(window,bg="green")
attempts_frame.pack(anchor="ne", padx=10, pady=10)
attempts_frame.config(bg="green")

attempts_text = tk.Label(attempts_frame, text="Attempts")
attempts_text.pack(side="left")

attempts_label = tk.Label(
    attempts_frame,
    text="0",
    width=3,
    bg="lightblue",
    relief="solid",
    borderwidth=2
)
attempts_label.pack(side="left", padx=5)

entry = tk.Entry(window, bg="lightblue", fg="black" , width=40)
entry.pack(pady=100)

guess = tk.Button(
    window,
    text="guess",
    command=check,
    bg="blue",
    fg="pink",
width=20)
guess.pack()

new_game_button = tk.Button(window, text="New Game", width=20 , bg="blue" , fg="lightpink" , command=new_game)
new_game_button.pack()

result = tk.Label(window, text="", fg="white",bg="darkgreen")
result.pack(pady=10)

window.mainloop()