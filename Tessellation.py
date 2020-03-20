# Case-study #5 "Tessellation"
# Developers: Besedina D. (%)
#             Setskov M. (%)
#             Moiseenko V.(%)
# The aim: to write a program for performing two-color paving of the plane with regular hexagons

import turtle

turtle = turtle.Turtle()

# TO-DO(Diana): function of choosing two colors from at least six suggested ones, reentry if the color's name is wrong
def get_color_choice():
    print('Допустимые цвета заливки:')
    print('  красный')
    print('  синий')
    print('  зеленый')
    print('  желтый')
    print('  пурпурный')
    print('  розовый')
    color1 = input('Пожалуйста, введите первый цвет:')
    while color1 != 'красный' or color1 != 'синий' or color1 != 'зеленый' or color1 != 'желтый' or color1 != 'пурпурный' or color1 != 'розовый':
        print("'" + color1 + "'", 'не является верным значением.')
        color1 = input('Пожалуйста, введите цвет:')
        if color1 == 'красный' or color1 == 'синий' or color1 == 'зеленый' or color1 == 'желтый' or color1 == 'пурпурный' or color1 == 'розовый':
            color2 = input('Пожалуйста, введите второй цвет:')
            if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                return color1, color2
            while color2 != 'красный' or color2 != 'синий' or color2 != 'зеленый' or color2 != 'желтый' or color2 != 'пурпурный' or color2 != 'розовый':
                print("'" + color2 + "'", 'не является верным значением.')
                color2 = input('Пожалуйста, введите цвет:')
                if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                    return color1, color2

# TO-DO(Victoria): function of number of the hexagons, need to check whether data entry is correct, 4 <= N <= 20
def get_num_hexagons(N):
    pass

# TO-DO(Maxim): to draw the lines of hexagons
# TO-DO(Victoria): to draw the hexagon + code review
def draw_hexagon(x, y, side_len, color):
    pass

turtle.done()
