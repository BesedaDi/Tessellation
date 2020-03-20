# Case-study #5 "Tessellation"
# Developers: Besedina D. (%)
#             Setskov M. (%)
#             Moiseenko V.(%)
# The aim: to write a program for performing two-color paving of the plane with regular hexagons

import turtle
import math

# TO-DO(Diana): function of choosing two colors from at least six suggested ones, reentry if the color's name is wrong
def get_color_choice():
    print('Допустимые цвета заливки:')
    print('  красный')
    print('  синий')
    print('  зеленый')
    print('  желтый')
    print('  пурпурный')
    print('  розовый')
    color1 = input('Пожалуйста, введите первый цвет:').lower().strip()
    if color1 == 'красный' or color1 == 'синий' or color1 == 'зеленый' or color1 == 'желтый' or color1 == 'пурпурный' or color1 == 'розовый':
        color2 = input('Пожалуйста, введите второй цвет:').lower().strip()
        if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
            return color1, color2
        while color2 != 'красный' or color2 != 'синий' or color2 != 'зеленый' or color2 != 'желтый' or color2 != 'пурпурный' or color2 != 'розовый':
            print("'" + color2 + "'", 'не является верным значением.')
            color2 = input('Пожалуйста, введите цвет:').lower().strip()
            if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                return color1, color2
    while color1 != 'красный' or color1 != 'синий' or color1 != 'зеленый' or color1 != 'желтый' or color1 != 'пурпурный' or color1 != 'розовый':
        print("'" + color1 + "'", 'не является верным значением.')
        color1 = input('Пожалуйста, введите цвет:').lower().strip()
        if color1 == 'красный' or color1 == 'синий' or color1 == 'зеленый' or color1 == 'желтый' or color1 == 'пурпурный' or color1 == 'розовый':
            color2 = input('Пожалуйста, введите второй цвет:').lower().strip()
            if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                return color1, color2
            while color2 != 'красный' or color2 != 'синий' or color2 != 'зеленый' or color2 != 'желтый' or color2 != 'пурпурный' or color2 != 'розовый':
                print("'" + color2 + "'", 'не является верным значением.')
                color2 = input('Пожалуйста, введите цвет:').lower().strip()
                if color2 == 'красный' or color2 == 'синий' or color2 == 'зеленый' or color2 == 'желтый' or color2 == 'пурпурный' or color2 == 'розовый':
                    return color1, color2

# TO-DO(Victoria): function of number of the hexagons, need to check whether data entry is correct, 4 <= N <= 20
def get_num_hexagons():
    try:
        N = int(input('Пожалуйста, введите количетсво шестиугольников, раполагаемых в ряд: '))
        while N < 4 or N > 20:
            print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
            N = int(input())
        return N
    except ValueError:
        print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
        N = get_num_hexagons()
        return N

def draw_hexagon(x, y, side_len, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.pencolor('black')
    turtle.width(1)
    turtle.right(30)
    turtle.forward(side_len)
    for i in range(5):
        turtle.right(60)
        turtle.forward(side_len)
    turtle.right(30)
    turtle.end_fill()
    turtle.penup()
    
def main():
    colors = get_color_choice()
    color1 = colors[0]
    color2 = colors[1]

    if color1 == 'зеленый':
        color1 == '#008000'
    if color1 == 'желтый':
        color1 == '#FFFF00'
    if color1 == 'пурпурный':
        color1 == '#9370DB'
    if color1 == 'розовый':
        color1 == '#FFC0CB'
    if color1 == 'красный':
        color1 == '#FF0000'
    if color1 == 'синий':
        color1 == '#00FFFF'

    if color2 == 'зеленый':
        color2 == '#008000'
    if color2 == 'желтый':
        color2 == '#FFFF00'
    if color2 == 'пурпурный':
        color2 == '#9370DB'
    if color2 == 'розовый':
        color2 == '#FFC0CB'
    if color2 == 'красный':
        color2 == '#FF0000'
    if color2 == 'синий':
        color2 == '#00FFFF'
        
    n = get_num_hexagons()
    a = (500 / n) / 2
    b = math.tan(0.523599) * a
    side_len = math.sqrt(a ** 2 + b ** 2)
    x = -250 + (500 / n)
    y = 250
    sh = 0
    ch = 0

    for lines in range(n):
        for column in range(n):
            if sh % 2 == 0:
                draw_hexagon(x, y, side_len, color1)
                x += a * 2
            if sh % 2 != 0:
                draw_hexagon(x, y, side_len, color2)
                x += a * 2
            sh += 1
        ch += 1
        if ch % 2 != 0:
            x = turtle.xcor() - (a * (n * 2 - 1))
            y = turtle.ycor() - b - side_len
        if ch % 2 == 0:
            x = turtle.xcor() - (a * (n * 2 - 3))
            y = turtle.ycor() - b - side_len
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
turtle.done()
