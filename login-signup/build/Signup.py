# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# This file was edited by ok-coder1
# https://github.com/ok-coder1


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from pymongo import MongoClient
import subprocess
import hashlib

CONNECTION_STRING = "mongodb+srv://codershubcode:yiEq1ICyfn1E6UsO@cluster0.jnw3vvs.mongodb.net/?retryWrites=true&w=majority"

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/User/Desktop/tkdesigner-figma/login-signup-form/login-signup/build/assets/frame0")
# Local Database - subprocess.Popen(["mongod", "--dbpath",  "/Users/User/Desktop/tkdesigner-figma/login-signup-form/DB-Storage/Data",  "--logpath",  "/Users/User/Desktop/tkdesigner-figma/login-signup-form/DB-Storage/Logs/mongo.log",  "--logappend"])
mongo_client = MongoClient(CONNECTION_STRING)
db = mongo_client.users
registered_users_collection = db.registered_users


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def openLogin():
    subprocess.Popen(["python3.11", "/Users/User/Desktop/tkdesigner-figma/login-signup-form/login-signup/build/Login.py"])
    exit()

def success():
    subprocess.Popen(["python3.11", "/Users/User/Desktop/tkdesigner-figma/login-signup-form/signup-success/build/Signup-Success.py"])
    exit()

def get_email_address_and_password_and_send_it():
    email_address = email_address_entry.get()
    password = password_entry.get()
    find_user = registered_users_collection.find_one({"email_address": email_address, "password": {"encryption": {"sha224": hashlib.sha224(password.encode("utf-8")).hexdigest(), "sha256": hashlib.sha256(password.encode("utf-8")).hexdigest(), "sha384": hashlib.sha384(password.encode("utf-8")).hexdigest(), "sha512": hashlib.sha512(password.encode("utf-8")).hexdigest()}}})
    sha224_encryption = hashlib.sha224(password.encode("utf-8")).hexdigest()
    sha256_encryption = hashlib.sha256(password.encode("utf-8")).hexdigest()
    sha384_encryption = hashlib.sha384(password.encode("utf-8")).hexdigest()
    sha512_encryption = hashlib.sha512(password.encode("utf-8")).hexdigest()
    login_details = {
        "email_address": email_address,
        "password": {
            "encryption": {
                "sha224": sha224_encryption,
                "sha256": sha256_encryption,
                "sha384": sha384_encryption,
                "sha512": sha512_encryption
            }
        }
    }
    if (find_user == None):
        registered_users_collection.insert_one(login_details)
        success()
    else:
        messagebox.showerror("Error", "User already registered. Please login!")


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
button_image_1 = PhotoImage(
    file=relative_to_assets("open_login.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=openLogin,
    relief="flat"
)
button_1.place(
    x=121.0,
    y=654.0,
    width=211.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("signup.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=get_email_address_and_password_and_send_it,
    relief="flat"
)
button_2.place(
    x=65.0,
    y=480.0,
    width=316.0,
    height=92.0
)

password_entry_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
password_entry_bg = canvas.create_image(
    223.0,
    346.5,
    image=password_entry_image
)
password_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show="•"
)
password_entry.place(
    x=37.0,
    y=311.0,
    width=372.0,
    height=69.0
)

canvas.create_text(
    13.0,
    279.0,
    anchor="nw",
    text="Password",
    fill="#808080",
    font=("Inter", 14 * -1)
)

email_address_entry_image = PhotoImage(
    file=relative_to_assets("entry_2.png"))
email_address_entry_bg = canvas.create_image(
    223.0,
    217.5,
    image=email_address_entry_image
)
email_address_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
email_address_entry.place(
    x=37.0,
    y=182.0,
    width=372.0,
    height=69.0
)

canvas.create_text(
    11.0,
    150.0,
    anchor="nw",
    text="Email Address",
    fill="#808080",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    170.0,
    53.0,
    anchor="nw",
    text="Signup",
    fill="#2E4F4F",
    font=("Inter", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
