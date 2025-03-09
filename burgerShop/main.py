import tkinter as tk
from PIL import Image, ImageTk
import time

#Self-note, tkinter does not support gifs properly
#----------------------------------------------------------------------------#

#IMAGES & GIFS:

SHOP_ENTRANCE = "burgerShop/images/entrance.gif"
SHOP_ICON = "burgerShop/images/burgerIcon.ico"
INSIDE = "burgerShop/images/inside.jpg"
DRIVE_GIF = "burgerShop/images/drive.gif"
CREDITS_GIF = "burgerShop/images/credits.gif"

#----------------------------------------------------------------------------#
    #basic infos

def start():

    def switchFrame(frame):
        frame.tkraise()

    def close_window():
        root.quit()
        root.destroy()

    speedMs = 100

    #Window
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", close_window)
    width = 1080
    heigth = 720
    root.geometry(f"{width}x{heigth}")

    #Images
    entranceGif = Image.open(SHOP_ENTRANCE)
    entranceStarterFrame = ImageTk.PhotoImage(entranceGif)

    insidePhoto = Image.open(INSIDE).resize((width, heigth), Image.Resampling.LANCZOS)
    insidePhoto = ImageTk.PhotoImage(insidePhoto)

    driveGif = Image.open(DRIVE_GIF)
    driveStarterFrame = ImageTk.PhotoImage(driveGif)


    creditsGif = Image.open(CREDITS_GIF)
    creditsStarterImage = ImageTk.PhotoImage(creditsGif)

    #Title & icon
    root.iconbitmap(SHOP_ICON)
    root.title('Burger Shop')

    #Frames
    entranceMenu = tk.Frame(root)
    insideShop = tk.Frame(root)
    driveMenu = tk.Frame(root)
    credits = tk.Frame(root)

    for frame in (entranceMenu, insideShop, driveMenu, credits):
        frame.place(x=0, y=0, relheight=1, relwidth=1)

    def update_gif(label, gif, frame_index=0):
        try:
            if hasattr(gif, "n_frames") and gif.n_frames > 1:
                gif.seek(frame_index)
                new_frame = ImageTk.PhotoImage(gif.copy().resize((width, heigth), Image.Resampling.LANCZOS))
                label.config(image=new_frame)
                label.image = new_frame
                root.after(speedMs, lambda: update_gif(label, gif, (frame_index + 1) % gif.n_frames))
            else:
                label.config(image=ImageTk.PhotoImage(gif))
        except Exception as e:
            print(f"Error updating GIF: {e}")




    #----------------------------------------------------------------------------#
    #Entrance 

    entrance_label = tk.Label(entranceMenu, image=entranceStarterFrame)
    entrance_label.pack()
    update_gif(entrance_label, entranceGif)

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

        moneyLabel.config(text=f'''
Menu 1: {inMenu1Amount.get()}
Menu 2: {inMenu2Amount.get()}
Menu 3: {inMenu3Amount.get()}
Menu 4: {inMenu4Amount.get()}
Coffee: {inCoffeeAmount.get()}
Drink: {inDrinkAmount.get()}

Total: 元{inTotalMoney.get():}''')
        
    def finishOrderInside():
        inTotalMoney.set(0)
        inMenu1Amount.set(0)
        inMenu2Amount.set(0)
        inMenu3Amount.set(0)
        inMenu4Amount.set(0)
        inCoffeeAmount.set(0)
        inDrinkAmount.set(0)

        moneyLabel.config(text=f'''
Menu 1: {inMenu1Amount.get()}
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
    text=f'''
Menu 1: {inMenu1Amount.get()}
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

    driveLabel = tk.Label(driveMenu, image=driveStarterFrame)
    driveLabel.pack()

    update_gif(driveLabel, driveGif)

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

        dvMoneyLabel.config(text=f'''
Menu 1: {dvMenu1Amount.get()}
Menu 2: {dvMenu2Amount.get()}
Menu 3: {dvMenu3Amount.get()}
Menu 4: {dvMenu4Amount.get()}
Coffee: {dvCoffeeAmount.get()}
Drink: {dvDrinkAmount.get()}

Total: 元{dvTotalMoney.get():}''')
        
    def finishOrderDrive():

        dvTotalMoney.set(0)
        dvMenu1Amount.set(0)
        dvMenu2Amount.set(0)
        dvMenu3Amount.set(0)
        dvMenu4Amount.set(0)
        dvCoffeeAmount.set(0)
        dvDrinkAmount.set(0)

        dvMoneyLabel.config(text=f'''
Menu 1: {dvMenu1Amount.get()}
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
    text=f'''
Menu 1: {dvMenu1Amount.get()}
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
        command= lambda: addItemDrive(35, 2)
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

    creditLabel = tk.Label(credits, image=creditsStarterImage)
    creditLabel.pack()
    update_gif(creditLabel, creditsGif)

    bgColorCredits = "#3498db"
    fgColorCredits = "#1b2631"

    creBackButton = tk.Button(
        credits,
        text="╔═══════════════════════╗\n║ Return to the entrance ║\n╚═══════════════════════╝",
        bg=bgColorCredits, fg="#1b2631", font=font,
        borderwidth=0, width=26, height=3,
        command=lambda: switchFrame(entranceMenu)
    )
    creBackButton.place(x=15, y=heigth - 80)

    codeCredits = tk.Label(
        credits,
        text="Code: Toki",
        font=font, bg=bgColorCredits, fg=fgColorCredits,
        borderwidth=1, relief="solid",
        width=26, height=3
    )
    codeCredits.place(y=65,x=15)

    entranceImageCredits = tk.Label(
        credits,
        text="Entrance GIF: \nhttps://www.newgrounds.com/art/view/chacegraves/late-night-burger-shop",
        font=font, bg=bgColorCredits, fg=fgColorCredits,
        borderwidth=1, relief="solid",
        width=105, height=3
    )
    entranceImageCredits.place(y=160,x=15)

    insideImageCredits = tk.Label(
        credits,
        text="Inside Image: \nhttps://pngtree.com/freepng/hamburg-restaurant-fast-food-pixel-style-illustration_7507249.html",
        font=font, bg=bgColorCredits, fg=fgColorCredits,
        borderwidth=1, relief="solid",
        width=105, height=3
    )
    insideImageCredits.place(y=250,x=15)

    driveImageCredits = tk.Label(
        credits,
        text= "Drive Through GIF: \nhttps://www.deviantart.com/justamereartist/art/Pixel-Scenario-Work-at-Fast-Food-Drive-Thru-738967456",
        font=font, bg=bgColorCredits, fg=fgColorCredits,
        borderwidth=1, relief="solid",
        width=105, height=3
    )
    driveImageCredits.place(y=340,x=15)

    creditsImageCredits = tk.Label(
        credits,
        text= "Credits Background GIF: \nhttps://www.pinterest.com/pin/pixel-art-cityscape-wallpaper--748160556869946767/",
        font=font, bg=bgColorCredits, fg=fgColorCredits,
        borderwidth=1, relief="solid",
        width=105, height=3
    )
    creditsImageCredits.place(y=430,x=15)

    #----------------------------------------------------------------------------#


    switchFrame(entranceMenu)
    root.mainloop()
