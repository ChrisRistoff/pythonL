array_a = [10, 20, 10, 2]
array_b = [10, 25, 5, -2]
#test

def solution(array_a, array_b):
    array_c = []
    for index in range(0, len(array_a)):
        num = 0
        if array_a[index] < array_b[index]:
            for i in range(array_a[index], array_b[index]):
                num += 1
        elif array_a[index] > array_b[index]:
            for i in range(array_b[index], array_a[index]):
                num += 1
        else:
            num = 0
        num = num * num
        array_c.append(num)
    result = sum(array_c) / len(array_c)
    return result


print(solution(array_a, array_b))
