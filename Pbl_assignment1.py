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

    def decrease_number(self):
        while self.running:
            self.number += self.increment
            time.sleep(0.1 / self.increment)

    def start_up(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.increase_number).start()

    def start_down(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.increase_number).start()

    def stop(self):
        self.running = False

    def increase_speed(self):
        self.increment += 1

root = Tk()
root.title("1")
root.geometry("300x200")

counter = NumberCounter()

def on_button_click():
    counter.start_up()

def on_button_release():
    counter.stop()

def on_button_hold():
    while counter.running:
        counter.increment += 2
        time.sleep(0.5)

def on_button_hold_start(event):
    counter.start_up()
    threading.Thread(target=on_button_hold).start()

def on_button_hold_stop(event):
    counter.stop()

button = Button(root, text="Up")
button.bind("<ButtonPress-1>", lambda event: on_button_hold_start(event))
button.bind("<ButtonRelease-1>", lambda event: on_button_hold_stop(event))
button.pack(pady=20)

button = Button(root, text="Down")
button.bind("<ButtonPress-1>", lambda event: on_button_hold_start(event))
button.bind("<ButtonRelease-1>", lambda event: on_button_hold_stop(event))
button.pack(pady=20)

label = Label(root, text="숫자: 0", font=("Helvetica", 24))
label.pack(pady=10)

def update_label():
    label.config(text="숫자: " + str(counter.number))
    root.after(50, update_label)

update_label()

root.mainloop()
