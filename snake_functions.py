__author__ = 'jfhuang'

from random import  randint
import snake_class

def score_elapse(bomb_line):
    score = -80
    for i in range(len(bomb_line)):
        score += abs(bomb_line[i][0][0]-bomb_line[i][0][1])+ abs(bomb_line[i][1][0]-bomb_line[i][1][1])
    return score

def move_snakeImage(canvas, snake_head,snake_tail):
    """
    get current direction!
    create white block along head, create black block along its tail
    :param canvas:
    :param snake_head:
    :param snake_body:
    """
    tailX = snake_tail.getX()
    tailY = snake_tail.getY()
    headX = snake_head.getX()
    headY = snake_head.getY()
    current = snake_head.get_direction()
    canvas.create_rectangle(headX+current[0]*20,  headY+current[1]*20, headX+20+current[0]*20, headY+20+current[1]*20,fill="white")
    canvas.create_rectangle(tailX ,tailY, tailX + 20, tailY + 20,fill = "black")

def eat_apple_check(apple, hx, hy,snake_tail):

    """
    吃到以后尾巴停住一次
    """
    if apple[0][0] == hx and apple[0][1] == hy:
        snake_tail.tail_linger()
        return True


def overlaid_apple_check(x,y, bomb_line):

    """
    check whether the generated apple is overlaid on the body of snake!!
    :param x:
    :param y:
    :param bomb_line:
    :return: boolvar
    """
    for i in bomb_line:
        if i[0][0] <= x <= i[0][1] and i[1][0] <= y <= i[1][1]:
            return True


def generator(canvas, bomb_line, apple):

    ## generating apple if it is still overlaid on bomb_line
    while overlaid_apple_check(apple[0][0],apple[0][1],bomb_line):
        del apple[0]
        apple.append((((randint(1, 48) * 20) - 10), (randint(0, 36) * 20)))
    canvas.create_oval(apple[0][0], apple[0][1],apple[0][0]+20,apple[0][1]+20, fill="pink")



def bomb_line(turning_array, tx, ty,hx, hy):

    """
    :param turning_array:
    :param snake_tail:
    :return: sorted lists of coordinates of lines in between of the whole snake~其实return的list是由tuple组成，每个
    tuple都是一段线段，每个tuple的第一个元素是X坐标，第二个元素是Y坐标~~~
    """
    bomb_line = []

    if turning_array == []:
        bomb_line.append((sorted([tx, hx]), sorted([ty, hy])))
    else:
        bomb_line.append((sorted([hx,turning_array[0][0]]),sorted([hy, turning_array[0][1]])))
        for i in range(len(turning_array)-1):
            bomb_line.append((sorted([turning_array[i][0],turning_array[i+1][0]]), sorted([turning_array[i][1], turning_array[i+1][1]])))
        bomb_line.append((sorted([tx, turning_array[-1][0]]), sorted([ty, turning_array[-1][1]])))
    return bomb_line


def snake_hit_bomb_line_check(bomb_line, hx, hy):

    """
    check snake_head's location with every element in bomb_line list,直接从index1开始检查（因为bomb_line的第0个元素永远是head和
    最新一个tp组成的，所以判断起来一定都是hit）我们每次检验相隔一位的线段，从index1的线段开始，5，7，。。。。因为中间的都是与head的运动方向暂时
    平行的，不会有危险～

    :param bomb_line:
    :param snake_head:
    :return: boolvar
    """
    for i in range(1, len(bomb_line), 2):
        if bomb_line[i][0][0] <= hx <= bomb_line[i][0][1] and bomb_line[i][1][0] <= hy <= bomb_line[i][1][1]:
            return True

def tail_direction_check(turning_array, snake_tail,D):
    last_turning_point_x = turning_array[-1][0]
    last_turning_point_y = turning_array[-1][1]
    if last_turning_point_x - snake_tail.getX() > 0:
        snake_tail.change_direction(D[0])
    elif last_turning_point_x - snake_tail.getX() <0:
        snake_tail.change_direction(D[1])
    if last_turning_point_y - snake_tail.getY() > 0:
        snake_tail.change_direction(D[3])
    elif last_turning_point_y - snake_tail.getY() <0:
        snake_tail.change_direction(D[2])
    if snake_tail.getY() == last_turning_point_y and snake_tail.getX() == last_turning_point_x:
        return True

if __name__ == "__main__":
    # snake_head = snake_class.Snake_head (600,20,(0,1))
    # snake_tail = snake_class.Snake_rectangle(20, 700,(1,0))
    # turning_array = [(500,20), (500, 100),(300,100), (300,300), (100,300), (100, 500),(80, 500), (80,700)]
    #
    # snake_head_hit = snake_class.Snake_head(300, 150, (-1,0))
    # turning_array_hit = [(500,150), (500, 100),(300,100), (300,300), (100,300), (100, 500),(80, 500), (80,700)]
    #
    # bomb_line = bomb_line(turning_array_hit, snake_tail,snake_head_hit)
    #
    # snake_check = snake_hit_bomb_line_check(bomb_line,snake_head_hit)

    print(score_elapse(50, 70, 80 ,10))
