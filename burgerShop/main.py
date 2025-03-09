import tkinter as tk
from PIL import Image, ImageTk

#self-note, tkinter does not support gifs properly
#----------------------------------------------------------------------------#

#IMAGES:

SHOP_ENTRANCE = "images/entrance.gif"
SHOP_ICON = "images/burgerIcon.ico"

#----------------------------------------------------------------------------#

#window
root = tk.Tk()
width = 1080
heigth = 720
root.geometry(f"{width}x{heigth}")

#title & icon
root.iconbitmap(default=SHOP_ICON)
root.title('Burger Shop')

#gifs
entrance_gif = Image.open(SHOP_ENTRANCE)

#frames
frames_list = []
try:
    while True:
        single_frame = entrance_gif.copy().resize((width, heigth)) # ".resize()"
        frames_list.append(ImageTk.PhotoImage(single_frame)) 
        entrance_gif.seek(len(frames_list)) 
except EOFError: #EOF (end of frames)
    pass

frame_count = len(frames_list)
frame_index = 0

#Entrance animation
entrance_label = tk.Label(root, image=frames_list[0])
entrance_label.pack()

def update_gif():
    global frame_index
    speed_ms = 100

    entrance_label.config(image=frames_list[frame_index])
    frame_index = (frame_index + 1) % frame_count # index % total count = 0 
    root.after(speed_ms, update_gif)

    
#button_test
#bg - button color
#fg - text color

first_x = 37
first_y = 85
fgColor= "#fffb80"
bgColor = "#5e0c2b"
font = "Courier"
fontSize = 12

enterButton = tk.Button(
    root, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔════════╗\n║  ENTER  ║\n╚════════╝", font=(font, fontSize), 
    command=lambda: print("Enter button")
)
enterButton.place(x=first_x, y=first_y*1.25)

driveThroughButton = tk.Button(
    root, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔════════════════╗\n║  DRIVE THROUGH  ║\n╚════════════════╝", font=(font, fontSize), 
    command=lambda: print("Drive through button")
)
driveThroughButton.place(x=first_x, y=first_y*2.5)

creditsButton = tk.Button(
    root, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔══════════╗\n║  CREDITS  ║\n╚══════════╝", font=(font, fontSize), 
    command=lambda: print("credits button")
)
creditsButton.place(x=first_x, y=first_y*3.75)

exitButton = tk.Button(
    root, width=20, height=3, 
    bg=bgColor, fg=fgColor, 
    text="╔═══════╗\n║  EXIT  ║\n╚═══════╝", font=(font, fontSize), 
    command=lambda: root.destroy()
)

exitButton.place(x=first_x, y=first_y*5)


update_gif()

root.mainloop()


