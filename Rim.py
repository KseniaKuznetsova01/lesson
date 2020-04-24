def check_input(number):
    key = True
    rome_num = 'IVXLCDM'
    new_num = ' ' + number
    fix_str = ''
    n = 1
    c = 1
    count_1 = 0
    count_2 = 0
    for i in number:
        i = i.upper()
        if i not in 'IVXLCDM':
            key = False
            break
        if (i == 'D' or i == 'V' or i == 'L') and i == new_num[c]:
            count_1 += 1
            if count_1 > 1:
                key = False
                break
        if i == new_num[n]:
            count_2 += 1
            if count_2 > 3:
                key = False
                break
        else:
            fix_str = rome_num[rome_num.find(i):]
            if new_num[n] in fix_str:
                key = False
                break
            
        c += 1
        n += 1
    if key:
        return number
    else:
        return 'None'

def translate(number):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    for i in range(len(number)):
        if i > 0 and d[number[i]] > d[number[i - 1]]:
            s += d[number[i]] - 2 * d[number[i - 1]]
        else:
            s += d[number[i]]
    return s


class Rim:
    def __init__(self, number):
        self.number = check_input(number).upper()

    def __str__(self):
        if self.number == 'None':
            return 'None'
        else:
            return translate(self.number)

    def __repr__(self):
        return self.__str__()
