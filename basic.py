def calculation(height, width, coverage
) :
    result = (height * width) / coverage
    if result < 2 :
        print('2')
    else :
        print(f'{round(result)}')

calculation(
    height = int(input('Height of the wall\n')),
width = int(input('width of the wall\n')),
coverage = 5 
)