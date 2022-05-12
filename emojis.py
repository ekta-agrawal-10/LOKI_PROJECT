from tkinter import *
import emoji

root = Tk()
frame = Frame(root)
frame.pack()
root.title('Emojis')

emoji1 = StringVar()
topframe = Frame(root)
topframe.pack(side=TOP)


def Enter_face1():
    txtDisplay.insert(14, '\U0001F600')
    return


def Enter_face2():
    txtDisplay.insert(14, '\U0001F62B')
    return


def Enter_face3():
    txtDisplay.insert(14, '\U0001F625')
    return


def Enter_face4():
    txtDisplay.insert(14, '\U0001F610')
    return


def Enter_face5():
    txtDisplay.insert(14, '\U0001F612')
    return


def Enter_face6():
    txtDisplay.insert(14, '\U0001F615')
    return


def Enter_face7():
    txtDisplay.insert(14, '\U0001F622')
    return


txtDisplay = Entry(frame, textvariable=emoji1, bd=10, insertwidth=1, font=50)
txtDisplay.pack(side=TOP)
button1 = Button(topframe, text='\U0001F600', fg="blue",
                 font=50, command=Enter_face1)
button1.pack(side=LEFT)
button2 = Button(topframe, text='\U0001F62B', fg="blue",
                 font=50, command=Enter_face2)
button2.pack(side=LEFT)
button3 = Button(topframe, text='\U0001F625', fg="blue",
                 font=50, command=Enter_face3)
button3.pack(side=LEFT)
button4 = Button(topframe, text='\U0001F610', fg="blue",
                 font=50, command=Enter_face4)
button4.pack(side=LEFT)
button5 = Button(topframe, text='\U0001F612', fg="blue",
                 font=50, command=Enter_face5)
button5.pack(side=LEFT)
button6 = Button(topframe, text='\U0001F615', fg="blue",
                 font=50, command=Enter_face6)
button6.pack(side=LEFT)
button7 = Button(topframe, text='\U0001F622', fg="blue",
                 font=50, command=Enter_face7)
button7.pack(side=LEFT)

frame1 = Frame(root)
frame1.pack(side=TOP)


def Enter_woman():
    txtDisplay.insert(14, emoji.emojize(":woman:"))
    return


def Enter_man():
    txtDisplay.insert(14, emoji.emojize(":man:"))
    return


def Enter_baby():
    txtDisplay.insert(14, emoji.emojize(":baby:"))
    return


def Enter_girl():
    txtDisplay.insert(14, emoji.emojize(":girl:"))
    return


def Enter_eyes():
    txtDisplay.insert(14, emoji.emojize(":eyes:"))
    return


def Enter_princess():
    txtDisplay.insert(14, emoji.emojize(":princess:"))
    return


def Enter_thumbsup():
    txtDisplay.insert(14, emoji.emojize(":thumbs_up:"))
    return


button1 = Button(frame1, text=emoji.emojize(":woman:"),
                 fg="blue", font=50, command=Enter_woman)
button1.pack(side=LEFT)
button2 = Button(frame1, text=emoji.emojize(":man:"),
                 fg="blue", font=50, command=Enter_man)
button2.pack(side=LEFT)
button3 = Button(frame1, text=emoji.emojize(":baby:"),
                 fg="blue", font=50, command=Enter_baby)
button3.pack(side=LEFT)
button4 = Button(frame1, text=emoji.emojize(":girl:"),
                 fg="blue", font=50, command=Enter_girl)
button4.pack(side=LEFT)
button5 = Button(frame1, text=emoji.emojize(":eyes:"),
                 fg="blue", font=50, command=Enter_eyes)
button5.pack(side=LEFT)
button6 = Button(frame1, text=emoji.emojize(":princess:"),
                 fg="blue", font=50, command=Enter_princess)
button6.pack(side=LEFT)
button7 = Button(frame1, text=emoji.emojize(":thumbs_up:"),
                 fg="blue", font=50, command=Enter_thumbsup)
button7.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=TOP)


def Enter_manwithcap():
    txtDisplay.insert(14, '\U000026D1')
    return


def Enter_wheelchair():
    txtDisplay.insert(14, '\U0000267F')
    return


def Enter_bouncingball():
    txtDisplay.insert(14, '\U000026F9')
    return


def Enter_tulip():
    txtDisplay.insert(14, '\U0001F337')
    return


def Enter_rocket():
    txtDisplay.insert(14, '\U0001F680')
    return


def Enter_boatman():
    txtDisplay.insert(14, '\U0001F6A3')
    return


def Enter_umbrella():
    txtDisplay.insert(14, '\U00012614')
    return


buttonl = Button(frame2, text='\U000026D1', fg="blue",
                 font=50, command=Enter_manwithcap)
buttonl.pack(side=LEFT)
button2 = Button(frame2, text='\U0000267F', fg="blue",
                 font=50, command=Enter_wheelchair)
button2.pack(side=LEFT)
button3 = Button(frame2, text='\U000026F9', fg="blue",
                 font=50, command=Enter_bouncingball)
button3.pack(side=LEFT)
button4 = Button(frame2, text='\U0001F337', fg="blue",
                 font=50, command=Enter_tulip)
button4.pack(side=LEFT)
button5 = Button(frame2, text='\U0001F680', fg="blue",
                 font=50, command=Enter_rocket)
button5.pack(side=LEFT)
button6 = Button(frame2, text='\U0001F6A3', fg="blue",
                 font=50, command=Enter_boatman)
button6.pack(side=LEFT)
button7 = Button(frame2, text='\U00002614', fg="blue",
                 font=50, command=Enter_umbrella)
button7.pack(side=LEFT)

frame3 = Frame(root)
frame3.pack(side=TOP)


def Enter_coffee():
    txtDisplay.insert(14, "\N{Hot beverage}")
    return


def Enter_snowman():
    txtDisplay.insert(14, "\N{Snowman without snow}")
    return


def Enter_paw():
    txtDisplay.insert(14, "\N{paw prints}")
    return


def Enter_trophy():
    txtDisplay.insert(14, "\N{trophy}")
    return


def Enter_friend():
    txtDisplay.insert(14, u"\U0001f46d")
    return


def Enter_combined():
    txtDisplay.insert(14, u'\u2600-\u26FF')
    return


def clear():
    txtDisplay.delete(0, END)
    return


button1 = Button(frame3, text="\N{hot beverage}",
                 fg="blue", font=50, command=Enter_coffee)
button1.pack(side=LEFT)
button2 = Button(frame3, text="\N{Snowman without snow}",
                 fg="blue", font=50, command=Enter_snowman)
button2.pack(side=LEFT)
button3 = Button(frame3, text="\N{paw prints}",
                 fg="blue", font=50, command=Enter_paw)
button3.pack(side=LEFT)
button4 = Button(frame3, text="\N{trophy}",
                 fg="blue", font=50, command=Enter_trophy)
button4.pack(side=LEFT)
button5 = Button(frame3, text=u"\U0001f46d", fg="blue",
                 font=50, command=Enter_friend)
button5.pack(side=LEFT)
button6 = Button(frame3, text=u'\u2600-\u26FF', fg="blue",
                 font=50, command=Enter_combined)
button6.pack(side=LEFT)
button7 = Button(frame3, text=u'\u267B', fg="blue", font=50, command=clear)
button7.pack(side=LEFT)

root.mainloop()
