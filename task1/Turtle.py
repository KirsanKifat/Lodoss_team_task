'''Координатное поле представим массивом из с 2 перменными: высотой и шириной.
Левый верхний край имеет координаты 0 0, первая координата - высота, увеличивается вниз,
вторая - ширина увеличивается вправо'''

import random

class Turtle():
    def __init__(self, field_size, start_position=[0,0]):
        self._position = start_position
        self._field_size = field_size

    def move(self, direction):
        if direction == 'up':
            if self._position[0] is not 0:
                self._position[0] -= 1
                print(self._position)
            else:
                print('Sorry, turtle can\'t go up, because this is the end of field')
        elif direction == 'down':
            if self._position[0] is not self._field_size:
                self._position[0] += 1
                print(self._position)
            else:
                print('Sorry, turtle can\'t go down, because this is the end of field')
        elif direction == 'left':
            if self._position[1] is not 0:
                self._position[1] -= 1
                print(self._position)
            else:
                print('Sorry, turtle can\'t go left, because this is the end of field')
        elif direction == 'right':
            if self._position[1] is not self._field_size:
                self._position[1] += 1
                print(self._position)
            else:
                print('Sorry, turtle can\'t go right, because this is the end of field')
        else:
            print('Invalid command')

turtle = Turtle(5,[3,3])
comand = ['up','down','left','right','lol']
for i in range(50):
    rand = random.randrange(5)
    turtle.move(comand[rand])
