import tkinter as tk
from tkinter import ttk
import time
import winsound
from threading import Thread

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.configure(bg="#333333")

        self.frame = tk.Frame(root, bg="#444444", padx=20, pady=20, borderwidth=2, relief="groove")
        self.frame.grid(row=0, column=0, padx=50, pady=50)

        self.title_label = tk.Label(self.frame, text="Set Alarm Time", font=("Helvetica", 20, "bold"), fg="#ffffff", bg="#444444")
        self.title_label.grid(row=0, columnspan=4, pady=(0, 10))

        self.hour_label = tk.Label(self.frame, text="Hour:", font=("Helvetica", 12), fg="#ffffff", bg="#444444")
        self.hour_label.grid(row=1, column=0)
        self.hour_combobox = ttk.Combobox(self.frame, values=list(range(24)), width=5)
        self.hour_combobox.grid(row=1, column=1)

        self.minute_label = tk.Label(self.frame, text="Minute:", font=("Helvetica", 12), fg="#ffffff", bg="#444444")
        self.minute_label.grid(row=1, column=2)
        self.minute_combobox = ttk.Combobox(self.frame, values=list(range(60)), width=5)
        self.minute_combobox.grid(row=1, column=3)

        self.set_button = tk.Button(self.frame, text="Set Alarm", command=self.set_alarm, font=("Helvetica", 14), bg="#00bfff", fg="#ffffff")
        self.set_button.grid(row=2, columnspan=4, pady=15)

        self.animation_label = tk.Label(root, text="", font=("Helvetica", 36, "bold"), fg="#ff0000", bg="#333333")
        self.animation_label.grid(row=1, column=0, pady=20)

    def set_alarm(self):
        selected_hour = self.hour_combobox.get()
        selected_minute = self.minute_combobox.get()
        alarm_time = f"{selected_hour.zfill(2)}:{selected_minute.zfill(2)}:00"

        alarm_thread = Thread(target=self.wait_for_alarm, args=(alarm_time,))
        alarm_thread.start()

    def wait_for_alarm(self, alarm_time):
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                self.animation_label.config(text="ALARM!")
                self.play_alarm()
                self.animation_label.config(text="")
                break
            time.sleep(1)

    def play_alarm(self):
        for _ in range(3):
            winsound.Beep(1000,1000)
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()