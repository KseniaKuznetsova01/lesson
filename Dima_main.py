from ufo import *
import turtle as tr


tr.tracer(0)
tr.hideturtle()
ufo1 = Ufo('Пришелец-1', 100, 200, 150, 'green', 'black', 'yellow', 'blue', 5, 6, 5)
ufo2 = Ufo('Пришелец-2', 50, 50, 200, 'red', 'pink', 'blue', 'yellow', 3, 4, 10)

time = 1000

ufo1.show()
ufo2.show()

for i in range(time):
    tr.clear()
    ufo1.move()
    ufo2.move()

tr.done()

print(ufo1, '\n')
print(ufo2.engine_grade)
