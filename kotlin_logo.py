def kotlin_logo(x):
    star = ''
    for item in range(x, 0, -1):
        for item1 in range(0,item):
            star += ' * '
        star += '\n'
    for item in range(x-(x-1), x):
        for item2 in range(0, item+1):
            star += ' * '
        star += '\n'
    print(star)

kotlin_logo(7)