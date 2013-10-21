__author__ = 'jfhuang'

from tkinter import *
###import welcome
import snake_class
import snake_functions
from tkinter import messagebox

"""
if vertical escape: score(elapse)/head_turn~
"""

root = Tk()
root.title("snake!!")
root.geometry("1000x1000")

canvas = Canvas(width=1000, height=1000, bg="black")


temp = list("a")
PAUSED = False
Time = 800
last_score = 0

##Direction
D = [(1,0), (-1, 0), (0,-1),(0,1)]
##   (R)     (L)     (Up)   (Down)

## initialized  head/tail and apple
snake_tail = snake_class.Snake_rectangle(370, 500, D[0])
snake_head = snake_class.Snake_head(450, 500,D[0])
apple = [(610, 400)]
turning_array = []



def start():

    """
    start game option.

    """
    for i in range(5):
        canvas.create_rectangle(450-i*20, 500, 470-i*20, 520,fill="white")
    canvas.create_oval(610 ,400 ,630,420, fill = "pink")

def stop_button():
    global  PAUSED
    PAUSED = not PAUSED

def clean_canvas():

    """
    clean canvas, remove all objects from the canvas.

    """
    canvas.delete(ALL)


def key(event):

    global PAUSED

    add_tp = True

    # if event.keysym
    if not PAUSED:

        d = snake_head.get_direction()

        if event.keysym == "Left":
            if d[0] + D[1][0] == 0 and d[1] + D[1][1] == 0 or d == D[1]:
                add_tp = not  add_tp
            else:
                snake_head.turn(D[1])

        if event.keysym == "Right":
            if d[0] + D[0][0] == 0 and d[1] + D[0][1] == 0 or d == D[0]:
                add_tp = not  add_tp
            else:
                snake_head.turn(D[0])

        if event.keysym == "Up":
            if d[0] + D[2][0] == 0 and d[1] + D[2][1] == 0 or d == D[2]:
                add_tp = not  add_tp
            else:
                snake_head.turn(D[2])

        if event.keysym == "Down":
            if d[0] + D[3][0] == 0 and d[1] + D[3][1] == 0 or d == D[3]:
                add_tp = not  add_tp
            else:
                snake_head.turn(D[3])

        if add_tp:
            turning_array.insert(0, (snake_head.getX(), snake_head.getY()))

    canvas.update()


def timer():

    global  PAUSED, Time, last_score

    if not PAUSED:

        ## evaluate if a vertical escape will happen for both head and tail.
        # snake_functions.vertical_escape_check(snake_tail,snake_head,canvas)
        ##move both front-end and back-end head/tail
        snake_functions.move_snakeImage(canvas, snake_head, snake_tail)

        snake_head.set_location()
        snake_tail.set_location()

        tx = snake_tail.getX()
        ty = snake_tail.getY()
        hx = snake_head.getX()
        hy = snake_head.getY()

        bomb_line = snake_functions.bomb_line(turning_array,tx, ty, hx, hy)

        score= snake_functions.score_elapse(bomb_line)

        if (score -last_score) > 0 and (score - last_score) % 100 == 0 and Time > 100 :
            Time -= 50

        last_score = score
        print(ty,hy)

        ## hit check or hy == 0 or hy == 980 
        if hx == 970 or hx == 10:
            messagebox.showinfo("game over", "you hit the wall, your score is {}".format(score))
            clean_canvas()
            root.destroy()
        if snake_functions.snake_hit_bomb_line_check(bomb_line,  hx, hy):
            messagebox.askokcancel("Game over","you hit yourself, your score is {}".format(score))
            #PAUSED = not PAUSED
            #clean_canvas()
            root.destroy()

        ##vertical escape new added function!!!!!   
        if hy == 0:
            snake_head.vertical_escape(0)
        if ty == 0:
            snake_tail.vertical_escape(0)
            canvas.create_rectangle(tx,0,tx+20,20,fill='black')
        if hy == 980:
            snake_head.vertical_escape(1)
        if ty == 980:
            snake_tail.vertical_escape(1)
            canvas.create_rectangle(tx,980,tx+20,1000,fill='black')


        if len(apple):
            if snake_functions.eat_apple_check(apple, hx, hy, snake_tail):
                snake_functions.generator(canvas,bomb_line,apple)

        if len(turning_array) > 0:
            if snake_functions.tail_direction_check(turning_array,snake_tail,D):
                del turning_array[-1]
                if len(turning_array) != 0:
                    snake_functions.tail_direction_check(turning_array,snake_tail,D)
                else:
                    snake_tail.change_direction(snake_head.direction)

    root.after(300,timer)



if __name__ == "__main__":

    start()
    root.grid()
    canvas.grid()
    canvas.bind("<Key>", key)
    canvas.focus_set()
    timer()
    root.mainloop()