__author__ = 'jfhuang'
"""
using points to draw polygon:refer to heart drawing!!!!


"""
from tkinter import *
root = Tk()
root.geometry("1000x1000")

canvas = Canvas(width = 1000, height = 1000, bg = "black")
name = ""
exit = 0

def kill():
    global exit
    global name
    root.destroy()
    name = name_input.get()
    exit = 0
    exit = 1
    return name, exit 

name_label        = Label(text = "So your name is: ", bg = "black", fg = "white")
name_label_window = canvas.create_window(285, 450, anchor = NW, window = name_label)

name_input        = Entry()
name_input_window = canvas.create_window(400, 450, anchor = NW, window = name_input)

start             = Button(text = "START", width = 10, command = kill)
start_window      = canvas.create_window(430, 500, anchor = NW, window = start)
start.configure(bg = "black", fg = "white")


def welcome():

    """
    create welcome window to begin.
    Character(SNAKE HEART>..<)

    """
    ### create the frame
    for i in range(0, 980, 30):
        #canvas.create_rectangle(i, 0, i+20, 20, fill = "white")
        canvas.create_rectangle(0, i, 20, i+20, fill = "white")
        canvas.create_rectangle(980, i, 1000,i+20,fill= "white")

    ### create Snake!!
    ##S
    for i in range(4):
        canvas.create_rectangle(150 + 10 * i, 100, 160 + 10 * i, 110, fill = "white")
        canvas.create_rectangle(130 , 100 + 15 * i, 145, 120 + 15 * i, fill= "white")
        canvas.create_rectangle(130 + 15 * i, 170, 150 + 15 * i, 185, fill = "white")
        canvas.create_rectangle(200, 170 + 15 * i, 215, 190 + 15 * i, fill = "white")
        canvas.create_rectangle(195 - 20*i, 240, 215 - 20 * i, 255, fill = "white")
    ## n
    for i in range(6):
        canvas.create_rectangle(260, 170 + 15 * i, 275,185 + 15 * i, fill = "white" )
        canvas.create_rectangle(320, 170 + 15 * i, 335,185 + 15 * i, fill = "white" )
    for i in range(3):
        canvas.create_rectangle(275 + 15* i, 170, 290 + 15 * i, 185, fill = "white")
    canvas.create_rectangle(260 ,150 ,275,170, fill = "white")

    ## A
    for i in range(4):
        canvas.create_rectangle(380+15*i, 170 , 395 + 15*i, 185, fill = "white")
        canvas.create_rectangle(440, 170 + 15 * i, 455, 185 + 15 * i, fill= "white")
        canvas.create_rectangle(440 - 15 * i,235,455 - 15 * i,250, fill = "white")
        canvas.create_rectangle(380, 190 + 15 * i, 395, 205 + 15 * i, fill= "white")
    canvas.create_rectangle(440, 255, 455, 270, fill = "white")
    canvas.create_oval(380,130,400,150, fill="pink")
    canvas.create_oval(440,130,460, 150, fill="pink")

    ##k
    for i in range(8):
        canvas.create_rectangle(500,130 + 18*i, 515, 145 + 18 * i, fill = "white")
    for i in range(3):
        canvas.create_rectangle(515 + 17 * i,202 + 17*i, 530 + 17 * i, 217 + 17 * i, fill="white")
        canvas.create_rectangle(515 + 17 * i, 184 - 17*i, 530 + 17*i, 199-17*i, fill="white")
    canvas.create_rectangle(551 , 258, 566,273, fill = "white")


    ## E
    for i in range(6):
        canvas.create_rectangle(600 + 15 *i ,217,613 + 15*i, 230, fill = "white")
        canvas.create_rectangle(600 + 15 *i ,172,613 + 15*i, 185, fill = "white")
        canvas.create_rectangle(600 + 15 *i ,260,613 + 15*i, 272, fill = "white")
    for i in range(2):
        canvas.create_rectangle(600, 202-15*i, 613, 215-15*i,fill="white")
        canvas.create_rectangle(675, 202-15*i,688,215-15*i,fill = "white")
        canvas.create_rectangle(600, 232+15*i,613, 245+15*i, fill="white")

    ##heart
    heart_triangle = [745,240,758,280,785,240]
    canvas.create_oval(745,227,765,247, fill = "#BBFF00")
    canvas.create_oval(765,227,785,247,fill = "#BBFF00")
    canvas.create_polygon(heart_triangle, fill = '#BBFF00')

if __name__ == "__main__":

    root.grid()
    canvas.grid()
    welcome()
    root.mainloop()