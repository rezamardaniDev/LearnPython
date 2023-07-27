def find_max_mark(list_of_markes):
    max_mark = 0
    max_name_mark = ''

    for name, mark in list_of_markes:
        if mark >= max_mark:
            max_mark = mark
            max_name_mark = name

    return max_name_mark, max_mark


marks = [('ali', 12), ('sara', 5), ('jahan', 14)]
print(find_max_mark(marks))