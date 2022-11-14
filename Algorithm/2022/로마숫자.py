import sys
input = sys.stdin.readline


dic = {'IV':1,'IX':1,'XL':1,'XC':1,'CD':1,'CM':1}
dic2 = {'IV':1,'IX':1,'XL':1,'XC':1,'CD':1,'CM':1}


def sum_value(a):
    a_value = 0
    idx = 0
    i_check = 0
    x_check = 0
    c_check = 0
    while idx < len(a):
        if a[idx] == 'I':
            if not i_check and idx != len(a)-1:
                if a[idx+1] == 'V':
                    a_value += 4
                    i_check += 1
                    idx += 1
                elif a[idx+1] == 'X':
                    a_value += 9
                    i_check += 1
                    idx += 1
                else:
                    a_value += 1
            else:
                a_value += 1
        elif a[idx] == 'V':
            a_value += 5
        elif a[idx] == 'X':
            if not x_check and idx != len(a)-1:
                if a[idx+1] == 'L':
                    a_value += 40
                    x_check += 1
                    idx += 1
                elif a[idx+1] == 'C':
                    a_value += 90
                    x_check += 1
                    idx += 1
                else:
                    a_value += 10
            else:
                a_value += 10
        elif a[idx] == 'L':
            a_value += 50
        elif a[idx] == 'C':
            if not c_check and idx != len(a)-1:
                if a[idx+1] == 'D':
                    a_value += 400
                    c_check += 1
                    idx += 1
                elif a[idx+1] == 'M':
                    a_value += 900
                    c_check += 1
                    idx += 1
                else:
                    a_value += 100
            else:
                a_value += 100
        elif a[idx] == 'D':
            a_value += 500
        elif a[idx] == 'M':
            a_value += 1000
        idx += 1
    return a_value

def make(target):
    target2 = ''
    i_check = 0
    x_check = 0
    c_check = 0

    v_check = 0
    l_check = 0
    d_check = 0

    i_con = 0
    x_con = 0
    c_con = 0
    m_con = 0
    while target != 0:
        if target >= 1000 and m_con < 3:
            target2 += 'M'
            target -= 1000
        elif target >= 900 and not c_check and dic2['CM'] and c_con < 3:
            dic2['CM'] = 0
            target2 += 'CM'
            target -= 900
            c_check += 1
        elif target >= 500 and d_check < 1:
            target2 += 'D'
            target -= 500
            d_check += 1
        elif target >= 400 and not c_check and dic2['CD'] and c_con < 3:
            target2 += 'CD'
            dic2['CD'] = 0
            c_check += 1
            target -= 400
        elif target >= 100 and c_con < 3:
            target2 += 'C'
            target -= 100
        elif target >= 90 and not x_check and dic2['XC'] and x_con < 3:
            target2 += 'XC'
            dic2['XC'] = 0
            target -= 90
            x_check += 1
        elif target >= 50 and l_check < 1:
            target2 += 'L'
            l_check += 1
            target -= 50
        elif target >= 40 and not x_check and dic2['XL'] and x_con < 3:
            target2 += 'XL'
            dic2['XL'] = 0
            target -= 40
            x_check += 1
        elif target >= 10 and x_con < 3:
            target2 += 'X'
            target -= 10
        elif target >= 9 and not i_check and dic2['IX'] and i_con < 3:
            target2 += 'IX'
            dic2['IX'] = 0
            i_check += 1
            target -= 9
        elif target >= 5 and v_check < 1:
            target2 += 'V'
            target -= 5
            v_check += 1
        elif target >= 4 and not i_check and dic2['IV'] and i_con < 3:
            target2 += 'IV'
            target -= 4
            i_check += 1
            dic2['IV'] = 0
        elif target >= 1 and i_con < 3:
            target2 += 'I'
            target -= 1

        if target2[-1] == 'I':
            i_con += 1
            x_con = 0
            c_con = 0
            m_con = 0
        elif target2[-1] == 'X':
            x_con += 1
            i_con = 0
            c_con = 0
            m_con = 0
        elif target2[-1] == 'C':
            c_con += 1
            i_con = 0
            x_con = 0
            m_con = 0
        elif target2[-1] == 'M':
            m_con += 1
            i_con = 0
            x_con = 0
            c_con = 0
    return target2

a = input().rstrip()
b = input().rstrip()

target = sum_value(a) + sum_value(b)
print(target)
print(make(target))