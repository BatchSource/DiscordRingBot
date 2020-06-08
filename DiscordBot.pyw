import time, sys, pyautogui, win32api, easygui
from pynput.mouse import Button, Controller as MouseController
from win32api import *
from win32con import *
import tkinter as tk

ppl = easygui.integerbox('Amount of people:', 'Discord Spammer')

####

root = tk.Tk()
root.title('Discord Spammer')
root.maxsize(350,200)
root.minsize(350,200)
root.resizable(False, False)
root.attributes('-alpha', 0.9)
root.config(background="#f0f0f0")
def on_closing(): sys.exit()
root.protocol("WM_DELETE_WINDOW", on_closing)

tk.Label(root, text='Discord Spammer', background="#f0f0f0", fg="black", font=("Arial Bold", 20)).pack()
tk.Label(root, text='(Hold Ctrl to close)', background="#f0f0f0", fg="black", font=("Arial Bold", 10)).pack(side='top')

tk.PanedWindow(root, orient="horizontal", width=300, background="#000000", height=2).pack(pady=10)
#tk.Label(root, text='', background="#f0f0f0", justify='left', fg="#787878", font=("Arial Bold", 10)).pack(side='bottom')


def tkadddata(x):
    tk.Label(root, text=x, background="#f0f0f0", fg="black", font=("Arial", 10)).pack(side='top', anchor='w', padx='20')
    root.update()
root.update()


####

timer = tk.StringVar()
loopvar = tk.StringVar()

message2 = tk.Label(root, text='Position cursor over the top person.', background="#f0f0f0", fg="black", font=("Arial", 10))
message2.pack(side='top', anchor='w', padx='20')
root.update()
time.sleep(2)

timer.set('Starting in 5...')

timelabel = tk.Label(root, textvariable=timer, background="#f0f0f0", fg="black", font=("Arial", 10))
timelabel.pack(side='top', anchor='w', padx='20')
root.update()
time.sleep(1)
timer.set(f'Starting in 4...')
root.update()
time.sleep(1)
timer.set(f'Starting in 3...')
root.update()
time.sleep(1)
timer.set(f'Starting in 2...')
root.update()
time.sleep(1)
timer.set(f'Starting in 1...')
root.update()
time.sleep(1)

message2.pack_forget()
timelabel.pack_forget()

x, y = pyautogui.position()
mouse = MouseController()

if ppl == 1: tkadddata(f'Spamming 1 person.')
else: tkadddata(f'Spamming {ppl} people.')

loopvar.set('Loops: 0')
amntclicked = tk.Label(root, textvariable=loopvar, background="#f0f0f0", fg="black", font=("Arial", 10)).pack(side='top', anchor='w', padx='20')

loops = 0
while True:
    for i in range(int(ppl)): # Amount of people

        if GetAsyncKeyState(VK_CONTROL) == -32768: sys.exit(0)
        yshift = 45*i

        prex, prey = pyautogui.position()
        win32api.SetCursorPos((x,y + yshift))
        mouse.press(Button.right); mouse.release(Button.right)
        win32api.SetCursorPos((prex, prey))

        x1, y1 = x, y + yshift

        prex, prey = pyautogui.position()
        win32api.SetCursorPos((x1-100,y1+150))
        mouse.press(Button.left); mouse.release(Button.left)
        win32api.SetCursorPos((prex, prey))

    if GetAsyncKeyState(VK_CONTROL) == -32768: sys.exit(0)
    loops+=1
    loopvar.set(f'Loops: {loops}')
    root.update()
    time.sleep(1)