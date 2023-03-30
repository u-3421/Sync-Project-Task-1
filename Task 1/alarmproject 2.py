import tkinter as tk
from datetime import datetime
import threading
from playsound import playsound
from tkinter import messagebox

class AlarmThread(threading.Thread):
    def __init__(self, alarm_time):
        super().__init__()
        self.alarm_time = alarm_time
    
    def run(self):
        while True:
            current_time = datetime.now().time()
            if current_time.hour == self.alarm_time.hour and current_time.minute == self.alarm_time.minute:
                playsound('C:/Users/udayr/OneDrive/Desktop/Sync/Task 1/alarm_sound.mp3')
                messagebox.showinfo("Wake up!", "Alarm stopped ringing. Time to wake up!")
                break



class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("400x350")
        self.root.configure(bg="#3D4A55")

        self.font = ("Arial", 16, "bold")

        # Current time label
        self.time_label = tk.Label(self.root, font=self.font,bg="#3D4A55",)
        self.time_label.pack(pady=10)

        # Date label
        self.date_label = tk.Label(self.root, font=self.font, bg="#3D4A55", anchor="e")
        self.date_label.pack(pady=5)

        # Day label
        self.day_label = tk.Label(self.root, font=("Arial", 30, "bold"), bg="#3D4A55", anchor="center")
        self.day_label.pack(expand=True)

        # Date entry field
        date_entry_label = tk.Label(self.root, text="Enter date (YYYY-MM-DD):", font=self.font, bg="#3D4A55")
        date_entry_label.pack(pady=5)
        self.date_entry = tk.Entry(self.root, font=self.font, bg="#C5C5C5")
        self.date_entry.pack()

        # Time entry field
        time_entry_label = tk.Label(self.root, text="Enter time (HH:MM):", font=self.font, bg="#3D4A55")
        time_entry_label.pack(pady=5)
        self.time_entry = tk.Entry(self.root, font=self.font, bg="#C5C5C5")
        self.time_entry.pack()

        # Set alarm button
        alarm_button = tk.Button(self.root, text="Set Alarm", font=self.font, command=self.set_alarm, bg="#525252", fg="white")
        alarm_button.pack(pady=10)

        self.timer = None
        self.alarm_thread = None

    def update_time(self):
        current_time = datetime.now().time()
        self.time_label.config(text=current_time.strftime("%H:%M:%S"))
        self.date_label.config(text=datetime.now().strftime("%A, %B %d"))

    def set_alarm(self):
        alarm_time_str = self.time_entry.get()
        alarm_date_str = self.date_entry.get()

        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time()
            alarm_date = datetime.strptime(alarm_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date/time format")
            return

        alarm_datetime = datetime.combine(alarm_date, alarm_time)
        if alarm_datetime <= datetime.now():
            print("Invalid date/time for alarm")
            return

        self.alarm_time = alarm_time
        self.day_label.config(text=alarm_time.strftime("%H:%M"))

        if self.alarm_thread:
            self.alarm_thread.terminate()

        self.alarm_thread = AlarmThread(self.alarm_time)
        self.alarm_thread.start()

    def start(self):
        self.update_time()
        self.timer = threading.Timer(1, self.start)
        self.timer.start()

    def run(self):
        self.start()
        self.root.mainloop()


if __name__ == "__main__":
    clock = AlarmClock()
    clock.run()
