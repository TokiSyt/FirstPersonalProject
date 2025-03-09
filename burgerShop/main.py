import tkinter as tk
from PIL import Image, ImageTk

#Self-note, tkinter does not support gifs properly
#----------------------------------------------------------------------------#

#IMAGES & GIFS:

SHOP_ENTRANCE = "images/entrance.gif"
SHOP_ICON = "images/burgerIcon.ico"
INSIDE = "images/inside.jpg"
DRIVE_GIF = "images/drive.gif"

#----------------------------------------------------------------------------#
#basic infos

def switchFrame(frame):
    frame.tkraise()

#Window
root = tk.Tk()
width = 1080
heigth = 720
root.geometry(f"{width}x{heigth}")

#Images
speedMs = 100
entranceGif = Image.open(SHOP_ENTRANCE)
insidePhoto = Image.open(INSIDE).resize((1080, 720), Image.Resampling.LANCZOS)
insidePhoto = ImageTk.PhotoImage(insidePhoto)
driveGif = Image.open(DRIVE_GIF)

#Title & icon
root.iconbitmap(default=SHOP_ICON)
root.title('Burger Shop')

#Frames for window switch
entranceMenu = tk.Frame(root)
insideShop = tk.Frame(root)
driveMenu = tk.Frame(root)

for frame in (entranceMenu, insideShop, driveMenu):
    frame.place(x=0, y=0, relheight=1, relwidth=1)

#----------------------------------------------------------------------------#
#Entrance 

entFramesList = []
try:
    while True:
        single_frame = entranceGif.copy().resize((width, heigth)) # ".resize()"
        entFramesList.append(ImageTk.PhotoImage(single_frame)) 
        entranceGif.seek(len(entFramesList)) 
except EOFError: #EOF (end of frames)
    pass

entFrameCount = len(entFramesList)
entFrameIndex = 0


entrance_label = tk.Label(entranceMenu, image=entFramesList[0])
entrance_label.pack()

def update_entrance_gif():
    global entFrameIndex
    global speedMs

    entrance_label.config(image=entFramesList[entFrameIndex])
    entFrameIndex = (entFrameIndex + 1) % entFrameCount # last index % total count = 0 
    root.after(speedMs, update_entrance_gif)

#bg - button color
#fg - text color

first_x = 37
first_y = 85
fgColor= "#fffb80"
bgColor = "#5e0c2b"
font = "Courier"
fontSize = 12

enterButton = tk.Button(
    entranceMenu, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔════════╗\n║  ENTER  ║\n╚════════╝", font=(font, fontSize), 
    command=lambda: switchFrame(insideShop)
)
enterButton.place(x=first_x, y=first_y*1.25)

driveThroughButton = tk.Button(
    entranceMenu, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔════════════════╗\n║  DRIVE THROUGH  ║\n╚════════════════╝", font=(font, fontSize), 
    command=lambda: switchFrame(driveMenu)
)
driveThroughButton.place(x=first_x, y=first_y*2.5)

creditsButton = tk.Button(
    entranceMenu, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔══════════╗\n║  CREDITS  ║\n╚══════════╝", font=(font, fontSize), 
    command=lambda: print("Credits button")
)
creditsButton.place(x=first_x, y=first_y*3.75)

exitButton = tk.Button(
    entranceMenu, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔═══════╗\n║  EXIT  ║\n╚═══════╝", font=(font, fontSize), 
    command=lambda: root.destroy()
)
exitButton.place(x=first_x, y=first_y*5)

update_entrance_gif()

#----------------------------------------------------------------------------#

#Inside

insideLabel = tk.Label(insideShop, image=insidePhoto)
insideLabel.pack()

backButton = tk.Button(
    insideShop,
    text="╔══════════╗\n║ Return to the entrance ║\n╚══════════╝",
    bg="#b03a2e",
    fg=fgColor,
    borderwidth=0,
    width=21,
    height=3,
    command=lambda: switchFrame(entranceMenu)
)
backButton.place(x=first_x, y=heigth - 80)

#----------------------------------------------------------------------------#

#Drive Through

driveFramesList = []
try:
    while True:
        single_frame = driveGif.copy().resize((width, heigth)) # ".resize()"
        driveFramesList.append(ImageTk.PhotoImage(single_frame)) 
        driveGif.seek(len(driveFramesList)) 
except EOFError: #EOF (end of frames)
    pass

driveFrameCount = len(driveFramesList)
driveFrameIndex = 0


driveLabel = tk.Label(driveMenu, image=driveFramesList[0])
driveLabel.pack()

def update_drive_gif():
    global driveFrameIndex
    global speedMs

    driveLabel.config(image=driveFramesList[driveFrameIndex])
    driveFrameIndex = (driveFrameIndex + 1) % driveFrameCount # last index % total count = 0 
    root.after(speedMs, update_drive_gif)

backDriveButton = tk.Button(
    driveMenu,
    text="╔══════════╗\n║ Return to the entrance ║\n╚══════════╝",
    bg="#f5b7b1",
    fg="#a93226",
    borderwidth=0,
    width=21,
    height=3,
    command=lambda: switchFrame(entranceMenu)
)
backDriveButton.place(x=first_x, y=heigth - 80)

update_drive_gif()

#----------------------------------------------------------------------------#

switchFrame(entranceMenu)

root.mainloop()


