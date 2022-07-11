import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    chks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    print(reps)
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_title.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_title.config(text="Work", fg=GREEN)

        
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        chks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title =  tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME, 35, 'bold'))
timer_title.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

chks= tkinter.Label(bg=YELLOW, fg=GREEN,font=(FONT_NAME, 15, 'bold'))
chks.grid(row=3, column=1)

start_button = tkinter.Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()