# Case-study #5 "Tessellation"
# Developers: Besedina D. (25%)
#             Setskov M. (%)
#             Moiseenko V.(%)
# The aim: to write a program for performing two-color paving of the plane with regular hexagons

import turtle

turtle = turtle.Turtle()

# TO-DO(Diana): function of choosing two colors from at least six suggested ones, reentry if the color's name is wrong
def get_color_choice():
    """

        Choosing the color of filling the hexagons

        :return : two colors of hexagons

        """

    print('Допустимые цвета заливки:')
    print('  красный')
    print('  синий')
    print('  зеленый')
    print('  желтый')
    print('  пурпурный')
    print('  розовый')
    color1 = input('Пожалуйста, введите первый цвет:').lower().strip()
    if color1 == 'красный' or color1 == 'синий' or color1 == 'зеленый' or color1 == 'желтый' or color1 == 'пурпурный' or color1 == 'розовый':
        if color1 == 'красный':
            color1 = 'red'
        if color1 == 'синий':
            color1 = 'blue'
        if color1 == 'зеленый':
            color1 = 'green'
        if color1 == 'желтый':
            color1 = 'yellow'
        if color1 == 'пурпурный':
            color1 = 'purple'
        if color1 == 'розовый':
            color1 = 'pink'
        color2 = input('Пожалуйста, введите второй цвет:').lower().strip()
        if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
            if color2 == 'красный':
                color2 = 'red'
            if color2 == 'синий':
                color2 = 'blue'
            if color2 == 'зеленый':
                color2 = 'green'
            if color2 == 'желтый':
                color2 = 'yellow'
            if color2 == 'пурпурный':
                color2 = 'purple'
            if color2 == 'розовый':
                color2 = 'pink'
            return color1, color2
        while color2 != 'красный' or color2 != 'синий' or color2 != 'зеленый' or color2 != 'желтый' or color2 != 'пурпурный' or color2 != 'розовый':
            print("'" + color2 + "'", 'не является верным значением.')
            color2 = input('Пожалуйста, введите цвет:').lower().strip()
            if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                if color2 == 'красный':
                    color2 = 'red'
                if color2 == 'синий':
                    color2 = 'blue'
                if color2 == 'зеленый':
                    color2 = 'green'
                if color2 == 'желтый':
                    color2 = 'yellow'
                if color2 == 'пурпурный':
                    color2 = 'purple'
                if color2 == 'розовый':
                    color2 = 'pink'
                return color1, color2
    while color1 != 'красный' or color1 != 'синий' or color1 != 'зеленый' or color1 != 'желтый' or color1 != 'пурпурный' or color1 != 'розовый':
        print("'" + color1 + "'", 'не является верным значением.')
        color1 = input('Пожалуйста, введите цвет:').lower().strip()
        if color1 == 'красный' or color1 == 'синий' or color1 == 'зеленый' or color1 == 'желтый' or color1 == 'пурпурный' or color1 == 'розовый':
            if color1 == 'красный':
                color1 = 'red'
            if color1 == 'синий':
                color1 = 'blue'
            if color1 == 'зеленый':
                color1 = 'green'
            if color1 == 'желтый':
                color1 = 'yellow'
            if color1 == 'пурпурный':
                color1 = 'purple'
            if color1 == 'розовый':
                color1 = 'pink'
            color2 = input('Пожалуйста, введите второй цвет:').lower().strip()
            if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                if color2 == 'красный':
                    color2 = 'red'
                if color2 == 'синий':
                    color2 = 'blue'
                if color2 == 'зеленый':
                    color2 = 'green'
                if color2 == 'желтый':
                    color2 = 'yellow'
                if color2 == 'пурпурный':
                    color2 = 'purple'
                if color2 == 'розовый':
                    color2 = 'pink'
                return color1, color2
            while color2 != 'красный' or color2 != 'синий' or color2 != 'зеленый' or color2 != 'желтый' or color2 != 'пурпурный' or color2 != 'розовый':
                print("'" + color2 + "'", 'не является верным значением.')
                color2 = input('Пожалуйста, введите цвет:').lower().strip()
                if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                    if color2 == 'красный':
                        color2 = 'red'
                    if color2 == 'синий':
                        color2 = 'blue'
                    if color2 == 'зеленый':
                        color2 = 'green'
                    if color2 == 'желтый':
                        color2 = 'yellow'
                    if color2 == 'пурпурный':
                        color2 = 'purple'
                    if color2 == 'розовый':
                        color2 = 'pink'
                    return color1, color2


# TO-DO(Victoria): function of number of the hexagons, need to check whether data entry is correct, 4 <= N <= 20
def get_num_hexagons(N):
    pass

# TO-DO(Maxim): to draw the lines of hexagons
# TO-DO(Victoria): to draw the hexagon + code review
def draw_hexagon(x, y, side_len, color):
    pass

turtle.done()
