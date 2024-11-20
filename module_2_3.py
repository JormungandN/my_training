my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    number = my_list[a]
    if my_list[a] > 0:
        print(my_list[a])
    elif my_list[a] == 0:
        pass
    else:
        break
    a += 1