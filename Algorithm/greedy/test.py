def count_blood(blood):
    dict = {}
    dict['A'] = blood.count('A')
    dict['AB'] = blood.count('AB')
    dict['B'] = blood.count('B')
    dict['O'] = blood.count('O')
    return dict


print(count_blood(['A','B','A','O','AB','AB','O','A','B','O','B','AB',]))