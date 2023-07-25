def suplise(number_list):
    for num in number_list:
        if num % 2 == 0:
            return True
    return False


print(suplise([1, 2]))