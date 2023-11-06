# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# This file was edited by ok-coder1
# https://github.com/ok-coder1


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pymongo import MongoClient
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/User/Desktop/tkdesigner-figma/login-signup-form/login-details/build/assets/frame0")
subprocess.Popen(["mongod", "--dbpath",  "/Users/User/Desktop/tkdesigner-figma/login-signup-form/DB-Storage/Data",  "--logpath",  "/Users/User/Desktop/tkdesigner-figma/login-signup-form/DB-Storage/Logs/mongo.log",  "--logappend"])
mongo_client = MongoClient("127.0.0.1", 27017)
db = mongo_client.users
users_collection = db.users
login_details = users_collection.find_one()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def refresh():
    subprocess.Popen(["python3", "/Users/User/Desktop/tkdesigner-figma/login-signup-form/login-details/build/Login-Details.py"])
    exit()

def close_window():
    subprocess.run(["killall", "mongod"])
    exit()


window = Tk()

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
refresh_button_image = PhotoImage(
    file=relative_to_assets("refresh_button.png"))
refresh_button = Button(
    image=refresh_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=refresh,
    relief="flat"
)
refresh_button.place(
    x=65.0,
    y=479.0,
    width=316.0,
    height=92.0
)

canvas.create_text(
    61.0,
    101.0,
    width=350.0,
    anchor="nw",
    text=login_details,
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    78.0,
    41.0,
    anchor="nw",
    text="Login details",
    fill="#808080",
    font=("Inter", 48 * -1)
)
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()
