
class Rim:
    def __init__(self, number):
        prev_letter = None
        key = True
        rome_num = 'IVXLCDM'
        count_rep = 0
        count_les = 0
        for i in number:
            i = i.upper()
            if i not in 'IVXLCDM':
                key = False
            if prev_letter and rome_num.index(prev_letter) < rome_num.index(i):
                count_les += 1
                count_rep = 0
            elif prev_letter and rome_num.index(prev_letter) == rome_num.index(i):
                count_rep += 1
                count_les = 0
            else:
                count_les = 0
                count_rep = 0
            if count_les > 1 or count_rep > 3:
                key = False
            prev_letter = i

            if key == True:
                self.number = number
            else:
                self.number = 'None'

        self.number = number

    def translate(self, number):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
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
