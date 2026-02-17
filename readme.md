# My First QR Code Generator

Hi! This is my first Python project. I wanted to create a simple tool that helps me create QR codes for links without having to use some sketchy websites.

## What it does
It's a simple CLI (Command Line Interface) tool. When you start it:
1. A Windows folder dialog opens so you can pick where to save your images.
2. You type in your link.
3. You give it a filename.
4. It saves a .png QR code for you.

## Why I built this
I'm currently learning Python and wanted to understand:
- How to work with external libraries like `qrcode`.
- How to handle file paths with `pathlib`.
- How to use a basic GUI element like `tkinter` in a script.

## How to use it
If you have Python installed:
1. Install the library: `pip install qrcode[pil]`
2. Run the script: `python "QR Code Generator.py"`

I also created a `.exe` version in the **Releases** section, so you can use it even if you don't have Python installed.

## Credits
Built with the `qrcode` library. Thanks to the community for the help!