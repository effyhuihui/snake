__author__ = 'jfhuang'

class Snake_rectangle(object):


    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def change_direction(self,direction):
        """
        check whether the body has passed the head yet,if yes, change direction to the last change

        """
        self.direction = direction

    def vertical_escape(self,choice):
        if choice == 1:
            self.y = 0
        if choice == 0:
            self.y = 980

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def get_direction(self):
        return self.direction

    def set_location(self):
        self.x += self.direction[0] * 20
        self.y += self.direction[1] * 20

    def tail_linger(self):
        self.x -= self.direction[0] * 20
        self.y -= self.direction[1] * 20

class Snake_head(Snake_rectangle):

    def turn(self,new_direction):

        """
        There will be no change in direction if one wants to reverse it
        :param new_direction: input from the key event
        :return: head location and direction
        """
        if new_direction[0] + self.direction[0] == 0 and new_direction[0] + self.direction[0] ==0:
            pass
        else:
            self.direction = new_direction


