def segitiga_siku_reverse(x):
    star = ''
    for item in range(x, 0, -1):
        for item1 in range(0,item):
            star += ' * '
        star += '\n'
    print(star)

segitiga_siku_reverse(5)