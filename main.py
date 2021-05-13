from tkinter import *


root = Tk()
root.title("TTR Cog Calculator")
root.geometry("180x150")
root.iconbitmap("assets/icon-ios7-gear-512.ico")

default_col = 500

cogLevel = Entry(root)
cogLevel.grid(row=0, column=default_col)
cogLevel.insert(0, "1")

lured = IntVar()
same_gag = IntVar()


def update_cog_info():
    level = int(cogLevel.get())
    if level == 12:
        health = 200
    elif 1 <= level < 12:
        health = (level+1)*(level+2)

    _lured = lured.get()
    _same_gag = same_gag.get()
    damage_needed = int(health / (1 + _lured * 0.5 + _same_gag * 0.2))

    healthLabel = Label(root, text="Health: " + str(health))
    damageLabel = Label(root, text="Damage Needed: " + str(damage_needed))

    healthLabel.grid(row=4, column=default_col)
    damageLabel.grid(row=5, column=default_col)


lureCheck = Checkbutton(root, text="Lured", variable=lured).grid(row=1, column=default_col)
same_gag_check = Checkbutton(root, text="Same Gag Bonus Damage", variable=same_gag).grid(row=2, column=default_col)
b = Button(root, text="Calculate!", command=lambda: update_cog_info())
b.grid(row=3, column=default_col)

# Event loop
root.mainloop()
