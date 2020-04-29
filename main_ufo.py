from Ufo import *
import turtle as tr

t = True
tr.tracer(0)
tr.hideturtle()
ufo1 = Ufo('Пришелец-1', 100, 200, 150, 'green', 'black','yellow','blue', 5, 6)
ufo2 = Ufo('Пришелец-2', 50, 50, 200, 'red','pink','blue','yellow', 3, 4)
while t == True:
    ufo1.show()
    ufo1.not_show()
    ufo1.show()
    ufo2.show()
    ufo2.not_show()
    ufo2.show()

tr.done

print(ufo1, '\n')
print(ufo2.engine_grade)