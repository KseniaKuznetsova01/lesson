from ufo import *
import turtle as tr
import time

start_time = time.time()
timer = int(input('Введите время работы программы: '))
tr.tracer(0)
tr.hideturtle()
ufo1 = Ufo('Пришелец-1', 50, 50, 50, 'green', 'black', 'yellow', 'blue', 5, 6, 5)
ufo2 = Ufo('Пришелец-2', -50, 50, 20, 'red', 'pink', 'blue', 'yellow', 3, 4, 10)

ufo1.show()
ufo2.show()

while (time.time() - start_time) < timer:
    tr.clear()
    ufo1.move()
    ufo2.move()

tr.done()

print(ufo1, '\n')
print(ufo2.engine_grade)

