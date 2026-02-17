import qrcode
import pathlib
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)

print("Please choose a place to save your QR Codes...")
ausgewaehlter_pfad = filedialog.askdirectory(title="Where do you want to save your QR Codes")

if not ausgewaehlter_pfad:
    print("No folder was selected. Program stops.")
    exit()

desktop_ordner = pathlib.Path(ausgewaehlter_pfad)

print("Welcome! This is your QR Code generator")

while True:
    link = input("Give me the link:\n")
    if link.strip() == "":
        print("You have to type your link here")
        input("Press enter to continue...")
        continue
    name = input("Enter the name for the file (don't type the file extension):\n")
    if name.strip() == "":
        print("You have to type your filename here")
        input("Press enter to continue...")
        continue

    speicher = desktop_ordner / f"{name}.png"
    
    img = qrcode.make(link)
    img.save(speicher)

    print(f"Your QR Code is saved under this name: {name}.png")

    frage = input("Do you want to create another QR Code?\n")
    if frage.lower() == "nein" or frage.lower() == "no":
        print("Thanks for using my QR Code generator and goodbye")
        input("Please press enter...")
        break