# True یا False یا None را با یه تابع تشخیص دادن و تحویل دادن
puzzle = ['ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]','[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}','{"a": 1}','True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1,0.1, -0.1]


def solve_puzzle(puzzle):
    list = []
    for i in puzzle:
        if i:
            list.append(True)
        elif i == None:
            list.append(None)
        else:
            list.append(False)
    return list


print(solve_puzzle(puzzle))