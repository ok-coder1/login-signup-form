
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login():
    subprocess.Popen(["python", r"../../login-signup/build/Login.py"])
    exit()


window = Tk()
window.title("Signup")

window.geometry("447x732")
window.configure(bg = "#97DEFF")


canvas = Canvas(
    window,
    bg = "#97DEFF",
    height = 732,
    width = 447,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    23.0,
    174.0,
    anchor="nw",
    text="You have successfully created an account!",
    fill="#808080",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    33.0,
    198.0,
    anchor="nw",
    text="Login to start using your account!",
    fill="#808080",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    170.0,
    53.0,
    anchor="nw",
    text="Signup",
    fill="#2E4F4F",
    font=("Inter", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=65.0,
    y=294.0,
    width=316.0,
    height=92.0
)
window.resizable(False, False)
window.mainloop()
