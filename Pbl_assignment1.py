import time
import threading
from tkinter import Tk, Button, Label

class NumberCounter:
    def __init__(self):
        self.number = 0
        self.increment = 1
        self.running = False

    def increase_number(self):
        while self.running:
            self.number += self.increment
            time.sleep(0.1 / self.increment)
            self.increase_speed()

    def start(self):
        self.increment = 1
        if not self.running:
            self.running = True
            threading.Thread(target=self.increase_number).start()

    def stop(self):
        self.running = False


    def increase_speed(self):
        self.increment *= 2

def on_button_click():
    counter.start()

def on_button_release():
    counter.stop()

def on_button_hold(event):
    elapsed_time = time.time() - event.time
    counter.number += int(elapsed_time) * counter.increment

root = Tk()
root.title("누르고 땡기면 숫자가 증가해요")
root.geometry("300x200")

counter = NumberCounter()

button = Button(root, text="UP", repeatdelay=500, repeatinterval=100)
button.bind("<Button-1>", lambda event: on_button_click())
button.bind("<ButtonRelease-1>", lambda event: on_button_release())
#button.bind("<B1-Motion>", lambda event: on_button_hold(event))
button.pack(pady=20)

label = Label(root, text="숫자: 0", font=("Helvetica", 24))
label.pack(pady=10)

def update_label():
    label.config(text="숫자: " + str(counter.number))
    root.after(100, update_label)

update_label()

root.mainloop()
