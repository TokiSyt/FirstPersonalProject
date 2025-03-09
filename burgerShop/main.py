import tkinter as tk
from PIL import Image, ImageTk
import time

#Self-note, tkinter does not support gifs properly
#----------------------------------------------------------------------------#

#IMAGES & GIFS:

SHOP_ENTRANCE = "images/entrance.gif"
SHOP_ICON = "images/burgerIcon.ico"
INSIDE = "images/inside.jpg"
DRIVE_GIF = "images/drive.gif"
CREDITS_IMAGE = "images/credits.gif"

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
insidePhoto = Image.open(INSIDE).resize((width, heigth), Image.Resampling.LANCZOS)
insidePhoto = ImageTk.PhotoImage(insidePhoto)
driveGif = Image.open(DRIVE_GIF)
creditsGif = Image.open(CREDITS_IMAGE)

#Title & icon
root.iconbitmap(default=SHOP_ICON)
root.title('Burger Shop')

#Frames for window switch
entranceMenu = tk.Frame(root)
insideShop = tk.Frame(root)
driveMenu = tk.Frame(root)
credits = tk.Frame(root)

for frame in (entranceMenu, insideShop, driveMenu, credits):
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
    command=lambda: switchFrame(credits)
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

inTotalMoney = tk.IntVar(value=0)
inMenu1Amount = tk.IntVar(value=0)
inMenu2Amount = tk.IntVar(value=0)
inMenu3Amount = tk.IntVar(value=0)
inMenu4Amount = tk.IntVar(value=0)
inCoffeeAmount = tk.IntVar(value=0)
inDrinkAmount = tk.IntVar(value=0)
y = 115

def addItemInside(amount, menu):
    inTotalMoney.set(inTotalMoney.get() + amount)

    match menu:
        case 1:
            inMenu1Amount.set(inMenu1Amount.get() + 1)
        case 2:
            inMenu2Amount.set(inMenu2Amount.get() + 1)
        case 3:
            inMenu3Amount.set(inMenu3Amount.get() + 1)
        case 4:
            inMenu4Amount.set(inMenu4Amount.get() + 1)
        case 5:
            inCoffeeAmount.set(inCoffeeAmount.get() + 1)
        case 6:
            inDrinkAmount.set(inDrinkAmount.get() + 1)

    moneyLabel.config(text=f'''Menu 1: {inMenu1Amount.get()}
Menu 2: {inMenu2Amount.get()}
Menu 3: {inMenu3Amount.get()}
Menu 4: {inMenu4Amount.get()}
Coffee: {inCoffeeAmount.get()}
Drink: {inDrinkAmount.get()}

Total: 元{inTotalMoney.get():}''')
    
def finishOrderInside():
    inTotalMoney.set(0)
    inTotalMoney.set(0)
    inMenu1Amount.set(0)
    inMenu2Amount.set(0)
    inMenu3Amount.set(0)
    inMenu4Amount.set(0)
    inCoffeeAmount.set(0)
    inDrinkAmount.set(0)

    moneyLabel.config(text=f'''Menu 1: {inMenu1Amount.get()}
Menu 2: {inMenu2Amount.get()}
Menu 3: {inMenu3Amount.get()}
Menu 4: {inMenu4Amount.get()}
Coffee: {inCoffeeAmount.get()}
Drink: {inDrinkAmount.get()}

Total: 元{inTotalMoney.get():}''')
    
    popUp = tk.Toplevel(insideShop, bg=bgColor)
    popUp.geometry("500x100")
    popUp.title("Order confirmation")

    message = tk.Label(popUp, text="\nThanks for ordering with us! :D\nEnjoy your meal.", 
                       font=font, bg=bgColor, fg=fgColor)
    message.pack()
    popUp.after(3000, lambda: [popUp.destroy(), switchFrame(entranceMenu)])
    

moneyLabel = tk.Label(insideShop,
                      bg= "#1b4f72",
                      fg= "#fdfefe",
                      font=font,
                      borderwidth=2,
                      relief="groove",
text=f'''Menu 1: {inMenu1Amount.get()}
Menu 2: {inMenu2Amount.get()}
Menu 3: {inMenu3Amount.get()}
Menu 4: {inMenu4Amount.get()}
Coffee: {inCoffeeAmount.get()}
Drink: {inDrinkAmount.get()}

Total: 元{inTotalMoney.get():}''')
moneyLabel.place(x=838, y=460)

inBuyItem1Button = tk.Button(
    insideShop,
    text="╔════╗\n║ Buy ║\n╚════╝",
    bg="#f4d03f", fg=bgColor, font=font,
    borderwidth=0, width=6, height=2,
    command= lambda: addItemInside(18, 1)
)
inBuyItem1Button.place(x=5, y=y)

inBuyItem2Button = tk.Button(
    insideShop,
    text="╔════╗\n║ Buy ║\n╚════╝",
    bg="#f4d03f", fg=bgColor, font=font,
    borderwidth=0, width=6, height=2,
    command= lambda: addItemInside(35, 2)
)
inBuyItem2Button.place(x=205, y=y)

inBuyItem3Button = tk.Button(
    insideShop,
    text="╔════╗\n║ Buy ║\n╚════╝",
    bg="#f4d03f", fg=bgColor, font=font,
    borderwidth=0, width=6, height=2,
    command= lambda: addItemInside(33, 3)
)
inBuyItem3Button.place(x=445, y=y)

inBuyItem4Button = tk.Button(
    insideShop,
    text="╔════╗\n║ Buy ║\n╚════╝",
    bg="#f4d03f", fg=bgColor, font=font,
    borderwidth=0, width=6, height=2,
    command= lambda: addItemInside(25, 4)
)
inBuyItem4Button.place(x=775, y=y)

inBuyCoffeButton = tk.Button(
    insideShop,
    text="╔════╗\n║ Buy ║\n╚════╝",
    bg="#b03a2e", fg=bgColor, font=font,
    borderwidth=0, width=6, height=2,
    command= lambda: addItemInside(7, 5)
)
inBuyCoffeButton.place(x=725, y=360)

inBuySeparatedDrink = tk.Button(
    insideShop,
    text="╔════╗\n║ Buy ║\n╚════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=6, height=2,
    command= lambda: addItemInside(12, 6)
)
inBuySeparatedDrink.place(y=377, x=0)

inFinishOrderButton = tk.Button(
    insideShop,
    text="╔═════════════╗\n║ Finish Order ║\n╚═════════════╝",
    bg="#f1948a", fg="#78281f", font=font,
    borderwidth=0, width=16, height=2,
    command= lambda: finishOrderInside()
)
inFinishOrderButton.place(x=380, y=435)

backButton = tk.Button(
    insideShop,
    text="╔═══════════════════════╗\n║ Return to the entrance ║\n╚═══════════════════════╝",
    bg="#b03a2e", fg=fgColor, font=font,
    borderwidth=0, width=26, height=3,
    command=lambda: switchFrame(entranceMenu)
)
backButton.place(x=first_x, y=heigth - 80)

#----------------------------------------------------------------------------#

#Drive Through
x = 80
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
update_drive_gif()

dvTotalMoney = tk.IntVar(value=0)
dvMenu1Amount = tk.IntVar(value=0)
dvMenu2Amount = tk.IntVar(value=0)
dvMenu3Amount = tk.IntVar(value=0)
dvMenu4Amount = tk.IntVar(value=0)
dvCoffeeAmount = tk.IntVar(value=0)
dvDrinkAmount = tk.IntVar(value=0)
y = 115

def addItemDrive(amount, menu):
    dvTotalMoney.set(dvTotalMoney.get() + amount)

    match menu:
        case 1:
            dvMenu1Amount.set(dvMenu1Amount.get() + 1)
        case 2:
            dvMenu2Amount.set(dvMenu2Amount.get() + 1)
        case 3:
            dvMenu3Amount.set(dvMenu3Amount.get() + 1)
        case 4:
            dvMenu4Amount.set(dvMenu4Amount.get() + 1)
        case 5:
            dvCoffeeAmount.set(dvCoffeeAmount.get() + 1)
        case 6:
            dvDrinkAmount.set(dvDrinkAmount.get() + 1)

    dvMoneyLabel.config(text=f'''Menu 1: {dvMenu1Amount.get()}
Menu 2: {dvMenu2Amount.get()}
Menu 3: {dvMenu3Amount.get()}
Menu 4: {dvMenu4Amount.get()}
Coffee: {dvCoffeeAmount.get()}
Drink: {dvDrinkAmount.get()}

Total: 元{dvTotalMoney.get():}''')
    
def finishOrderDrive():
    dvTotalMoney.set(0)

    dvTotalMoney.set(0)
    dvTotalMoney.set(0)
    dvMenu1Amount.set(0)
    dvMenu2Amount.set(0)
    dvMenu3Amount.set(0)
    dvMenu4Amount.set(0)
    dvCoffeeAmount.set(0)
    dvDrinkAmount.set(0)

    dvMoneyLabel.config(text=f'''Menu 1: {dvMenu1Amount.get()}
Menu 2: {dvMenu2Amount.get()}
Menu 3: {dvMenu3Amount.get()}
Menu 4: {dvMenu4Amount.get()}
Coffee: {dvCoffeeAmount.get()}
Drink: {dvDrinkAmount.get()}

Total: 元{dvTotalMoney.get():}''')
    
    popUp = tk.Toplevel(driveMenu, bg=bgColor)
    popUp.geometry("500x100")
    popUp.title("Order confirmation")

    message = tk.Label(popUp, text="\nThanks for ordering with us! :D\nEnjoy your meal.", 
                       font=font, bg=bgColor, fg=fgColor)
    message.pack()
    popUp.after(3000, lambda: [popUp.destroy(), switchFrame(entranceMenu)])

backDriveButton = tk.Button(
    driveMenu,
    text="╔══════════╗\n║ Return to the entrance ║\n╚══════════╝",
    bg="#f5b7b1",
    fg="#a93226",
    borderwidth=0, width=21, height=3,
    command=lambda: switchFrame(entranceMenu)
)
backDriveButton.place(x=first_x, y=heigth - 80)

dvMoneyLabel = tk.Label(driveMenu,
                      bg= "#ec7063",
                      fg= "#fdfefe",
                      font=font,
                      borderwidth=2,
                      relief="groove",
text=f'''Menu 1: {dvMenu1Amount.get()}
Menu 2: {dvMenu2Amount.get()}
Menu 3: {dvMenu3Amount.get()}
Menu 4: {dvMenu4Amount.get()}
Coffee: {dvCoffeeAmount.get()}
Drink: {dvDrinkAmount.get()}

Total: 元{dvTotalMoney.get():}''')
dvMoneyLabel.place(x=832, y=213)

infoButton = tk.Button(
    driveMenu,
    text="PS: Pretend there are the images of each menu next to the texts. :)",
    bg="darkgray", font=font,
    borderwidth=0, width=68, height=1,
    command= lambda: addItemDrive(18, 1)
)
infoButton.place(x=400, y=692)

dvBuyItem1Button = tk.Button(
    driveMenu,
    text="╔═══════╗\n║ Menu 1 ║\n╚═══════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=9, height=2,
    command= lambda: addItemDrive(18, 1)
)
dvBuyItem1Button.place(x=80, y=40)

dvBuyItem2Button = tk.Button(
    driveMenu,
    text="╔═══════╗\n║ Menu 2 ║\n╚═══════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=9, height=2,
    command= lambda: addItemDrive(18, 2)
)
dvBuyItem2Button.place(x=80, y=120)

dvBuyItem3Button = tk.Button(
    driveMenu,
    text="╔═══════╗\n║ Menu 3 ║\n╚═══════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=9, height=2,
    command= lambda: addItemDrive(18, 3)
)
dvBuyItem3Button.place(x=80, y=200)

dvBuyItem4Button = tk.Button(
    driveMenu,
    text="╔═══════╗\n║ Menu 4 ║\n╚═══════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=9, height=2,
    command= lambda: addItemDrive(18, 4)
)
dvBuyItem4Button.place(x=80, y=280)

dvBuyCoffeButton = tk.Button(
    driveMenu,
    text="╔═══════╗\n║ Coffee ║\n╚═══════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=9, height=2,
    command= lambda: addItemDrive(18, 5)
)
dvBuyCoffeButton.place(x=80, y=360)

dvBuySeparatedDrink = tk.Button(
    driveMenu,
    text="╔══════╗\n║ Drink ║\n╚══════╝",
    bg="#f1948a", fg=bgColor, font=font,
    borderwidth=0, width=8, height=2,
    command= lambda: addItemDrive(12, 6)
)
dvBuySeparatedDrink.place(x=80, y=440)

dvFinishOrderButton = tk.Button(
    driveMenu,
    text="╔═════════════╗\n║ Finish Order ║\n╚═════════════╝",
    bg="#f1948a", fg="#78281f", font=font,
    borderwidth=0, width=16, height=2,
    command= lambda: finishOrderDrive()
)
dvFinishOrderButton.place(x=500, y=400)

dvBackButton = tk.Button(
    driveMenu,
    text="╔═══════════════════════╗\n║ Return to the entrance ║\n╚═══════════════════════╝",
    bg="#ec7063", fg="#943126", font=font,
    borderwidth=0, width=26, height=3,
    command=lambda: switchFrame(entranceMenu)
)
dvBackButton.place(x=first_x, y=heigth - 80)
#----------------------------------------------------------------------------#
#credits

creFramesList = []
try:
    while True:
        single_frame = creditsGif.copy().resize((width, heigth)) # ".resize()"
        creFramesList.append(ImageTk.PhotoImage(single_frame)) 
        creditsGif.seek(len(creFramesList)) 
except EOFError: #EOF (end of frames)
    pass

creFrameCount = len(creFramesList)
creFrameIndex = 0

creditLabel = tk.Label(credits, image=creFramesList[0])
creditLabel.pack()

def update_credits_gif():
    global creFrameIndex
    global speedMs

    creditLabel.config(image=creFramesList[creFrameIndex])
    creFrameIndex = (creFrameIndex + 1) % creFrameCount # last index % total count = 0 
    root.after(speedMs, update_entrance_gif)

update_credits_gif()

#----------------------------------------------------------------------------#

switchFrame(entranceMenu)

root.mainloop()