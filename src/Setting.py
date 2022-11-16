import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import Text

def SettingWindow():
    root = tk.Tk()
    root.title('設定')
    root.geometry('800x500')

    versionLavel = tk.Label(
        root,
        text = 'ver.1.0.0'
        )
    versionLavel.pack(
        anchor = tk.W
        )

    OSSButton = tk.Button(
        root,
        text = "LICENSE"
        )
    OSSButton.pack(
        anchor = tk.W,
        pady = 5
        )
    OSSButton.bind(
        "<ButtonRelease>",
        clickOSSButton
        )

def clickOSSButton(event):
    root = tk.Tk()
    root.title('LICENSE')
    root.geometry('800x500')

    LicenseCanvas = tk.Canvas(
        root,
        highlightthickness = 0,
        width = 780,
        height = 500
        )
    LicenseCanvas.pack(
        anchor = tk.NW,
        side = tk.LEFT
        )
    LicenseCanvasScrollbar = tk.Scrollbar(
        root,
        orient = tk.VERTICAL,
        command = LicenseCanvas.yview
        )
    LicenseCanvasScrollbar.pack(
        anchor = tk.NW,
        fill = tk.Y,
        side = tk.LEFT
    )
    LicenseCanvas["yscrollcommand"] = LicenseCanvasScrollbar.set
    LicenseCanvas.yview_moveto(0)
    LicenseCanvas.config(scrollregion = (0, 0, 0, 6500))
    LicenseCanvas.create_text(0, 0, text = Text.LicenseText, anchor="nw")        