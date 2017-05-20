'''переводим координаты полей в численные значения, проверяем условие
если разность координат вертикали по модулю равны разности координат горизантали,
значит слон ходил по диагонали'''
def convert_coordinate(coordinate):
    cordinate_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    if cordinate_dict.get(coordinate[0]) is not None and 8 >= int(coordinate[1]) >= 1:
        int_cor = [cordinate_dict.get(coordinate[0]), int(coordinate[1])]
        return int_cor

def elephant(coordinate, move_coordinate):
    flag = False
    coordinate = convert_coordinate(coordinate)
    move_coordinate = convert_coordinate(move_coordinate)
    if move_coordinate is not None and coordinate is not None:
        if abs(coordinate[0] - move_coordinate[0]) == abs(coordinate[1] - move_coordinate[1]):
            flag = True
        return flag
    else:
        return 'Invalid cordinate'

print(elephant('b4','e7'))