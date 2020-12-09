import psutil
import tkinter
import time
import sys

# battery percentage to start warning
warn_at = 97
# delay between checks
delay = 30


# dismiss
def dismiss():
    sys.exit()


# popup
def popup(msg='battery overcharge warning'):
    popup = tkinter.Tk()
    popup.geometry("300x100")
    popup.wm_title("!")
    label = tkinter.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    B2 = tkinter.Button(popup, text="Dismiss", command=dismiss)
    B2.pack()
    popup.bell()
    popup.mainloop()


while True:
    battery = psutil.sensors_battery()
    print(battery)
    if battery.percent >= warn_at:
        popup()
    time.sleep(delay)