
class Rim:
    def __init__(self, number):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        N = 0
        PrevLetter = None
        key = True
        ROMENUMBER = 'IVXLCDM'
        CountRepeat = 0
        CountLess = 0
        for i in number:
            i = i.upper()
            if i not in 'IVXLCDM':
                key = False
            if PrevLetter and ROMENUMBER.index(PrevLetter) < ROMENUMBER.index(i):
                CountLess += 1
                CountRepeat = 0
            elif PrevLetter and ROMENUMBER.index(PrevLetter) == ROMENUMBER.index(i):
                CountRepeat += 1
                CountLess = 0
            else:
                CountLess = 0
                CountRepeat = 0
            if CountLess > 1 or CountRepeat > 3:
                key = False
            PrevLetter = i

            if key == True:
                self.number = number
            else:
                self.number = 'None'

        self.number = number

    def translate(self, number):
        s = 0
        for i in range(len(number)):
            if i > 0 and d[number[i]] > d[number[i - 1]]:
                s += d[number[i]] - 2 * d[number[i - 1]]
        else:
            s += d[number[i]]
        return s
    def __str__(self):
        self.translate()

    def __repr__(self):
        return self.__str__()